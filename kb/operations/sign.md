---
title: Sign
category: operation
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.55"
v1_source_section: "4.31"
status: reviewed
related: ["signature-verify", "get-usage-allocation", "cryptographic-parameters", "digital-signature-algorithm", "private-key"]
keywords: ["sign", "signature", "digital signature", "private key", "signing"]
xml_text: "Sign"
---

# Sign

## Purpose

`Sign` has the server produce a digital signature over client-supplied data
using a managed private key. Added in KMIP 1.2, it lets the private key stay
under server control while signing happens server-side.

## Request Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | No | The signing key; the ID Placeholder is used when omitted. |
| Cryptographic Parameters | `42002B` | `CryptographicParameters` | No | The signature algorithm (or the algorithm plus hash) to use. |
| Data | `4200C2` | `Data` | Yes (single-part, unless digested data is given) | The data to sign, as a byte string. |
| Digested Data | `420107` | `DigestedData` | No | A pre-computed digest to sign instead of raw data. |
| Correlation Value | `4200D6` | `CorrelationValue` | No | Ties this call to an in-progress multi-part operation. |
| Init Indicator | `4200D7` | `InitIndicator` | No | Marks the first call of a multi-part operation. |
| Final Indicator | `4200D8` | `FinalIndicator` | No | Marks the last call of a multi-part operation. |

## Response Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes | The key that was used. |
| Signature Data | `4200C3` | `SignatureData` | Yes (single-part) | The resulting signature, as a byte string. |
| Correlation Value | `4200D6` | `CorrelationValue` | No | A handle to pass to subsequent calls of a multi-part operation. |

## Behavior & Server Requirements

The client can pass either the raw data or an already-computed digest. The
[cryptographic parameters](../attributes/cryptographic-parameters.md) may be
omitted and taken from the key's attributes when present. If the key has a
[usage-limits](../attributes/usage-limits.md) attribute, the server reserves an
allocation before signing and fails with Permission Denied if it cannot. One-shot
and streamed signing are both supported via the Correlation Value with Init and
Final indicators. The header's result status reports the outcome.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: required parameters missing and not derivable from the key, a usage
allocation that cannot be obtained, an unknown key, or a key whose usage mask
does not permit signing.

## Related Operations

[Signature Verify](signature-verify.md) · [Get Usage Allocation](get-usage-allocation.md)
