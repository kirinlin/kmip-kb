#!/usr/bin/env python3
"""Add enumeration value tables to the Fields & Structure section of enumeration docs.

Each kb/enumerations/*.md doc describes a KMIP enumeration whose values are
defined in the spec.  The Fields & Structure section should contain a table with:

    | Name | Value | XML Text | Description |
    |---|---|---|---|
    | Certificate | `00000001` | `Certificate` | ... |

* ``Name``     — enumeration value name from the spec.
* ``Value``    — 8-digit hex integer string in backticks.
* ``XML Text`` — CamelCase text per KMIP-ENCODE §6.1.3 (same algorithm as xml_text
                 front matter, applied to the value name rather than the tag name).
* ``Description`` — left blank; authors fill in per-value descriptions.
                    Omitted entirely for enumerations listed in NO_DESCRIPTION_TABLES
                    where per-value descriptions add no meaning beyond the value name.

The script parses every enumeration section from the v2.1 spec (and v2.0/v1.x for
removed enumerations), then for each KB enumeration doc looks up the spec section
via the source_section front matter field and inserts or corrects the table.

The operation is idempotent: docs whose table header already matches the expected
format are skipped.  Docs in NO_DESCRIPTION_TABLES that carry a stale four-column
header have the Description column removed.

Usage:
    python scripts/enrich_enum_tables.py [--dry-run] [--check] [--kb PATH]

Options:
    --dry-run    Report what would change without writing files.
    --check      Exit non-zero if any file would change (CI guard); implies --dry-run.
    --kb PATH    Root KB directory to scan (default: kb/).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Reuse the CamelCase algorithm from populate_tag_fields.
sys.path.insert(0, str(Path(__file__).parent))
from populate_tag_fields import to_xml_element  # noqa: E402


# --------------------------------------------------------------------------- #
# Whitelist — enumerations whose table omits the Description column because
# per-value descriptions add no meaning beyond the value name itself.
# --------------------------------------------------------------------------- #

NO_DESCRIPTION_TABLES: frozenset[str] = frozenset({
    "adjustment-type-enumeration.md",
    "asynchronous-indicator-enumeration.md",
    "data-enumeration.md",
    "digital-signature-algorithm-enumeration.md",
    "nist-key-type-enumeration.md",
    "operation-enumeration.md",
    "recommended-curve-enumeration.md",
    "tag-enumeration.md",
    "unique-identifier-enumeration.md",
})


# --------------------------------------------------------------------------- #
# Spec parsing — extract enumeration value tables
# --------------------------------------------------------------------------- #

_SECTION_RE = re.compile(r'^## (\d+\.\d+(?:\.\d+)?) (.+?)\s*$', re.MULTILINE)
_PROF_SECTION_RE = re.compile(r'^## (\d+(?:\.\d+)+) (.+?)\s*$', re.MULTILINE)


def _parse_enum_values(section_body: str) -> list[tuple[str, str]] | None:
    """Parse an enumeration value table from a spec section body.

    Returns a list of (name, hex8) pairs, or None if no value table found.
    Skips (Reserved), (Unused), Extensions, and wildcard (8XXXXXXX) rows.
    """
    rows: list[tuple[str, str]] = []
    in_table = False
    past_header = False

    for line in section_body.splitlines():
        if not line.startswith("|"):
            if in_table and rows:
                break  # end of table
            continue
        cells = [c.strip() for c in line.split("|")]
        # Filter out separator lines like |---|---|
        if all(re.fullmatch(r'[-: ]+', c) for c in cells if c):
            past_header = True
            continue
        if len(cells) < 3:
            continue
        name, value = cells[1], cells[2]
        if not name or not value:
            continue
        # Skip header rows
        if name.lower() in ("name", "**name**"):
            in_table = True
            continue
        # Skip column-header bold rows and reserved/extension rows
        if name.startswith("**") and value.startswith("**"):
            continue
        if not past_header and not in_table:
            continue
        # Skip reserved / extension rows
        if re.search(r'Reserved|Unused|Extension', name, re.IGNORECASE):
            continue
        # Skip wildcard hex like 8XXXXXXX
        clean = value.replace(" ", "")
        if re.search(r'[XxYyZz]', clean):
            continue
        # Normalise hex value (strip 0x prefix, not all leading zeros)
        if clean.lower().startswith("0x"):
            clean = clean[2:]
        if not re.fullmatch(r'[0-9A-Fa-f]+', clean):
            continue
        hex8 = clean.upper().zfill(8)
        rows.append((name, hex8))

    return rows if rows else None


def parse_all_enumerations(spec_path: Path) -> dict[str, list[tuple[str, str]]]:
    """Return {section_number: [(name, hex8), ...]} for every enumeration section
    in the given spec file."""
    text = spec_path.read_text(encoding="utf-8")
    matches = list(_SECTION_RE.finditer(text))
    result: dict[str, list[tuple[str, str]]] = {}

    for i, m in enumerate(matches):
        sec_num = m.group(1)
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[m.end(): end]
        rows = _parse_enum_values(body)
        if rows:
            result[sec_num] = rows

    return result


# --------------------------------------------------------------------------- #
# Front matter helpers
# --------------------------------------------------------------------------- #

_FM_END_RE = re.compile(r'\n---(?:\n|$)')


def _frontmatter_end(text: str) -> int:
    if not text.startswith("---\n"):
        return -1
    m = _FM_END_RE.search(text, 3)
    return m.start() if m else -1


def _read_fm_field(text: str, field: str) -> str | None:
    end = _frontmatter_end(text)
    if end == -1:
        return None
    fm = text[3:end]
    m = re.search(rf'^{re.escape(field)}:\s*(.+)$', fm, re.MULTILINE)
    if not m:
        return None
    return m.group(1).strip().strip('"').strip("'")


# --------------------------------------------------------------------------- #
# Table generation and insertion
# --------------------------------------------------------------------------- #

def _render_table(rows: list[tuple[str, str]], with_description: bool = True) -> str:
    """Render the enumeration value table as Markdown."""
    if with_description:
        lines = ["| Name | Value | XML Text | Description |", "|---|---|---|---|"]
        for name, hex8 in rows:
            xml_t = to_xml_element(name)
            lines.append(f"| {name} | `{hex8}` | `{xml_t}` |  |")
    else:
        lines = ["| Name | Value | XML Text |", "|---|---|---|"]
        for name, hex8 in rows:
            xml_t = to_xml_element(name)
            lines.append(f"| {name} | `{hex8}` | `{xml_t}` |")
    return "\n".join(lines)


_FS_HEADING_RE = re.compile(r'^## Fields & Structure\s*$', re.MULTILINE)
_VALUE_TABLE_RE = re.compile(r'\|\s*Name\s*\|')


def insert_enum_table(
    text: str,
    rows: list[tuple[str, str]],
    with_description: bool = True,
) -> str | None:
    """Insert or correct a value table in the Fields & Structure section.

    Returns the modified text, or None if the doc was skipped (table already
    matches expected format, or section is missing).

    When an existing table's header does not match the expected format (e.g. a
    NO_DESCRIPTION_TABLES doc still carries a stale four-column header), the
    entire table block is replaced with a freshly rendered one.
    """
    m = _FS_HEADING_RE.search(text)
    if not m:
        return None

    # Find the content start (after the heading line and any blank lines)
    content_start = m.end()
    while content_start < len(text) and text[content_start] == "\n":
        content_start += 1

    expected_header = (
        "| Name | Value | XML Text | Description |"
        if with_description
        else "| Name | Value | XML Text |"
    )
    table = _render_table(rows, with_description)

    # Check for an existing Name table near the top of the section
    upcoming = text[content_start: content_start + 300]
    existing_m = _VALUE_TABLE_RE.search(upcoming)

    if existing_m:
        # Find the start of the header line (back up to beginning of line)
        table_start = content_start + existing_m.start()
        while table_start > 0 and text[table_start - 1] != "\n":
            table_start -= 1
        # Extract the header line and compare to expected
        header_line = text[table_start:].split("\n", 1)[0]
        if header_line.strip() == expected_header:
            return None  # already correct format
        # Header mismatch: replace the entire table block (header + separator + rows)
        pos = table_start
        for line in text[table_start:].splitlines(True):
            if not line.startswith("|"):
                break
            pos += len(line)
        return text[:table_start] + table + "\n" + text[pos:]

    # No Name table: insert with a blank line before existing content
    existing_content = text[content_start:]
    if existing_content.startswith("<!-- "):
        comment_end = existing_content.find("-->")
        if comment_end != -1:
            comment_end += 3
            while comment_end < len(existing_content) and existing_content[comment_end] == "\n":
                comment_end += 1
            existing_content = existing_content[comment_end:]

    return text[:content_start] + table + "\n\n" + existing_content


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

# Paths to all spec versions; v2.1 is primary, earlier ones add removed enums.
_SPEC_PATHS = [
    ("2.1", "raw/kmip/kmip-spec/v2.1/kmip-spec-v2.1.md"),
    ("2.0", "raw/kmip/kmip-spec/v2.0/kmip-spec-v2.0.md"),
    ("1.4", "raw/kmip/spec/v1.4/kmip-spec-v1.4.md"),
    ("1.3", "raw/kmip/spec/v1.3/kmip-spec-v1.3.md"),
    ("1.2", "raw/kmip/spec/v1.2/kmip-spec-v1.2.md"),
    ("1.1", "raw/kmip/spec/v1.1/os/kmip-spec-v1.1-os.md"),
    ("1.0", "raw/kmip/spec/v1.0/kmip-spec-1.0.md"),
]


def build_enum_lookup(repo_root: Path) -> dict[str, list[tuple[str, str]]]:
    """Build {section_number: rows} from all available spec versions."""
    combined: dict[str, list[tuple[str, str]]] = {}
    for ver, rel in _SPEC_PATHS:
        path = repo_root / rel
        if not path.exists():
            continue
        print(f"  Parsing {rel} ...")
        enums = parse_all_enumerations(path)
        for sec, rows in enums.items():
            if sec not in combined:
                combined[sec] = rows
    return combined


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Add enumeration value tables to Fields & Structure sections."
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

    print("Building enumeration value lookup from spec files...")
    enum_lookup = build_enum_lookup(repo_root)
    print(f"  Found {len(enum_lookup)} enumeration sections.\n")

    enum_dir = kb_root / "enumerations"
    if not enum_dir.exists():
        sys.exit(f"ERROR: enumeration dir not found: {enum_dir}")

    changed = skipped_exists = skipped_no_sec = skipped_no_rows = 0

    for doc in sorted(enum_dir.glob("*.md")):
        if doc.name == "index.md":
            continue
        text = doc.read_text(encoding="utf-8")

        source_sec = _read_fm_field(text, "source_section")
        if not source_sec or source_sec.startswith("prof-") or source_sec.startswith("ug-"):
            skipped_no_sec += 1
            continue

        rows = enum_lookup.get(source_sec)
        if not rows:
            skipped_no_rows += 1
            print(f"  NO DATA  {doc.name}  (section {source_sec})")
            continue

        with_desc = doc.name not in NO_DESCRIPTION_TABLES
        new_text = insert_enum_table(text, rows, with_description=with_desc)
        if new_text is None:
            skipped_exists += 1
            continue

        changed += 1
        rel = doc.relative_to(repo_root)
        verb = "[DRY RUN]" if dry else "WRITE   "
        print(f"  {verb}  {rel}  ({len(rows)} values, desc={'yes' if with_desc else 'no'})")
        if not dry:
            doc.write_text(new_text, encoding="utf-8")

    suffix = "would be updated" if dry else "updated"
    print(
        f"\nResults: {changed} {suffix} | "
        f"{skipped_exists} already correct | "
        f"{skipped_no_rows} sections not found in spec | "
        f"{skipped_no_sec} no source_section"
    )
    if args.check and changed:
        sys.exit(1)


if __name__ == "__main__":
    main()
