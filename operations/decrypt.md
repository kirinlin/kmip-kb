---
title: Decrypt
category: operation
spec_version: "1.4"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.30"
status: draft
related: ["encrypt", "cryptographic-parameters", "cryptographic-usage-mask", "symmetric-key"]
keywords: ["decrypt", "decryption", "cipher", "AEAD", "plaintext recovery"]
---

# Decrypt

## Purpose

`Decrypt` has the server decrypt client-supplied ciphertext using a managed key,
keeping the key material server-side. It is the inverse of [Encrypt](encrypt.md)
and was added in KMIP 1.2.

## Request Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | No | The key to decrypt with; the ID Placeholder is used when omitted. |
| Cryptographic Parameters | No | The mode, padding, and related settings for this operation. |
| Data | Yes (single-part) | The ciphertext to decrypt, as raw bytes. |
| IV/Counter/Nonce | No | The IV, counter, or nonce the algorithm calls for. |
| Correlation Value | No | Ties this call to an in-progress multi-part operation. |
| Init Indicator | No | Marks the first call of a multi-part operation. |
| Final Indicator | No | Marks the last call of a multi-part operation. |
| Authenticated Encryption Additional Data | No | Extra data to authenticate (AEAD); for multi-part it goes on the first call. |
| Authenticated Encryption Tag | No | The tag to check against (AEAD); for multi-part it goes on the first call. |

## Response Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | Yes | The key that was used. |
| Data | Yes (single-part) | The recovered plaintext, as a byte string. |
| Correlation Value | No | A handle to pass to subsequent calls of a multi-part operation. |

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
