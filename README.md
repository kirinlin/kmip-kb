# kmip-dev

An independently written **KMIP developer knowledge base** — summaries,
explanations, implementation guidance, examples, and machine-readable metadata
for the OASIS Key Management Interoperability Protocol (KMIP), structured for
LLM wikis, RAG / vector search, GraphRAG, and coding agents.

It targets the **KMIP 1.x** specification family (v1.0–v1.4), with **v1.4** as
the baseline.

## Structure

| Directory | Contents |
|---|---|
| `concepts/` | Cross-cutting concepts: authentication, transport, error handling, key state. |
| `operations/` | Client-to-server operations; `operations/server-to-client/` for the reverse. |
| `objects/` | Managed objects (symmetric/asymmetric keys, certificates, secret data, templates). |
| `attributes/` | Object attributes — data types, constraints, applicability. |
| `ttlv/` | TTLV encoding plus base-object structures and message contents/format. |
| `profiles/` | Conformance profiles and implementation conformance. |
| `workflows/` | End-to-end workflows that chain operations. |
| `examples/` | Worked request/response examples (original, not copied). |
| `schemas/` | JSON Schemas and machine-readable contracts; `schemas/agent/` holds GraphRAG relation files. |
| `mappings/` | Cross-version / cross-implementation mapping tables. |
| `versions/` | Per-version TOC maps (`<ver>-toc.yaml`) and 1.0–1.4 delta notes. |
| `references/` | Terminology and pointers to normative / non-normative references. |
| `templates/` | Document skeletons used by the scaffold generator. |

Each document carries YAML front matter validated against
[`schemas/frontmatter.schema.json`](schemas/frontmatter.schema.json):

```yaml
---
title: Create
category: operation
spec_version: "1.4"
spec_versions: ["1.4"]
source_section: "4.1"     # traceability only — never verbatim text
status: stub              # stub | draft | reviewed
related: []
keywords: []
---
```

`status` tracks progress: `stub` (generated skeleton) → `draft` (authored) →
`reviewed` (human-verified per [CONTRIBUTING.md](CONTRIBUTING.md)).

**Authoring status:** `operations/` (all client-to-server operations) and
`objects/` (all managed object types) are authored as `draft`; the remaining
categories are generated stubs awaiting prose.

## Scaffold generator

[`scripts/build_kb_scaffold.py`](scripts/build_kb_scaffold.py) parses a locally
mirrored spec and (re)generates the directory structure, one empty stub per
section, and the section→file map in `versions/<ver>-toc.yaml`. It is pure
standard library and **never overwrites a file whose `status` is no longer
`stub`**, so it is safe to re-run as authoring proceeds.

```sh
python scripts/build_kb_scaffold.py            # generate for v1.4
python scripts/build_kb_scaffold.py --check    # validate all front matter
python scripts/build_kb_scaffold.py --toc-only # only refresh the TOC map
python scripts/build_kb_scaffold.py --prune    # delete orphaned stubs
```

| Flag | Default | Effect |
|---|---|---|
| `--version` | `1.4` | KMIP 1.x version to scaffold from |
| `--spec FILE` | *(derived)* | Explicit raw spec path (overrides `--version`) |
| `--out DIR` | `.` | Output root |
| `--toc-only` | *(off)* | Only regenerate `versions/<ver>-toc.yaml` |
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
python scripts/check_verbatim.py operations    # check a directory
python scripts/check_verbatim.py --n 8         # adjust the run length
```

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
| `--no-skip` | — | Re-download files that already exist |

Path prefixes listed in `EXCLUDE_PREFIXES` at the top of the script are pruned
from both the crawl and any `--urls` list — currently the
`kmip-profiles/v3.0/csd01/test-cases/kmip-v3.0` subtree, which self-references
into runaway depth from server mis-linking.

Progress and errors are logged to `logs/kmip_crawler-{timestamp}.log`.
