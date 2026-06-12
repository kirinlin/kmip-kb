---
title: Cryptographic Usage Mask
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "12.1"
status: reviewed
related: ["cryptographic-usage-mask", "key-block", "create", "create-key-pair", "register", "locate"]
keywords: ["cryptographic usage mask", "bit mask", "key usage", "encrypt", "decrypt", "sign", "verify", "wrap key", "unwrap key", "export"]
---

# Cryptographic Usage Mask

## Overview

The Cryptographic Usage Mask is a 32-bit integer bit field that controls which cryptographic purposes a key is permitted to serve. Rather than listing permitted operations as a set of enumeration values, KMIP compresses the allowed-uses policy into individual flag bits — one per distinct usage — making it efficient to store and fast to evaluate at operation time.

This document covers the §12.1 bit mask definition, which is distinct from the [Cryptographic Usage Mask attribute](../attributes/cryptographic-usage-mask.md) article that describes how the mask is stored on managed objects. The bit positions are fixed across all KMIP versions, though new positions have been added as the protocol evolved.

## Encoding (Tag / Type / Length / Value)

The Cryptographic Usage Mask value encodes as a 32-bit Integer (tag `42002C`). It is not a Structure — it is a scalar field whose bits are interpreted individually.

| Tag | Type | Width |
|---|---|---|
| `42002C` | Integer | 32 bits |

When embedded in an Attribute structure it appears as the Attribute Value of the `"Cryptographic Usage Mask"` attribute.

## Fields & Structure

The 32 bits are allocated to distinct usage categories. The following summarizes the defined bit positions and their meanings:

| Bit | Usage |
|---|---|
| 0 (0x00000001) | Sign |
| 1 (0x00000002) | Verify |
| 2 (0x00000004) | Encrypt |
| 3 (0x00000008) | Decrypt |
| 4 (0x00000010) | Wrap Key |
| 5 (0x00000020) | Unwrap Key |
| 6 (0x00000040) | Export |
| 7 (0x00000080) | MAC Generate |
| 8 (0x00000100) | MAC Verify |
| 9 (0x00000200) | Derive Key |
| 10 (0x00000400) | Content Commitment (Non-Repudiation) |
| 11 (0x00000800) | Key Agreement |
| 12 (0x00001000) | Certificate Sign |
| 13 (0x00002000) | CRL Sign |
| 14 (0x00004000) | Generate Cryptogram |
| 15 (0x00008000) | Validate Cryptogram |
| 16 (0x00010000) | Translate Encrypt |
| 17 (0x00020000) | Translate Decrypt |
| 18 (0x00040000) | Translate Wrap |
| 19 (0x00080000) | Translate Unwrap |
| 20 (0x00100000) | Authenticate |
| 31 (0x80000000) | Unrestricted |

Bits 21–30 are reserved. The Unrestricted bit (31) indicates that all defined usage operations are permitted; it overrides all other bits when set.

Servers that store a key with a particular Cryptographic Usage Mask are expected to enforce it — refusing to perform operations the key is not permitted to support. For example, a key stored with only the Encrypt bit set cannot legally be used in a Decrypt operation.

## Examples

An AES key intended solely for encrypting data would carry a Cryptographic Usage Mask of `0x00000004` (Encrypt only). A signing key for an RSA certificate authority would set bits for Certificate Sign and CRL Sign: `0x00003000`. A symmetric key authorized to both encrypt and decrypt plaintext gets `0x0000000C` (Encrypt | Decrypt).

## Related

[Cryptographic Usage Mask (attribute)](../attributes/cryptographic-usage-mask.md) · [Key Block](key-block.md) · [Create](../operations/create.md) · [Create Key Pair](../operations/create-key-pair.md) · [Register](../operations/register.md)
