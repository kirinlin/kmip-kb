"""KMIP Raw MCP server — exposes raw downloaded spec documents to coding agents."""

from __future__ import annotations

import re
import sys
import pathlib
from typing import Optional

try:
    import yaml
except ImportError:
    sys.exit("pyyaml is required: pip install pyyaml")

try:
    from rank_bm25 import BM25Okapi
except ImportError:
    sys.exit("rank-bm25 is required: pip install rank-bm25")

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    sys.exit("mcp is required: pip install mcp")


RAW_ROOT = pathlib.Path(__file__).parent.parent / "raw"

# ---------------------------------------------------------------------------
# Version pattern — matches directory components like "v2.1", "v1.4", "v3.0"
# ---------------------------------------------------------------------------

_VER_RE = re.compile(r"^v(\d+\.\d+)$")

# ---------------------------------------------------------------------------
# Index — loaded once at startup
# ---------------------------------------------------------------------------

_docs: list[dict] = []
_bm25: Optional[BM25Okapi] = None


def _extract_path_meta(path: pathlib.Path) -> dict:
    """Derive doc_type, version, and is_final from the file path.

    The path structure under raw/kmip/ is:
        <doc-family>/v<x.y>/[<stage>/]<filename>.md
    where <stage> is absent for the canonical top-level link.

    doc_type  — the family directory name (e.g. "kmip-spec", "spec", "profiles")
    version   — the numeric string extracted from the first vX.Y component
    is_final  — True when the file sits directly inside the vX.Y dir (no stage subdir)
    """
    parts = path.relative_to(RAW_ROOT).parts  # e.g. ("kmip","kmip-spec","v2.1","kmip-spec-v2.1.md")
    doc_type = ""
    version = ""
    ver_idx = -1
    for i, p in enumerate(parts):
        m = _VER_RE.match(p)
        if m:
            version = m.group(1)
            ver_idx = i
            if i > 0:
                doc_type = parts[i - 1]
            break

    # is_final: the file is directly inside the version dir (no intermediate stage dir)
    is_final = ver_idx >= 0 and (len(parts) - ver_idx == 2)  # only [filename] after version dir

    return {"doc_type": doc_type, "version": version, "is_final": is_final}


def _parse(path: pathlib.Path) -> dict | None:
    """Parse a raw Markdown file into a document dict.

    Returns None for files without a valid YAML front matter block or
    whose front matter lacks a recognisable title (e.g. stub index files).
    """
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    try:
        end = text.index("---", 3)
    except ValueError:
        return None
    try:
        fm = yaml.safe_load(text[3:end]) or {}
    except yaml.YAMLError:
        return None

    # Skip files that have no meaningful title — these are usually navigation pages.
    if not fm.get("title"):
        return None

    body = text[end + 3:].strip()
    slug = str(path.relative_to(RAW_ROOT).with_suffix(""))
    meta = _extract_path_meta(path)

    return {
        "slug": slug,
        "path": str(path),
        "fm": fm,
        "body": body,
        "full": text,
        "doc_type": meta["doc_type"],
        "version": meta["version"],
        "is_final": meta["is_final"],
    }


def _tokenize(doc: dict) -> list[str]:
    """Build BM25 tokens for a raw document.

    Combines title, description, doc_type/version path words, and the first
    5 000 characters of body. Body is capped to keep memory reasonable given
    that raw spec files can be hundreds of kilobytes each.
    """
    parts = [
        doc["fm"].get("title", ""),
        doc["fm"].get("description", ""),
        doc["doc_type"].replace("-", " "),
        doc["version"],
        doc["body"][:5000],
    ]
    return re.findall(r"\w+", " ".join(parts).lower())


def _build_index() -> None:
    global _docs, _bm25
    _docs = []
    for md in sorted(RAW_ROOT.rglob("*.md")):
        if md.name == "index.md":
            continue
        doc = _parse(md)
        if doc:
            _docs.append(doc)
    _bm25 = BM25Okapi([_tokenize(d) for d in _docs])


_build_index()

# ---------------------------------------------------------------------------
# MCP server
# ---------------------------------------------------------------------------

mcp = FastMCP(
    "kmip-raw",
    instructions=(
        "Provides search and retrieval over the raw KMIP source documents — "
        "250+ crawled Markdown files covering every OASIS KMIP specification, "
        "profiles, usage guide, test cases, and use cases across all versions "
        "(v1.0–v3.0) and draft stages. "
        "Use search_raw to locate documents, then get_doc to read their content. "
        "Raw documents are large; get_doc supports char_offset/max_chars pagination."
    ),
)


@mcp.tool()
def search_raw(
    query: str,
    doc_type: Optional[str] = None,
    version: Optional[str] = None,
    final_only: bool = True,
    limit: int = 10,
) -> str:
    """
    BM25 full-text search over raw KMIP spec documents (title, description, body excerpt).

    Args:
        query: Free-text query (e.g. "symmetric key wrapping", "TTLV encoding").
        doc_type: Filter by document family directory name — e.g. "kmip-spec", "spec",
                  "kmip-profiles", "profiles", "kmip-ug", "ug", "kmip-testcases",
                  "testcases", "usecases", "kmip-addtl-msg-enc", "kmip-asym-key-profile",
                  "kmip-cs-profile", "kmip-sa-sed-profile", "kmip-suite-b-profile",
                  "kmip-sym-foundry-profile", "kmip-sym-key-profile",
                  "kmip-opaque-obj-profile", "kmip-tape-lib-profile".
        version: Filter by version string — e.g. "2.1", "1.4", "3.0".
        final_only: When True (default), return only the canonical top-level document
                    for each version (not intermediate draft/stage subdirectories).
        limit: Max results (default 10).

    Returns ranked list of matching document summaries with slugs and metadata.
    Use get_doc(slug) to fetch content.
    """
    tokens = re.findall(r"\w+", query.lower())
    if not tokens:
        return "Empty query."

    scores = _bm25.get_scores(tokens)
    ranked = sorted(
        ((score, doc) for score, doc in zip(scores, _docs) if score > 0),
        key=lambda x: -x[0],
    )

    if final_only:
        ranked = [(s, d) for s, d in ranked if d["is_final"]]
    if doc_type:
        ranked = [(s, d) for s, d in ranked if d["doc_type"] == doc_type]
    if version:
        ranked = [(s, d) for s, d in ranked if d["version"] == version]

    top = ranked[:limit]
    if not top:
        return "No results found."

    lines: list[str] = []
    for score, doc in top:
        fm = doc["fm"]
        lines.append(f"### {fm.get('title', doc['slug'])}")
        lines.append(f"slug: `{doc['slug']}`")
        lines.append(
            f"doc_type={doc['doc_type'] or '?'}  "
            f"version={doc['version'] or '?'}  "
            f"final={doc['is_final']}"
        )
        if fm.get("description"):
            lines.append(f"description: {fm['description']}")
        if fm.get("url"):
            lines.append(f"url: {fm['url']}")
        lines.append(f"score: {score:.3f}")
        lines.append("")
    return "\n".join(lines)


@mcp.tool()
def get_doc(
    slug: str,
    char_offset: int = 0,
    max_chars: int = 20000,
) -> str:
    """
    Return a paginated slice of a raw spec document (front matter + prose).

    Raw spec files are large (often hundreds of kilobytes). Use char_offset and
    max_chars to page through the content without exceeding context limits.

    Args:
        slug: Document slug as returned by search_raw or list_docs.
              Accepts the full relative slug (e.g. "kmip/kmip-spec/v2.1/kmip-spec-v2.1")
              or a bare filename stem (e.g. "kmip-spec-v2.1") — the first match is returned.
        char_offset: Character position to start reading from (default 0).
        max_chars: Maximum characters to return (default 20 000).

    Returns the requested slice with a header showing total length and current range,
    so you can determine whether further pages exist.
    """
    doc = next((d for d in _docs if d["slug"] == slug), None)

    if doc is None:
        # Fallback: bare stem match
        doc = next((d for d in _docs if d["slug"].endswith("/" + slug)), None)

    if doc is None:
        available = [d["slug"] for d in _docs if slug.split("/")[-1] in d["slug"]]
        hint = f"\nDid you mean one of: {available[:5]}" if available else ""
        return f"Document not found: '{slug}'.{hint}"

    full = doc["full"]
    total = len(full)
    start = max(0, char_offset)
    end = min(total, start + max_chars)
    chunk = full[start:end]

    header = (
        f"<!-- slug: {doc['slug']} | total: {total} chars | "
        f"showing: {start}–{end} -->\n\n"
    )
    return header + chunk


@mcp.tool()
def list_docs(
    doc_type: Optional[str] = None,
    version: Optional[str] = None,
    final_only: bool = True,
) -> str:
    """
    List raw spec documents with slug and metadata, sorted alphabetically.

    Args:
        doc_type: Filter by document family (e.g. "kmip-spec", "kmip-profiles",
                  "kmip-ug", "kmip-testcases").
        version: Filter by version string (e.g. "2.1", "1.4").
        final_only: When True (default), return only the canonical top-level
                    document for each version (not draft stage subdirectories).

    Returns one line per document: slug | doc_type | version | final | title.
    """
    results = _docs
    if final_only:
        results = [d for d in results if d["is_final"]]
    if doc_type:
        results = [d for d in results if d["doc_type"] == doc_type]
    if version:
        results = [d for d in results if d["version"] == version]

    lines = [
        (
            f"{d['slug']} | {d['doc_type'] or '?'} | "
            f"{d['version'] or '?'} | {d['is_final']} | "
            f"{d['fm'].get('title', '?')}"
        )
        for d in sorted(results, key=lambda d: d["slug"])
    ]
    return "\n".join(lines) if lines else "No documents found."


if __name__ == "__main__":
    mcp.run(transport="stdio")
