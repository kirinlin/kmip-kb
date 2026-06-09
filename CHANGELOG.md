# Changelog

All notable changes to this project are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project aims
to follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
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
