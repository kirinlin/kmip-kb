---
title: Unwrap Mode Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["2.0","2.1"]
source_section: "11.59"
status: reviewed
related: ["key-wrapping-data", "key-block", "get", "cryptographic-parameters"]
keywords: ["unwrap mode", "key unwrap", "MAC verify", "decrypt", "key extraction", "wrap mode", "4200F2", "UnwrapMode"]
tag_hex: "4200F2"
xml_text: "UnwrapMode"
---

# Unwrap Mode Enumeration

## Overview

The Unwrap Mode enumeration controls the sequence of operations applied when extracting wrapped key material from a Key Block. Wrapping combines encryption and/or integrity protection; the Unwrap Mode specifies whether the server should first verify integrity before decrypting, or decrypt first and then verify, when both operations are present. Selecting the wrong order can expose implementations to padding oracle or timing attacks.

## Fields & Structure

| Value | Hex | XML Text | Description |
|---|---|---|---|
| Unspecified | `0x00000001` | `Unspecified` |  |
| Processed | `0x00000002` | `Processed` |  |
| Not Processed | `0x00000003` | `NotProcessed` |  |

- **Unwrap**: Default behaviour — the server unwraps the key material using only decryption, without any MAC verification step. Used when the Key Wrapping Data contains only an encryption-based wrap (e.g., AES Key Wrap per RFC 3394).
- **MAC/Verify Then Unwrap**: The server first verifies the MAC or cryptographic integrity of the wrapped data, and only if verification succeeds does it decrypt and extract the key material. Prevents the server from performing decryption on data that may have been tampered with.
- **Decrypt Then MAC/Verify**: The server first decrypts and then verifies the MAC on the resulting plaintext. Less common; appropriate for specific construction orders used in legacy protocols.

## Examples

A key wrapped using AES-GCM (which provides authenticated encryption) specifies **Unwrap** since the AEAD tag covers both authentication and confidentiality in a single step. A key wrapped with RSA-OAEP followed by an HMAC-SHA-256 integrity tag uses **MAC/Verify Then Unwrap** to ensure the outer integrity is checked before attempting decryption.

## Related

[Key Wrapping Data](../../structures/key-wrapping-data.md) · [Key Block](../../structures/key-block.md) · [Get](../../operations/get.md)
