#!/usr/bin/env python3
"""Report authoring status for the KMIP knowledge base.

Walks every KB category directory, reads front-matter status fields, and
prints a per-category progress table plus quality warnings. Excludes index.md
files and infrastructure directories (schemas/, versions/, mappings/).

Usage:
    python scripts/status_report.py
    python scripts/status_report.py --category operations
    python scripts/status_report.py --next 10
    python scripts/status_report.py --next 5 --category attributes
    python scripts/status_report.py --json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_kb_scaffold import read_front_matter  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent

# Content directories to track (infrastructure dirs are excluded).
CONTENT_DIRS = [
    "kb/attributes",
    "kb/concepts",
    "kb/objects",
    "kb/operations",
    "kb/operations/server-to-client",
    "kb/profiles",
    "kb/references",
    "kb/ttlv",
    "kb/workflows",
    "kb/examples",
    "kb/usage-guide",
]

# Human-readable labels for display grouping (sub-dirs collapse under parent).
_DISPLAY_LABEL = {
    "kb/operations/server-to-client": "kb/operations/server-to-client",
}


def collect_docs(root: Path, dirs: list[str]) -> list[dict]:
    """Return one record per non-index .md file across the given directories."""
    docs = []
    for rel_dir in dirs:
        d = root / rel_dir
        if not d.exists():
            continue
        for f in sorted(d.glob("*.md")):
            if f.name == "index.md":
                continue
            fm = read_front_matter(f)
            status = (fm or {}).get("status", "unknown")
            title = (fm or {}).get("title", f.stem)
            keywords = (fm or {}).get("keywords", [])
            related = (fm or {}).get("related", [])
            docs.append({
                "path": f.relative_to(root).as_posix(),
                "category": rel_dir,
                "stem": f.stem,
                "title": title,
                "status": status,
                "keywords_empty": isinstance(keywords, list) and len(keywords) == 0,
                "related_empty": isinstance(related, list) and len(related) == 0,
            })
    return docs


def build_table(docs: list[dict], categories: list[str]) -> list[dict]:
    rows = []
    for cat in categories:
        cat_docs = [d for d in docs if d["category"] == cat]
        if not cat_docs:
            continue
        stub = sum(1 for d in cat_docs if d["status"] == "stub")
        draft = sum(1 for d in cat_docs if d["status"] == "draft")
        reviewed = sum(1 for d in cat_docs if d["status"] == "reviewed")
        total = len(cat_docs)
        done = draft + reviewed
        pct = int(100 * done / total) if total else 0
        rows.append({
            "category": cat,
            "total": total,
            "stub": stub,
            "draft": draft,
            "reviewed": reviewed,
            "pct": pct,
        })
    return rows


def quality_warnings(docs: list[dict]) -> list[str]:
    warnings = []
    authored = [d for d in docs if d["status"] in ("draft", "reviewed")]
    empty_kw = [d["path"] for d in authored if d["keywords_empty"]]
    empty_rel = [d["path"] for d in authored if d["related_empty"]]
    if empty_kw:
        warnings.append(f"  {len(empty_kw)} authored doc(s) with empty keywords:")
        for p in empty_kw[:10]:
            warnings.append(f"    {p}")
        if len(empty_kw) > 10:
            warnings.append(f"    ... and {len(empty_kw) - 10} more")
    if empty_rel:
        warnings.append(f"  {len(empty_rel)} authored doc(s) with empty related:")
        for p in empty_rel[:10]:
            warnings.append(f"    {p}")
        if len(empty_rel) > 10:
            warnings.append(f"    ... and {len(empty_rel) - 10} more")
    return warnings


def print_table(rows: list[dict], docs: list[dict], args) -> None:
    col_w = max((len(r["category"]) for r in rows), default=10) + 2
    header = f"{'Category':<{col_w}}  {'Total':>5}  {'stub':>5}  {'draft':>5}  {'reviewed':>8}  Progress"
    sep = "-" * len(header)
    print(header)
    print(sep)
    for r in rows:
        bar = f"{r['pct']:3d}%"
        print(f"{r['category']:<{col_w}}  {r['total']:>5}  {r['stub']:>5}  "
              f"{r['draft']:>5}  {r['reviewed']:>8}  {bar}")
    print(sep)
    total_docs = sum(r["total"] for r in rows)
    total_stub = sum(r["stub"] for r in rows)
    total_draft = sum(r["draft"] for r in rows)
    total_reviewed = sum(r["reviewed"] for r in rows)
    total_done = total_draft + total_reviewed
    total_pct = int(100 * total_done / total_docs) if total_docs else 0
    print(f"{'TOTAL':<{col_w}}  {total_docs:>5}  {total_stub:>5}  "
          f"{total_draft:>5}  {total_reviewed:>8}  {total_pct:3d}%")

    warnings = quality_warnings(docs)
    if warnings:
        print()
        print("Quality warnings:")
        for w in warnings:
            print(w)

    if args.next:
        stubs = [d for d in docs if d["status"] == "stub"]
        if args.category:
            stubs = [d for d in stubs if d["category"] == args.category]
        n = args.next
        print()
        print(f"Next {min(n, len(stubs))} stub(s) to author"
              + (f" in {args.category}" if args.category else "") + ":")
        for i, d in enumerate(stubs[:n], 1):
            print(f"  {i:>3}.  {d['path']:<50}  {d['title']}")
        if not stubs:
            print("  (none — all docs are authored!)")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--category", default=None,
                   help="Restrict report to one category directory (e.g. attributes)")
    p.add_argument("--next", type=int, default=None, metavar="N",
                   help="List the next N stubs to author (default: 5 when flag given)")
    p.add_argument("--json", action="store_true",
                   help="Output machine-readable JSON instead of the table")
    p.add_argument("--out", default=".", help="Repo root (default: current dir)")
    args = p.parse_args(argv)

    # --next with no value means 5
    if "--next" in (argv or sys.argv[1:]) and args.next is None:
        args.next = 5

    root = Path(args.out).resolve()
    dirs = CONTENT_DIRS
    if args.category:
        dirs = [d for d in dirs if d == args.category or d.startswith(args.category + "/")]
        if not dirs:
            print(f"ERROR: unknown category {args.category!r}. "
                  f"Valid: {', '.join(CONTENT_DIRS)}", file=sys.stderr)
            return 2

    docs = collect_docs(root, dirs)
    if not docs:
        print("No KB documents found. Has the scaffold been generated?")
        return 1

    rows = build_table(docs, dirs)

    if args.json:
        payload = {
            "categories": rows,
            "totals": {
                "total": sum(r["total"] for r in rows),
                "stub": sum(r["stub"] for r in rows),
                "draft": sum(r["draft"] for r in rows),
                "reviewed": sum(r["reviewed"] for r in rows),
            },
            "quality_warnings": quality_warnings(docs),
            "next_stubs": [
                {"path": d["path"], "title": d["title"]}
                for d in docs if d["status"] == "stub"
            ][:args.next or 0] if args.next else [],
        }
        print(json.dumps(payload, indent=2))
        return 0

    print(f"KMIP Knowledge Base — Authoring Status")
    print()
    print_table(rows, docs, args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
