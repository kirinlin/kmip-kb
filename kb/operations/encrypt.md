---
title: Encrypt
category: operation
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.17"
v1_source_section: "4.29"
status: draft
related: ["decrypt", "get-usage-allocation", "cryptographic-parameters", "cryptographic-usage-mask", "symmetric-key"]
keywords: ["encrypt", "encryption", "cipher", "IV", "AEAD", "block cipher mode"]
---

# Encrypt

## Purpose

`Encrypt` has the server encrypt client-supplied data using a managed key,
without the key material ever leaving the server. It was introduced in KMIP 1.2
as part of the server-side cryptographic operations.

## Request Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | No | The key to encrypt with; the ID Placeholder is used when omitted. |
| Cryptographic Parameters | No | The mode, padding, and related settings for this operation. |
| Data | Yes (single-part) | The plaintext bytes. Omitted in the continuation calls of a multi-part operation. |
| IV/Counter/Nonce | No | The IV, counter, or nonce the mode calls for. |
| Correlation Value | No | Ties this call to an in-progress multi-part operation started by an earlier call. |
| Init Indicator | No | Marks the first call of a multi-part operation. |
| Final Indicator | No | Marks the last call of a multi-part operation. |
| Authenticated Encryption Additional Data | No | Extra data covered by the authentication tag (AEAD); for multi-part it goes on the first call. |

## Response Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | Yes | The key that was used. |
| Data | Yes (single-part) | The resulting ciphertext, as raw bytes. |
| IV/Counter/Nonce | No | When a random IV was requested and none supplied, the generator output the server used. |
| Correlation Value | No | A handle to pass to subsequent calls of a multi-part operation. |
| Authenticated Encryption Tag | No | The AEAD tag, returned once the final block of plaintext has been processed. |

## Behavior & Server Requirements

[Cryptographic parameters](../attributes/cryptographic-parameters.md) may be left
out of the request, in which case the server takes them from the key's own
attributes (the lowest-indexed instance); if the algorithm needs parameters and
none are available, the operation fails. The server does not store or track the
IV/counter/nonce. When the key carries a [usage-limits](../attributes/usage-limits.md)
attribute, the server first reserves an allocation against it, and the operation
fails with Permission Denied if that allocation cannot be obtained. Both
one-shot and streamed (multi-part) encryption are supported: a multi-part
operation threads a Correlation Value through its calls and marks the first and
last with the Init and Final indicators. Success or failure is reported through
the result status in the response header.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: required parameters missing and not derivable from the key, a usage
allocation that cannot be obtained, an unknown key, or a key whose usage mask
does not permit encryption.

## Related Operations

[Decrypt](decrypt.md) · [Get Usage Allocation](get-usage-allocation.md) ·
[MAC](mac.md)
