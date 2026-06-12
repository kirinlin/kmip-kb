# KMIP KB — authoring conventions skill

## When to use the kmip-kb MCP tools

| Goal | Tool |
|---|---|
| Find an article on a concept | `search_kb(query)` |
| Browse a category | `list_articles(category=…)` |
| Read a full article | `get_article(slug)` |
| Find what relates to a topic | `get_related(slug)` |

Start every KB task with `search_kb` to orient. If you already know the slug, go straight to `get_article`.

## The one hard rule: never copy spec prose

Never paste specification text, tables, or definitions into any tracked file.
`source_section` front matter is traceability only — it does not license quoting.
Read `raw/` (gitignored) for understanding, then write original prose.

## Front matter requirements

Every doc must have these required YAML keys:

```yaml
title:          # human-readable title (from spec section heading)
category:       # one of: operation | attribute | object | concept | ttlv |
                #         profile | reference | workflow | example | schema | index
spec_version:   # "2.1"  (baseline)
spec_versions:  # list of KMIP versions where this concept exists, e.g. ["1.0","1.1","2.1"]
source_section: # v2.1 dotted section, e.g. "6.1.8". "del_v2" if removed in v2.0.
                # Use "prof-X.Y" for KMIP-Prof articles; "ug-X.Y" for KMIP-UG articles.
status:         # stub | draft | reviewed
related:        # list of slugs or titles (use bare slug, not path)
keywords:       # retrieval keywords for RAG
```

Optional fields:

```yaml
v1_source_section: # v1.x section for the same concept (omit for v2.x-only features).
                   # Use "enc-X" if the v1.x source is KMIP-ENCODE, not KMIP-SPEC.
tag_hex:           # 6-digit uppercase hex KMIP tag, e.g. "42000D" — enables hex-lookup search
xml_element:       # CamelCase XML element name per KMIP-ENCODE §6.1.3, e.g. "BatchCount"
```

`source_section` prefix rules:
- No prefix → KMIP-SPEC main document
- `prof-` → KMIP Profiles document (e.g. `prof-5.1`)
- `ug-` → KMIP Usage Guide document (e.g. `ug-3.1`)
- `del_v2` in `source_section` + `v1_source_section` set → concept removed in v2.0; last v1.x section in `v1_source_section`

## Status lifecycle

- `stub` → skeleton only, prose pending
- `draft` → authored, needs review
- `reviewed` → human-verified per CONTRIBUTING checklist

When filling in a stub, flip `status: stub` → `status: draft` when done.

## KB layout (baseline v2.1 section mapping)

| Spec section | KB path |
|---|---|
| §2 Objects | `kb/objects/` |
| §4 Attributes | `kb/attributes/` |
| §6.1 Client operations | `kb/operations/` |
| §6.2 Server-to-client operations | `kb/operations/server-to-client/` |
| §3/§5/§7/§8/§9/§10.1 TTLV & message structure | `kb/ttlv/` |
| §11 Enumerations | `kb/ttlv/enumerations/` |
| §10.3/§10.4 Auth/Transport + §13 Algorithm Impl | `kb/concepts/` |
| §14 Profiles | `kb/profiles/` |
| §1 References | `kb/references/` |
| KMIP-UG content | `kb/usage-guide/` |
| Version delta notes | `kb/versions/` |
| Workflow articles | `kb/workflows/` |
| Worked examples | `kb/examples/` |
| Cross-spec mappings | `kb/mappings/` |

## Cross-references

Use relative links from the file's own directory:
```markdown
[Key Block](../ttlv/key-block.md)
[Create](create.md)
```

Confirm the target exists before linking (`stub` is fine; a missing file is not).

## Scaffold generator

`scripts/build_kb_scaffold.py` parses a raw spec and generates stubs + a version TOC file. Safe to re-run — never overwrites a file whose `status` ≠ `stub`.

```bash
python scripts/build_kb_scaffold.py [--version 2.1] [--source spec|prof|ug] [--out .] [--toc-only] [--no-stubs] [--check]
```

- `--source spec` (default): KMIP-SPEC; writes `kb/versions/<ver>-toc.yaml`
- `--source prof`: KMIP Profiles doc; writes `kb/versions/<ver>-prof-toc.yaml`; prefixes `source_section` with `prof-`
- `--source ug`: KMIP Usage Guide; writes `kb/versions/<ver>-ug-toc.yaml`; prefixes `source_section` with `ug-`
- `--check`: validates front matter against JSON Schema only (no writes)

## Validation before committing

Always run all three checks after authoring or editing:

```bash
# 1. Front matter vs JSON Schema
python scripts/build_kb_scaffold.py --check

# 2. Flags shared 8+-word runs vs the spec source (verbatim detection)
python scripts/check_verbatim.py <dir>

# 3. Checks related slugs + relative body links resolve
python scripts/validate_links.py [dir ...]
```

Fix any errors before marking `status: draft` or `status: reviewed`.

## Authoring style

- Match depth and cross-reference style of `kb/operations/register.md` and `kb/objects/symmetric-key.md`.
- Do not quote spec text — paraphrase and synthesize.
- `spec_versions` must be accurate: check `kb/versions/index.md` for delta notes between releases.
- Slugs in `related:` are bare names (e.g. `"symmetric-key"`, not `"objects/symmetric-key"`).

## Checking status at a glance

```bash
python scripts/status_report.py                      # table by category
python scripts/status_report.py --next 10            # next stubs to author
python scripts/status_report.py --category kb/ttlv   # one category
python scripts/status_report.py --json               # machine-readable output
```
