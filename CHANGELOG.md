# Changelog

All notable changes to this project are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project aims
to follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `mcp_go/` — Go MCP server implementation: two standalone binaries (`kmip-kb`, `kmip-raw`) that are drop-in replacements for the Python FastMCP servers with no Python/venv dependency. Uses SQLite FTS5 BM25 search (via pure-Go `modernc.org/sqlite`) and the `mark3labs/mcp-go` stdio transport. `kmip-kb` supports an embedded-DB build (`make build-kb-embed`) that bakes the pre-indexed FTS5 database into the binary for deployment without a `kb/` tree on disk. 38 tests, all fixture-based with no dependency on live `kb/` or `raw/` data.
- `kb/examples/annotated-ttlv.md` — full worked example of an annotated TTLV hex dump, covering how to read the format (type-code table, header/value/padding layout), a complete Locate request with authentication, and the matching success response, each shown in both XML and annotated binary.
- Top-level `kb/index.md` — a knowledge-base landing page linking every category index, grouped into protocol surface, encoding/structure, cross-cutting guidance, and reference material.
- `kb/profiles/v1/index.md` — a sub-index listing all 52 v1.x named conformance profiles, grouped by capability (baseline, symmetric/asymmetric key, certificate, secret data, discover-versions, storage); linked from the profiles index.
- `xml_text` frontmatter field added to all 59 operation docs (`kb/operations/*.md` plus `server-to-client/notify.md` and `server-to-client/put.md`), recording the CamelCase XML text of each operation's value in the Operation Enumeration (e.g. `"CreateKeyPair"`, `"PKCS_11"`).
- Operation Enumeration table (`kb/enumerations/operation-enumeration.md`) now links every row's Name cell to its corresponding operation doc.
- `XML Text` column added to the message-structure encoding table.
- `tag_type` frontmatter field added to 223 KB docs that carry `tag_hex`/`xml_text`, recording the TTLV wire type (`Structure`, `Enumeration`, `Text String`, `Date-Time`, etc.) for each named KMIP tag. The one genuinely polymorphic tag (`UniqueIdentifier`) is intentionally omitted.
- `scripts/populate_tag_type.py` — derives `tag_type` from KMIP XML test-case files and a static override table; supports `--dry-run` and `--check` CI guard.
- `tag_type` property added to `schemas/frontmatter.schema.json` (optional enum of all eleven TTLV types).
- `scripts/enrich_mask_tables.py` — inserts an `XML Text` column (CamelCase KMIP-ENCODE §6.1.3 form) into the bit tables of `kb/encoding/*-mask.md` docs; idempotent with `--dry-run` and `--check` CI guard.
- `XML Text` column added to the `Fields & Structure` bit tables of all three mask docs (`cryptographic-usage-mask.md`, `protection-storage-mask.md`, `storage-status-mask.md`).

### Changed

- `Makefile` `build` target now builds both Go MCP binaries (`mcp_go/bin/kmip-kb` and `mcp_go/bin/kmip-raw`). New targets: `build-kb`, `build-raw`, `build-kb-embed`, `gen-db`, `test`, `test-kb`, `test-raw`, `test-parser`, `clean`.

### Fixed

- `kmip-raw` MCP server now exits immediately with a diagnostic message pointing to `scripts/kmip_crawler.py` if `raw/kmip/` is absent or empty, instead of silently building an empty index.

### Changed

- Category index pages now link every article in their tree: backfilled 35 previously-unlisted entries across the attributes, operations, objects, concepts, and references indexes (mostly v2.1 additions such as the `Rotate *`, protection-storage, session, and server-configuration families).
- Request Header and Response Header section headings in `kb/structures/operations.md` now include the CamelCase XML text identifier alongside the hex tag (e.g. `420077`, `RequestHeader`).
- `templates/object.md` now includes `tag_hex`, `xml_text`, and `tag_type` placeholder fields, matching the other managed-object templates.
- `templates/operation.md` now includes `tag_hex`, `xml_text`, and `tag_type` placeholder fields, with `tag_type` defaulting to `Structure`.
- `templates/structures.md`, `templates/enumeration.md`, and `templates/messages.md` now include a `tag_type` placeholder field (`Structure`, `Enumeration`, and `{{TagType}}` respectively).
- `scripts/populate_tag_type.py` now recognises the `object` and `operation` categories as deterministic `Structure` types in both conflict-resolution and category-fallback logic.
- Renamed field-table column `XML Element` to `XML Text` across all 146 KB docs, templates, and `scripts/enrich_field_tables.py` to align with the KMIP-ENCODE §6.1.3 term.
- Renamed `templates/ttlv.md` to `templates/encoding.md`; `scripts/build_kb_scaffold.py` and authoring docs updated.
- Enumeration `Fields & Structure` table columns renamed: `Value` → `Name`, `Hex` → `Value`; hex values no longer carry the `0x` prefix (e.g. `00000001` instead of `0x00000001`). `scripts/enrich_enum_tables.py` and all 62 enumeration docs updated.
- Removed `0x` prefix from inline hex values in structure and encoding docs (`kb/structures/`, `kb/encoding/`).

## [0.16.0] - 2026-06-16

### Added

- `kmip-raw` MCP server (`mcp_py/kmip_raw_server.py`) — FastMCP server exposing the 250+ raw crawled spec documents in `raw/` over stdio. Provides three tools: `search_raw` (BM25 full-text search with `doc_type`, `version`, and `final_only` filters), `get_doc` (paginated character-offset retrieval for large spec files), and `list_docs` (browse by doc type and version). Pre-wired in `.mcp.json` alongside `kmip-kb`.
- `mcp_py/README.md` — usage guide, quick Python test commands, and tool reference for both MCP servers.
- `mcp_py/start_kmip-raw.sh` — venv-aware start script for the `kmip-raw` server.

### Changed

- Renamed `mcp_py/start.sh` to `mcp_py/start_kmip-kb.sh` for consistency with the new `start_kmip-raw.sh`.
- Updated `.mcp.json` to use the renamed `start_kmip-kb.sh` and register the new `kmip-raw` server.

- New `templates/enumeration.md` template for `kb/enumerations/` docs. The `Fields & Structure` section now uses a table with `Value | Hex | XML Text | Description` columns, where `Hex` is the 8-digit integer value (e.g. `0x00000001`) and `XML Text` is the CamelCase enumeration value text per KMIP-ENCODE §6.1.3.
- `scripts/enrich_enum_tables.py` — inserts `Value | Hex | XML Text` tables into enumeration docs from spec data; idempotent with `--check` CI guard.
- New `templates/structures.md`, `templates/messages.md`, and `templates/profile.md` templates for the `structures`, `messages`, and `profile` KB categories (previously had no dedicated template).
- `tag_hex` and `xml_text` front matter values are now automatically included in each doc's `keywords` array to improve RAG retrieval by hex code and CamelCase identifier.
- Renamed front matter field `xml_element` → `xml_text` across all 223 KB docs, the frontmatter JSON Schema, scripts, templates, README, and authoring docs. The field represents the CamelCase XML text identifier used both as an element name for structure fields and as enumeration value text — `xml_text` captures this dual role more precisely.
- The `Encoding (Tag / Type / Length / Value)` section is now omitted from standard enumeration docs (all 60 that contained only the trivial "Encoded as a 4-byte integer" statement), since the tag is already in `tag_hex` front matter and the encoding is uniform for all enumerations. Four docs with non-standard encoding (item type, PKCS#11 return code, Tag, Unique Identifier) keep their Encoding sections.
- Reorganised `kb/profiles/` into four subdirectories by source section:
  `authentication/` ([KMIP-Prof] §3 auth suites), `base-encoding/`
  ([KMIP-Prof] §5.1–5.5 base/encoding profiles), `key-management/`
  ([KMIP-Prof] §5.6+ use-case profiles), and `v1/` (v1.x legacy named
  profiles from [KMIP-Prof] §4/§5). All intra-profile links and the profiles
  index are updated; `status_report.py` and `build_kb_scaffold.py` reflect the
  new layout; all seven prof-toc YAML files carry updated `target_path` values.
- Renamed `kb/ttlv/` directory to `kb/encoding/`; all 70 content docs, cross-links,
  scripts, TOC YAML files, MCP server docstrings, JSON Schema enum, and templates
  updated. `category: ttlv` → `category: encoding` across all affected docs.
- Narrowed the `kb/encoding/` category to TTLV wire encoding and bit masks.
  Data-structure articles (object, attribute, and operation building blocks)
  moved to a new `kb/structures/` category, and message-structure articles
  (request/response envelope and message fields) moved to a new `kb/messages/`
  category. Article paths and `category` front-matter values for the moved docs
  change accordingly.
- Moved enumeration docs from `kb/encoding/enumerations/` to a new top-level
  `kb/enumerations/` directory. All 64 enumeration docs change to
  `category: enumerations`. TOC YAML files, scripts, cross-links, and front-matter
  schema updated accordingly.
- Enriched `kb/attributes/key-format-type.md` with `tag_hex`/`xml_text` front
  matter (`420042`/`KeyFormatType`), structured Attribute Rules and Default Key
  Format Type tables (§4.26 Tables 79–81), and a Digest Interaction section
  covering dual-digest behaviour.

## [0.12.0] - 2026-06-15

### Added

- Field tables that document a structure's or payload's fields now carry `Tag`
  (6-digit hex) and `XML Text` (CamelCase name) columns next to each field,
  filled for fields that are named KMIP tags.
- `enrich_field_tables.py` populates and validates those columns (`--check`
  guard); included in the authoring validation checklist.

### Changed

- Renamed `mcp_server/` directory to `mcp_py/`; updated `.mcp.json`, `README.md`,
  and `CHANGELOG.md` references accordingly.

## [0.11.0] - 2026-06-12

### Added

- **All 135 remaining stubs authored and promoted to `reviewed`**, bringing the
  KB to 452/452 (100%) reviewed. Groups covered:
  - **16 v2.1 attributes**: `certificate-attributes`, `key-format-type`,
    `nist-key-type`, `opaque-data-type`, `protection-level`, `protection-period`,
    `protection-storage-mask`, `quantum-safe`, `rotate-automatic`, `rotate-date`,
    `rotate-generation`, `rotate-interval`, `rotate-latest`, `rotate-name`,
    `rotate-offset`, `short-unique-identifier`.
  - **1 concept**: `split-key-algorithms` (XOR, Shamir polynomial, Blakley).
  - **1 object**: `certificate-request` (v2.1 CSR managed object, PKCS#10/PEM/CRMF/CMC).
  - **1 reference**: `item-data-types` (all 10 TTLV primitive types).
  - **16 v2.1 operations**: `login`, `logout`, `delegated-login`, `ping`, `log`,
    `set-attribute`, `adjust-attribute`, `set-defaults`, `set-constraints`,
    `get-constraints`, `set-endpoint-role`, `re-provision`, `interop`, `pkcs-11`,
    `process`, `query-asynchronous-requests`.
  - **2 server-to-client operations**: `discover-versions` (§6.2.1),
    `set-endpoint-role` (§6.2.5).
  - **34 TTLV structures** (§5, §7, §12): `constraint`, `constraints`, `right`,
    `rights`, `ticket`, `defaults-information`, `object-defaults`,
    `derivation-parameters`, `asynchronous-request`,
    `asynchronous-correlation-values`, `pkcs-11-{function,interface,
    input-parameters,output-parameters,return-code}`, `interop-{function,
    identifier}`, `log-message`, `protection-storage-{mask,masks}`,
    `server-information`, `profile-version`, `usage-limits`,
    `storage-status-mask`, `attribute-reference`, `{common,private,public}-
    key-attributes`, `{new,current}-attribute`, `objects`, `object-{types,groups}`,
    `cryptographic-usage-mask`.
  - **64 enumeration docs** (§11.1–§11.64): all KMIP v2.1 enumerations.

## [0.10.0] - 2026-06-12

### Changed
- **All 317 KB content docs promoted `draft` → `reviewed`** after a full review
  pass per the CONTRIBUTING checklist: front-matter schema, no-verbatim, and
  link validators all clean; per-category technical spot checks. The 3 remaining
  `check_verbatim.py` flags are literal identifiers (TLS cipher-suite names,
  `LIBRARY-LTO*` namespaces) and are accepted as unavoidable.
- **KMIP 2.0 version notes** added to the 10 operation docs (Create, Register,
  Create Key Pair, Re-key, Re-key Key Pair, Re-certify, Certify, Derive Key,
  Create Split Key, Join Split Key) and `kb/ttlv/template-attribute-structures.md`,
  noting that the v1.x Template-Attribute wrappers were replaced by the flat §5
  Attributes structures in 2.0+.
- **Rewrote 3 prose overlaps** in `kb/profiles/suite-b-profiles.md` flagged by
  `check_verbatim.py`.
- **Removed the scaffold authoring comment** left in 82 `kb/usage-guide/` docs.
- **`kb/usage-guide/index.md`** — the last remaining stub, now an authored
  grouped index of all 83 usage-guide articles.

### Added
- **`tag_hex` and `xml_element` frontmatter fields** on 107 KB docs that map to a
  named KMIP tag (§11.56 Tag Enumeration). `tag_hex` is the 6-digit uppercase hex
  value (e.g. `"42000D"`); `xml_element` is the CamelCase XML element name per the
  official KMIP-ENCODE §6.1.3 algorithm (e.g. `"BatchCount"`), implemented and
  verified against v2.1 test-case XML. Covers `kb/attributes/`, `kb/ttlv/`,
  `kb/objects/`, `kb/concepts/`, and matching `kb/usage-guide/` docs. Edge cases:
  `X_509CertificateIdentifier`, `PKCS_12FriendlyName` (underscore before digit,
  per official spec algorithm). Both fields declared as optional in
  `schemas/frontmatter.schema.json`.
- **`scripts/populate_tag_fields.py`** — parses all v1.x, v2.0, and v2.1 spec
  tag tables and populates `tag_hex` / `xml_element` frontmatter in KB docs whose
  title matches a KMIP tag name. v2.1 is the primary source (354 tags); earlier
  versions add 17 tags deprecated by v2.0 so that `del_v2` docs are covered (6
  matched). Cross-version diff confirmed 0 renames and 79 tags first introduced
  in v2.0–v2.1. Idempotent (skips docs already populated). Supports `--dry-run`.

- **`kb/usage-guide/` — 83 new KMIP Usage Guide articles** (`status: draft`),
  covering the full KMIP-UG v2.1 document (§2 Design Goals, §3 Usage Notes,
  §4 Usage Examples, §5 Deprecations). All articles carry accurate `spec_versions`
  arrays, `related` slugs, and `keywords`; all pass `check_verbatim.py` (0-word
  runs), `validate_links.py` (0 issues), and `build_kb_scaffold.py --check`
  (0 schema errors). Brings the total KB to 317 draft articles, 0 stubs.
- **`ug-` prefix convention** for `source_section` (e.g., `source_section: "ug-3.1"`),
  analogous to the existing `prof-` prefix; `check_verbatim.py` routes `ug-`
  prefixed sections to the KMIP-UG source document rather than KMIP-SPEC.
- **`--source ug` scaffold support** in `build_kb_scaffold.py`: new
  `UG_PREFIX_RULES` dict, `ug_path_for(version)` helper, and TOC output at
  `kb/versions/<ver>-ug-toc.yaml`; v1.x UG sourced from `raw/kmip/ug/`,
  v2.x from `raw/kmip/kmip-ug/`.
- **7 UG TOC files** generated for all supported versions: `1.0-ug-toc.yaml`
  (36 sections) through `2.1-ug-toc.yaml` (83 sections).
- `"usage-guide"` added to the `category` enum in `schemas/frontmatter.schema.json`.
- `templates/usage-guide.md` — new stub template for UG articles (Overview,
  Guidance, Implementation Notes, Related Concepts sections).
- `"kb/usage-guide"` added to `CONTENT_DIRS` in `status_report.py` and to
  `ALL_KB_DIRS` in `validate_links.py`.

- **Authored all 56 remaining `kb/profiles/` stubs** (`stub → draft`), bringing
  the knowledge base to 234 docs, 0 stubs, 234 drafts (100% draft coverage):
  - `tls-1-2-authentication-suite.md` — TLS 1.2 Authentication Suite, v1.0–v1.2;
    `spec_versions` corrected from `["1.0"]` to `["1.0", "1.1", "1.2"]`.
  - **v1.0 combined client+server profiles** (6 files): `secret-data-kmip-profile.md`,
    `basic-symmetric-key-store-and-server-kmip-profile.md` (updated to `["1.0","1.1"]`),
    `basic-symmetric-key-foundry-and-server-kmip-profile.md` (updated to `["1.0","1.1"]`),
    and their three TLS 1.2 authentication variants.
  - **v1.1 Basic server profiles** (8 files): Discover Versions, Baseline, Secret
    Data, Asymmetric Key Store, Asymmetric Key + Certificate Store, Asymmetric Key
    Foundry, Certificate, and Asymmetric Key Foundry + Certificate.
  - **v1.1 Basic client profiles** (10 files): the full client-side mirror of the
    server set, plus Symmetric Key Store and Symmetric Key Foundry clients.
  - **v1.1 TLS 1.2 server and client variants** (20 files): one-for-one TLS 1.2
    transport variants of each v1.1 Basic server and client profile.
  - **Storage client profiles** (2 files): `storage-client-kmip-profile.md` and its
    TLS 1.2 variant — Opaque Managed Object storage (not Secret Data).
  - **v1.2 renamed Baseline and Complete profiles** (6 files): `baseline-server-basic-kmip-profile.md`,
    `baseline-server-tls-v1-2-kmip-profile.md`, `baseline-client-basic-kmip-profile.md`,
    `baseline-client-tls-v1-2-kmip-profile.md`, `complete-server-basic-kmip-profile.md`,
    `complete-server-tls-v1-2-kmip-profile.md` — v1.2 cosmetic word-order renames
    from v1.1 "Basic Baseline" → "Baseline Basic"; Complete Server profiles introduce
    the highest v1.2 compliance tier.
  - **Quantum Safe trio** (3 files): `quantum-safe-client.md` and
    `quantum-safe-server.md` (both `spec_versions` corrected from `["2.0"]` to
    `["2.0","2.1"]`), and `mandatory-quantum-safe-test-cases-kmip-v2-0.md` —
    includes full algorithm matrix (AES, ChaCha20, McEliece-6960119,
    McEliece-8192128, SPHINCS-256, ECDSA, Ed25519), three new attributes (Protection
    Level, Protection Period, Quantum Safe), algorithm-selection behavior, and the
    two mandatory v2.0 test cases (QS-M-1-20, QS-M-2-20).
- **KMIP KB MCP server** (`mcp_py/kmip_kb_server.py`) — FastMCP server
  exposing the knowledge base over stdio with four tools: `search_kb` (BM25
  full-text search), `get_article` (full article retrieval), `list_articles`
  (front-matter-filtered listing), `get_related` (related-article discovery).
  Pre-wired for Claude Code via `.mcp.json` and `.claude/settings.json`; a
  `kmip-authoring` coding-agent skill added at `.claude/skills/kmip-authoring.md`.
- **59 new `kb/profiles/` stubs** generated from KMIP-Prof v1.0–v1.4 and v2.0:
  granular per-profile entries (basic/complete server variants, symmetric and
  asymmetric key foundry variants, certificate, secret data, storage, and
  discover-versions profiles), plus `quantum-safe-client.md`,
  `quantum-safe-server.md`, and `mandatory-quantum-safe-test-cases-kmip-v2-0.md`.
- `kb/versions/2.0-prof-toc.yaml`, `1.4-prof-toc.yaml`, `1.3-prof-toc.yaml`,
  `1.2-prof-toc.yaml`, `1.1-prof-toc.yaml`, `1.0-prof-toc.yaml` — KMIP-Prof
  section→file maps for all v1.x and v2.0 releases (8–44 sections each).
- `PROF_V1X_EARLY_RULES` and `get_prof_prefix_rules(version)` in
  `build_kb_scaffold.py` — handles v1.0–v1.2 KMIP-Prof documents where profile
  definitions sit in §4 (§5 is Conformance Clauses in those releases) rather
  than §5 as in v1.3+.
- **`enc-` prefix convention** for `v1_source_section` values that trace to the
  separate `[KMIP-ENCODE]` document (*KMIP Additional Message Encodings v1.0*);
  documented in `CLAUDE.md`. `v1_source_section: "enc-2/4/6"` added to
  `https-profiles.md`, `json-profiles.md`, and `xml-profiles.md` respectively,
  along with a Version History section in each article.
- **Suite B profile articles authored** (`stub → draft`): `suite-b-profiles.md`,
  `suite-b-minlos-128-authentication-suite.md`,
  `suite-b-minlos-192-authentication-suite.md` — covering v1.0–v1.4, sourced
  from the standalone `kmip-suite-b-profile/v1.0` companion and KMIP-Prof
  §3.3/§3.4/§5.13; includes P-256/P-384 algorithm table, cipher-suite
  requirements, NSA deprecation note (2017), and absence from KMIP-Prof v2.0+.
- **Enriched 7 use-case profile articles** from standalone companion docs
  (`kmip-*-profile/v1.0`): added test case naming convention, Permitted Test
  Case Variations sections, conformance asymmetry rules (client vs. server pass
  requirements), and v1.x provenance notes to `asymmetric-key-lifecycle-profiles.md`,
  `cryptographic-profiles.md`, `opaque-managed-object-store-profiles.md`,
  `storage-array-with-self-encrypting-drives-profiles.md`
  (including Template-removal and capacity deltas),
  `symmetric-key-foundry-for-fips-140-profiles.md`,
  `symmetric-key-lifecycle-profiles.md`, and `tape-library-profiles.md`
  (including VENDOR-LIBRARY-LTO namespace and x-Barcode Custom Attribute).
- **17 new `kb/profiles/` articles** sourced from the KMIP Profiles document
  ([KMIP-Prof] v2.1, separate from KMIP-SPEC):
  - Authentication suites: `basic-authentication-suite.md`,
    `https-authentication-suite.md`
  - Base/encoding profiles: `base-profiles.md`, `complete-server-profile.md`,
    `https-profiles.md`, `xml-profiles.md`, `json-profiles.md`
  - Key-management use-case profiles: `symmetric-key-lifecycle-profiles.md`,
    `symmetric-key-foundry-for-fips-140-profiles.md`,
    `asymmetric-key-lifecycle-profiles.md`, `cryptographic-profiles.md`,
    `opaque-managed-object-store-profiles.md`,
    `storage-array-with-self-encrypting-drives-profiles.md`,
    `tape-library-profiles.md`, `aes-xts-profiles.md`,
    `quantum-safe-profiles.md` (§5.14–5.17 consolidated),
    `pkcs-11-profiles.md`
  - `kb/profiles/index.md` updated with links to all articles.
- `kb/versions/2.1-prof-toc.yaml` — machine-readable section→file map for
  KMIP-Prof v2.1 (20 profile-family entries from §3 and §5).
- **`build_kb_scaffold.py --source prof`** flag: scaffolds from the KMIP-Prof
  document instead of KMIP-SPEC. Adds `PROF_PREFIX_RULES` (§3 auth suites,
  §5 profile definitions at depth 2), `prof_path_for()` resolver, and writes
  TOC to `<ver>-prof-toc.yaml`. Stubs emitted with `source_section: "prof-N.M"`.
- **`check_verbatim.py`** now resolves `prof-*` `source_section` values against
  the KMIP-Prof document rather than KMIP-SPEC.

### Fixed
- `spec_versions` in `schemas/index.md` and `schemas/agent/index.md` narrowed
  to `["1.0"]`; these are project-level index files, not versioned spec content.
- Typo in `symmetric-key-foundry-for-fips-140-profiles.md`: attribute name
  corrected from `Protect Stop Date` to `Process Stop Date`.

## [0.9.0] - 2026-06-11

### Added
- `Makefile`: `report` target runs `scripts/status_report.py`; `crawl` target
  runs `scripts/kmip_crawler.py` (extracted from old `build`).
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
  ttlv, reference) plus `agent-relations.yaml` for Graph RAG relation files.
- `versions/1.4-toc.yaml` — generated section→file map for KMIP v1.4.
- `CONTRIBUTING.md` — content rules, the no-verbatim rule, authoring workflow,
  and review checklist.

### Changed
- `Makefile`: `build` target is now a stub (`echo "Coming Soon"`).
- `.gitignore`: removed `docs/` exclusion so a generated `docs/` directory can
  be tracked.
- **Repo restructured: all KB content moved under `kb/`.** The 11 content
  directories (`attributes`, `concepts`, `examples`, `mappings`, `objects`,
  `operations`, `profiles`, `references`, `ttlv`, `versions`, `workflows`)
  now live under `kb/`; the root retains only `schemas/`, `templates/`, and
  `scripts/`. Scripts updated: `CATEGORY_DIR` and `STRUCTURE_DIRS` in
  `build_kb_scaffold.py`, `CONTENT_DIRS` in `status_report.py`,
  `ALL_KB_DIRS` in `validate_links.py`, and the default path in
  `check_verbatim.py`. Cross-links in `kb/workflows`, `kb/examples`, and
  `kb/mappings` index pages corrected for their new sibling position inside
  `kb/`. `README.md` and `CLAUDE.md` updated throughout.
- **Baseline moved from v1.4 to v2.1.** Each doc now carries both
  `source_section` (the v2.1 baseline section) and a new optional
  `v1_source_section` (the v1.x section for the same concept, e.g.
  `attributes/link.md` → `source_section: "4.31"`, `v1_source_section: "3.35"`).
  The five docs removed in v2.0 carry `source_section: "del_v2"` with their last
  v1.x section in `v1_source_section`. v2.x-only features (no v1 mapping) omit
  `v1_source_section`. The schema, `build_kb_scaffold.py` (render + validate),
  and `check_verbatim.py` (anchors `del_v2` docs against their v1.x section)
  were updated accordingly.
  `source_section` front matter is now v2.1 section numbering: 142 docs renumbered from the committed
  `versions/2.1-toc.yaml` (e.g. `operations/create.md` §4.1 → §6.1.8,
  `attributes/name.md` §3.2 → §4.32, `ttlv/key-block.md` §2.1.3 → §3.1), plus
  renamed/restructured docs mapped by hand (client/server correlation values →
  §9.9/§9.10, `ttlv/ttlv-encoding.md` → §10.1, `concepts/error-handling.md` →
  no discrete v2.x section). `spec_version` set to `"2.1"` on every doc present
  in v2.1. The five docs removed in v2.0 (`objects/template.md`,
  `attributes/certificate-identifier/subject/issuer.md`,
  `attributes/operation-policy-name.md`) keep their last-present v1.x
  baseline and numbering.
- `scripts/build_kb_scaffold.py` `--version` default changed `1.4` → `2.1`.
- Baseline declarations updated in `README.md`, `CLAUDE.md`, and the
  `schemas/frontmatter.schema.json` example; CLAUDE.md's section→category map
  now leads with v2.1 numbering.
- In-body `§` cross-references across ~20 content docs re-anchored to v2.1
  numbering (v1.x noted where useful) — references, profiles, concepts,
  operations/attributes/ttlv index pages, and the `protocol-version` /
  `ttlv-encoding` / `operation(s)` / `result-reason` / `attribute` structures.
  Version-negotiation examples in `ttlv/protocol-version.md` now use 2.x.
- Reworded five field-table rows (`attributes/digest`, `link`,
  `revocation-reason`; `operations/export`, `get-usage-allocation`) to keep
  the no-verbatim guard green against the v2.1 source, which it now checks.
- Meta/index pages (`examples`, `mappings`, `workflows`, `schemas`,
  `schemas/agent` indexes) extended to the full `spec_versions` range; document
  skeletons in `templates/` rebased to `spec_version: "2.1"`,
  `spec_versions: ["2.1"]`.
- `README.md` rewritten knowledge-base-first; the crawler is documented as
  secondary, private source-preparation tooling.
- `CLAUDE.md` updated with the knowledge-base layout, the scaffold generator,
  the front-matter contract, and the no-verbatim rule.

### Fixed
- `scripts/kmip_crawler.py` now prunes paths in `EXCLUDE_PREFIXES` from both the
  crawl and any `--urls` list, starting with the
  `kmip-profiles/v3.0/csd01/test-cases/kmip-v3.0` subtree that self-references
  into runaway depth from server mis-linking.
- Removed two orphaned operation stubs (`operations/notify.md`,
  `operations/put.md`) left at the top level before server-to-client routing
  existed; the correct copies live under `operations/server-to-client/`.

[Unreleased]: https://github.com/kmip-dev/kmip-dev/compare/v0.16.0...HEAD
[0.16.0]: https://github.com/kmip-dev/kmip-dev/compare/v0.12.0...v0.16.0
[0.12.0]: https://github.com/kmip-dev/kmip-dev/compare/v0.11.0...v0.12.0
[0.11.0]: https://github.com/kmip-dev/kmip-dev/compare/v0.10.0...v0.11.0
[0.10.0]: https://github.com/kmip-dev/kmip-dev/compare/v0.9.0...v0.10.0
[0.9.0]: https://github.com/kmip-dev/kmip-dev/releases/tag/v0.9.0
