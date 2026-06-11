---
title: JSON Profiles
category: profile
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "prof-5.5"
status: draft
related: ["base-profiles", "xml-profiles", "https-profiles"]
keywords: ["JSON", "message encoding", "CamelCase", "TTLV", "alternative encoding"]
---

# JSON Profiles

## Overview

The JSON Profiles substitute a JSON message encoding for TTLV binary while keeping all KMIP message semantics unchanged. JSON-encoded KMIP is logically equivalent to TTLV; size and length fields are interpreted as TTLV byte counts regardless of the JSON representation.

## JSON Encoding

Each TTLV item maps to a JSON object with `tag`, optional `name`, `type`, and `value` properties. Tags use the same CamelCase normalization as XML profiles. Structures encode `value` as a JSON array of child objects; the `type` property defaults to `Structure` and may be omitted. Scalar types use `type` to disambiguate (e.g., `"type":"DateTime"`, `"type":"Enumeration"`).

Integer mask values may be expressed as a `|`-separated string of component names or hex values (e.g., `"Encrypt|Decrypt|CertificateSign"`). Long integers and big integers that exceed JavaScript's 53-bit precision limit must be represented as hex strings.

DateTime values must be ISO 8601 with an explicit time zone; fractional seconds should be ignored on receipt.

## JSON Client and Server

Both client and server start from the corresponding [Base Profiles](base-profiles.md) and add conformance to JSON Encoding. No additional operations are mandatory.

## Mandatory Test Cases

`MSGENC-JSON-M-1-21` runs the same batch-size error + retry query scenario used by the XML and HTTPS encoding test cases, verifying that the JSON encoding correctly represents both the error response and the full Query response.

## Implications for Implementers

- JSON encoding is human-readable and tooling-friendly, making it useful for debugging and REST-style API gateways that inspect payloads.
- The `|` separator for mask values is not standard JSON and must be handled as a special case in your parser; do not rely on generic JSON libraries to handle it automatically.
- Because JavaScript numbers lack 64-bit integer precision, always use hex strings for Long Integer and Big Integer values when building clients that run in JavaScript environments.
- `Maximum Response Size` is still based on hypothetical TTLV encoding, not JSON byte count.

## Related Concepts

[Base Profiles](base-profiles.md) ·
[XML Profiles](xml-profiles.md) ·
[HTTPS Profiles](https-profiles.md)
