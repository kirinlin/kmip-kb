---
title: Hash
category: operation
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.24"
v1_source_section: "4.37"
status: reviewed
related: ["mac", "sign", "cryptographic-parameters", "digest"]
keywords: ["hash", "digest", "message digest", "sha", "hashing"]
---

# Hash

## Purpose

`Hash` has the server compute a message digest over client-supplied data. Unlike
the other cryptographic operations it needs no key — only a hash algorithm. It
was added in KMIP 1.2.

## Request Fields

| Field | Required | Description |
|---|---|---|
| Cryptographic Parameters | Yes | The hashing algorithm to apply. |
| Data | Yes (single-part) | The data to hash, as a byte string. |
| Correlation Value | No | Ties this call to an in-progress multi-part operation. |
| Init Indicator | No | Marks the first call of a multi-part operation. |
| Final Indicator | No | Marks the last call of a multi-part operation. |

## Response Fields

| Field | Required | Description |
|---|---|---|
| Data | Yes (single-part) | The resulting digest, as a byte string. |
| Correlation Value | No | A handle to pass to subsequent calls of a multi-part operation. |

## Behavior & Server Requirements

Because hashing is unkeyed, the hashing algorithm must be supplied explicitly in
the [cryptographic parameters](../attributes/cryptographic-parameters.md) — there
is no key whose attributes could provide a default. Both one-shot and streamed
hashing are supported through a Correlation Value with Init and Final indicators.
The result status in the header reports success or failure.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: a missing or unsupported hashing algorithm, or malformed input.

## Related Operations

[MAC](mac.md) · [Sign](sign.md)
