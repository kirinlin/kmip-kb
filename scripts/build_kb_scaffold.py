#!/usr/bin/env python3
"""Generate the KMIP knowledge-base scaffold from a raw spec document.

Parses a locally-mirrored KMIP specification (under ``raw/``), maps each spec
section to a knowledge-base category, and emits:

  * the directory structure (with an ``index.md`` per directory),
  * an empty Markdown *stub* per section (YAML front matter + section headers,
    NO spec prose), and
  * ``versions/<ver>-toc.yaml`` -- the machine-readable section -> file map.

Stubs are skeletons only. Authors fill in original prose later (see
CONTRIBUTING.md). The generator never copies specification text and never
overwrites a file whose ``status`` is no longer ``stub``.

Pure standard library -- no third-party dependencies required. If PyYAML is
installed it is used for front-matter parsing; otherwise a minimal built-in
parser handles the subset this tool emits.

Usage:
    python scripts/build_kb_scaffold.py [--version 1.4] [--out .]
    python scripts/build_kb_scaffold.py --toc-only
    python scripts/build_kb_scaffold.py --no-stubs
    python scripts/build_kb_scaffold.py --check
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
    _HAVE_YAML = True
except Exception:  # pragma: no cover - optional dependency
    _HAVE_YAML = False

# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #

# Longest-prefix classification of a dotted spec section number.
# value = (category, stub_depth, subdir) where stub_depth is the number of
# dotted components at which exactly one stub is emitted for that branch, and
# subdir is an optional path appended under the category directory (used to
# keep same-named operations -- e.g. client vs server Query -- separate).
PREFIX_RULES: dict[str, tuple[str, int, str]] = {
    "2.1": ("ttlv", 3, ""),       # Base Objects -> TTLV structures (Key Block, ...)
    "2.2": ("object", 3, ""),     # Managed Objects (Symmetric Key, Certificate, ...)
    "3": ("attribute", 2, ""),    # Attributes 3.1 .. 3.N
    "4": ("operation", 2, ""),    # Client-to-Server Operations
    "5": ("operation", 2, "server-to-client"),  # Server-to-Client Operations
    "6": ("ttlv", 2, ""),         # Message Contents
    "7": ("ttlv", 2, ""),         # Message Format
    "8": ("concept", 1, ""),      # Authentication (whole section)
    "9": ("ttlv", 2, ""),         # Message Encoding (TTLV)
    "10": ("concept", 1, ""),     # Transport
    "11": ("concept", 1, ""),     # Error Handling
    "12": ("profile", 2, ""),     # Conformance
    "1": ("reference", 2, ""),    # Introduction / Terminology / References
}

CATEGORY_DIR: dict[str, str] = {
    "operation": "operations",
    "attribute": "attributes",
    "object": "objects",
    "concept": "concepts",
    "ttlv": "ttlv",
    "profile": "profiles",
    "reference": "references",
}

CATEGORY_TEMPLATE: dict[str, str] = {
    "operation": "operation.md",
    "attribute": "attribute.md",
    "object": "object.md",
    "concept": "concept.md",
    "ttlv": "ttlv.md",
    "profile": "concept.md",   # profiles reuse the concept skeleton
    "reference": "reference.md",
}

# Directories that make up the knowledge base. Each gets an index.md. The ones
# without spec-derived stubs (workflows/examples/schemas/...) are seeded empty.
STRUCTURE_DIRS: dict[str, str] = {
    "concepts": "Cross-cutting concepts: authentication, transport, error handling, key state and lifecycle.",
    "operations": "Client-to-server and server-to-client operations (Create, Locate, Get, ...).",
    "objects": "Managed objects: symmetric/asymmetric keys, certificates, secret data, templates.",
    "attributes": "Object attributes and their data types, constraints, and applicability.",
    "ttlv": "TTLV encoding plus base-object structures and message contents/format.",
    "profiles": "Conformance profiles and implementation conformance requirements.",
    "workflows": "End-to-end usage workflows that chain operations together.",
    "examples": "Worked request/response examples (original, not copied from the spec).",
    "schemas": "JSON Schemas and machine-readable contracts (e.g. front-matter schema).",
    "operations/server-to-client": "Server-to-client operations (Notify, Put, Query).",
    "schemas/agent": "GraphRAG / coding-agent relation files (operation/object graphs).",
    "mappings": "Cross-version and cross-implementation mapping tables.",
    "versions": "Per-version TOC maps and 1.0-1.4 delta notes.",
    "references": "Terminology and pointers to normative / non-normative references.",
}

VALID_CATEGORIES = {
    "operation", "attribute", "object", "concept", "ttlv", "profile",
    "reference", "workflow", "example", "schema", "index",
}
VALID_STATUS = {"stub", "draft", "reviewed"}

HEADING_RE = re.compile(r"^(#{2,6})\s+(\d+(?:\.\d+)*)\s+(.*?)\s*$")
REPO_ROOT = Path(__file__).resolve().parent.parent


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #

def slugify(title: str) -> str:
    """Kebab-case a section title into a filename stem.

    "Create Key Pair" -> "create-key-pair"
    "PKCS#12 Friendly Name" -> "pkcs-12-friendly-name"
    "X.509 Certificate Identifier" -> "x-509-certificate-identifier"
    """
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower())
    return slug.strip("-")


def spec_path_for(version: str) -> Path:
    """Return the raw OASIS-Standard spec path for a 1.x version."""
    base = REPO_ROOT / "raw" / "kmip" / "spec" / f"v{version}" / "os"
    candidates = [
        base / f"kmip-spec-v{version}-os.md",
        base / f"kmip-spec-{version}-os.md",  # v1.0 uses this form
    ]
    for c in candidates:
        if c.exists():
            return c
    return candidates[0]


def classify(num: str) -> tuple[str, int, str] | None:
    """Longest-prefix match of a section number to (category, depth, subdir)."""
    parts = num.split(".")
    for i in range(len(parts), 0, -1):
        prefix = ".".join(parts[:i])
        if prefix in PREFIX_RULES:
            return PREFIX_RULES[prefix]
    return None


def target_path(category: str, subdir: str, slug: str) -> str:
    """Repo-relative posix path for a stub."""
    base = CATEGORY_DIR[category]
    if subdir:
        base = f"{base}/{subdir}"
    return f"{base}/{slug}.md"


def parse_headings(text: str) -> list[tuple[str, str]]:
    """Return [(dotted_number, title)] for every numbered ## .. ###### heading."""
    out: list[tuple[str, str]] = []
    for line in text.splitlines():
        m = HEADING_RE.match(line)
        if m:
            out.append((m.group(2), m.group(3).strip()))
    return out


def select_stubs(headings: list[tuple[str, str]]) -> list[dict]:
    """Choose which headings become stubs and attach their classification."""
    stubs: list[dict] = []
    for num, title in headings:
        rule = classify(num)
        if rule is None:
            continue
        category, stub_depth, subdir = rule
        depth = len(num.split("."))
        if depth != stub_depth:
            continue
        if not title:
            continue
        stubs.append({
            "section": num,
            "title": title,
            "category": category,
            "subdir": subdir,
            "slug": slugify(title),
        })
    return stubs


def _strip_front_matter(text: str) -> str:
    """Return the markdown body after a leading ``---`` front-matter block."""
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    if end == -1:
        return text
    rest = text[end + 4:]
    return rest.lstrip("\n")


def render_front_matter(fm: dict) -> str:
    """Deterministically render the front-matter block we emit."""
    def fmt_list(values: list[str]) -> str:
        if not values:
            return "[]"
        return "[" + ", ".join(f'"{v}"' for v in values) + "]"

    lines = [
        "---",
        f'title: {fm["title"]}',
        f'category: {fm["category"]}',
        f'spec_version: "{fm["spec_version"]}"',
        f'spec_versions: {fmt_list(fm["spec_versions"])}',
        f'source_section: "{fm["source_section"]}"',
        f'status: {fm["status"]}',
        f'related: {fmt_list(fm["related"])}',
        f'keywords: {fmt_list(fm["keywords"])}',
        "---",
    ]
    return "\n".join(lines) + "\n\n"


# --- minimal front-matter reader (fallback when PyYAML is absent) ----------- #

def _mini_parse_front_matter(block: str) -> dict:
    data: dict = {}
    key = None
    for raw in block.splitlines():
        if not raw.strip():
            continue
        if raw.startswith("  - ") and key is not None:
            data.setdefault(key, [])
            if isinstance(data[key], list):
                data[key].append(raw[4:].strip().strip('"'))
            continue
        if ":" not in raw:
            continue
        key, _, val = raw.partition(":")
        key = key.strip()
        val = val.strip()
        if val == "" :
            data[key] = []  # assume block list follows; may be overwritten
        elif val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            data[key] = [v.strip().strip('"') for v in inner.split(",")] if inner else []
        else:
            data[key] = val.strip('"')
    return data


def read_front_matter(path: Path) -> dict | None:
    """Return the parsed front matter of a markdown file, or None if absent."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end].strip("\n")
    if _HAVE_YAML:
        try:
            loaded = yaml.safe_load(block)
            return loaded if isinstance(loaded, dict) else None
        except Exception:
            return _mini_parse_front_matter(block)
    return _mini_parse_front_matter(block)


# --------------------------------------------------------------------------- #
# Front-matter validation (mirrors schemas/frontmatter.schema.json)
# --------------------------------------------------------------------------- #

_VER_RE = re.compile(r"^[0-9]+\.[0-9]+$")
_REQUIRED = ["title", "category", "spec_version", "spec_versions",
             "source_section", "status", "related", "keywords"]


def validate_front_matter(fm: dict) -> list[str]:
    errors: list[str] = []
    for key in _REQUIRED:
        if key not in fm:
            errors.append(f"missing required key: {key}")
    if "title" in fm and not (isinstance(fm["title"], str) and fm["title"].strip()):
        errors.append("title must be a non-empty string")
    if "category" in fm and fm["category"] not in VALID_CATEGORIES:
        errors.append(f"category not allowed: {fm['category']!r}")
    if "spec_version" in fm and not (isinstance(fm["spec_version"], str)
                                     and _VER_RE.match(str(fm["spec_version"]))):
        errors.append(f"spec_version must match N.M: {fm.get('spec_version')!r}")
    if "spec_versions" in fm:
        if not isinstance(fm["spec_versions"], list):
            errors.append("spec_versions must be a list")
        else:
            for v in fm["spec_versions"]:
                if not _VER_RE.match(str(v)):
                    errors.append(f"spec_versions entry must match N.M: {v!r}")
    if "status" in fm and fm["status"] not in VALID_STATUS:
        errors.append(f"status not allowed: {fm['status']!r}")
    for listkey in ("related", "keywords"):
        if listkey in fm and not isinstance(fm[listkey], list):
            errors.append(f"{listkey} must be a list")
    return errors


# --------------------------------------------------------------------------- #
# Generation
# --------------------------------------------------------------------------- #

def write_if_stub(path: Path, content: str) -> str:
    """Write content unless an authored (non-stub) file already exists.

    Returns one of: "created", "updated", "skipped-authored", "unchanged".
    """
    if path.exists():
        fm = read_front_matter(path)
        status = (fm or {}).get("status")
        if status and status != "stub":
            return "skipped-authored"
        if path.read_text(encoding="utf-8") == content:
            return "unchanged"
        path.write_text(content, encoding="utf-8")
        return "updated"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return "created"


def build_index(out: Path, dirname: str, purpose: str, version: str) -> str:
    title = dirname.split("/")[-1].replace("-", " ").title()
    fm = {
        "title": title,
        "category": "index",
        "spec_version": version,
        "spec_versions": [version],
        "source_section": "",
        "status": "stub",
        "related": [],
        "keywords": [],
    }
    body = f"# {title}\n\n{purpose}\n\n_Stubs generated; prose pending. See CONTRIBUTING.md._\n"
    return render_front_matter(fm) + body


def build_stub(stub: dict, version: str, bodies: dict[str, str]) -> str:
    fm = {
        "title": stub["title"],
        "category": stub["category"],
        "spec_version": version,
        "spec_versions": [version],
        "source_section": stub["section"],
        "status": "stub",
        "related": [],
        "keywords": [],
    }
    body = bodies[stub["category"]].replace("{{title}}", stub["title"])
    return render_front_matter(fm) + body


def render_toc(version: str, spec_rel: str, stubs: list[dict]) -> str:
    lines = [
        f"# Generated by scripts/build_kb_scaffold.py -- do not edit by hand.",
        f"spec_version: \"{version}\"",
        f"source_document: \"{spec_rel}\"",
        f"stub_count: {len(stubs)}",
        "sections:",
    ]
    for s in stubs:
        target = target_path(s["category"], s["subdir"], s["slug"])
        lines.append(f"  - section: \"{s['section']}\"")
        lines.append(f"    title: \"{s['title']}\"")
        lines.append(f"    category: {s['category']}")
        lines.append(f"    target_path: {target}")
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------- #
# Commands
# --------------------------------------------------------------------------- #

def cmd_generate(args) -> int:
    out = Path(args.out).resolve()
    version = args.version
    spec = Path(args.spec).resolve() if args.spec else spec_path_for(version)
    if not spec.exists():
        print(f"ERROR: spec not found: {spec}", file=sys.stderr)
        return 2

    text = spec.read_text(encoding="utf-8")
    headings = parse_headings(text)
    stubs = select_stubs(headings)

    # detect slug collisions within a category
    seen: dict[tuple[str, str, str], str] = {}
    for s in stubs:
        key = (s["category"], s["subdir"], s["slug"])
        if key in seen:
            print(f"WARNING: slug collision {key} from sections "
                  f"{seen[key]} and {s['section']}", file=sys.stderr)
        else:
            seen[key] = s["section"]

    try:
        spec_rel = str(spec.relative_to(REPO_ROOT)).replace("\\", "/")
    except ValueError:
        spec_rel = str(spec)

    # 1. directory structure + index.md
    counts = {"created": 0, "updated": 0, "unchanged": 0, "skipped-authored": 0}
    if not args.toc_only:
        for dirname, purpose in STRUCTURE_DIRS.items():
            (out / dirname).mkdir(parents=True, exist_ok=True)
            idx = out / dirname / "index.md"
            res = write_if_stub(idx, build_index(out, dirname, purpose, version))
            counts[res] += 1

    # 2. TOC map
    (out / "versions").mkdir(parents=True, exist_ok=True)
    toc_path = out / "versions" / f"{version}-toc.yaml"
    toc_path.write_text(render_toc(version, spec_rel, stubs), encoding="utf-8")

    # 3. stubs
    if not args.toc_only and not args.no_stubs:
        bodies = {cat: _strip_front_matter(
                    (REPO_ROOT / "templates" / tmpl).read_text(encoding="utf-8"))
                  for cat, tmpl in CATEGORY_TEMPLATE.items()}
        for s in stubs:
            path = out / target_path(s["category"], s["subdir"], s["slug"])
            res = write_if_stub(path, build_stub(s, version, bodies))
            counts[res] += 1

    print(f"spec: {spec_rel}")
    print(f"headings parsed: {len(headings)}  stubs: {len(stubs)}")
    print(f"toc: versions/{version}-toc.yaml")
    print("files: " + "  ".join(f"{k}={v}" for k, v in counts.items()))
    return 0


def cmd_check(args) -> int:
    out = Path(args.out).resolve()
    dirs = [d for d in STRUCTURE_DIRS if d != "schemas"]  # schemas holds JSON
    md_files: list[Path] = []
    for dirname in dirs:
        d = out / dirname
        if d.exists():
            md_files.extend(sorted(d.glob("*.md")))
    if not md_files:
        print("no knowledge-base markdown files found (run generate first)")
        return 1

    total_errors = 0
    for f in md_files:
        fm = read_front_matter(f)
        rel = f.relative_to(out).as_posix()
        if fm is None:
            print(f"FAIL {rel}: no front matter")
            total_errors += 1
            continue
        errs = validate_front_matter(fm)
        for e in errs:
            print(f"FAIL {rel}: {e}")
        total_errors += len(errs)
    print(f"checked {len(md_files)} files, {total_errors} error(s)")
    return 0 if total_errors == 0 else 1


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--version", default="1.4",
                   help="KMIP 1.x version to scaffold from (default: 1.4)")
    p.add_argument("--spec", default=None,
                   help="Explicit path to a raw spec markdown file (overrides --version)")
    p.add_argument("--out", default=".", help="Output root (default: repo root)")
    p.add_argument("--toc-only", action="store_true",
                   help="Only (re)generate versions/<ver>-toc.yaml")
    p.add_argument("--no-stubs", action="store_true",
                   help="Create dirs + TOC but no per-section stub files")
    p.add_argument("--check", action="store_true",
                   help="Validate front matter of all KB docs and exit")
    args = p.parse_args(argv)

    if args.check:
        return cmd_check(args)
    return cmd_generate(args)


if __name__ == "__main__":
    raise SystemExit(main())
