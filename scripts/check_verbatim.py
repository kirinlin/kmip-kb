#!/usr/bin/env python3
"""Flag verbatim overlap between authored KB docs and the source spec.

For every authored document (``status: draft`` or ``reviewed``) that records a
``source_section``, this loads that section's text from the raw KMIP spec and
reports any shared run of >= N words (default 8) between the authored prose and
the source. It mechanically enforces the project's central rule: never copy
specification text (see CONTRIBUTING.md, Stage 6).

Comparison is case-folded and reduced to alphanumeric word tokens, so markdown,
punctuation, and capitalization differences are ignored -- only genuine shared
wording trips the check. Protocol field names appear as short tokens and do not
form long shared runs on their own.

Pure standard library.

Usage:
    python scripts/check_verbatim.py [PATH ...] [--n 8] [--version 1.4]

PATH may be a directory (searched recursively for *.md) or a file. Defaults to
``operations``. Exit code is non-zero if any overlap is found.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Reuse front-matter reading and spec-path resolution from the scaffold tool.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_kb_scaffold import read_front_matter, spec_path_for, prof_path_for, ug_path_for  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
HEADING_RE = re.compile(r"^(#{1,6})\s+(\d+(?:\.\d+)*)\s+(.*)$")
WORD_RE = re.compile(r"[a-z0-9]+")

# Front-matter markdown body skeletons emit these; never count them as overlap.
_OUR_HEADINGS = {
    "purpose", "request fields", "response fields",
    "behavior server requirements", "errors", "examples",
    "related operations", "overview", "details", "structure",
}


def tokenize(text: str) -> list[str]:
    return WORD_RE.findall(text.lower())


def extract_section(spec_text: str, section: str) -> str | None:
    """Return the raw text of a dotted spec section, including its subsections."""
    lines = spec_text.splitlines()
    out: list[str] = []
    capturing = False
    child_prefix = section + "."
    for line in lines:
        m = HEADING_RE.match(line)
        if m:
            num = m.group(2)
            if not capturing:
                if num == section:
                    capturing = True  # skip the heading line itself
                continue
            # already capturing: stop at the next non-child heading
            if num == section or num.startswith(child_prefix):
                continue
            break
        if capturing:
            out.append(line)
    return "\n".join(out) if capturing else None


def body_after_front_matter(text: str) -> str:
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    return text[end + 4:] if end != -1 else text


def ngrams(tokens: list[str], n: int) -> dict[tuple[str, ...], int]:
    """Map each n-gram to the token index where it starts (first occurrence)."""
    out: dict[tuple[str, ...], int] = {}
    for i in range(len(tokens) - n + 1):
        gram = tuple(tokens[i:i + n])
        out.setdefault(gram, i)
    return out


def iter_md(paths: list[str]) -> list[Path]:
    files: list[Path] = []
    for p in paths:
        path = Path(p)
        if path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
        elif path.is_file():
            files.append(path)
    return files


def check_file(path: Path, default_version: str, n: int) -> list[str]:
    fm = read_front_matter(path)
    if not fm:
        return []
    if fm.get("status") not in ("draft", "reviewed"):
        return []
    section = str(fm.get("source_section") or "").strip()
    if section == "del_v2":
        # Removed in v2.0: anchor against the v1.x section it last appeared in.
        # These docs keep spec_version 1.x, so the v1 spec is selected below.
        section = str(fm.get("v1_source_section") or "").strip()
    if not section:
        return []

    version = str(fm.get("spec_version") or default_version)

    # Sections prefixed "prof-" come from the KMIP-Prof document, not KMIP-SPEC.
    # Sections prefixed "ug-" come from the KMIP-UG document, not KMIP-SPEC.
    if section.startswith("prof-"):
        bare_section = section[len("prof-"):]
        spec = prof_path_for(version)
        if not spec.exists():
            print(f"WARN {path.name}: KMIP-Prof not found for version {version}",
                  file=sys.stderr)
            return []
        section = bare_section
    elif section.startswith("ug-"):
        bare_section = section[len("ug-"):]
        spec = ug_path_for(version)
        if not spec.exists():
            print(f"WARN {path.name}: KMIP-UG not found for version {version}",
                  file=sys.stderr)
            return []
        section = bare_section
    else:
        spec = spec_path_for(version)
        if not spec.exists():
            print(f"WARN {path.name}: source spec not found for version {version}",
                  file=sys.stderr)
            return []

    src = extract_section(spec.read_text(encoding="utf-8"), section)
    if src is None:
        # Heading may be absent from the converted source (e.g. lost in
        # conversion). Can't auto-compare; flag for manual review, don't fail.
        print(f"WARN {path.name}: source section {section} not found in "
              f"{spec.name} (manual no-verbatim review needed)", file=sys.stderr)
        return []

    src_grams = set(ngrams(tokenize(src), n))
    body_tokens = tokenize(body_after_front_matter(path.read_text(encoding="utf-8")))

    findings: list[str] = []
    i = 0
    while i <= len(body_tokens) - n:
        gram = tuple(body_tokens[i:i + n])
        if gram in src_grams and " ".join(gram) not in _OUR_HEADINGS:
            # extend the run as far as it stays shared
            j = i + n
            while j < len(body_tokens) and tuple(body_tokens[j - n + 1:j + 1]) in src_grams:
                j += 1
            findings.append(" ".join(body_tokens[i:j]))
            i = j
        else:
            i += 1
    return findings


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("paths", nargs="*", default=["kb/operations"],
                   help="Directories or files to check (default: kb/operations)")
    p.add_argument("--n", type=int, default=8,
                   help="Minimum shared word-run length to flag (default: 8)")
    p.add_argument("--version", default="1.4",
                   help="Fallback spec version when a doc omits spec_version")
    args = p.parse_args(argv)

    files = iter_md(args.paths or ["kb/operations"])
    checked = 0
    flagged = 0
    for f in files:
        fm = read_front_matter(f)
        if not fm or fm.get("status") not in ("draft", "reviewed"):
            continue
        checked += 1
        findings = check_file(f, args.version, args.n)
        if findings:
            flagged += 1
            rel = f.relative_to(REPO_ROOT).as_posix() if f.is_absolute() else f.as_posix()
            print(f"FAIL {rel}")
            for run in findings:
                print(f'    shared {len(run.split())} words: "{run}"')
    print(f"checked {checked} authored doc(s), {flagged} with verbatim overlap "
          f"(n={args.n})")
    return 1 if flagged else 0


if __name__ == "__main__":
    raise SystemExit(main())
