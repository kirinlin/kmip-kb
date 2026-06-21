# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This project is an **independently written KMIP knowledge base** — original summaries, explanations, implementation guidance, examples, and machine-readable metadata for the OASIS Key Management Interoperability Protocol, structured for LLM wikis, RAG, Graph RAG, and coding agents. It targets the **KMIP 1.x and 2.x** families (v1.0–v1.4, v2.0–v2.1), baseline **v2.1**.

The spec is mirrored locally into `raw/` (gitignored) only as a *source* for authoring; the crawler that builds that mirror is secondary tooling.

## The one hard rule: never copy spec prose

Never paste specification text, tables, or definitions into any tracked file. Read `raw/` for understanding, then write original prose. `source_section` front matter is traceability only — it does not license quoting. See `CONTRIBUTING.md`.

## Knowledge-base layout

`kb/concepts/ kb/operations/ (kb/operations/server-to-client/) kb/objects/ kb/attributes/ kb/encoding/ kb/enumerations/ kb/structures/ kb/messages/ kb/profiles/ (kb/profiles/authentication/ kb/profiles/base-encoding/ kb/profiles/key-management/ kb/profiles/v1/) kb/usage-guide/ (kb/usage-guide/messaging/ kb/usage-guide/discovery/ kb/usage-guide/identity/ kb/usage-guide/lifecycle/ kb/usage-guide/identification/ kb/usage-guide/attributes/ kb/usage-guide/key-material/ kb/usage-guide/asymmetric/ kb/usage-guide/crypto-services/) kb/versions/ kb/references/ kb/workflows/ kb/examples/ kb/mappings/` plus `schemas/ (schemas/agent/) templates/` and `mcp_py/` (two FastMCP servers: `kmip-kb` over `kb/`, `kmip-raw` over `raw/`). The `kmip-raw` server exits immediately with a diagnostic message if `raw/kmip/` is absent or empty — run `python scripts/kmip_crawler.py` first.

`kb/profiles/` subdirectories: `authentication/` ([KMIP-Prof] §3 — auth suites), `base-encoding/` ([KMIP-Prof] §5.1–5.5 — base, complete-server, HTTPS/XML/JSON encoding profiles), `key-management/` ([KMIP-Prof] §5.6+ — symmetric/asymmetric lifecycle, cryptographic services, tape/SED/AES-XTS/quantum-safe/PKCS#11 profiles), `v1/` ([KMIP-Prof] §4 — v1.x legacy named profiles). Index and implementation-conformance docs stay at the `kb/profiles/` root.

Spec section → category mapping (baseline **v2.1** numbering): §2 Objects→`kb/objects/`, §10.1 TTLV + §12 Bit Masks→`kb/encoding/`, §11 Enumerations→`kb/enumerations/`, §3 Object Data Structures + §5 Attribute Data Structures + §7 Operations Data Structures→`kb/structures/`, §8/§9 Messages→`kb/messages/`, §4 Attributes→`kb/attributes/`, §6.1 client + §6.2 server-to-client→`kb/operations/`, §10.3/§10.4 Authentication/Transport + §13 Algorithm Implementation→`kb/concepts/`, §14→`kb/profiles/`, §1→`kb/references/`. (v1.x used a different scheme: §2.1 Base Objects→`kb/structures/`, §2.2→`kb/objects/`, §3→`kb/attributes/`, §4/§5→`kb/operations/`, §6/§7→`kb/messages/`, §9→`kb/encoding/`, §8/§10/§11→`kb/concepts/`, §12→`kb/profiles/`; both rule sets live in `V1X_PREFIX_RULES`/`V20_PREFIX_RULES`.)

Every doc has YAML front matter validated against `schemas/frontmatter.schema.json`, with `status: stub | draft | reviewed`. `source_section` is the **v2.1** baseline section; `v1_source_section` (optional) records the v1.x section for the same concept. Features removed in v2.0 use `source_section: "del_v2"` and keep their last v1.x section in `v1_source_section`; v2.x-only features omit `v1_source_section`.

Three optional fields are present on docs that map to a named KMIP tag (§11.56 Tag Enumeration):
- `tag_hex`: 6-digit uppercase hex tag value, e.g. `"42000D"` — enables hex-lookup search.
- `xml_text`: CamelCase XML text identifier per KMIP-ENCODE §6.1.3, e.g. `"BatchCount"` — used as the XML element name for structure fields and as the enumeration value text for enumeration tags. Enables XML-context search. Populated by `scripts/populate_tag_fields.py`; 223 docs carry these fields. Edge-case forms: `X_509CertificateIdentifier`, `PKCS_12FriendlyName` (underscore before digits, per the official spec algorithm verified against v2.1 test-case XML). The script also parses all v1.x and v2.0 specs to cover the 17 tags deprecated by v2.0 (17 identified via cross-version diff; 6 have KB docs). Both `tag_hex` and `xml_text` values are automatically added to `keywords` for RAG retrieval.
- `tag_type`: TTLV type byte for this tag — what encoding the tag's value uses on the wire. One of: `Structure`, `Integer`, `Long Integer`, `Big Integer`, `Enumeration`, `Boolean`, `Text String`, `Byte String`, `Date-Time`, `Interval`, `Date-Time Extended`. Populated by `scripts/populate_tag_type.py` (requires `raw/` XML test cases); 223 docs carry this field. Omitted for the single genuinely polymorphic tag (`UniqueIdentifier`, which may be Text String, Integer, or Enumeration depending on context). The script infers type from KMIP XML test-case files, supplemented by `_STATIC_OVERRIDES` for tags absent from the test corpus (del_v2 attributes, obscure v2.1 fields) and category fallbacks for unambiguous cases (`enumerations` → Enumeration, `structures` → Structure, `operation` → Structure). Run it after `populate_tag_fields.py`:

```
python scripts/populate_tag_type.py [--dry-run] [--check]   # --check exits non-zero if any resolvable doc is missing tag_type
```

## Field tables (Tag / XML Text columns)

Every table that documents the fields of a KMIP structure or operation payload
starts with a `Field` column, followed by `Tag` and `XML Text` columns, then
the table's own columns (`Required`, `Type`, `Description`, …):

```
| Field | Tag | XML Text | Required | Description |
```

`Tag` holds the 6-digit uppercase hex tag value in backticks (e.g. `` `420057` ``)
and `XML Text` the CamelCase element name in backticks (e.g. `` `ObjectType` ``)
— the same two identifiers carried in front matter by `tag_hex`/`xml_text`.
Rows whose field is not a named tag (e.g. a generic "Managed Object" placeholder)
leave both cells blank. `scripts/enrich_field_tables.py` fills these columns from
the shared tag lookup; it only targets tables whose header's first column is
exactly `Field`, reuses an existing `Tag` column where one is present, never
overwrites a populated cell, and is idempotent. 137 docs / 199 field tables /
506 tagged rows currently carry these columns. Run it after authoring or editing
a field table:

```
python scripts/enrich_field_tables.py [--dry-run] [--check]   # --check exits non-zero if any table is stale
```

## Enumeration docs (kb/enumerations/)

Enumeration docs use the `templates/enumeration.md` template (not `templates/encoding.md`). Their `Fields & Structure` section holds a value table with columns `Name | Value | XML Text | Description`:

```
| Name | Value | XML Text | Description |
|---|---|---|---|
| Certificate | `00000001` | `Certificate` | ... |
```

`Value` is the 8-digit hex integer value of each enumeration value (e.g. `00000001`). `XML Text` is the CamelCase text per KMIP-ENCODE §6.1.3 — the text that appears inside the XML element when encoding the value in XML. The `Description` column is author-filled.

`scripts/enrich_enum_tables.py` inserts these tables from spec data and is idempotent. Run it when adding or editing enumeration docs:

```
python scripts/enrich_enum_tables.py [--dry-run] [--check]   # --check exits non-zero if any table is stale
```

The `Encoding (Tag / Type / Length / Value)` section is **omitted** from enumeration docs that encode as a standard 4-byte TTLV Integer (type `05`) — the tag is already in `tag_hex` front matter and the encoding is uniform. Only docs where the encoding is non-standard (e.g. `item-type-enumeration.md`, `tag-enumeration.md`) keep an Encoding section.

## Bit-mask docs (kb/encoding/*-mask.md)

Bit-mask docs (`cryptographic-usage-mask.md`, `protection-storage-mask.md`,
`storage-status-mask.md`) have a `Fields & Structure` section with a bit table
whose second column names each flag. An `XML Text` column follows the name column:

```
| Bit | Usage | XML Text |
|---|---|---|
| 0 (0x00000001) | Sign | `Sign` |
| 4 (0x00000010) | Wrap Key | `WrapKey` |
```

`XML Text` is the CamelCase form derived by the KMIP-ENCODE §6.1.3 algorithm
applied to the bit name (e.g. "Wrap Key" → `WrapKey`, "On-Line Storage" →
`OnLineStorage`). `scripts/enrich_mask_tables.py` inserts this column and is
idempotent. Run it when adding or editing a mask doc:

```
python scripts/enrich_mask_tables.py [--dry-run] [--check]   # --check exits non-zero if any table is stale
```

## source_section for KMIP-Prof articles

Articles sourced from the separate OASIS Profiles document ([KMIP-Prof]) use
the prefix `prof-` in `source_section` (e.g., `source_section: "prof-5.1"`)
to distinguish them from sections of KMIP-SPEC. `check_verbatim.py` and
`build_kb_scaffold.py` both resolve this prefix against the profiles document
(`raw/kmip/kmip-profiles/v<ver>/kmip-profiles-v<ver>.md`) rather than the main
spec.

## source_section for KMIP-UG articles

Articles sourced from the separate OASIS Usage Guide document ([KMIP-UG]) use
the prefix `ug-` in `source_section` (e.g., `source_section: "ug-3.1"`)
to distinguish them from sections of KMIP-SPEC. `check_verbatim.py` and
`build_kb_scaffold.py` both resolve this prefix against the usage guide document
(`raw/kmip/kmip-ug/v<ver>/kmip-ug-v<ver>.md` for v2.x, `raw/kmip/ug/v<ver>/`
for v1.x) rather than the main spec. UG source for `--source ug` is generated
with the `UG_PREFIX_RULES` ruleset covering §2–§5 of the UG at depth 2; TOC
files land at `kb/versions/<ver>-ug-toc.yaml`.

## source_section for KMIP-ENCODE articles

Articles whose v1.x origin is the separate `[KMIP-ENCODE]` document (*KMIP
Additional Message Encodings v1.0*, `raw/kmip/kmip-addtl-msg-enc/v1.0/`) use
the prefix `enc-` in `v1_source_section` (e.g., `v1_source_section: "enc-2"`).
This applies to the HTTPS, JSON, and XML encoding profiles, which were defined
in KMIP-ENCODE for v1.0–v1.2 before being absorbed into KMIP-Prof in v2.0.
The `enc-` prefix is traceability only; no scaffold tooling currently resolves
it automatically.

## Authoring content

Fill a stub's existing section headers with original prose, populate front
matter (`spec_versions` per the versions a concept appears in, real `related`
slugs, `keywords`), then flip `status: stub` → `draft`. Match the depth and
cross-reference style of already-authored docs (e.g. `kb/operations/register.md`,
`kb/objects/symmetric-key.md`). Use relative links (e.g.
`[Key Block](../structures/key-block.md)`) and confirm targets exist (stub or
authored) before linking. Validate before committing:

```
python scripts/build_kb_scaffold.py --check    # front matter vs JSON Schema
python scripts/check_verbatim.py <dir>          # flags shared 8+-word runs vs source_section
python scripts/validate_links.py [dir ...]      # checks related slugs + relative body links resolve
python scripts/enrich_field_tables.py --check   # Field tables carry up-to-date Tag/XML Text columns
python scripts/enrich_enum_tables.py --check    # Enumeration value tables carry up-to-date Value/XML Text
python scripts/enrich_mask_tables.py --check    # Bit-mask tables carry up-to-date XML Text column
python scripts/populate_tag_type.py --check     # tag_hex docs carry tag_type (requires raw/ XML test cases)
```

Authored so far: **452 content docs total — 452 `reviewed`, 0 `draft`, 0
`stub`**. All docs are reviewed per the CONTRIBUTING checklist (validators
clean; identifier-only verbatim flags accepted as unavoidable: TLS
cipher-suite names and `LIBRARY-LTO*` namespaces in 3 profile docs, plus
EC key-compression enum value names in `kb/enumerations/
key-compression-type-enumeration.md`). Every `target_path` in
`kb/versions/2.1-toc.yaml` now exists on disk at `reviewed` status, and
re-running the generator is a no-op (created=0). Remaining work: net-new
content in `kb/examples/`, `kb/workflows/`, and `kb/mappings/`.

Deliberate consolidations/renames are encoded in `V21_SLUG_OVERRIDES` in
`build_kb_scaffold.py` (25 sections → existing authored docs: §1.3→
`normative-references`, §3.4–§3.12→`transparent-key-structures`, §4.60→
`custom-attribute`, §5.1→`attribute`, §8.1–§8.6→`message-structure`,
§9.9/§9.10→`client-/server-correlation-value`, §10.1.1–§10.1.5→
`ttlv-encoding`); the TOC points at the authored doc for those sections
and the generator never emits stubs for them. Two caveats:
`kb/operations/re-key.md` (v2.1 §6.1.46) and `kb/messages/protocol-version.md`
(v2.1 §9.16) cannot be auto-checked by `check_verbatim.py` because their
headings were lost in source conversion (§9.16 is the only numbered
heading missing from the converted v2.1 spec) — re-verify them manually
when editing.

## Authoring status

```
python scripts/status_report.py                 # per-category stub/draft/reviewed table
python scripts/status_report.py --next 10       # list next 10 stubs to author
python scripts/status_report.py --category kb/encoding --next 5   # filter to one category
python scripts/status_report.py --json          # machine-readable output
```

## Scaffold generator

`scripts/build_kb_scaffold.py` — parses a raw spec and (re)generates dirs, one empty stub per section, and a version TOC file. Pure stdlib. **Never overwrites a file whose `status` ≠ `stub`**, so it is safe to re-run. Supports v1.0–v1.4 (from `raw/kmip/spec/`) and v2.0–v2.1 (from `raw/kmip/kmip-spec/`). Also supports the KMIP Profiles document via `--source prof` and the KMIP Usage Guide via `--source ug`.

```
python scripts/build_kb_scaffold.py [--version 2.1] [--source spec|prof|ug] [--out .] [--toc-only] [--no-stubs] [--check]
```

- `--source spec` (default): parses KMIP-SPEC; writes `kb/versions/<ver>-toc.yaml`
- `--source prof`: parses KMIP-Prof (`raw/kmip/kmip-profiles/v<ver>/`); writes `kb/versions/<ver>-prof-toc.yaml`; prefixes `source_section` with `prof-`
- `--source ug`: parses KMIP-UG (`raw/kmip/kmip-ug/v<ver>/` or `raw/kmip/ug/v<ver>/`); writes `kb/versions/<ver>-ug-toc.yaml`; prefixes `source_section` with `ug-`

ToC maps for all seven spec releases and all KMIP-Prof versions are committed under `kb/versions/`:

| File | Sections |
|---|---|
| `kb/versions/2.1-toc.yaml` | 302 |
| `kb/versions/2.0-toc.yaml` | 281 |
| `kb/versions/1.4-toc.yaml` | 157 |
| `kb/versions/1.3-toc.yaml` | 143 |
| `kb/versions/1.2-toc.yaml` | 134 |
| `kb/versions/1.1-toc.yaml` | 112 |
| `kb/versions/1.0-toc.yaml` | 104 |
| `kb/versions/2.1-prof-toc.yaml` | 20 (KMIP-Prof §3 + §5) |
| `kb/versions/2.0-prof-toc.yaml` | 20 (KMIP-Prof §3 + §5) |
| `kb/versions/1.4-prof-toc.yaml` | 19 (KMIP-Prof §3 + §5) |
| `kb/versions/1.3-prof-toc.yaml` | 18 (KMIP-Prof §3 + §5) |
| `kb/versions/1.2-prof-toc.yaml` | 8 (KMIP-Prof §3 + §4) |
| `kb/versions/1.1-prof-toc.yaml` | 44 (KMIP-Prof §3 + §4) |
| `kb/versions/1.0-prof-toc.yaml` | 8 (KMIP-Prof §3 + §4) |
| `kb/versions/2.1-ug-toc.yaml` | 83 (KMIP-UG §2–§5) |
| `kb/versions/2.0-ug-toc.yaml` | 74 (KMIP-UG §2–§5) |
| `kb/versions/1.4-ug-toc.yaml` | 60 (KMIP-UG §2–§4) |
| `kb/versions/1.3-ug-toc.yaml` | 55 (KMIP-UG §2–§4) |
| `kb/versions/1.2-ug-toc.yaml` | 51 (KMIP-UG §2–§4) |
| `kb/versions/1.1-ug-toc.yaml` | 44 (KMIP-UG §2–§4) |
| `kb/versions/1.0-ug-toc.yaml` | 36 (KMIP-UG §2–§4) |

v1.0–v1.2 profiles put profile definitions in §4 (§5 is Conformance Clauses in those releases); v1.3+ and v2.x use §5. KMIP-UG §5 (Deprecations) first appears in v2.0.

`kb/versions/index.md` contains delta notes for every release (v1.1–v2.1). `spec_versions` front matter has been audited across all releases: 53 version-boundary docs for v1.1–v1.4 (0 errors); v2.0/v2.1 audited across all 162 KB docs (5 correctly excluded as removed in v2.0).

The section→category rules and per-section stub depth live in `V1X_PREFIX_RULES` / `V20_PREFIX_RULES` / `PROF_PREFIX_RULES` / `PROF_V1X_EARLY_RULES` / `UG_PREFIX_RULES` at the top of the script; `get_prof_prefix_rules(version)` selects the right ruleset for `--source prof`. `V21_SLUG_OVERRIDES` (applied for `--source spec --version 2.1` only) maps consolidated/renamed sections to their authored doc's slug so re-runs stay idempotent. Stub bodies come from `templates/<category>.md`.

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
