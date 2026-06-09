# Changelog

All notable changes to this project are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project aims
to follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Authored all 9 managed object types plus the category index (`objects/*.md`)
  as original prose (`status: draft`): purpose, structure, key attributes,
  lifecycle/state, and cross-references into `operations/`, `attributes/`, and
  `ttlv/`. `spec_versions` reflect availability per type (PGP Key from v1.2;
  Template present v1.0–v1.4 but deprecated in v1.3). Verified clean by
  `check_verbatim.py`.
- Authored all 41 client-to-server operations (`operations/*.md`) as original
  prose (`status: draft`): purpose, request/response fields, behavior, errors,
  and cross-references, with `spec_versions` computed per operation across
  v1.0–v1.4. Includes `operations/re-key.md` (§4.4), whose heading was lost in
  source conversion and which is therefore not produced by the generator.
- `scripts/check_verbatim.py` — no-verbatim guard that flags any shared 8+-word
  run between an authored doc and its `source_section` in the raw spec.
- `--prune` mode on `scripts/build_kb_scaffold.py` — removes orphaned stub files
  no longer produced by the rules (never touches `draft`/`reviewed` docs).
- `--skip-file` option on `scripts/kmip_crawler.py` (default `./raw/404skip.txt`)
  — skips URLs listed in the file, e.g. known 404s, before download; a missing
  file is ignored.

### Fixed
- `scripts/kmip_crawler.py` now prunes paths in `EXCLUDE_PREFIXES` from both the
  crawl and any `--urls` list, starting with the
  `kmip-profiles/v3.0/csd01/test-cases/kmip-v3.0` subtree that self-references
  into runaway depth from server mis-linking.
- Removed two orphaned operation stubs (`operations/notify.md`,
  `operations/put.md`) left at the top level before server-to-client routing
  existed; the correct copies live under `operations/server-to-client/`.

### Added (scaffold)
- Knowledge-base scaffold targeting the KMIP 1.x family (baseline v1.4):
  directory structure (`concepts/`, `operations/` + `operations/server-to-client/`,
  `objects/`, `attributes/`, `ttlv/`, `profiles/`, `workflows/`, `examples/`,
  `schemas/` + `schemas/agent/`, `mappings/`, `versions/`, `references/`).
- `scripts/build_kb_scaffold.py` — pure-stdlib generator that parses a raw 1.x
  spec, classifies each section, and emits one stub per section, an `index.md`
  per directory, and `versions/<ver>-toc.yaml`. Modes: `--check`, `--toc-only`,
  `--no-stubs`, `--version`, `--spec`, `--out`. Never overwrites a file whose
  `status` is no longer `stub`.
- 157 section stubs + per-directory index files generated from KMIP v1.4
  (front matter + headers only; no specification prose).
- `schemas/frontmatter.schema.json` — JSON Schema for document front matter,
  enforced by the generator's `--check` mode.
- `templates/` — document skeletons (operation, attribute, object, concept,
  ttlv, reference) plus `agent-relations.yaml` for GraphRAG relation files.
- `versions/1.4-toc.yaml` — generated section→file map for KMIP v1.4.
- `CONTRIBUTING.md` — content rules, the no-verbatim rule, authoring workflow,
  and review checklist.

### Changed
- `README.md` rewritten knowledge-base-first; the crawler is documented as
  secondary, private source-preparation tooling.
- `CLAUDE.md` updated with the knowledge-base layout, the scaffold generator,
  the front-matter contract, and the no-verbatim rule.

[Unreleased]: https://github.com/kmip-dev/kmip-dev/commits/main
