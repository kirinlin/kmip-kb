# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This project is an **independently written KMIP knowledge base** — original summaries, explanations, implementation guidance, examples, and machine-readable metadata for the OASIS Key Management Interoperability Protocol, structured for LLM wikis, RAG, GraphRAG, and coding agents. It targets the **KMIP 1.x and 2.x** families (v1.0–v1.4, v2.0–v2.1), baseline **v2.1**.

The spec is mirrored locally into `raw/` (gitignored) only as a *source* for authoring; the crawler that builds that mirror is secondary tooling.

## The one hard rule: never copy spec prose

Never paste specification text, tables, or definitions into any tracked file. Read `raw/` for understanding, then write original prose. `source_section` front matter is traceability only — it does not license quoting. See `CONTRIBUTING.md`.

## Knowledge-base layout

`kb/concepts/ kb/operations/ (kb/operations/server-to-client/) kb/objects/ kb/attributes/ kb/ttlv/ kb/profiles/ kb/versions/ kb/references/ kb/workflows/ kb/examples/ kb/mappings/` plus `schemas/ (schemas/agent/) templates/`.

Spec section → category mapping (baseline **v2.1** numbering): §2 Objects→`kb/objects/`, §3 Object Data Structures + §5 Attribute Data Structures + §7 Operations Data Structures + §8/§9 Messages + §10.1 TTLV→`kb/ttlv/`, §4 Attributes→`kb/attributes/`, §6.1 client + §6.2 server-to-client→`kb/operations/`, §10.3/§10.4 Authentication/Transport→`kb/concepts/`, §14→`kb/profiles/`, §1→`kb/references/`. (v1.x used a different scheme: §2.2→`kb/objects/`, §3→`kb/attributes/`, §4/§5→`kb/operations/`, §6/§7/§9→`kb/ttlv/`, §8/§10/§11→`kb/concepts/`, §12→`kb/profiles/`; both rule sets live in `V1X_PREFIX_RULES`/`V20_PREFIX_RULES`.)

Every doc has YAML front matter validated against `schemas/frontmatter.schema.json`, with `status: stub | draft | reviewed`. `source_section` is the **v2.1** baseline section; `v1_source_section` (optional) records the v1.x section for the same concept. Features removed in v2.0 use `source_section: "del_v2"` and keep their last v1.x section in `v1_source_section`; v2.x-only features omit `v1_source_section`.

## source_section for KMIP-Prof articles

Articles sourced from the separate OASIS Profiles document ([KMIP-Prof]) use
the prefix `prof-` in `source_section` (e.g., `source_section: "prof-5.1"`)
to distinguish them from sections of KMIP-SPEC. `check_verbatim.py` and
`build_kb_scaffold.py` both resolve this prefix against the profiles document
(`raw/kmip/kmip-profiles/v<ver>/kmip-profiles-v<ver>.md`) rather than the main
spec.

## Authoring content

Fill a stub's existing section headers with original prose, populate front
matter (`spec_versions` per the versions a concept appears in, real `related`
slugs, `keywords`), then flip `status: stub` → `draft`. Match the depth and
cross-reference style of already-authored docs (e.g. `kb/operations/register.md`,
`kb/objects/symmetric-key.md`). Use relative links (e.g.
`[Key Block](../ttlv/key-block.md)`) and confirm targets exist (stub or
authored) before linking. Validate before committing:

```
python scripts/build_kb_scaffold.py --check    # front matter vs JSON Schema
python scripts/check_verbatim.py <dir>          # flags shared 8+-word runs vs source_section
python scripts/validate_links.py [dir ...]      # checks related slugs + relative body links resolve
```

Authored so far: **everything** — all 158 content docs across every category
are `draft` (0 stubs). Remaining work is review (`draft` → `reviewed` per the
CONTRIBUTING checklist) and net-new content in `kb/examples/`, `kb/workflows/`, and
`kb/mappings/`, whose index pages list the planned items. One caveat:
`kb/operations/re-key.md` (v2.1 §6.1.46) cannot be auto-checked by `check_verbatim.py`
because its heading was lost in source conversion — re-verify it manually
when editing.

## Authoring status

```
python scripts/status_report.py                 # per-category stub/draft/reviewed table
python scripts/status_report.py --next 10       # list next 10 stubs to author
python scripts/status_report.py --category kb/ttlv --next 5   # filter to one category
python scripts/status_report.py --json          # machine-readable output
```

## Scaffold generator

`scripts/build_kb_scaffold.py` — parses a raw spec and (re)generates dirs, one empty stub per section, and a version TOC file. Pure stdlib. **Never overwrites a file whose `status` ≠ `stub`**, so it is safe to re-run. Supports v1.0–v1.4 (from `raw/kmip/spec/`) and v2.0–v2.1 (from `raw/kmip/kmip-spec/`). Also supports the separate KMIP Profiles document via `--source prof`.

```
python scripts/build_kb_scaffold.py [--version 2.1] [--source spec|prof] [--out .] [--toc-only] [--no-stubs] [--check]
```

- `--source spec` (default): parses KMIP-SPEC; writes `kb/versions/<ver>-toc.yaml`
- `--source prof`: parses KMIP-Prof (`raw/kmip/kmip-profiles/v<ver>/`); writes `kb/versions/<ver>-prof-toc.yaml`; prefixes `source_section` with `prof-`

ToC maps for all seven spec releases and KMIP-Prof v2.1 are committed under `kb/versions/`:

| File | Sections |
|---|---|
| `kb/versions/2.1-toc.yaml` | 234 |
| `kb/versions/2.0-toc.yaml` | 215 |
| `kb/versions/1.4-toc.yaml` | 157 |
| `kb/versions/1.3-toc.yaml` | 143 |
| `kb/versions/1.2-toc.yaml` | 134 |
| `kb/versions/1.1-toc.yaml` | 112 |
| `kb/versions/1.0-toc.yaml` | 104 |
| `kb/versions/2.1-prof-toc.yaml` | 20 (KMIP-Prof §3 + §5) |

`kb/versions/index.md` contains delta notes for every release (v1.1–v2.1). `spec_versions` front matter has been audited across all releases: 53 version-boundary docs for v1.1–v1.4 (0 errors); v2.0/v2.1 audited across all 162 KB docs (5 correctly excluded as removed in v2.0).

The section→category rules and per-section stub depth live in `V1X_PREFIX_RULES` / `V20_PREFIX_RULES` / `PROF_PREFIX_RULES` at the top of the script; stub bodies come from `templates/<category>.md`.

## Crawler (source preparation, private)

`scripts/kmip_crawler.py` — unified crawl + download in one pass.

```
python scripts/kmip_crawler.py [--out raw] [--workers 4] [--save-urls ./raw/kmip_urls.txt] [--urls FILE] [--skip-file ./raw/404skip.txt] [--no-skip]
```

| Flag | Default | Effect |
|---|---|---|
| `--out` | `raw` | Output root directory |
| `--workers` | `4` | Parallel download workers |
| `--save-urls` | `./raw/kmip_urls.txt` | Where to write discovered URLs |
| `--urls FILE` | *(crawl first)* | Skip crawl; load URLs from an existing file |
| `--skip-file FILE` | `./raw/404skip.txt` | Skip URLs listed in this file, e.g. known 404s (missing file is fine) |
| `--no-skip` | *(off)* | Re-download files that already exist |

Requires PullMD running locally. Override the default `http://localhost:3000` with `PULLMD_URL` env var.

## Behaviour

- HTML pages → Markdown via PullMD (`frontmatter=true`). XML files → downloaded directly.
- URL path structure under `docs.oasis-open.org` is preserved under `--out`.
- Paths in `EXCLUDE_PREFIXES` (top of the script) are pruned from both the crawl and any `--urls` list. Currently excludes the `kmip-profiles/v3.0/csd01/test-cases/kmip-v3.0` subtree, which self-references into runaway depth from server mis-linking.
- Logs written to `./logs/kmip_crawler-{timestamp}.log` (directory is gitignored but kept via placeholder `.gitignore`).
- `raw/` contents and the script itself are gitignored — local-only artifacts.
- Python dependencies: `requests`, `beautifulsoup4`.
