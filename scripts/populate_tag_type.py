#!/usr/bin/env python3
"""Add tag_type frontmatter field to KB docs that already have tag_hex and xml_text.

Scans all KMIP test-case XML files under raw/ to build a lookup
{xml_element_name: ttlv_type}. Each element is classified by its `type=`
attribute: Integer → "Integer", Enumeration → "Enumeration", etc. Elements
without a `type=` attribute are classified as "Structure" (KMIP structure
items are container elements with no type annotation in XML encoding).

Must be run after populate_tag_fields.py (requires tag_hex + xml_text to be
present). Docs that already have tag_type are skipped. Docs whose tag is
genuinely polymorphic (same xml_text maps to different types in different
contexts) are skipped with a warning; they must be populated manually.

Usage:
    python scripts/populate_tag_type.py [--dry-run] [--check] [--kb PATH] [--raw PATH]

Options:
    --dry-run    Print what would be written without modifying files.
    --check      Exit non-zero if any resolvable doc is missing tag_type.
    --kb PATH    Root KB directory (default: kb/).
    --raw PATH   Root raw directory containing XML test cases (default: raw/).
"""
from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

# Map XML `type=` attribute values → canonical TTLV type names (§10.1 names)
_XML_TYPE_TO_TTLV: dict[str, str] = {
    "Integer": "Integer",
    "LongInteger": "Long Integer",
    "BigInteger": "Big Integer",
    "Enumeration": "Enumeration",
    "Boolean": "Boolean",
    "TextString": "Text String",
    "ByteString": "Byte String",
    "DateTime": "Date-Time",
    "DateTimeExtended": "Date-Time Extended",
    "Interval": "Interval",
}

# Top-level XML wrapper element — not a KMIP tag; excluded from the lookup.
_XML_WRAPPER = {"KMIP"}

# Static type overrides for tags absent from the XML test-case corpus or where
# a false conflict exists from an edge-case test file. Types derived directly
# from the KMIP spec: v2.1 §4/§9 for current attributes/messages; v1.x §3 for
# del_v2 tags; the kmip-testcases/ (official) subset for conflict resolution.
_STATIC_OVERRIDES: dict[str, str] = {
    # Attributes not exercised in the KMIP XML test suite
    "ArchiveDate": "Date-Time",
    "Comment": "Text String",
    "CompromiseDate": "Date-Time",
    "CustomAttribute": "Structure",
    "NISTKeyType": "Enumeration",
    "OperationPolicyName": "Text String",
    "RotateDate": "Date-Time",
    "RotateInterval": "Interval",
    "RotateOffset": "Interval",
    # Del-v2 attributes whose TTLV type is a Structure (v1.x spec §3.13–§3.15)
    "CertificateIdentifier": "Structure",
    "CertificateIssuer": "Structure",
    "CertificateSubject": "Structure",
    # Message fields not in XML test cases (v2.1 spec §9)
    "AttestationCapableIndicator": "Boolean",
    "MessageExtension": "Structure",
    "Nonce": "Structure",
    # Structures not in XML test cases
    "ExtensionInformation": "Structure",
    "PKCS_11Interface": "Structure",
    "ProfileVersion": "Structure",
    "ProtectionStorageMasks": "Structure",
    # Conflict resolution: ResultMessage is Text String in v2.1.  One profile
    # test file (QS-M-2-20.xml) encodes it as Enumeration in error, creating a
    # spurious conflict.
    "ResultMessage": "Text String",
}


# --------------------------------------------------------------------------- #
# Build type lookup from XML test cases
# --------------------------------------------------------------------------- #

def _build_type_lookup(
    raw_root: Path,
) -> tuple[dict[str, str], dict[str, set[str]]]:
    """Scan all *.xml files under raw_root and return (type_map, conflicts).

    type_map  — {xml_element_name: ttlv_type} for elements whose type is
                the same in every file they appear in.
    conflicts — {xml_element_name: set[ttlv_type]} for elements that appear
                with more than one type across the corpus.
    """
    all_types: dict[str, set[str]] = defaultdict(set)

    xml_files = list(raw_root.rglob("*.xml"))
    if not xml_files:
        sys.exit(
            f"ERROR: no XML files found under {raw_root}.\n"
            "Run the crawler (scripts/kmip_crawler.py) first to populate raw/."
        )

    for xml_file in xml_files:
        try:
            tree = ET.parse(xml_file)
        except ET.ParseError:
            continue
        for elem in tree.iter():
            name = elem.tag
            if "}" in name:  # strip XML namespace prefix
                name = name.split("}", 1)[1]
            if name in _XML_WRAPPER:
                continue
            type_attr = elem.get("type")
            if type_attr is not None:
                ttlv = _XML_TYPE_TO_TTLV.get(type_attr, type_attr)
            else:
                ttlv = "Structure"
            all_types[name].add(ttlv)

    type_map: dict[str, str] = {}
    conflicts: dict[str, set[str]] = {}
    for name, types in all_types.items():
        if len(types) == 1:
            type_map[name] = next(iter(types))
        else:
            conflicts[name] = types

    return type_map, conflicts


# --------------------------------------------------------------------------- #
# Conflict resolution
# --------------------------------------------------------------------------- #

def _resolve_conflict(
    xml_text: str, category: str, types: set[str]
) -> str | None:
    """Try to resolve an ambiguous type using the KB document's category.

    Returns the resolved TTLV type string, or None if the conflict cannot be
    resolved without manual inspection.
    """
    # Enumeration KB docs always encode as Enumeration
    if category == "enumerations" and "Enumeration" in types:
        return "Enumeration"
    # Structure, operation, and object KB docs always encode as Structure
    if category in ("structures", "operation", "object") and "Structure" in types:
        return "Structure"
    # For other categories: if exactly one non-Structure type appears,
    # the tag is a leaf value (not a container) and the non-structure type wins
    non_struct = types - {"Structure"}
    if len(non_struct) == 1:
        return next(iter(non_struct))
    return None


def _category_fallback(category: str) -> str | None:
    """Return a TTLV type for tags absent from the XML corpus, based on category.

    Enumerations, structures, operation, and object categories have deterministic
    TTLV types regardless of what the XML test suite covers.
    """
    if category == "enumerations":
        return "Enumeration"
    if category in ("structures", "operation", "object"):
        return "Structure"
    return None


# --------------------------------------------------------------------------- #
# Frontmatter helpers
# --------------------------------------------------------------------------- #

_FM_END_RE = re.compile(r"\n---(?:\n|$)")


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
    return bool(re.search(rf"^{re.escape(field)}\s*:", fm, re.MULTILINE))


def _get_field(text: str, field: str) -> str | None:
    """Return the scalar value of a frontmatter field, or None."""
    end = _frontmatter_end(text)
    if end == -1:
        return None
    fm = text[3:end]
    m = re.search(
        rf'^{re.escape(field)}:\s+(?:"([^"]+)"|(\S[^\n]*))\s*$',
        fm,
        re.MULTILINE,
    )
    if not m:
        return None
    return (m.group(1) or m.group(2)).strip()


def _insert_tag_type(text: str, tag_type: str) -> str:
    """Append a tag_type line just before the closing --- of frontmatter."""
    end = _frontmatter_end(text)
    if end == -1:
        return text
    return text[:end] + f'\ntag_type: "{tag_type}"' + text[end:]


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

def main() -> None:
    ap = argparse.ArgumentParser(
        description="Populate tag_type frontmatter field in KB docs."
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be written without modifying files.",
    )
    ap.add_argument(
        "--check",
        action="store_true",
        help="Exit non-zero if any resolvable doc is missing tag_type.",
    )
    ap.add_argument(
        "--kb",
        default="kb",
        help="Root KB directory to scan (default: kb/).",
    )
    ap.add_argument(
        "--raw",
        default="raw",
        help="Root raw spec directory containing XML test cases (default: raw/).",
    )
    args = ap.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    kb_root = repo_root / args.kb
    raw_root = repo_root / args.raw

    if not kb_root.exists():
        sys.exit(f"ERROR: kb directory not found: {kb_root}")
    if not raw_root.exists():
        sys.exit(
            f"ERROR: raw directory not found: {raw_root}\n"
            "Run scripts/kmip_crawler.py first."
        )

    print("Scanning XML test-case files for TTLV type information ...")
    type_map, conflicts = _build_type_lookup(raw_root)
    print(
        f"  {len(type_map)} unambiguous element types, "
        f"{len(conflicts)} conflicting elements.\n"
    )

    docs = sorted(kb_root.rglob("*.md"))
    updated = already_done = no_tag = ambiguous = 0

    for doc in docs:
        text = doc.read_text(encoding="utf-8")

        if not _has_field(text, "tag_hex"):
            no_tag += 1
            continue
        if _has_field(text, "tag_type"):
            already_done += 1
            continue

        xml_text = _get_field(text, "xml_text")
        if not xml_text:
            ambiguous += 1
            print(f"  SKIP (no xml_text): {doc.relative_to(repo_root)}")
            continue

        category = _get_field(text, "category") or ""

        if xml_text in _STATIC_OVERRIDES:
            tag_type = _STATIC_OVERRIDES[xml_text]
        elif xml_text in type_map:
            tag_type = type_map[xml_text]
        elif xml_text in conflicts:
            tag_type_or_none = _resolve_conflict(
                xml_text, category, conflicts[xml_text]
            )
            if tag_type_or_none is None:
                tag_type_or_none = _category_fallback(category)
            if tag_type_or_none is None:
                ambiguous += 1
                print(
                    f"  SKIP (ambiguous {sorted(conflicts[xml_text])}): "
                    f"{doc.relative_to(repo_root)}"
                )
                continue
            tag_type = tag_type_or_none
        else:
            tag_type_or_none = _category_fallback(category)
            if tag_type_or_none is None:
                ambiguous += 1
                print(
                    f"  SKIP (not in XML lookup): {doc.relative_to(repo_root)}"
                )
                continue
            tag_type = tag_type_or_none

        updated += 1
        rel = doc.relative_to(repo_root)
        verb = "[DRY RUN]" if (args.dry_run or args.check) else "WRITE   "
        print(f"  {verb}  {rel}  →  {tag_type}")

        if not args.dry_run and not args.check:
            doc.write_text(_insert_tag_type(text, tag_type), encoding="utf-8")

    if args.check:
        print(
            f"\nResults: {updated} stale | {already_done} already populated | "
            f"{ambiguous} unresolvable (manual) | {no_tag} no tag_hex"
        )
        if updated:
            print(f"ERROR: {updated} docs are missing tag_type.")
            sys.exit(1)
        print("OK — all resolvable docs have tag_type.")
        return

    suffix = "would be updated" if args.dry_run else "updated"
    print(
        f"\nResults: {updated} {suffix} | {already_done} already had tag_type | "
        f"{ambiguous} unresolvable (skipped) | {no_tag} no tag_hex"
    )
    if args.dry_run and updated:
        print("Re-run without --dry-run to apply changes.")


if __name__ == "__main__":
    main()
