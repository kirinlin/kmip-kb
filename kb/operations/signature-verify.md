---
title: Signature Verify
category: operation
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.56"
v1_source_section: "4.32"
status: draft
related: ["sign", "cryptographic-parameters", "digital-signature-algorithm", "public-key"]
keywords: ["signature verify", "verify signature", "validity indicator", "public key"]
---

# Signature Verify

## Purpose

`Signature Verify` has the server check a digital signature against a managed
key, reporting whether it is valid. It is the counterpart to [Sign](sign.md) and
was added in KMIP 1.2.

## Request Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | No | The verification key; the ID Placeholder is used when omitted. |
| Cryptographic Parameters | No | The signature algorithm (or the algorithm plus hash) to use. |
| Data | No | The original signed data, for algorithms that need it to verify. |
| Digested Data | No | A pre-computed digest of the signed data. |
| Signature Data | Yes (single-part) | The signature to check, as a byte string. |
| Correlation Value | No | Ties this call to an in-progress multi-part operation. |
| Init Indicator | No | Marks the first call of a multi-part operation. |
| Final Indicator | No | Marks the last call of a multi-part operation. |

## Response Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | Yes | The key that was used. |
| Validity Indicator | Yes | Whether the signature checks out: valid, invalid, or indeterminate. |
| Data | No | Data recovered from the signature, for algorithms that support recovery. |
| Correlation Value | No | A handle to pass to subsequent calls of a multi-part operation. |

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
