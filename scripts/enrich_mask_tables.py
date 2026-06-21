#!/usr/bin/env python3
"""Add XML Text column to bit-mask tables in *-mask.md docs under kb/encoding/.

Each mask doc has a Fields & Structure section with a two-column bit table:

    | Bit | <Usage / Category / Status> |

This script inserts an ``XML Text`` column immediately after the second column:

    | Bit | <Usage / Category / Status> | XML Text |

The XML Text for each bit is derived by applying the standard KMIP-ENCODE
§6.1.3 CamelCase algorithm (shared with populate_tag_fields.py) to the bit
name in the second column, e.g. "Wrap Key" → ``WrapKey``,
"On-Line Storage" → ``OnLineStorage``.

The insertion is idempotent: tables that already carry an ``XML Text`` column
are skipped entirely.

Usage:
    python scripts/enrich_mask_tables.py [--dry-run] [--check] [--kb PATH]

Options:
    --dry-run    Report changes without writing files.
    --check      Exit non-zero if any file would change (CI guard); implies
                 --dry-run.
    --kb PATH    Root KB directory to scan (default: kb/).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from populate_tag_fields import to_xml_element  # noqa: E402

_SEP_RE = re.compile(r'^\s*\|?[\s:|-]*-[\s:|-]*\|?\s*$')
BIT_HEADER = "Bit"


def _split_row(line: str) -> list[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def _render_row(cells: list[str]) -> str:
    return "| " + " | ".join(cells) + " |"


def process_text(text: str) -> tuple[str, int, int]:
    """Add XML Text column to bit-mask tables. Returns (new_text, tables, rows_filled)."""
    lines = text.splitlines(keepends=False)
    out: list[str] = []
    i = 0
    n = len(lines)
    in_fence = False
    tables = rows_filled = 0

    while i < n:
        line = lines[i]
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            out.append(line)
            i += 1
            continue

        is_header = (
            not in_fence
            and line.lstrip().startswith("|")
            and i + 1 < n
            and _SEP_RE.match(lines[i + 1])
        )
        if is_header:
            header = _split_row(line)
            if (
                header
                and header[0] == BIT_HEADER
                and len(header) >= 2
                and "XML Text" not in header
            ):
                j = i + 2
                data: list[list[str]] = []
                while j < n and lines[j].lstrip().startswith("|"):
                    data.append(_split_row(lines[j]))
                    j += 1

                xml_idx = 2  # insert after the name column (index 1)
                new_header = header[:xml_idx] + ["XML Text"] + header[xml_idx:]
                new_rows = []
                filled = 0
                for row in data:
                    bit_name = row[1].strip() if len(row) > 1 else ""
                    xml_t = to_xml_element(bit_name) if bit_name else ""
                    new_row = row[:xml_idx] + [f"`{xml_t}`" if xml_t else ""] + row[xml_idx:]
                    new_rows.append(new_row)
                    if xml_t:
                        filled += 1

                out.append(_render_row(new_header))
                out.append("|" + "---|" * len(new_header))
                for r in new_rows:
                    out.append(_render_row(r))
                tables += 1
                rows_filled += filled
                i = j
                continue

        out.append(line)
        i += 1

    new_text = "\n".join(out)
    if text.endswith("\n") and not new_text.endswith("\n"):
        new_text += "\n"
    return new_text, tables, rows_filled


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Add XML Text column to bit-mask tables in *-mask.md docs."
    )
    ap.add_argument("--dry-run", action="store_true",
                    help="Report changes without writing files.")
    ap.add_argument("--check", action="store_true",
                    help="Exit non-zero if any file would change (implies --dry-run).")
    ap.add_argument("--kb", default="kb",
                    help="Root KB directory to scan (relative to repo root).")
    args = ap.parse_args()
    dry = args.dry_run or args.check

    repo_root = Path(__file__).resolve().parent.parent
    kb_root = repo_root / args.kb
    if not kb_root.exists():
        sys.exit(f"ERROR: kb directory not found: {kb_root}")

    encoding_dir = kb_root / "encoding"
    if not encoding_dir.exists():
        sys.exit(f"ERROR: encoding directory not found: {encoding_dir}")

    changed = total_tables = total_rows = 0

    for doc in sorted(encoding_dir.glob("*-mask.md")):
        text = doc.read_text(encoding="utf-8")
        new_text, ntables, nrows = process_text(text)
        if ntables:
            total_tables += ntables
            total_rows += nrows
        if new_text != text:
            changed += 1
            rel = doc.relative_to(repo_root)
            verb = "[DRY RUN]" if dry else "WRITE   "
            print(f"  {verb}  {rel}  ({ntables} table(s), {nrows} row(s))")
            if not dry:
                doc.write_text(new_text, encoding="utf-8")

    suffix = "would be updated" if dry else "updated"
    print(f"\nResults: {changed} file(s) {suffix} | "
          f"{total_tables} mask table(s) | {total_rows} row(s) with XML Text")
    if args.check and changed:
        sys.exit(1)


if __name__ == "__main__":
    main()
