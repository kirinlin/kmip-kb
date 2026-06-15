---
title: XML Profiles
category: profile
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "prof-5.4"
v1_source_section: "enc-6"
status: reviewed
related: ["base-profiles", "json-profiles", "https-profiles"]
keywords: ["XML", "message encoding", "CamelCase", "TTLV", "alternative encoding"]
---

# XML Profiles

## Overview

The XML Profiles replace TTLV binary encoding with an XML message encoding while keeping message semantics identical. An XML-encoded KMIP message is logically equivalent to the same message in TTLV form; all size and length values are interpreted as if the message were TTLV-encoded even though the wire bytes are XML.

## XML Encoding

Each TTLV item maps to an XML element. Tags become element names in CamelCase (e.g., `ActivationDate`, `BatchCount`). Unknown tags or extension tags may use either the hex form `0x54FFFF` or a published name. Structures encode as nested XML elements; scalar values use a `value` attribute. The `type` attribute defaults to `Structure` and may be omitted for structural elements.

The namespace for all KMIP XML elements is `urn:oasis:tc:kmip:xmlns`, but its use is optional unless namespace disambiguation is required.

Enumeration values may appear as either the hex integer string or the CamelCase text. Integer mask fields (e.g., `CryptographicUsageMask`) accept a space-separated list of component names or hex values in addition to the combined hex representation.

DateTime values must be ISO 8601 with an explicit time-zone specifier; fractional seconds should be ignored.

## XML Client and Server

Both client and server start from the corresponding [Base Profiles](base-profiles.md) and add conformance to the XML Encoding clause. No additional operations are mandatory beyond the Baseline; the encoding substitution is the entire addition.

## Mandatory Test Cases

`MSGENC-XML-M-1-21` runs a Query with a small `Maximum Response Size`, validates the error response, then re-runs with a larger limit and validates the full response — identical to the HTTPS and JSON encoding tests, exercising the same batch-size error path in XML format.

## Implications for Implementers

- The `Maximum Response Size` field in XML requests still governs the length of a hypothetical TTLV-encoded response. Size your limit based on TTLV byte counts, not XML byte counts.
- CamelCase normalization follows a deterministic algorithm (split on whitespace/dashes, capitalize each word, concatenate). Implement the algorithm rather than maintaining a lookup table to handle future tags correctly.
- Validating against the KMIP XML Schema (published as an appendix to the profiles document) catches encoding errors early; use it in your test suite.

## Version History

For v1.0–v1.2 the XML encoding rules were published in the separate
`[KMIP-ENCODE]` document (*KMIP Additional Message Encodings v1.0*, §6), not
in KMIP-PROF. XML Client and Server profile IDs for v1.3 appeared in the
core spec enumerations, and by v2.0 the full encoding specification was
absorbed into KMIP-Prof §5.4 (where it remains in v2.1). The `enc-6`
traceability in `v1_source_section` points to §6 of that earlier document.

## Related Concepts

[Base Profiles](base-profiles.md) ·
[JSON Profiles](json-profiles.md) ·
[HTTPS Profiles](https-profiles.md)
