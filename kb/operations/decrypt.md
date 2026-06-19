---
title: Decrypt
category: operation
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.11"
v1_source_section: "4.30"
status: reviewed
related: ["encrypt", "cryptographic-parameters", "cryptographic-usage-mask", "symmetric-key"]
keywords: ["decrypt", "decryption", "cipher", "AEAD", "plaintext recovery"]
---

# Decrypt

## Purpose

`Decrypt` has the server decrypt client-supplied ciphertext using a managed key,
keeping the key material server-side. It is the inverse of [Encrypt](encrypt.md)
and was added in KMIP 1.2.

## Request Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | No | The key to decrypt with; the ID Placeholder is used when omitted. |
| Cryptographic Parameters | `42002B` | `CryptographicParameters` | No | The mode, padding, and related settings for this operation. |
| Data | `4200C2` | `Data` | Yes (single-part) | The ciphertext to decrypt, as raw bytes. |
| IV/Counter/Nonce | `42003D` | `IVCounterNonce` | No | The IV, counter, or nonce the algorithm calls for. |
| Correlation Value | `4200D6` | `CorrelationValue` | No | Ties this call to an in-progress multi-part operation. |
| Init Indicator | `4200D7` | `InitIndicator` | No | Marks the first call of a multi-part operation. |
| Final Indicator | `4200D8` | `FinalIndicator` | No | Marks the last call of a multi-part operation. |
| Authenticated Encryption Additional Data | `4200FE` | `AuthenticatedEncryptionAdditionalData` | No | Extra data to authenticate (AEAD); for multi-part it goes on the first call. |
| Authenticated Encryption Tag | `4200FF` | `AuthenticatedEncryptionTag` | No | The tag to check against (AEAD); for multi-part it goes on the first call. |

## Response Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes | The key that was used. |
| Data | `4200C2` | `Data` | Yes (single-part) | The recovered plaintext, as a byte string. |
| Correlation Value | `4200D6` | `CorrelationValue` | No | A handle to pass to subsequent calls of a multi-part operation. |

## Behavior & Server Requirements

As with [Encrypt](encrypt.md), the
[cryptographic parameters](../attributes/cryptographic-parameters.md) may be
omitted and taken from the key's attributes, and the algorithm's IV is supplied
only when needed. For authenticated ciphers the additional data and the
expected tag accompany the request so the server can verify integrity while
decrypting. One-shot and streamed operation work the same way as for Encrypt,
using a Correlation Value with Init and Final indicators. The result status in
the header reports success or failure.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: required parameters missing and not derivable from the key, a failed
authentication-tag check, an unknown key, or a key whose usage mask does not
permit decryption.

## Related Operations

[Encrypt](encrypt.md) · [Signature Verify](signature-verify.md)
