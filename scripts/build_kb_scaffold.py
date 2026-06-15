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

# v1.x section numbering (v1.0 – v1.4)
V1X_PREFIX_RULES: dict[str, tuple[str, int, str]] = {
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

# v2.0 section numbering (completely reorganised from v1.x)
V20_PREFIX_RULES: dict[str, tuple[str, int, str]] = {
    "1": ("reference", 2, ""),           # Introduction / Terminology / References
    "2": ("object", 2, ""),              # Objects (managed objects)
    "3": ("ttlv", 2, ""),                # Object Data Structures (Key Block, ...)
    "4": ("attribute", 2, ""),           # Object Attributes
    "5": ("ttlv", 2, ""),                # Attribute Data Structures
    "6.1": ("operation", 3, ""),         # Client-to-Server Operations
    "6.2": ("operation", 3, "server-to-client"),  # Server-to-Client Operations
    "7": ("ttlv", 2, ""),                # Operations Data Structures
    "8": ("ttlv", 2, ""),                # Messages
    "9": ("ttlv", 2, ""),                # Message Data Structures
    "10.1": ("ttlv", 3, ""),             # TTLV encoding details (Tag, Type, Length, ...)
    "10.3": ("concept", 2, ""),          # Authentication
    "10.4": ("concept", 2, ""),          # Transport
    "11": ("ttlv", 2, "enumerations"),   # Enumerations (Tag, Operation, State, ...)
    "12": ("ttlv", 2, ""),               # Bit Masks (Cryptographic Usage, ...)
    "13": ("concept", 2, ""),            # Algorithm Implementation (Split Key)
    "14": ("profile", 2, ""),            # Conformance
}

PREFIX_RULES = V1X_PREFIX_RULES  # default; overridden per-version in cmd_generate

# Sections whose content is deliberately covered by an already-authored doc
# under a different slug (rename or many-sections-into-one consolidation).
# Applied for --source spec --version 2.1 only: the stub target resolves to
# the existing doc (so write_if_stub skips it as authored) and the TOC points
# at the real file instead of a slug that will never exist.
V21_SLUG_OVERRIDES: dict[str, str] = {
    "1.3": "normative-references",          # renamed from NormativeReferences
    "3.4": "transparent-key-structures",    # §3.4–3.12 consolidated
    "3.5": "transparent-key-structures",
    "3.6": "transparent-key-structures",
    "3.7": "transparent-key-structures",
    "3.8": "transparent-key-structures",
    "3.9": "transparent-key-structures",
    "3.10": "transparent-key-structures",
    "3.11": "transparent-key-structures",
    "3.12": "transparent-key-structures",
    "4.60": "custom-attribute",             # Vendor Attribute, authored as Custom Attribute
    "5.1": "attribute",                     # Attributes structure, authored singular
    "8.1": "message-structure",             # §8 Messages consolidated
    "8.2": "message-structure",
    "8.3": "message-structure",
    "8.4": "message-structure",
    "8.5": "message-structure",
    "8.6": "message-structure",
    "9.9": "client-correlation-value",      # Correlation Value (Client)
    "9.10": "server-correlation-value",     # Correlation Value (Server)
    "10.1.1": "ttlv-encoding",              # §10.1.1–10.1.5 consolidated
    "10.1.2": "ttlv-encoding",
    "10.1.3": "ttlv-encoding",
    "10.1.4": "ttlv-encoding",
    "10.1.5": "ttlv-encoding",
}

# KMIP Profiles document ([KMIP-Prof]) section classification.
# The profiles doc is versioned in sync with KMIP-SPEC (both 2.1, etc.) but is a
# separate OASIS document. Section numbers here come from that document, not
# KMIP-SPEC, so stubs emitted from this ruleset use source_section "prof-N.M".
#
# v1.3–v2.x: §3 = Auth Suites, §5 = Profile definitions.
PROF_PREFIX_RULES: dict[str, tuple[str, int, str]] = {
    "3": ("profile", 2, ""),  # §3 Authentication Suites (Basic, HTTPS, Suite B, ...)
    "5": ("profile", 2, ""),  # §5 Profile definitions (Baseline, Complete, HTTPS, ...)
}

# v1.0–v1.2: §4 = KMIP Profiles (§5 is Conformance Clauses, not profiles).
PROF_V1X_EARLY_RULES: dict[str, tuple[str, int, str]] = {
    "3": ("profile", 2, ""),  # §3 Authentication Suites (Basic, TLS 1.2)
    "4": ("profile", 2, ""),  # §4 KMIP Profiles
}


def get_prefix_rules(version: str) -> dict[str, tuple[str, int, str]]:
    """Return the section-classification rules for the given spec version."""
    if version.startswith("2."):
        return V20_PREFIX_RULES
    return V1X_PREFIX_RULES


def get_prof_prefix_rules(version: str) -> dict[str, tuple[str, int, str]]:
    """Return the KMIP-Prof section-classification rules for the given version.

    v1.0–v1.2 moved profiles to §4 (§5 is Conformance Clauses in those releases).
    v1.3+ and v2.x use §5 for profiles, matching PROF_PREFIX_RULES.
    """
    major, minor = version.split(".", 1)
    if major == "1" and minor in ("0", "1", "2"):
        return PROF_V1X_EARLY_RULES
    return PROF_PREFIX_RULES


def prof_path_for(version: str) -> Path:
    """Return the raw KMIP-Prof document path for a given version.

    v2.x profiles live under ``raw/kmip/kmip-profiles/v<ver>/``.
    v1.x profiles live under ``raw/kmip/profiles/v<ver>/os/``.
    """
    if version.startswith("2."):
        base = REPO_ROOT / "raw" / "kmip" / "kmip-profiles" / f"v{version}"
        return base / f"kmip-profiles-v{version}.md"
    base = REPO_ROOT / "raw" / "kmip" / "profiles" / f"v{version}" / "os"
    candidates = [
        base / f"kmip-profiles-v{version}-os.md",
        base / f"kmip-profiles-{version}-os.md",  # v1.0 uses this form
    ]
    for c in candidates:
        if c.exists():
            return c
    return candidates[0]

CATEGORY_DIR: dict[str, str] = {
    "operation": "kb/operations",
    "attribute": "kb/attributes",
    "object": "kb/objects",
    "concept": "kb/concepts",
    "ttlv": "kb/ttlv",
    "profile": "kb/profiles",
    "reference": "kb/references",
    "usage-guide": "kb/usage-guide",
}

CATEGORY_TEMPLATE: dict[str, str] = {
    "operation": "operation.md",
    "attribute": "attribute.md",
    "object": "object.md",
    "concept": "concept.md",
    "ttlv": "ttlv.md",
    "profile": "concept.md",   # profiles reuse the concept skeleton
    "reference": "reference.md",
    "usage-guide": "usage-guide.md",
}

# Directories that make up the knowledge base. Each gets an index.md. The ones
# without spec-derived stubs (workflows/examples/schemas/...) are seeded empty.
STRUCTURE_DIRS: dict[str, str] = {
    "kb/concepts": "Cross-cutting concepts: authentication, transport, error handling, key state and lifecycle.",
    "kb/operations": "Client-to-server and server-to-client operations (Create, Locate, Get, ...).",
    "kb/objects": "Managed objects: symmetric/asymmetric keys, certificates, secret data, templates.",
    "kb/attributes": "Object attributes and their data types, constraints, and applicability.",
    "kb/ttlv": "TTLV encoding plus base-object structures and message contents/format.",
    "kb/profiles": "Conformance profiles and implementation conformance requirements.",
    "kb/workflows": "End-to-end usage workflows that chain operations together.",
    "kb/examples": "Worked request/response examples (original, not copied from the spec).",
    "schemas": "JSON Schemas and machine-readable contracts (e.g. front-matter schema).",
    "kb/operations/server-to-client": "Server-to-client operations (Notify, Put, Query).",
    "kb/ttlv/enumerations": "Enumerations (§11): named value sets used in TTLV-encoded fields.",
    "schemas/agent": "Graph RAG / coding-agent relation files (operation/object graphs).",
    "kb/mappings": "Cross-version and cross-implementation mapping tables.",
    "kb/versions": "Per-version TOC maps and 1.0-1.4 delta notes.",
    "kb/references": "Terminology and pointers to normative / non-normative references.",
    "kb/usage-guide": "KMIP Usage Guide articles: design goals, usage notes, worked examples, and deprecation guidance.",
}

VALID_CATEGORIES = {
    "operation", "attribute", "object", "concept", "ttlv", "profile",
    "reference", "workflow", "example", "schema", "index", "usage-guide",
}
VALID_STATUS = {"stub", "draft", "reviewed"}

# KMIP Usage Guide ([KMIP-UG]) section classification.
# The UG is a separate OASIS document, versioned in sync with KMIP-SPEC.
# Stubs emitted from this ruleset use source_section "ug-N.M".
# §1 (Introduction/References) is intentionally excluded.
UG_PREFIX_RULES: dict[str, tuple[str, int, str]] = {
    "2": ("usage-guide", 2, ""),  # §2 Design Goals
    "3": ("usage-guide", 2, ""),  # §3 Usage Notes
    "4": ("usage-guide", 2, ""),  # §4 Usage Examples
    "5": ("usage-guide", 2, ""),  # §5 Deprecation notes
}


def ug_path_for(version: str) -> Path:
    """Return the raw KMIP-UG document path for a given version.

    v2.x docs live under ``raw/kmip/kmip-ug/v<ver>/``.
    v1.x docs live under ``raw/kmip/ug/v<ver>/``.
    v1.0 uses no leading "v" in the filename (kmip-ug-1.0.md).
    v1.1+ use the "v" prefix (kmip-ug-v1.1.md).
    """
    if version.startswith("2."):
        base = REPO_ROOT / "raw" / "kmip" / "kmip-ug" / f"v{version}"
        return base / f"kmip-ug-v{version}.md"
    base = REPO_ROOT / "raw" / "kmip" / "ug" / f"v{version}"
    _, minor = version.split(".", 1)
    if minor == "0":
        return base / f"kmip-ug-{version}.md"  # v1.0: no "v" prefix
    return base / f"kmip-ug-v{version}.md"


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
    """Return the raw OASIS-Standard spec path for a given version.

    v1.x specs live under ``raw/kmip/spec/v<ver>/os/``.
    v2.0+ specs live under ``raw/kmip/kmip-spec/v<ver>/os/`` (different subdirectory).
    """
    if version.startswith("2."):
        base = REPO_ROOT / "raw" / "kmip" / "kmip-spec" / f"v{version}" / "os"
        return base / f"kmip-spec-v{version}-os.md"
    base = REPO_ROOT / "raw" / "kmip" / "spec" / f"v{version}" / "os"
    candidates = [
        base / f"kmip-spec-v{version}-os.md",
        base / f"kmip-spec-{version}-os.md",  # v1.0 uses this form
    ]
    for c in candidates:
        if c.exists():
            return c
    return candidates[0]


def classify(num: str, rules: dict | None = None) -> tuple[str, int, str] | None:
    """Longest-prefix match of a section number to (category, depth, subdir)."""
    if rules is None:
        rules = PREFIX_RULES
    parts = num.split(".")
    for i in range(len(parts), 0, -1):
        prefix = ".".join(parts[:i])
        if prefix in rules:
            return rules[prefix]
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


def select_stubs(headings: list[tuple[str, str]],
                 rules: dict | None = None) -> list[dict]:
    """Choose which headings become stubs and attach their classification."""
    stubs: list[dict] = []
    for num, title in headings:
        rule = classify(num, rules)
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
    ]
    # Optional cross-version trace: the v1.x section, when the concept existed
    # in the 1.x family. New v2.x-only stubs have no v1 mapping, so it is absent.
    if fm.get("v1_source_section") is not None:
        lines.append(f'v1_source_section: "{fm["v1_source_section"]}"')
    lines += [
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
    if "v1_source_section" in fm and not isinstance(fm["v1_source_section"], str):
        errors.append("v1_source_section must be a string")
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


def build_stub(stub: dict, version: str, bodies: dict[str, str],
               section_prefix: str = "") -> str:
    fm = {
        "title": stub["title"],
        "category": stub["category"],
        "spec_version": version,
        "spec_versions": [version],
        "source_section": f"{section_prefix}{stub['section']}" if section_prefix else stub["section"],
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
    source = getattr(args, "source", "spec")

    if args.spec:
        spec = Path(args.spec).resolve()
    elif source == "prof":
        spec = prof_path_for(version)
    elif source == "ug":
        spec = ug_path_for(version)
    else:
        spec = spec_path_for(version)
    if not spec.exists():
        print(f"ERROR: spec not found: {spec}", file=sys.stderr)
        return 2

    text = spec.read_text(encoding="utf-8")
    headings = parse_headings(text)
    if source == "prof":
        rules = get_prof_prefix_rules(version)
        section_prefix = "prof-"
    elif source == "ug":
        rules = UG_PREFIX_RULES
        section_prefix = "ug-"
    else:
        rules = get_prefix_rules(version)
        section_prefix = ""
    stubs = select_stubs(headings, rules)

    # resolve consolidated/renamed sections to their authored doc's slug
    if source == "spec" and version == "2.1":
        for s in stubs:
            if s["section"] in V21_SLUG_OVERRIDES:
                s["slug"] = V21_SLUG_OVERRIDES[s["section"]]
                s["consolidated"] = True

    # detect slug collisions within a category
    seen: dict[tuple[str, str, str], str] = {}
    for s in stubs:
        if s.get("consolidated"):
            continue
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
    (out / "kb" / "versions").mkdir(parents=True, exist_ok=True)
    if source == "prof":
        toc_name = f"{version}-prof-toc.yaml"
    elif source == "ug":
        toc_name = f"{version}-ug-toc.yaml"
    else:
        toc_name = f"{version}-toc.yaml"
    toc_path = out / "kb" / "versions" / toc_name
    toc_path.write_text(render_toc(version, spec_rel, stubs), encoding="utf-8")

    # 3. stubs
    if not args.toc_only and not args.no_stubs:
        bodies = {cat: _strip_front_matter(
                    (REPO_ROOT / "templates" / tmpl).read_text(encoding="utf-8"))
                  for cat, tmpl in CATEGORY_TEMPLATE.items()}
        for s in stubs:
            path = out / target_path(s["category"], s["subdir"], s["slug"])
            res = write_if_stub(path, build_stub(s, version, bodies, section_prefix))
            counts[res] += 1

    print(f"spec: {spec_rel}")
    print(f"headings parsed: {len(headings)}  stubs: {len(stubs)}")
    print(f"toc: versions/{toc_name}")
    print("files: " + "  ".join(f"{k}={v}" for k, v in counts.items()))
    return 0


def cmd_check(args) -> int:
    out = Path(args.out).resolve()
    dirs = [d for d in STRUCTURE_DIRS if d not in ("schemas", "schemas/agent")]  # hold JSON
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


def cmd_prune(args) -> int:
    """Delete orphaned *stub* files no longer produced by the current rules.

    An orphan is a ``.md`` in a category directory whose path is not among the
    target paths the generator would emit for this version. Only files still at
    ``status: stub`` are removed -- authored (draft/reviewed) files are reported
    and left untouched so re-classification never destroys real content.
    """
    out = Path(args.out).resolve()
    version = args.version
    spec = Path(args.spec).resolve() if args.spec else spec_path_for(version)
    if not spec.exists():
        print(f"ERROR: spec not found: {spec}", file=sys.stderr)
        return 2

    stubs = select_stubs(parse_headings(spec.read_text(encoding="utf-8")),
                         get_prefix_rules(version))
    expected = {target_path(s["category"], s["subdir"], s["slug"]) for s in stubs}

    category_dirs = {CATEGORY_DIR[c] for c in CATEGORY_DIR}
    removed = 0
    kept_authored = 0
    for dirname in sorted(category_dirs):
        d = out / dirname
        if not d.exists():
            continue
        for f in sorted(d.rglob("*.md")):
            rel = f.relative_to(out).as_posix()
            if f.name == "index.md" or rel in expected:
                continue
            status = (read_front_matter(f) or {}).get("status")
            if status and status != "stub":
                print(f"KEEP  {rel}: orphan but status={status} (authored)")
                kept_authored += 1
                continue
            f.unlink()
            print(f"PRUNE {rel}")
            removed += 1
    print(f"pruned {removed} orphan stub(s); kept {kept_authored} authored orphan(s)")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--version", default="2.1",
                   help="KMIP version to scaffold from, 1.0-1.4 or 2.0-2.1 (default: 2.1)")
    p.add_argument("--source", default="spec", choices=["spec", "prof", "ug"],
                   help="Source document: spec = KMIP-SPEC, prof = KMIP-Prof, ug = KMIP-UG (default: spec)")
    p.add_argument("--spec", default=None,
                   help="Explicit path to a raw spec markdown file (overrides --version)")
    p.add_argument("--out", default=".", help="Output root (default: repo root)")
    p.add_argument("--toc-only", action="store_true",
                   help="Only (re)generate versions/<ver>-toc.yaml")
    p.add_argument("--no-stubs", action="store_true",
                   help="Create dirs + TOC but no per-section stub files")
    p.add_argument("--check", action="store_true",
                   help="Validate front matter of all KB docs and exit")
    p.add_argument("--prune", action="store_true",
                   help="Delete orphaned stub files no longer in the rules and exit")
    args = p.parse_args(argv)

    if args.check:
        return cmd_check(args)
    if args.prune:
        return cmd_prune(args)
    return cmd_generate(args)


if __name__ == "__main__":
    raise SystemExit(main())
