"""KMIP KB MCP server — exposes the knowledge base to coding agents via tools."""

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


# KB root is two levels up from this file (mcp_py/ → repo root → kb/).
KB_ROOT = pathlib.Path(__file__).parent.parent / "kb"

# ---------------------------------------------------------------------------
# Index — loaded once at startup
# ---------------------------------------------------------------------------

# Module-level globals so the index is built once and reused across all tool
# calls for the lifetime of the server process.  Mutation only happens in
# _build_index(); all tool handlers treat these as read-only.
_docs: list[dict] = []
_bm25: Optional[BM25Okapi] = None


def _parse(path: pathlib.Path) -> dict | None:
    """Parse a KB Markdown file into a document dict.

    Returns None for files that lack a valid YAML front matter block (the
    leading "---" / "---" delimiters), because those files are either
    templates or non-article assets that should not be indexed.

    The returned dict carries:
      slug   — relative path without extension, used as the stable article ID
      path   — absolute filesystem path (kept for potential future use)
      fm     — parsed front-matter dict (title, keywords, category, …)
      body   — article text after the closing "---", with leading whitespace stripped
      full   — the original raw file content (returned verbatim by get_article)
    """
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    try:
        # Find the *second* "---" that closes the front-matter block.
        # Search from index 3 to skip the opening delimiter itself.
        end = text.index("---", 3)
    except ValueError:
        # No closing delimiter → malformed file, skip it.
        return None
    try:
        fm = yaml.safe_load(text[3:end]) or {}
    except yaml.YAMLError:
        return None
    body = text[end + 3 :].strip()
    # Slug is the path relative to KB_ROOT without the .md suffix.
    # e.g. kb/operations/register.md → "operations/register"
    slug = str(path.relative_to(KB_ROOT).with_suffix(""))
    return {"slug": slug, "path": str(path), "fm": fm, "body": body, "full": text}


def _tokenize(doc: dict) -> list[str]:
    """Build the token list used by BM25 for a single document.

    We combine four text sources so that a query matches on any of:
      - the human-readable title ("Register")
      - explicit keywords ("symmetric key", "create")
      - the slug path words ("operations register") — catches bare category/name searches
      - the first 3 000 characters of the body — avoids over-indexing on boilerplate
        near the end of long articles while still covering the core prose

    All tokens are lower-cased and split on non-word characters so that
    hyphenated slug segments ("symmetric-key") become individual tokens.
    """
    parts = [
        doc["fm"].get("title", ""),
        " ".join(doc["fm"].get("keywords", [])),
        doc["slug"].replace("/", " ").replace("-", " "),
        doc["body"][:3000],
    ]
    return re.findall(r"\w+", " ".join(parts).lower())


def _build_index() -> None:
    """Scan all KB Markdown files, parse them, and build the BM25 index.

    Called exactly once at module import time.  Uses a sorted glob so that
    the document order (and therefore BM25 IDF weights) is deterministic
    across platforms.  Files that fail _parse() (no front matter) are
    silently excluded from the index.
    """
    global _docs, _bm25
    _docs = []
    for md in sorted(KB_ROOT.rglob("*.md")):
        doc = _parse(md)
        if doc:
            _docs.append(doc)
    # BM25Okapi expects a list of token lists; order must match _docs.
    _bm25 = BM25Okapi([_tokenize(d) for d in _docs])


# Build the index eagerly so the first tool call pays no extra latency.
_build_index()

# ---------------------------------------------------------------------------
# MCP server
# ---------------------------------------------------------------------------

mcp = FastMCP(
    "kmip-kb",
    instructions=(
        "Provides search and retrieval over the KMIP Knowledge Base — "
        "170+ original-prose articles covering KMIP 1.0–2.1 operations, attributes, "
        "objects, TTLV encoding, profiles, concepts, workflows, and examples. "
        "Use search_kb first, then get_article to read full content."
    ),
)


@mcp.tool()
def search_kb(
    query: str,
    category: Optional[str] = None,
    status: Optional[str] = None,
    spec_version: Optional[str] = None,
    limit: int = 10,
) -> str:
    """
    BM25 full-text search over KMIP KB articles (title, keywords, slug, body).

    Args:
        query: Free-text search query (e.g. "symmetric key creation", "TTLV encoding").
        category: Filter by category — one of: operation, attribute, object, concept,
                  ttlv, profile, reference, workflow, example, schema, index.
        status: Filter by status — stub | draft | reviewed.
        spec_version: Filter to articles present in a specific version (e.g. "2.1", "1.4").
        limit: Max results (default 10).

    Returns ranked list of matching article summaries with slugs, metadata, and keywords.
    Use get_article(slug) to fetch the full text of any result.
    """
    tokens = re.findall(r"\w+", query.lower())
    if not tokens:
        return "Empty query."

    # get_scores returns one float per document in the same order as _docs.
    scores = _bm25.get_scores(tokens)

    # Filter out zero-score docs before sorting — BM25 assigns 0 to docs that
    # share no tokens with the query; including them would pollute the ranking.
    ranked = sorted(
        ((score, doc) for score, doc in zip(scores, _docs) if score > 0),
        key=lambda x: -x[0],
    )

    # Post-filter by front-matter fields.  Filtering after ranking (rather than
    # before) preserves correct IDF weights — excluding docs from the corpus
    # before scoring would artificially inflate scores for rare terms.
    if category:
        ranked = [(s, d) for s, d in ranked if d["fm"].get("category") == category]
    if status:
        ranked = [(s, d) for s, d in ranked if d["fm"].get("status") == status]
    if spec_version:
        # spec_versions is a list (e.g. ["1.4", "2.0", "2.1"]); membership test.
        ranked = [
            (s, d)
            for s, d in ranked
            if spec_version in d["fm"].get("spec_versions", [])
        ]

    top = ranked[:limit]
    if not top:
        return "No results found."

    # Render as Markdown so the caller (typically an LLM) gets structured,
    # scannable output without needing to parse JSON.
    lines: list[str] = []
    for score, doc in top:
        fm = doc["fm"]
        lines.append(f"### {fm.get('title', doc['slug'])}")
        lines.append(f"slug: `{doc['slug']}`")
        lines.append(
            f"category={fm.get('category','?')}  "
            f"status={fm.get('status','?')}  "
            f"spec_versions={fm.get('spec_versions', [])}"
        )
        if fm.get("keywords"):
            lines.append(f"keywords: {', '.join(fm['keywords'])}")
        if fm.get("related"):
            lines.append(f"related: {', '.join(fm['related'])}")
        lines.append(f"score: {score:.3f}")
        lines.append("")
    return "\n".join(lines)


@mcp.tool()
def get_article(slug: str) -> str:
    """
    Return the full Markdown content (front matter + prose) of a KB article.

    Args:
        slug: Article slug as returned by search_kb or list_articles.
              Accepts both the full relative slug (e.g. "operations/register")
              and a bare name (e.g. "register") — the first matching article is returned.

    Returns the complete file content including YAML front matter.
    """
    # Exact match first — cheapest and unambiguous.
    for doc in _docs:
        if doc["slug"] == slug:
            return doc["full"]

    # Fallback: treat the slug as a bare trailing segment.  Useful when the
    # caller knows the article name but not its category directory.
    # Only the *first* match is returned, so prefer the exact form when the
    # same name appears in multiple categories.
    for doc in _docs:
        if doc["slug"].endswith("/" + slug):
            return doc["full"]

    # Surface nearby candidates so the caller can self-correct without a
    # second round-trip.
    available = [d["slug"] for d in _docs if slug.split("/")[-1] in d["slug"]]
    hint = f"\nDid you mean one of: {available[:5]}" if available else ""
    return f"Article not found: '{slug}'.{hint}"


@mcp.tool()
def list_articles(
    category: Optional[str] = None,
    status: Optional[str] = None,
) -> str:
    """
    List KB articles with slug and front matter metadata, sorted alphabetically.

    Args:
        category: Filter by category (operation, attribute, object, concept, ttlv,
                  profile, reference, workflow, example, schema, index).
        status: Filter by status (stub, draft, reviewed).

    Returns one line per article: slug | category | status | title.
    """
    results = _docs
    if category:
        results = [d for d in results if d["fm"].get("category") == category]
    if status:
        results = [d for d in results if d["fm"].get("status") == status]

    # One compact line per article — callers can grep this to locate slugs
    # without fetching full article content.
    lines = [
        f"{d['slug']} | {d['fm'].get('category','?')} | {d['fm'].get('status','?')} | {d['fm'].get('title','?')}"
        for d in sorted(results, key=lambda d: d["slug"])
    ]
    return "\n".join(lines) if lines else "No articles found."


@mcp.tool()
def get_related(slug: str, limit: int = 5) -> str:
    """
    Return the articles listed in the 'related' front matter of a given article,
    plus a BM25 search using its title and keywords to surface additional neighbours.

    Args:
        slug: Article slug (e.g. "operations/register").
        limit: Max additional BM25 neighbours beyond the explicit related list (default 5).

    Returns article summaries the same way search_kb does.
    """
    source = next((d for d in _docs if d["slug"] == slug), None)
    if source is None:
        return f"Article not found: '{slug}'"

    fm = source["fm"]
    explicit_slugs: list[str] = fm.get("related", [])

    lines: list[str] = []
    # Track already-emitted slugs to avoid duplicates between the explicit
    # list and the BM25 neighbours section.  Start with the source itself
    # so self-matches from BM25 are suppressed.
    seen: set[str] = {slug}

    # ---- Explicit related docs ----------------------------------------
    # These are authored by hand in front matter and are the highest-quality
    # cross-references; always emit them first.
    if explicit_slugs:
        lines.append("## Explicitly related")
        for rel in explicit_slugs:
            # Allow bare names (e.g. "register") as well as full slugs.
            match = next(
                (d for d in _docs if d["slug"] == rel or d["slug"].endswith("/" + rel)),
                None,
            )
            if match:
                mfm = match["fm"]
                lines.append(f"- **{mfm.get('title', match['slug'])}** (`{match['slug']}`)")
                seen.add(match["slug"])
            else:
                # The referenced slug may be planned but not yet authored; surface
                # the broken reference so callers know the article is missing.
                lines.append(f"- _{rel}_ (not yet in KB)")

    # ---- BM25 neighbours -----------------------------------------------
    # Use the article's own title + keywords as the query so that semantically
    # adjacent articles surface even when they are not explicitly cross-linked.
    query_text = " ".join(
        [fm.get("title", ""), " ".join(fm.get("keywords", []))]
    )
    tokens = re.findall(r"\w+", query_text.lower())
    if tokens and limit > 0:
        scores = _bm25.get_scores(tokens)
        neighbours = sorted(
            (
                (score, doc)
                for score, doc in zip(scores, _docs)
                # Exclude the source article and anything already listed above.
                if score > 0 and doc["slug"] not in seen
            ),
            key=lambda x: -x[0],
        )[:limit]
        if neighbours:
            lines.append("\n## BM25 neighbours")
            for score, doc in neighbours:
                nfm = doc["fm"]
                lines.append(
                    f"- **{nfm.get('title', doc['slug'])}** (`{doc['slug']}`) score={score:.3f}"
                )

    return "\n".join(lines) if lines else "No related articles found."


if __name__ == "__main__":
    mcp.run(transport="stdio")
