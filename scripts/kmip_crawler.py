#!/usr/bin/env python3
"""
Crawl https://docs.oasis-open.org/kmip/, then download each page as Markdown
(via a local PullMD instance) or raw XML.

Usage:
    python kmip_crawl.py [--out raw] [--workers 4] [--save-urls ./raw/kmip_urls.txt]
                         [--urls ./raw/kmip_urls.txt] [--no-skip]
                         [--skip-file ./raw/404skip.txt]

Environment:
    PULLMD_URL   Base URL of the PullMD instance (default: http://localhost:3000)
"""

import argparse
import logging
import os
import sys
import time
from collections import deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse, quote

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://docs.oasis-open.org/kmip/"
PULLMD_URL = os.environ.get("PULLMD_URL", "http://localhost:3000")

# Path prefixes to exclude from crawl/download. The test-cases tree under
# kmip-profiles v3.0 self-references via "kmip-v3.0", producing runaway depth
# from server mis-linking, so we prune that subtree entirely.
# usecases/v1.1 is excluded because OASIS renamed "usecases" to "testcases"
# in v1.1; keeping it would duplicate content already available under testcases/.
EXCLUDE_PREFIXES = (
    "/kmip/kmip-profiles/v3.0/csd01/test-cases/kmip-v3.0",
    "/kmip/usecases/v1.1",
)

# 0.3 s gap between crawl requests to avoid hammering the OASIS server and
# triggering rate-limiting or temporary blocks. Download workers run in
# parallel against PullMD (a local process), so no delay is needed there.
CRAWL_DELAY = 0.3   # seconds between crawl requests

# PullMD can take several minutes to process a large XML or deeply nested HTML
# document (it fetches the page, parses, and converts). 1-hour ceiling prevents
# silent hangs from killing a multi-hour batch run.
REQUEST_TIMEOUT = 3600

RETRY_ATTEMPTS = 3
# Exponential back-off: sleep RETRY_DELAY * attempt before each retry so that
# transient 5xx errors or momentary network blips resolve themselves.
RETRY_DELAY = 2

# Dedicated session for the crawl phase only; keeps TCP connections alive
# across the BFS loop to avoid repeated TLS handshakes on the same host.
crawl_session = requests.Session()
crawl_session.headers["User-Agent"] = "kmip-doc-crawler/1.0 (educational)"

_TS = datetime.now().strftime("%Y%m%d_%H%M%S")
LOG_FILE = f"./logs/kmip_crawler-{_TS}.log"

def _setup_logger() -> logging.Logger:
    fmt = logging.Formatter("%(asctime)s  %(levelname)-7s  %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    logger = logging.getLogger("kmip_crawler")
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(LOG_FILE, encoding="utf-8")
    fh.setFormatter(fmt)
    sh = logging.StreamHandler(sys.stderr)
    sh.setFormatter(fmt)
    logger.addHandler(fh)
    logger.addHandler(sh)
    return logger

log = _setup_logger()


# ---------------------------------------------------------------------------
# Crawl
# ---------------------------------------------------------------------------

def is_in_scope(url: str) -> bool:
    """Return True only for URLs that belong to the KMIP subtree on docs.oasis-open.org.

    Guards against the crawler accidentally following links to other OASIS
    working groups (e.g. /pkcs/, /saml/) that share the same host, or to
    external domains referenced inline in the KMIP pages.
    """
    parsed = urlparse(url)
    return (
        parsed.scheme in ("http", "https")
        and parsed.netloc == "docs.oasis-open.org"
        and parsed.path.startswith("/kmip/")
        and not parsed.path.startswith(EXCLUDE_PREFIXES)
    )


def looks_like_html(url: str) -> bool:
    """Heuristic: decide whether a URL is likely to produce a renderable page.

    The OASIS server serves HTML for:
      - bare directory paths (no extension or trailing slash)
      - .html / .htm pages
      - .xml and .txt spec files (we download these directly, not via PullMD)

    PDFs, Word docs, and other binary formats are excluded here so they don't
    end up in the download queue with a misleading .md output path.
    The "." not in last segment check catches extensionless directory URLs
    that the server renders as index pages.
    """
    path = urlparse(url).path.rstrip("/")
    return not path or path.endswith(("/", ".html", ".htm", ".xml", ".txt")) or "." not in path.split("/")[-1]


def fetch_links(url: str) -> list[str]:
    """Fetch a page and return all absolute, in-document href links (fragments stripped).

    Fragments (#section) and query strings are normalised away before
    returning so that "page.html#intro" and "page.html" are treated as the
    same URL during deduplication in crawl(). Without this, sections with
    many in-page anchor links would flood the visited set with near-duplicates
    and trigger redundant downloads.
    """
    try:
        resp = crawl_session.get(url, timeout=15)
        resp.raise_for_status()
        # Skip binary responses — only HTML pages contain crawlable links.
        if "html" not in resp.headers.get("Content-Type", ""):
            return []
        soup = BeautifulSoup(resp.text, "html.parser")
        links = []
        for tag in soup.find_all("a", href=True):
            href = tag["href"].split("#")[0].strip()
            if not href:
                continue
            full = urljoin(url, href)
            parsed = urlparse(full)
            # Drop fragment and query — we want the canonical document URL only.
            full = parsed._replace(fragment="", query="").geturl()
            links.append(full)
        return links
    except Exception as exc:
        log.warning("[warn] %s: %s", url, exc)
        return []


def crawl(start: str) -> list[str]:
    """BFS crawl from start, returning a sorted list of in-scope HTML/XML/TXT URLs.

    Uses a deque for O(1) popleft and a visited set to guarantee each URL is
    enqueued at most once regardless of how many pages link to it. The result
    is sorted so that repeated runs produce a deterministic file for diffing.
    """
    visited: set[str] = set()
    html_urls: list[str] = []
    queue: deque[str] = deque([start])
    visited.add(start)

    while queue:
        url = queue.popleft()
        log.info("Crawling: %s", url)

        if looks_like_html(url):
            html_urls.append(url)

        for link in fetch_links(url):
            if link not in visited and is_in_scope(link):
                visited.add(link)
                queue.append(link)

        time.sleep(CRAWL_DELAY)

    return sorted(html_urls)


# ---------------------------------------------------------------------------
# Download
# ---------------------------------------------------------------------------

def url_to_local_path(url: str, out_dir: Path) -> Path | None:
    """Map a remote URL to the local file path where its content will be saved.

    Mapping rules (mirrors the URL path structure under out_dir):
      - Bare directory URL or trailing slash  →  <path>/index.md
      - .html / .htm                          →  <stem>.md  (extension replaced)
      - .xml / .txt                           →  <path>     (extension kept, raw bytes)
      - No extension (extensionless dir slug) →  <path>/index.md
      - Anything else (.pdf, .docx, ...)      →  None  (caller will skip)

    Preserving the URL path under out_dir means re-running the script after
    the OASIS server reorganises a subtree only produces changed files in the
    moved subdirectory, making diffs easy to audit.
    """
    parsed = urlparse(url)
    rel = parsed.path.lstrip("/")

    if not rel or rel.endswith("/"):
        return out_dir / rel / "index.md"

    stem, *ext_parts = rel.rsplit(".", 1)
    ext = ext_parts[0].lower() if ext_parts else ""

    if ext in ("html", "htm"):
        return out_dir / (stem + ".md")
    if ext in ("xml", "txt"):
        return out_dir / rel
    if ext == "":
        return out_dir / rel / "index.md"
    return None  # skip PDFs, DOCs, etc.


def fetch_markdown(url: str) -> tuple[str | None, int, str]:
    """Fetch a page through PullMD and return (markdown_text, http_status, info).

    PullMD is queried with frontmatter=true so its response includes YAML
    front matter with the source URL and title — useful for the KB pipeline.
    404 and 403 are returned immediately without retrying because they
    indicate a permanent server-side state, not transient failures.
    """
    api_url = f"{PULLMD_URL}/api?url={quote(url, safe='')}&frontmatter=true"
    for attempt in range(1, RETRY_ATTEMPTS + 1):
        try:
            resp = requests.get(api_url, timeout=REQUEST_TIMEOUT)
            source = resp.headers.get("X-Source", "unknown")
            quality = resp.headers.get("X-Quality", "?")
            if resp.status_code == 200:
                return resp.text, resp.status_code, f"{source} quality={quality}"
            if resp.status_code in (404, 403):
                # Permanent error — no point retrying.
                return None, resp.status_code, source
            if attempt < RETRY_ATTEMPTS:
                time.sleep(RETRY_DELAY * attempt)
        except requests.RequestException as exc:
            if attempt < RETRY_ATTEMPTS:
                time.sleep(RETRY_DELAY * attempt)
            else:
                return None, -1, str(exc)
    return None, -1, "max retries exceeded"


def fetch_direct(url: str) -> tuple[bytes | None, int, str]:
    """Download a URL directly as raw bytes (used for .xml and .txt files).

    XML spec documents and plain-text files are not sent through PullMD
    because PullMD's Markdown conversion would discard structure that is
    valuable to the KB pipeline (e.g. TTLV encoding tables in XML).
    """
    for attempt in range(1, RETRY_ATTEMPTS + 1):
        try:
            resp = requests.get(url, timeout=REQUEST_TIMEOUT)
            if resp.status_code == 200:
                return resp.content, resp.status_code, "direct"
            if resp.status_code in (404, 403):
                return None, resp.status_code, "direct"
            if attempt < RETRY_ATTEMPTS:
                time.sleep(RETRY_DELAY * attempt)
        except requests.RequestException as exc:
            if attempt < RETRY_ATTEMPTS:
                time.sleep(RETRY_DELAY * attempt)
            else:
                return None, -1, str(exc)
    return None, -1, "max retries exceeded"


def load_skip_urls(skip_file: str | None) -> set[str]:
    """Load a newline-separated list of URLs to skip during download.

    A missing file is silently tolerated so that a fresh checkout (where
    404skip.txt hasn't been populated yet) doesn't abort the run.
    """
    if not skip_file:
        return set()
    path = Path(skip_file)
    if not path.exists():
        log.info("Skip file %s not found; nothing to skip.", path)
        return set()
    urls = {u.strip() for u in path.read_text(encoding="utf-8").splitlines() if u.strip()}
    log.info("Loaded %d skip URL(s) from %s", len(urls), path)
    return urls


def process_url(url: str, out_dir: Path, skip_existing: bool, skip_urls: set[str]) -> dict:
    """Download one URL and write its content to disk; return a status dict.

    Decision tree:
      1. URL is in the explicit skip list          → skip (known 404 / unwanted)
      2. url_to_local_path returns None            → skip (PDF, DOCX, …)
      3. File already exists and skip_existing     → skip (incremental mode)
      4. Extension is .xml or .txt                 → fetch_direct (raw bytes)
      5. Everything else                           → fetch_markdown via PullMD
    """
    if url in skip_urls:
        return {"url": url, "status": "skipped", "reason": "in skip file"}

    local = url_to_local_path(url, out_dir)
    if local is None:
        return {"url": url, "status": "skipped", "reason": "non-HTML file"}

    if skip_existing and local.exists():
        return {"url": url, "status": "skipped", "reason": "already exists", "path": str(local)}

    # Determine fetch strategy from the original URL extension, not the local
    # path extension (which may be .md after remapping from .html).
    ext = urlparse(url).path.rsplit(".", 1)[-1].lower() if "." in urlparse(url).path else ""

    if ext in ("xml", "txt"):
        raw, code, info = fetch_direct(url)
        if raw is None:
            return {"url": url, "status": "error", "code": code, "info": info}
        local.parent.mkdir(parents=True, exist_ok=True)
        local.write_bytes(raw)
        return {"url": url, "status": "ok", "path": str(local), "info": info}

    content, code, info = fetch_markdown(url)
    if content is None:
        return {"url": url, "status": "error", "code": code, "info": info}

    local.parent.mkdir(parents=True, exist_ok=True)
    local.write_text(content, encoding="utf-8")
    return {"url": url, "status": "ok", "path": str(local), "info": info}


def download_all(urls: list[str], out_dir: Path, workers: int, skip_existing: bool,
                 skip_urls: set[str]) -> None:
    """Submit all URLs to a thread pool and log progress as futures complete.

    as_completed is used (rather than iterating futures in submission order)
    so that fast responses are logged immediately instead of waiting behind
    a slow PullMD conversion. This also surfaces errors early in long runs.
    """
    ok = skipped = errors = 0
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(process_url, url, out_dir, skip_existing, skip_urls): url for url in urls}
        for future in as_completed(futures):
            result = future.result()
            status = result["status"]
            if status == "ok":
                ok += 1
                log.info("[ok]    %s  (%s)", result["path"], result["info"])
            elif status == "skipped":
                skipped += 1
                log.info("[skip]  %s  (%s)", result["url"], result["reason"])
            else:
                errors += 1
                log.error("[error] %s  HTTP %s  %s", result["url"], result.get("code"), result.get("info"))
    log.info("Done. ok=%d  skipped=%d  errors=%d", ok, skipped, errors)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--urls", metavar="FILE",
                        help="Skip crawl; load URLs from this file instead")
    parser.add_argument("--save-urls", metavar="FILE", default="./raw/kmip_urls.txt",
                        help="Save discovered URLs to this file (default: ./raw/kmip_urls.txt)")
    parser.add_argument("--out", default="raw", help="Output root directory (default: raw)")
    parser.add_argument("--workers", type=int, default=4, help="Parallel download workers (default: 4)")
    parser.add_argument("--no-skip", action="store_true", help="Re-download files that already exist")
    parser.add_argument("--skip-file", metavar="FILE", default="./raw/404skip.txt",
                        help="Skip URLs listed in this file, e.g. known 404s (default: ./raw/404skip.txt)")
    args = parser.parse_args()

    if args.urls:
        urls_file = Path(args.urls)
        if not urls_file.exists():
            print(f"Error: {urls_file} not found.", file=sys.stderr)
            sys.exit(1)
        urls = [u.strip() for u in urls_file.read_text(encoding="utf-8").splitlines() if u.strip()]
        before = len(urls)
        # Re-apply EXCLUDE_PREFIXES even when loading a pre-built URL list,
        # in case the list was saved before a subtree was added to the exclusion set.
        urls = [u for u in urls if not urlparse(u).path.startswith(EXCLUDE_PREFIXES)]
        log.info("Loaded %d URL(s) from %s (%d excluded)", len(urls), urls_file, before - len(urls))
    else:
        log.info("Starting crawl from %s", BASE_URL)
        urls = crawl(BASE_URL)
        save_path = Path(args.save_urls)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        save_path.write_text("\n".join(urls) + "\n", encoding="utf-8")
        log.info("Found %d URL(s). Saved to %s", len(urls), save_path)

    skip_urls = load_skip_urls(args.skip_file)

    out_dir = Path(args.out)
    log.info("Log file: %s", LOG_FILE)
    log.info("PullMD:  %s", PULLMD_URL)
    log.info("URLs:    %d", len(urls))
    log.info("Skip:    %d", len(skip_urls))
    log.info("Output:  %s", out_dir.resolve())
    log.info("Workers: %d", args.workers)

    download_all(urls, out_dir, args.workers, skip_existing=not args.no_skip, skip_urls=skip_urls)


if __name__ == "__main__":
    main()
