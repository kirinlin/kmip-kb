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

1. **Find the stub.** Use `versions/<ver>-toc.yaml` to locate the generated
   file for a spec section. Stubs have `status: stub` and section headers only.
2. **Read the source.** Open the corresponding section in `raw/` for
   understanding — never to copy.
3. **Write original prose** under the existing headers. Explain purpose,
   fields, behavior, and relationships for an implementer audience.
4. **Fill front matter.** Set `spec_versions` to the versions where the concept
   appears, add `related` cross-references and `keywords`, and set
   `status: draft`.
5. **Validate.** Run `python scripts/build_kb_scaffold.py --check` (front matter)
   and `python scripts/check_verbatim.py <dir>` (no copied prose).
6. **Review** against the checklist below, then set `status: reviewed`.

The generator never overwrites a file whose `status` is no longer `stub`, so
re-running it to pick up new sections is safe.

## Review checklist

- [ ] No substantial verbatim specification text remains (`check_verbatim.py` clean).
- [ ] Technical meaning is preserved and correct.
- [ ] No hallucinated fields, operations, or behaviors.
- [ ] Cross-references (`related`) resolve to real documents.
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
