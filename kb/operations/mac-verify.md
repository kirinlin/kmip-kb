---
title: MAC Verify
category: operation
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.33"
v1_source_section: "4.34"
status: reviewed
related: ["mac", "signature-verify", "cryptographic-parameters", "symmetric-key"]
keywords: ["mac verify", "verify mac", "validity indicator", "integrity check"]
---

# MAC Verify

## Purpose

`MAC Verify` has the server check a message authentication code against a managed
key, reporting whether it is valid. It is the counterpart to [MAC](mac.md) and
was added in KMIP 1.2.

## Request Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | No | The MAC key; the ID Placeholder is used when omitted. |
| Cryptographic Parameters | No | The algorithm to use for the MAC. |
| Data | No | The original data that was authenticated. |
| MAC Data | Yes (single-part) | The MAC to check, as a byte string. |
| Correlation Value | No | Ties this call to an in-progress multi-part operation. |
| Init Indicator | No | Marks the first call of a multi-part operation. |
| Final Indicator | No | Marks the last call of a multi-part operation. |

## Response Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | Yes | The key that was used. |
| Validity Indicator | Yes | Whether the MAC checks out: valid, invalid, or indeterminate. |
| Correlation Value | No | A handle to pass to subsequent calls of a multi-part operation. |

## Behavior & Server Requirements

The server recomputes the MAC over the supplied data and compares it with the
one provided, returning the verdict in the Validity Indicator — an invalid MAC is
a successful operation reporting "invalid", not an error. The
[cryptographic parameters](../attributes/cryptographic-parameters.md) may be
omitted and taken from the key's attributes. Streamed verification works as it
does for [MAC](mac.md).

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). An invalid
MAC is reported through the Validity Indicator; genuine errors include missing
parameters not derivable from the key, an unknown key, or a key whose usage mask
does not permit MAC verification.

## Related Operations

[MAC](mac.md) · [Signature Verify](signature-verify.md)
