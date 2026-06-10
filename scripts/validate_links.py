#!/usr/bin/env python3
"""Validate cross-references in KB documents.

Two checks are run for every document:

1. ``related`` slugs — every entry in the front-matter ``related`` list must
   match the stem of at least one ``.md`` file somewhere in the knowledge base.

2. Relative Markdown links — every ``[text](../path.md)`` or
   ``[text](./path.md)`` link in the document body must resolve to a file that
   actually exists.

Documents with ``status: stub`` are included in check 1 (related slugs are
usually empty stubs, which pass). Body-link check 2 applies to all statuses.

Pure standard library.

Usage:
    python scripts/validate_links.py
    python scripts/validate_links.py operations objects
    python scripts/validate_links.py --related-only
    python scripts/validate_links.py --links-only
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_kb_scaffold import read_front_matter  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent

# All directories that contain KB documents (same list as status_report.py).
ALL_KB_DIRS = [
    "attributes", "concepts", "objects", "operations",
    "operations/server-to-client", "profiles", "references",
    "ttlv", "workflows", "examples",
]

_LINK_RE = re.compile(r"\[(?:[^\]]*)\]\(([^)]+)\)")


def build_slug_index(root: Path) -> dict[str, list[Path]]:
    """Map every .md stem to its absolute path(s). Slugs may be non-unique."""
    index: dict[str, list[Path]] = {}
    for rel in ALL_KB_DIRS:
        d = root / rel
        if not d.exists():
            continue
        for f in d.rglob("*.md"):
            if f.name == "index.md":
                continue
            index.setdefault(f.stem, []).append(f)
    return index


def iter_docs(root: Path, paths: list[str]) -> list[Path]:
    docs = []
    for p in paths:
        target = root / p
        if target.is_dir():
            docs.extend(sorted(f for f in target.rglob("*.md") if f.name != "index.md"))
        elif target.is_file():
            docs.append(target)
        else:
            print(f"WARN: path not found: {p}", file=sys.stderr)
    return docs


def body_after_front_matter(text: str) -> str:
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    return text[end + 4:] if end != -1 else text


def check_related(path: Path, fm: dict, slug_index: dict[str, list[Path]]) -> list[str]:
    related = fm.get("related", [])
    if not isinstance(related, list):
        return [f"related is not a list"]
    issues = []
    for slug in related:
        if not isinstance(slug, str):
            issues.append(f"related entry is not a string: {slug!r}")
            continue
        if slug not in slug_index:
            issues.append(f"RELATED slug not found: {slug!r}")
    return issues


def check_body_links(path: Path, text: str) -> list[str]:
    body = body_after_front_matter(text)
    issues = []
    for line_no, line in enumerate(body.splitlines(), start=1):
        for m in _LINK_RE.finditer(line):
            href = m.group(1).strip()
            # Skip anchors, external URLs, and mailto links.
            if href.startswith(("#", "http://", "https://", "mailto:")):
                continue
            # Strip fragment
            href_path = href.split("#")[0]
            if not href_path:
                continue
            target = (path.parent / href_path).resolve()
            if not target.exists():
                rel_from = path.relative_to(REPO_ROOT).as_posix()
                issues.append(f"LINK broken at line {line_no}: {href!r} -> {target.relative_to(REPO_ROOT).as_posix()}")
    return issues


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("paths", nargs="*", default=ALL_KB_DIRS,
                   help="Directories or files to check (default: all KB dirs)")
    p.add_argument("--related-only", action="store_true",
                   help="Only check related slugs; skip body-link check")
    p.add_argument("--links-only", action="store_true",
                   help="Only check body links; skip related-slug check")
    p.add_argument("--out", default=".", help="Repo root (default: current dir)")
    args = p.parse_args(argv)

    root = Path(args.out).resolve()
    slug_index = build_slug_index(root)
    docs = iter_docs(root, args.paths)

    if not docs:
        print("No documents found.")
        return 1

    total_issues = 0
    checked = 0
    for doc in docs:
        text = doc.read_text(encoding="utf-8")
        fm = read_front_matter(doc) or {}
        issues = []

        if not args.links_only:
            issues += check_related(doc, fm, slug_index)
        if not args.related_only:
            issues += check_body_links(doc, text)

        if issues:
            rel = doc.relative_to(root).as_posix()
            print(f"\n{rel}")
            for issue in issues:
                print(f"  {issue}")
            total_issues += len(issues)
        checked += 1

    print(f"\nchecked {checked} doc(s): {total_issues} issue(s)")
    return 0 if total_issues == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
