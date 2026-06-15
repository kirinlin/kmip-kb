---
title: Padding Method Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.37"
status: reviewed
related: ["cryptographic-algorithm-enumeration", "block-cipher-mode-enumeration"]
keywords: ["padding", "OAEP", "PKCS#1 v1.5", "PSS", "RSA padding", "block padding", "padding method", "42005F", "PaddingMethod"]
tag_hex: "42005F"
xml_text: "PaddingMethod"
---

# Padding Method Enumeration

## Overview

The Padding Method enumeration specifies the padding scheme applied during asymmetric encryption or during block-cipher operations that require padding to fill the final block. It appears in the [Cryptographic Parameters](../../attributes/cryptographic-parameters.md) structure whenever padding is a configurable aspect of the operation — primarily for RSA encryption and signing, and for block ciphers operating in modes that do not handle arbitrary-length plaintext natively.

## Fields & Structure

| Value | Hex | XML Text | Description |
|---|---|---|---|
| None | `0x00000001` | `None` |  |
| OAEP | `0x00000002` | `OAEP` |  |
| PKCS5 | `0x00000003` | `PKCS5` |  |
| SSL3 | `0x00000004` | `SSL3` |  |
| Zeros | `0x00000005` | `Zeros` |  |
| ANSI X9.23 | `0x00000006` | `ANSIX9_23` |  |
| ISO 10126 | `0x00000007` | `ISO10126` |  |
| PKCS1 v1.5 | `0x00000008` | `PKCS1V1_5` |  |
| X9.31 | `0x00000009` | `X9_31` |  |
| PSS | `0x0000000A` | `PSS` |  |

- **None**: No padding applied. Used for algorithms and modes that handle arbitrary data lengths or where the caller guarantees block-aligned input.
- **OAEP** (PKCS#1 OAEP): Optimal Asymmetric Encryption Padding. The recommended padding for RSA encryption in modern systems, using a mask generation function and a hash to randomise the ciphertext.
- **PKCS5**: PKCS #5 / PKCS #7 padding for block ciphers: the last block is padded with bytes whose value equals the number of padding bytes added, always padding even if the input is already block-aligned.
- **SSL3**: SSL 3.0-style block cipher padding, retained for legacy TLS record decryption.
- **Zeros**: Pad with zero bytes. Defined but not recommended for most uses.
- **ANSI X9.23**: Right-pad with zeros and set the last byte to the pad count. Used in some financial message standards.
- **ISO 10126**: Pad with random bytes and set the last byte to the pad count.
- **PKCS#1 v1.5**: The original RSA padding scheme from PKCS#1 v1.5. Deprecated for encryption due to the ROBOT/Bleichenbacher attacks, but still used for signatures in legacy systems.
- **X9.31**: ANSI X9.31 signature padding for RSA.
- **PSS** (Probabilistic Signature Scheme): The recommended RSA signature padding per PKCS#1 v2.1 and later, using a random salt for each signature.

## Examples

A [Cryptographic Parameters](../../attributes/cryptographic-parameters.md) structure for RSA-OAEP encryption sets Padding Method = **OAEP** and Hashing Algorithm = SHA-256. An AES-CBC operation that needs to handle variable-length plaintext sets Padding Method = **PKCS5**.

## Related

[Cryptographic Parameters](../../attributes/cryptographic-parameters.md) · [Cryptographic Algorithm Enumeration](cryptographic-algorithm-enumeration.md) · [Block Cipher Mode Enumeration](block-cipher-mode-enumeration.md) · [Mask Generator Enumeration](mask-generator-enumeration.md)
