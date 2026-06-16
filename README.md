# kmip-dev

An independently written **KMIP developer knowledge base** — summaries,
explanations, implementation guidance, examples, and machine-readable metadata
for the OASIS Key Management Interoperability Protocol (KMIP), structured for
LLM wikis, RAG / vector search, Graph RAG, and coding agents.

It targets the **KMIP 1.x and 2.x** specification families (v1.0–v1.4,
v2.0–v2.1), with **v2.1** as the baseline.

## Structure

| Directory | Contents |
|---|---|
| `kb/concepts/` | Cross-cutting concepts: authentication, transport, error handling, key state. |
| `kb/operations/` | Client-to-server operations; `kb/operations/server-to-client/` for the reverse. |
| `kb/objects/` | Managed objects (symmetric/asymmetric keys, certificates, secret data, templates). |
| `kb/attributes/` | Object attributes — data types, constraints, applicability. |
| `kb/ttlv/` | TTLV wire encoding, enumerations (`kb/ttlv/enumerations/`), and bit masks. |
| `kb/structures/` | Data structures: object (Key Block, …), attribute, and operation building blocks. |
| `kb/messages/` | Protocol message structures: request/response envelope and message fields. |
| `kb/profiles/` | Conformance profiles and implementation conformance. |
| `kb/usage-guide/` | Design goals, usage notes, usage examples, and deprecation guidance from the KMIP Usage Guide ([KMIP-UG]), sourced with `ug-` prefix on `source_section`. |
| `kb/versions/` | Per-version TOC maps — `1.0-toc.yaml` → `2.1-toc.yaml` (104–234 sections), `1.0-prof-toc.yaml` → `2.1-prof-toc.yaml` (8–44 sections), and `1.0-ug-toc.yaml` → `2.1-ug-toc.yaml` (36–83 sections) — plus full 1.0–2.1 delta notes. |
| `kb/references/` | Terminology and pointers to normative / non-normative references. |
| `kb/workflows/` | End-to-end workflows that chain operations. |
| `kb/examples/` | Worked request/response examples (original, not copied). |
| `kb/mappings/` | Cross-version / cross-implementation mapping tables. |
| `schemas/` | JSON Schemas and machine-readable contracts; `schemas/agent/` holds Graph RAG relation files. |
| `templates/` | Document skeletons used by the scaffold generator. |
| `mcp_py/` | FastMCP server exposing the knowledge base to coding agents via BM25 search, article retrieval, listing, and related-article discovery. |

Each document carries YAML front matter validated against
[`schemas/frontmatter.schema.json`](schemas/frontmatter.schema.json):

```yaml
---
title: Create
category: operation
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.8"      # v2.1 baseline section — traceability only
v1_source_section: "4.1"     # v1.x section, when the concept existed there
status: draft                # stub | draft | reviewed
related: []
keywords: []
tag_hex: "420018"            # optional — 6-digit hex from §11.56 Tag Enumeration
xml_text: "CertificateRequest"     # optional — CamelCase XML text identifier (KMIP-ENCODE §6.1.3)
---
```

`source_section` is the **v2.1** (baseline) section; `v1_source_section` records
the v1.x section for the same concept (omitted for v2.x-only features). Docs for
features removed in v2.0 carry `source_section: "del_v2"` with their last v1.x
section in `v1_source_section`. `status` tracks progress: `stub` (generated
skeleton) → `draft` (authored) → `reviewed` (human-verified per
[CONTRIBUTING.md](CONTRIBUTING.md)).

**Authoring status:** 452 content documents — **452 `reviewed`**, 0 `draft`,
0 `stub`. All categories are at 100% reviewed. Covers every KMIP 2.1 section:
operations (client and server-to-client), attributes, objects, data structures
(§3/§5/§7) and message structures (§8/§9), TTLV encoding (§10.1),
all 64 enumerations (§11), bit masks (§12), algorithm implementation (§13),
profiles (KMIP-Prof v1.0–v2.1), and 83 usage-guide articles (KMIP-UG v2.1).
Validators clean (front-matter schema, no-verbatim, link resolution,
field-table Tag/XML Element columns) per the
[CONTRIBUTING.md](CONTRIBUTING.md) checklist. Remaining work is the planned
content in `kb/examples/`, `kb/workflows/`, and `kb/mappings/`.

## Tag field populator

[`scripts/populate_tag_fields.py`](scripts/populate_tag_fields.py) adds `tag_hex`
and `xml_text` frontmatter fields to any KB doc whose title matches a named
KMIP tag. Parses all v1.x, v2.0, and v2.1 spec tag tables: v2.1 is the primary
source (354 tags); earlier versions supply the 17 tags deprecated by v2.0 so
that `del_v2` docs are also covered. Implements the official KMIP-ENCODE §6.1.3
CamelCase algorithm verified against v2.1 test-case XML (e.g.
`X_509CertificateIdentifier`, `PKCS_12FriendlyName`). Safe to re-run — skips
docs that already have `tag_hex`.

```sh
python scripts/populate_tag_fields.py --dry-run   # preview matches
python scripts/populate_tag_fields.py              # apply
```

## Field-table enrichment

[`scripts/enrich_field_tables.py`](scripts/enrich_field_tables.py) adds `Tag`
(6-digit hex) and `XML Element` (CamelCase name) columns to every Markdown table
that documents a structure's or payload's fields — those whose header's first
column is `Field`:

```
| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Object Type | `420057` | `ObjectType` | Yes | The type of object being handed over. |
```

It draws on the same tag lookup as the front-matter populator, reuses an
existing `Tag` column where one is present, fills only cells matching a named
KMIP tag (non-tag fields stay blank), never overwrites populated cells, and is
idempotent. `--check` exits non-zero if any table is stale (CI guard).

```sh
python scripts/enrich_field_tables.py --dry-run   # preview changes
python scripts/enrich_field_tables.py              # apply
python scripts/enrich_field_tables.py --check      # fail if any table is stale
```

## Enumeration-table enrichment

[`scripts/enrich_enum_tables.py`](scripts/enrich_enum_tables.py) inserts or
refreshes the `Value | Hex | XML Text | Description` table in every enumeration
doc under `kb/ttlv/enumerations/`. `Hex` is the 8-digit integer value (e.g.
`0x00000001`); `XML Text` is the CamelCase text per KMIP-ENCODE §6.1.3 that
appears inside the XML element when encoding the value. `--check` exits non-zero
if any table is stale (CI guard).

```sh
python scripts/enrich_enum_tables.py --dry-run   # preview changes
python scripts/enrich_enum_tables.py              # apply
python scripts/enrich_enum_tables.py --check      # fail if any table is stale
```

## Scaffold generator

[`scripts/build_kb_scaffold.py`](scripts/build_kb_scaffold.py) parses a locally
mirrored spec and (re)generates the directory structure, one empty stub per
section, and the section→file map in `kb/versions/<ver>-toc.yaml`. It is pure
standard library and **never overwrites a file whose `status` is no longer
`stub`**, so it is safe to re-run as authoring proceeds.

```sh
python scripts/build_kb_scaffold.py            # generate for v2.1
python scripts/build_kb_scaffold.py --check    # validate all front matter
python scripts/build_kb_scaffold.py --toc-only # only refresh the TOC map
python scripts/build_kb_scaffold.py --prune    # delete orphaned stubs
```

| Flag | Default | Effect |
|---|---|---|
| `--version` | `2.1` | KMIP version to scaffold from (`1.0`–`1.4` and `2.0`–`2.1` all supported) |
| `--source` | `spec` | Source document: `spec` = KMIP-SPEC, `prof` = KMIP-Prof (writes `<ver>-prof-toc.yaml`, prefixes sections with `prof-`), `ug` = KMIP-UG (writes `<ver>-ug-toc.yaml`, prefixes sections with `ug-`) |
| `--spec FILE` | *(derived)* | Explicit raw spec path (overrides `--version`) |
| `--out DIR` | `.` | Output root |
| `--toc-only` | *(off)* | Only regenerate the TOC map |
| `--no-stubs` | *(off)* | Create dirs + TOC but no stub files |
| `--check` | *(off)* | Validate front matter against the JSON Schema and exit |
| `--prune` | *(off)* | Delete stub files no longer in the rules (keeps authored docs) |

## No-verbatim guard

[`scripts/check_verbatim.py`](scripts/check_verbatim.py) enforces the
no-verbatim rule mechanically: for every authored doc (`status: draft` or
`reviewed`) it compares the prose against the doc's `source_section` in the raw
spec and flags any shared run of 8+ words. Run it before committing authored
content:

```sh
python scripts/check_verbatim.py kb/operations  # check a directory
python scripts/check_verbatim.py --n 8         # adjust the run length
```

## MCP server

[`mcp_py/kmip_kb_server.py`](mcp_py/kmip_kb_server.py) is a FastMCP
server that exposes the knowledge base to coding agents over stdio. It provides
four tools: BM25 full-text search (`search_kb`), full article retrieval
(`get_article`), article listing with front-matter filters (`list_articles`),
and related-article discovery (`get_related`). Start it with:

```sh
bash mcp_py/start.sh          # activate venv and run via stdio
```

Dependencies (`fastmcp`, `rank-bm25`, `pyyaml`) are listed in
`mcp_py/requirements.txt`. The server is pre-wired for Claude Code via
`.mcp.json` and `.claude/settings.json`; a `kmip-authoring` skill at
`.claude/skills/kmip-authoring.md` bundles authoring conventions for agents
working in this repo.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the content rules — most importantly
the **no-verbatim** rule: never copy specification prose into tracked files.

## Source preparation (private, local-only)

The knowledge base is written *from* a local mirror of the OASIS docs, which is
**not** published here — `raw/` is gitignored. To build that mirror,
[`scripts/kmip_crawler.py`](scripts/kmip_crawler.py) crawls
`https://docs.oasis-open.org/kmip/` and converts pages to Markdown via
[PullMD](https://github.com/AeternaLabsHQ/pullmd) (running locally, default
`http://localhost:3000`, override with `PULLMD_URL`). Requires Python 3.11+ with
`requests` and `beautifulsoup4`.

```sh
python scripts/kmip_crawler.py                          # crawl + download
python scripts/kmip_crawler.py --urls ./raw/kmip_urls.txt   # resume from saved URLs
```

| Flag | Default | Description |
|---|---|---|
| `--out DIR` | `raw` | Output root directory |
| `--workers N` | `4` | Parallel download workers |
| `--save-urls FILE` | `./raw/kmip_urls.txt` | File to write discovered URLs |
| `--urls FILE` | — | Skip crawl; use a previously saved URL list |
| `--skip-file FILE` | `./raw/404skip.txt` | Skip URLs listed in this file (e.g. known 404s); a missing file is ignored |
| `--no-skip` | — | Re-download files that already exist |

Path prefixes listed in `EXCLUDE_PREFIXES` at the top of the script are pruned
from both the crawl and any `--urls` list — currently the
`kmip-profiles/v3.0/csd01/test-cases/kmip-v3.0` subtree, which self-references
into runaway depth from server mis-linking.

Progress and errors are logged to `logs/kmip_crawler-{timestamp}.log`.
