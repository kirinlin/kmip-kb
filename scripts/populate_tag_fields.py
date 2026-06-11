#!/usr/bin/env python3
"""Add tag_hex and xml_element to KB docs that map to a named KMIP tag.

Parses §11.56 Tag Enumeration from raw/kmip/kmip-spec/v2.1/kmip-spec-v2.1.md,
builds a name→hex lookup, then for each KB doc whose title exactly matches a
tag name inserts two frontmatter fields:

    tag_hex: "42000D"          # 6-char uppercase hex, no 0x prefix
    xml_element: "BatchCount"  # CamelCase XML element name per KMIP XML encoding

Fields are only added if absent; already-populated docs are skipped.

Usage:
    python scripts/populate_tag_fields.py [--dry-run] [--spec PATH] [--kb PATH]

Options:
    --dry-run    Print matches without writing any files.
    --spec PATH  Path to KMIP v2.1 spec markdown
                 (default: raw/kmip/kmip-spec/v2.1/kmip-spec-v2.1.md).
    --kb PATH    Root KB directory to scan (default: kb/).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


# --------------------------------------------------------------------------- #
# CamelCase conversion
# --------------------------------------------------------------------------- #

def to_xml_element(name: str) -> str:
    """Convert a KMIP tag name to its CamelCase XML element name.

    Implements the official KMIP-ENCODE §6.1.3 normalisation algorithm:
      1. Replace ( ) with spaces
      2. Non-word char followed by [letter][lowercase] → replace with space
      3. Remaining non-word chars (not whitespace) → underscore
      4. First word starting with digit → move leading digits to end
      5. Capitalise first letter of each word
      6. Concatenate with spaces removed

    Verified against KMIP v2.1 test-case XML files.

    >>> to_xml_element("Batch Count")
    'BatchCount'
    >>> to_xml_element("IV/Counter/Nonce")
    'IVCounterNonce'
    >>> to_xml_element("X.509 Certificate Identifier")
    'X_509CertificateIdentifier'
    >>> to_xml_element("PKCS#12 Friendly Name")
    'PKCS_12FriendlyName'
    >>> to_xml_element("MAC/Signature")
    'MACSignature'
    >>> to_xml_element("D")
    'D'
    """
    s = name
    # Rule 1
    s = s.replace('(', ' ').replace(')', ' ')
    # Rule 2: non-word char before [letter][lower-letter] → space
    s = re.sub(r'[^A-Za-z0-9_](?=[A-Za-z][a-z])', ' ', s)
    # Rule 3: remaining non-word chars (not whitespace) → underscore
    s = re.sub(r'[^A-Za-z0-9_\s]', '_', s)
    # Split into words
    words = s.split()
    # Rule 4: first word starting with digit → move leading digits to end
    if words and words[0] and words[0][0].isdigit():
        m = re.match(r'^(\d+)(.*)', words[0])
        if m:
            words[0] = m.group(2) + m.group(1)
    # Rule 5: capitalise first letter of each word
    words = [w[0].upper() + w[1:] if w else w for w in words]
    # Rule 6: concatenate
    return ''.join(words)


# --------------------------------------------------------------------------- #
# Parse §11.56 Tag Enumeration
# --------------------------------------------------------------------------- #

def _normalize_hex(val: str) -> str:
    val = val.strip()
    return val[2:].upper() if val.lower().startswith("0x") else val.upper()


def parse_tag_table(spec_path: Path) -> dict[str, tuple[str, str]]:
    """Return {tag_name_lower: (hex6, xml_element)} from §11.56 Tag Enumeration."""
    text = spec_path.read_text(encoding="utf-8")

    start = text.find("## 11.56 Tag Enumeration")
    if start == -1:
        sys.exit(f"ERROR: '## 11.56 Tag Enumeration' not found in {spec_path}")

    # Slice to the next ## heading so we don't parse past the table
    rest = text[start:]
    next_sec = re.search(r'\n## ', rest[5:])
    section = rest[: next_sec.start() + 5] if next_sec else rest

    tags: dict[str, tuple[str, str]] = {}

    for line in section.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")]
        # After split: ['', cell1, cell2, '']
        if len(cells) < 3:
            continue
        name = cells[1]
        value = cells[2]

        # Skip header, separator, empty rows
        if not name or not value:
            continue
        if name.startswith("-") or name.startswith("*") or name.startswith("("):
            continue
        if "Reserved" in name or "Unused" in name or "Extensions" in name:
            continue

        # Validate that value is a plain hex string (no ranges, no X placeholders)
        clean = value[2:] if value.lower().startswith("0x") else value
        if not re.fullmatch(r'[0-9A-Fa-f]{4,8}', clean):
            continue

        hex6 = _normalize_hex(value)
        tags[name.lower()] = (hex6, to_xml_element(name))

    return tags


# --------------------------------------------------------------------------- #
# Frontmatter helpers
# --------------------------------------------------------------------------- #

_FM_END_RE = re.compile(r'\n---(?:\n|$)')


def _frontmatter_end(text: str) -> int:
    """Return the index of the \\n that precedes the closing --- marker, or -1."""
    if not text.startswith("---\n"):
        return -1
    m = _FM_END_RE.search(text, 3)
    return m.start() if m else -1


def _has_field(text: str, field: str) -> bool:
    end = _frontmatter_end(text)
    if end == -1:
        return False
    fm = text[3:end]
    return bool(re.search(rf'^{re.escape(field)}\s*:', fm, re.MULTILINE))


def _read_title(text: str) -> str | None:
    end = _frontmatter_end(text)
    if end == -1:
        return None
    fm = text[3:end]
    m = re.search(r'^title:\s+(.+)$', fm, re.MULTILINE)
    if not m:
        return None
    return m.group(1).strip().strip('"').strip("'")


def _insert_tag_fields(text: str, tag_hex: str, xml_element: str) -> str:
    """Append tag_hex and xml_element lines just before the closing --- of frontmatter."""
    end = _frontmatter_end(text)
    if end == -1:
        return text
    insertion = f'\ntag_hex: "{tag_hex}"\nxml_element: "{xml_element}"'
    return text[:end] + insertion + text[end:]


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

def main() -> None:
    ap = argparse.ArgumentParser(
        description="Populate tag_hex and xml_element frontmatter fields in KB docs."
    )
    ap.add_argument("--dry-run", action="store_true",
                    help="Print matches without writing files.")
    ap.add_argument("--spec",
                    default="raw/kmip/kmip-spec/v2.1/kmip-spec-v2.1.md",
                    help="Path to v2.1 spec markdown (relative to repo root).")
    ap.add_argument("--kb", default="kb",
                    help="Root KB directory to scan (relative to repo root).")
    args = ap.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    spec_path = repo_root / args.spec
    kb_root = repo_root / args.kb

    if not spec_path.exists():
        sys.exit(f"ERROR: spec not found: {spec_path}")
    if not kb_root.exists():
        sys.exit(f"ERROR: kb directory not found: {kb_root}")

    print(f"Parsing tag table from {args.spec} ...")
    tags = parse_tag_table(spec_path)
    print(f"  Loaded {len(tags)} named tags.\n")

    docs = sorted(kb_root.rglob("*.md"))
    matched = skipped_existing = unmatched = 0

    for doc in docs:
        text = doc.read_text(encoding="utf-8")
        title = _read_title(text)
        if not title:
            continue

        entry = tags.get(title.lower())
        if entry is None:
            unmatched += 1
            continue

        hex6, xml_el = entry

        if _has_field(text, "tag_hex"):
            skipped_existing += 1
            continue

        rel = doc.relative_to(repo_root)
        verb = "[DRY RUN]" if args.dry_run else "WRITE   "
        print(f"  {verb}  {rel}  →  {hex6}  /  {xml_el}")

        if not args.dry_run:
            doc.write_text(_insert_tag_fields(text, hex6, xml_el), encoding="utf-8")

        matched += 1

    suffix = "would be updated" if args.dry_run else "updated"
    print(
        f"\nResults: {matched} {suffix} | "
        f"{skipped_existing} already had tag_hex | "
        f"{unmatched} titles without a matching tag"
    )
    if args.dry_run and matched:
        print("Re-run without --dry-run to apply changes.")


if __name__ == "__main__":
    main()
