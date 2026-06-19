#!/usr/bin/env python3
"""Add Tag (hex) and XML Text columns to field tables in KB docs.

Many KB articles describe a KMIP structure or operation payload with a Markdown
table whose first column lists the *fields* of that structure.  Most of those
field names are themselves named KMIP tags (§11.56 Tag Enumeration), so each
row can be annotated with the field's 6-digit hex tag value and its CamelCase
XML element name — the same two identifiers carried in front matter by ``populate_tag_fields.py``
as ``tag_hex`` and ``xml_text``.

This script enriches every table whose header's first column is exactly
``Field`` by inserting two columns immediately after it::

    | Field | Tag | XML Text | <existing columns...> |

* ``Tag``         — 6-digit uppercase hex in backticks, e.g. ``420057``.
* ``XML Text`` — CamelCase element name in backticks, e.g. ``ObjectType``.

A table that already has a ``Tag`` column (the TTLV structure tables use
``Field | Tag | Type | Required``) keeps it and only gains the ``XML Text``
column right after it.  Rows whose field is not a named tag get blank cells.
Cells already populated (e.g. an existing hex Tag value) are left untouched, so
the script is idempotent and safe to re-run.

The tag lookup is shared with ``populate_tag_fields.py`` and is built from the
v2.1 spec plus the v1.x/v2.0 specs (for tags removed in v2.0).

Usage:
    python scripts/enrich_field_tables.py [--dry-run] [--kb PATH] [--check]

Options:
    --dry-run    Report what would change without writing any files.
    --check      Exit non-zero if any file would change (CI guard); implies
                 --dry-run.
    --kb PATH    Root KB directory to scan (default: kb/).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Reuse the tag lookup + name->XML conversion already used for front matter.
from populate_tag_fields import build_tag_lookup, to_xml_element  # noqa: F401

# Header first-column labels that trigger enrichment.
FIELD_HEADER = "Field"
TAG_HEADER = "Tag"

# A Markdown table separator row, e.g. ``|---|---|`` or ``| :--- | ---: |``.
_SEP_RE = re.compile(r'^\s*\|?[\s:|-]*-[\s:|-]*\|?\s*$')

# ``[text](link)`` -> ``text``
_LINK_RE = re.compile(r'\[([^\]]+)\]\([^)]*\)')


def _split_row(line: str) -> list[str]:
    """Split a Markdown table row into trimmed cell strings."""
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def _render_row(cells: list[str]) -> str:
    return "| " + " | ".join(cells) + " |"


def clean_field_name(cell: str) -> str:
    """Reduce a field-cell to the bare tag name for lookup.

    Strips Markdown links, bold/inline-code markers, and a trailing
    parenthetical (often an inline hex value), then collapses whitespace.
    """
    text = _LINK_RE.sub(r'\1', cell)
    text = re.sub(r'\s*\([^)]*\)\s*$', '', text)   # trailing "(...)"
    text = text.replace('`', '').replace('*', '')
    return re.sub(r'\s+', ' ', text).strip()


def enrich_table(header: list[str], rows: list[list[str]],
                 tags: dict[str, tuple[str, str]],
                 rev_tags: dict[str, str] | None = None,
                 ) -> tuple[list[str], list[list[str]], int, int]:
    """Return (new_header, new_rows, filled, orig_ncols) for one field table.

    Two modes:
    * Field-first (``header[0] == "Field"``): inserts ``Tag`` then
      ``XML Text`` columns after ``Field``; fills both from the name→tag
      lookup.
    * Tag-first (``header[0] == "Tag"``): the Tag column is already present
      at index 0; only inserts ``XML Text`` at index 1 and fills it via
      the hex→element reverse lookup (``rev_tags``).

    ``filled`` counts rows that matched a tag.
    """
    header = list(header)
    rows = [list(r) for r in rows]
    ncols = len(header)
    tag_first = header[0] == TAG_HEADER

    if tag_first:
        # Tag column is already at index 0; don't insert another one.
        tag_idx = 0
    else:
        # Field-first: ensure Tag column immediately after Field (index 0).
        if "Tag" in header:
            tag_idx = header.index("Tag")
        else:
            tag_idx = 1
            header.insert(tag_idx, "Tag")
            for r in rows:
                r.insert(min(tag_idx, len(r)), "")

    # Ensure an XML Text column immediately after Tag.
    if "XML Text" in header:
        xml_idx = header.index("XML Text")
    else:
        xml_idx = tag_idx + 1
        header.insert(xml_idx, "XML Text")
        for r in rows:
            r.insert(min(xml_idx, len(r)), "")

    filled = 0
    for r in rows:
        # Defend against ragged rows: pad to header width.
        while len(r) < len(header):
            r.append("")

        if tag_first:
            # Reverse lookup: hex tag value → XML element name.
            hex_val = r[0].strip().strip("`").upper()
            if rev_tags and hex_val and not r[xml_idx].strip():
                xml_el = rev_tags.get(hex_val)
                if xml_el:
                    r[xml_idx] = f"`{xml_el}`"
                    filled += 1
        else:
            name = clean_field_name(r[0])
            entry = tags.get(name.lower())
            if not entry:
                continue
            hex6, xml_el = entry
            if not r[tag_idx].strip():
                r[tag_idx] = f"`{hex6}`"
            if not r[xml_idx].strip():
                r[xml_idx] = f"`{xml_el}`"
            filled += 1

    return header, rows, filled, ncols


def process_text(text: str, tags: dict[str, tuple[str, str]]) -> tuple[str, int, int]:
    """Enrich every field table in a document. Returns (new_text, tables, rows_filled)."""
    lines = text.splitlines(keepends=False)
    out: list[str] = []
    i = 0
    n = len(lines)
    in_fence = False
    tables = rows_filled = 0
    # Reverse lookup: hex6 → xml_el (for Tag-first tables).
    rev_tags = {hex6: xml_el for hex6, xml_el in tags.values()}

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
            if header and header[0] in (FIELD_HEADER, TAG_HEADER):
                # Collect contiguous data rows.
                j = i + 2
                data: list[list[str]] = []
                ragged = False
                while j < n and lines[j].lstrip().startswith("|"):
                    cells = _split_row(lines[j])
                    if len(cells) != len(header):
                        ragged = True
                        break
                    data.append(cells)
                    j += 1
                if ragged:
                    # Leave the whole table untouched; emit verbatim.
                    out.append(line)
                    i += 1
                    continue
                new_header, new_rows, filled, _ = enrich_table(header, data, tags, rev_tags)
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
        description="Add Tag (hex) and XML Text columns to KB field tables.")
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

    tags = build_tag_lookup(repo_root)

    changed = total_tables = total_rows = 0
    for doc in sorted(kb_root.rglob("*.md")):
        text = doc.read_text(encoding="utf-8")
        new_text, ntables, nrows = process_text(text, tags)
        if ntables:
            total_tables += ntables
            total_rows += nrows
        if new_text != text:
            changed += 1
            rel = doc.relative_to(repo_root)
            verb = "[DRY RUN]" if dry else "WRITE   "
            print(f"  {verb}  {rel}  ({ntables} table(s), {nrows} row(s) tagged)")
            if not dry:
                doc.write_text(new_text, encoding="utf-8")

    suffix = "would be updated" if dry else "updated"
    print(f"\nResults: {changed} file(s) {suffix} | "
          f"{total_tables} field table(s) | {total_rows} row(s) carry a tag")
    if args.check and changed:
        sys.exit(1)


if __name__ == "__main__":
    main()
