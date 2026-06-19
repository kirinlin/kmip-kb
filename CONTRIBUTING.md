# Contributing

This repository is an **independently written** KMIP knowledge base. It is
*based on* the OASIS KMIP specification but must never **republish** it.

## The one hard rule: no verbatim spec text

Do **not** copy specification prose, tables, or definitions into any tracked
file. Read the source in `raw/` (gitignored, local-only), understand it, then
explain it **in your own words** for software engineers. `source_section` in a
document's front matter is for traceability only — it does not license quoting
that section.

A quick self-check before committing: if a sentence would read identically in
the official spec, rewrite it.

## Allowed vs. avoid

| Allowed | Avoid |
|---|---|
| Summaries & explanations | Publishing KMIP PDFs |
| Developer guides & FAQs | Large verbatim excerpts |
| Original examples, diagrams, schemas | Markdown conversions of the spec |
| Metadata & cross-references | Content that substantially reproduces spec text |

## Authoring workflow

1. **Find the stub.** Use `python scripts/status_report.py --next 10` to see
   the next stubs to author, or `versions/<ver>-toc.yaml` for the full section
   map. Stubs have `status: stub` and section headers only.
2. **Read the source.** Open the corresponding section in `raw/` for
   understanding — never to copy.
3. **Write original prose** under the existing headers. Explain purpose,
   fields, behavior, and relationships for an implementer audience.
4. **Format field tables.** A table that documents the fields of a KMIP
   structure or operation payload starts with a `Field` column, then `Tag` and
   `XML Text` columns, then the table's own columns:
   ```
   | Field | Tag | XML Text | Required | Description |
   ```
   Author the prose columns; leave `Tag`/`XML Text` blank and let
   `scripts/enrich_field_tables.py` fill them (6-digit hex and CamelCase element
   name, both in backticks) for fields that are named KMIP tags. Non-tag fields
   keep both cells blank.
5. **Fill front matter.** Set `spec_versions` to the versions where the concept
   appears, add `related` cross-references and `keywords`, and set
   `status: draft`.
6. **Validate.** Run the checks:
   ```
   python scripts/build_kb_scaffold.py --check   # front-matter schema
   python scripts/check_verbatim.py <dir>         # no copied spec prose
   python scripts/validate_links.py <dir>         # related slugs + body links resolve
   python scripts/enrich_field_tables.py --check  # Tag/XML Text columns current
   ```
7. **Review** against the checklist below, then set `status: reviewed`.

The generator never overwrites a file whose `status` is no longer `stub`, so
re-running it to pick up new sections is safe.

## Review checklist

- [ ] No substantial verbatim specification text remains (`check_verbatim.py` clean).
- [ ] Technical meaning is preserved and correct.
- [ ] No hallucinated fields, operations, or behaviors.
- [ ] Cross-references (`related`) resolve to real documents.
- [ ] Field tables carry `Tag`/`XML Text` columns (`enrich_field_tables.py --check` clean).
- [ ] Front matter validates (`--check` passes); `spec_versions` accurate.
- [ ] Examples are original, not lifted from the spec.

## Front-matter contract

Every document's front matter must validate against
[`schemas/frontmatter.schema.json`](schemas/frontmatter.schema.json). See the
README for the field reference and the `stub → draft → reviewed` lifecycle.

## What not to commit

`raw/` (the local spec mirror) is gitignored and must stay out of version
control. Commit only original knowledge content, examples, metadata, schemas,
and the tooling that produces the scaffold.
