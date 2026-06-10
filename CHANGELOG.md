# Changelog

All notable changes to this project are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project aims
to follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `versions/2.0-toc.yaml` (215 sections) and `versions/2.1-toc.yaml` (234
  sections) — generated section→file maps for KMIP v2.0 and v2.1.
  `scripts/build_kb_scaffold.py` extended with `V20_PREFIX_RULES` (v2.x has a
  completely different section numbering from v1.x) and `spec_path_for()`
  updated to resolve `raw/kmip/kmip-spec/v<ver>/os/` for v2.x.
- Full per-release delta notes in `versions/index.md` for v2.0 and v2.1:
  - **v2.0**: structural renumbering, 9 new client-to-server operations
    (Adjust Attribute, Delegated Login, Interop, Log, Login/Logout, PKCS#11,
    Re-Provision, Set Attribute, Set Endpoint Role), 2 new server-to-client
    operations, Certificate Request object, 5 new attributes (NIST Key Type,
    Protection Level/Period/Storage Mask, Quantum Safe, Short Unique
    Identifier), §5 Attribute Data Structures overhaul, §10.2 alternate wire
    formats, and removal of Template, deprecated cert attributes, and
    Operation Policy Name.
  - **v2.1**: 7 Rotate* key-rotation policy attributes, constraints sub-system
    (Get/Set Constraints + Constraint/Constraints structures), asynchronous-
    request management (Query Asynchronous Requests + companion structures),
    and Ping/Process/Set Defaults utility operations.
- `spec_versions` front matter updated across all 162 KB docs: "2.0" added
  to all docs whose feature is present in v2.0; "2.1" added to all docs
  carrying "2.0" (v2.1 is purely additive). Five docs correctly excluded from
  both (removed in v2.0): `objects/template.md`, `attributes/certificate-
  identifier/subject/issuer.md`, `attributes/operation-policy-name.md`.

### Added
- `versions/1.0-toc.yaml`, `versions/1.1-toc.yaml`, `versions/1.2-toc.yaml`,
  `versions/1.3-toc.yaml` — generated section→file maps for KMIP v1.0–v1.3,
  produced by `scripts/build_kb_scaffold.py --version <ver> --toc-only`
  (section counts: 104 / 112 / 134 / 143 respectively). All five 1.x releases
  now have committed ToC maps.
- Full per-release delta notes in `versions/index.md` covering v1.1–v1.3 (v1.4
  summary unchanged), each section linking to the relevant KB docs:
  - **v1.1**: X.509 certificate attribute expansion and deprecations, Discover
    Versions, Re-key Key Pair, Extension Information, Encoding Option.
  - **v1.2**: 11 cryptographic service operations (Encrypt/Decrypt, Sign/Verify,
    MAC/MAC Verify, RNG Retrieve/Seed, Hash), Create/Join Split Key, PGP Key
    object, 5 crypto-op structures (Data, Data Length, Signature Data, MAC Data,
    Nonce), 4 attributes, and the full attestation story (Attestation credential
    type, Nonce challenge/response, Attestation Capable Indicator, Query
    Attestation Types).
  - **v1.3**: streaming multi-part crypto (Correlation Value, Init/Final
    Indicator), capability reporting structures (RNG Parameters, Profile/
    Validation/Capability Information), Random Number Generator attribute,
    server-to-client Query, and deprecations (Template, Operation Policy Name,
    legacy Transparent EC key forms).
- `spec_versions` front matter verified against ToC diffs across all 53
  version-boundary docs (v1.1/1.2/1.3/1.4 new sections); 0 errors found.

### Added
- Authored all remaining stub content (119 docs) as original prose
  (`status: draft`), bringing the knowledge base to 100% draft coverage
  (158 content docs, 0 stubs):
  - `attributes/` — all 51 attributes (§3.1–§3.51) plus a grouped index:
    data types and structure tables, constraints (instance rules, mutability,
    lifecycle freezing), applies-to object types, and set/modified-by rules;
    `spec_versions` computed per attribute across v1.0–v1.4.
  - `ttlv/` — all 45 docs covering §2.1 base objects, §6 message contents,
    §7 message format, and §9.1 TTLV encoding, with tag hex values from the
    §9.1.3.1 registry, plus a structured index.
  - `concepts/` — authentication, transport, and error handling, plus index.
  - `operations/` — the three server-to-client operations (Notify, Put, and
    the v1.3+ Query) with their index, and a categorized top-level
    operations index.
  - `profiles/` — server and client implementation conformance plus index.
  - `references/` — IPR policy, terminology, normative and non-normative
    references, plus index.
  - Index pages for `examples/`, `mappings/`, `workflows/`, and `versions/`,
    each listing planned content.
  - Validated by `build_kb_scaffold.py --check`, `validate_links.py`, and
    `check_verbatim.py` (all categories clean; `operations/re-key.md`
    remains manual-review-only because §4.4's heading was lost in source
    conversion).
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
