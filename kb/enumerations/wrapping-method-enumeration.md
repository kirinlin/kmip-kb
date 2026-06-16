---
title: Wrapping Method Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.64"
status: reviewed
related: ["key-wrapping-data", "key-block", "get", "cryptographic-parameters", "encoding-option-enumeration", "unwrap-mode-enumeration"]
keywords: ["wrapping method", "key wrap", "encrypt", "MAC", "TR-31", "key protection", "key transport", "42009E", "WrappingMethod"]
tag_hex: "42009E"
xml_text: "WrappingMethod"
---

# Wrapping Method Enumeration

## Overview

The Wrapping Method enumeration specifies the cryptographic technique used to protect key material during transport or storage in wrapped form. It appears in the Key Wrapping Data structure inside a Key Block, describing how the Key Value was protected before delivery to the client. The method determines what cryptographic operations the recipient must perform to recover the plaintext key material.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Unspecified | `00000001` | `Unspecified` |  |
| Hardware | `00000002` | `Hardware` |  |
| Software | `00000003` | `Software` |  |
| Firmware | `00000004` | `Firmware` |  |
| Hybrid | `00000005` | `Hybrid` |  |

- **Encrypt**: The key material is wrapped using a key-encryption key (KEK) via symmetric encryption. The most common method — typically AES Key Wrap (RFC 3394), AES-GCM, or RSA-OAEP. The recipient decrypts with the corresponding KEK or private key to recover the plaintext.
- **MAC/Hash**: The key material is integrity-protected using a MAC or cryptographic hash but is not encrypted. The plaintext key is present; only its integrity is verified. Rarely used for key transport; used in specific financial protocols where the recipient already holds the key.
- **Encrypt Then MAC/Hash**: The key material is first encrypted, then a MAC is computed over the ciphertext. The recipient verifies the MAC before decrypting. A common Encrypt-then-MAC construction for strong authenticated key transport.
- **MAC/Hash Then Encrypt**: A MAC over the plaintext is computed first, then the entire structure (plaintext + MAC) is encrypted. Less common than Encrypt-then-MAC; vulnerable to certain attacks if the encryption is malleable.
- **TR-31** (ANSI X9.143 / ISO 20038): The key is wrapped in a ANSI TR-31 key block format — a standardised format for key exchange in payment card industry environments. The TR-31 block bundles key material, key usage flags, and an integrity check in a single interoperable container.

## Examples

A KMIP server delivering an AES-256 key wrapped for a specific client RSA key uses Wrapping Method = **Encrypt** (RSA-OAEP wrapping). A payment HSM exchanging a PIN encryption key with a partner device uses **TR-31** for PCI-DSS compliance.

## Related

[Key Wrapping Data](../structures/key-wrapping-data.md) · [Key Block](../structures/key-block.md) · [Unwrap Mode Enumeration](unwrap-mode-enumeration.md) · [Encoding Option Enumeration](encoding-option-enumeration.md) · [Get](../operations/get.md)
