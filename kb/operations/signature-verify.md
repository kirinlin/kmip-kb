---
title: Signature Verify
category: operation
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.56"
v1_source_section: "4.32"
status: reviewed
related: ["sign", "cryptographic-parameters", "digital-signature-algorithm", "public-key"]
keywords: ["signature verify", "verify signature", "validity indicator", "public key"]
---

# Signature Verify

## Purpose

`Signature Verify` has the server check a digital signature against a managed
key, reporting whether it is valid. It is the counterpart to [Sign](sign.md) and
was added in KMIP 1.2.

## Request Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | No | The verification key; the ID Placeholder is used when omitted. |
| Cryptographic Parameters | `42002B` | `CryptographicParameters` | No | The signature algorithm (or the algorithm plus hash) to use. |
| Data | `4200C2` | `Data` | No | The original signed data, for algorithms that need it to verify. |
| Digested Data | `420107` | `DigestedData` | No | A pre-computed digest of the signed data. |
| Signature Data | `4200C3` | `SignatureData` | Yes (single-part) | The signature to check, as a byte string. |
| Correlation Value | `4200D6` | `CorrelationValue` | No | Ties this call to an in-progress multi-part operation. |
| Init Indicator | `4200D7` | `InitIndicator` | No | Marks the first call of a multi-part operation. |
| Final Indicator | `4200D8` | `FinalIndicator` | No | Marks the last call of a multi-part operation. |

## Response Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes | The key that was used. |
| Validity Indicator | `42009B` | `ValidityIndicator` | Yes | Whether the signature checks out: valid, invalid, or indeterminate. |
| Data | `4200C2` | `Data` | No | Data recovered from the signature, for algorithms that support recovery. |
| Correlation Value | `4200D6` | `CorrelationValue` | No | A handle to pass to subsequent calls of a multi-part operation. |

## Behavior & Server Requirements

The verdict is returned in the Validity Indicator rather than as a pass/fail
status — a well-formed request that produces an invalid signature is a
successful operation reporting "invalid". Some signature schemes recover the
original data from the signature, which is then returned in the Data field. The
[cryptographic parameters](../attributes/cryptographic-parameters.md) may be
omitted and taken from the key's attributes. Streamed verification works the
same way as for [Sign](sign.md).

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Note that
an invalid signature is reported through the Validity Indicator, not as an error;
genuine errors include missing parameters not derivable from the key, an unknown
key, or a key whose usage mask does not permit verification.

## Related Operations

[Sign](sign.md) · [MAC Verify](mac-verify.md)
