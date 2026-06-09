# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This project is an **independently written KMIP knowledge base** — original summaries, explanations, implementation guidance, examples, and machine-readable metadata for the OASIS Key Management Interoperability Protocol, structured for LLM wikis, RAG, GraphRAG, and coding agents. It targets the **KMIP 1.x** family (v1.0–v1.4), baseline **v1.4**.

The spec is mirrored locally into `raw/` (gitignored) only as a *source* for authoring; the crawler that builds that mirror is secondary tooling.

## The one hard rule: never copy spec prose

Never paste specification text, tables, or definitions into any tracked file. Read `raw/` for understanding, then write original prose. `source_section` front matter is traceability only — it does not license quoting. See `CONTRIBUTING.md`.

## Knowledge-base layout

`concepts/ operations/ (operations/server-to-client/) objects/ attributes/ ttlv/ profiles/ workflows/ examples/ schemas/ (schemas/agent/) mappings/ versions/ references/` plus `templates/`.

Spec section → category mapping: §2.2 Managed Objects→`objects/`, §2.1 Base Objects + §6/§7/§9 Message Contents/Format/Encoding→`ttlv/`, §3→`attributes/`, §4/§5→`operations/`, §8/§10/§11→`concepts/`, §12→`profiles/`, §1→`references/`.

Every doc has YAML front matter validated against `schemas/frontmatter.schema.json`, with `status: stub | draft | reviewed`.

## Authoring content

Fill a stub's existing section headers with original prose, populate front
matter (`spec_versions` per the versions a concept appears in, real `related`
slugs, `keywords`), then flip `status: stub` → `draft`. Match the depth and
cross-reference style of already-authored docs (e.g. `operations/register.md`,
`objects/symmetric-key.md`). Use relative links (e.g.
`[Key Block](../ttlv/key-block.md)`) and confirm targets exist (stub or
authored) before linking. Validate before committing:

```
python scripts/build_kb_scaffold.py --check    # front matter vs JSON Schema
python scripts/check_verbatim.py <dir>          # flags shared 8+-word runs vs source_section
```

Authored so far: all of `operations/` (client-to-server) and `objects/`.

## Scaffold generator

`scripts/build_kb_scaffold.py` — parses a raw 1.x spec and (re)generates dirs, one empty stub per section, and `versions/<ver>-toc.yaml`. Pure stdlib. **Never overwrites a file whose `status` ≠ `stub`**, so it is safe to re-run.

```
python scripts/build_kb_scaffold.py [--version 1.4] [--out .] [--toc-only] [--no-stubs] [--check]
```

The section→category rules and per-section stub depth live in `PREFIX_RULES` at the top of the script; stub bodies come from `templates/<category>.md`.

## Crawler (source preparation, private)

`scripts/kmip_crawler.py` — unified crawl + download in one pass.

```
python scripts/kmip_crawler.py [--out raw] [--workers 4] [--save-urls ./raw/kmip_urls.txt] [--urls FILE] [--no-skip]
```

| Flag | Default | Effect |
|---|---|---|
| `--out` | `raw` | Output root directory |
| `--workers` | `4` | Parallel download workers |
| `--save-urls` | `./raw/kmip_urls.txt` | Where to write discovered URLs |
| `--urls FILE` | *(crawl first)* | Skip crawl; load URLs from an existing file |
| `--no-skip` | *(off)* | Re-download files that already exist |

Requires PullMD running locally. Override the default `http://localhost:3000` with `PULLMD_URL` env var.

## Behaviour

- HTML pages → Markdown via PullMD (`frontmatter=true`). XML files → downloaded directly.
- URL path structure under `docs.oasis-open.org` is preserved under `--out`.
- Paths in `EXCLUDE_PREFIXES` (top of the script) are pruned from both the crawl and any `--urls` list. Currently excludes the `kmip-profiles/v3.0/csd01/test-cases/kmip-v3.0` subtree, which self-references into runaway depth from server mis-linking.
- Logs written to `./logs/kmip_crawler-{timestamp}.log` (directory is gitignored but kept via placeholder `.gitignore`).
- `raw/` contents and the script itself are gitignored — local-only artifacts.
- Python dependencies: `requests`, `beautifulsoup4`.
