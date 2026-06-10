---
title: Key Block
category: ttlv
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4"]
source_section: "2.1.3"
status: draft
related: ["key-value", "key-wrapping-data", "transparent-key-structures", "cryptographic-algorithm"]
keywords: ["key block", "key format type", "key compression", "wrapped key", "key container"]
---

# Key Block

## Overview

The universal key container: every key-bearing managed object —
[Symmetric Key](../objects/symmetric-key.md),
[Public](../objects/public-key.md) / [Private Key](../objects/private-key.md),
[Split Key](../objects/split-key.md),
[Secret Data](../objects/secret-data.md),
[PGP Key](../objects/pgp-key.md) — holds its material inside one Key Block.
It bundles the format declaration, the material itself (the
[Key Value](key-value.md)), the algorithm/length description, and — when the
material is wrapped — the [Key Wrapping Data](key-wrapping-data.md).

## Encoding (Tag / Type / Length / Value)

Structure, tag `420040`:

| Field | Tag | Type | Required |
|---|---|---|---|
| Key Format Type | `420042` | Enumeration | Yes |
| Key Compression Type | `420041` | Enumeration | No — EC public key point compression; uncompressed if absent |
| Key Value | `420045` | Structure (plaintext) or Byte String (wrapped) | No — may be absent for metadata-only registrations (1.2+) |
| Cryptographic Algorithm | `420028` | Enumeration | Yes unless derivable from the Key Value; n/a for Secret Data and Opaque Objects; paired with Length |
| Cryptographic Length | `42002A` | Integer | Same rule as Algorithm |
| Key Wrapping Data | `420046` | Structure | Only — and always — when the material is wrapped |

## Fields & Structure

Key Format Types fall into four families:

- **Byte-oriented**: Raw (bare key bytes), Opaque (encoding unknown to the
  server).
- **DER-encoded standards**: PKCS#1, PKCS#8 (plain or encrypted), X.509,
  ECPrivateKey, and PKCS#12 (1.4).
- **Transparent**: per-algorithm component structures — see
  [Transparent Key Structures](transparent-key-structures.md).
- **Extensions**: vendor formats.

Typical lengths the algorithm/length pair expresses: AES 128/192/256, 3DES
112–192, RSA 1024–3072. A [Get](../operations/get.md) may request a specific
format; servers unable to convert return the
`Key Format Type Not Supported` result reason.

## Examples

A plaintext AES-256 key: Key Block { Key Format Type = Raw, Key Value =
structure with 32 key bytes, Cryptographic Algorithm = AES, Cryptographic
Length = 256 }. The same key delivered wrapped adds Key Wrapping Data and
turns the Key Value into a byte string.

## Related

[Key Value](key-value.md) · [Key Wrapping Data](key-wrapping-data.md) ·
[Transparent Key Structures](transparent-key-structures.md) ·
[objects/ index](../objects/index.md)
