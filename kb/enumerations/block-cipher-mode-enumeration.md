---
title: Block Cipher Mode Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.6"
status: reviewed
related: ["cryptographic-parameters", "cryptographic-algorithm-enumeration", "padding-method-enumeration"]
keywords: ["cipher mode", "CBC", "GCM", "CCM", "CTR", "ECB", "AEAD", "block cipher", "encryption mode", "420011", "BlockCipherMode"]
tag_hex: "420011"
xml_text: "BlockCipherMode"
tag_type: "Enumeration"
---

# Block Cipher Mode Enumeration

## Overview

The Block Cipher Mode enumeration specifies the mode of operation for a symmetric block cipher, which determines how the cipher processes data longer than a single block and whether it provides authentication as well as confidentiality. The choice of mode has significant security implications: some modes (like ECB) are generally discouraged for general use because identical plaintext blocks produce identical ciphertext, while authenticated encryption modes (like GCM and CCM) provide both confidentiality and integrity in a single pass. This enumeration appears in the [Cryptographic Parameters](../attributes/cryptographic-parameters.md) structure used across encryption, decryption, wrapping, and MAC operations.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| CBC | `00000001` | `CBC` |  |
| ECB | `00000002` | `ECB` |  |
| PCBC | `00000003` | `PCBC` |  |
| CFB | `00000004` | `CFB` |  |
| OFB | `00000005` | `OFB` |  |
| CTR | `00000006` | `CTR` |  |
| CMAC | `00000007` | `CMAC` |  |
| CCM | `00000008` | `CCM` |  |
| GCM | `00000009` | `GCM` |  |
| CBC-MAC | `0000000A` | `CBC_MAC` |  |
| XTS | `0000000B` | `XTS` |  |
| AESKeyWrapPadding | `0000000C` | `AESKeyWrapPadding` |  |
| NISTKeyWrap | `0000000D` | `NISTKeyWrap` |  |
| X9.102 AESKW | `0000000E` | `X9_102AESKW` |  |
| X9.102 TDKW | `0000000F` | `X9_102TDKW` |  |
| X9.102 AKW1 | `00000010` | `X9_102AKW1` |  |
| X9.102 AKW2 | `00000011` | `X9_102AKW2` |  |
| AEAD | `00000012` | `AEAD` |  |

Common confidentiality-only modes:
- **ECB** (Electronic Code Book): Processes each block independently with no chaining. Suitable for encrypting a single block or small random values; not recommended for multi-block messages due to pattern leakage.
- **CBC** (Cipher Block Chaining): Each block is XORed with the previous ciphertext block before encryption. Requires an initialization vector (IV) and is widely used for file and storage encryption.
- **PCBC** (Propagating CBC): A variant of CBC where both plaintext and ciphertext are XORed, causing errors to propagate further.
- **CFB** (Cipher Feedback): Converts a block cipher into a stream cipher. Errors propagate for one block width.
- **OFB** (Output Feedback): Generates a keystream from the cipher independently of the data, giving a synchronous stream cipher. Bit errors do not propagate.
- **CTR** (Counter): Also a stream cipher mode; the cipher encrypts a counter value to produce a keystream. Highly parallelizable and widely used in TLS and disk encryption.
- **XTS** (XEX-based Tweaked CodeBook with ciphertext Stealing): Designed for disk sector encryption where a tweak value (sector number) is used to vary the encryption per sector.

Integrity and authenticated encryption modes:
- **CMAC**: A CBC-MAC variant that produces a message authentication code from a block cipher. Used for integrity-only protection.
- **CBC-MAC**: Classic cipher-based MAC; predecessor to CMAC.
- **CCM** (Counter with CBC-MAC): An AEAD mode combining CTR encryption with CBC-MAC authentication. Used in IEEE 802.11 (WPA2) and TLS.
- **GCM** (Galois/Counter Mode): The most widely deployed AEAD mode, combining CTR encryption with GHASH-based authentication. Provides both confidentiality and integrity efficiently with hardware support.
- **AEAD**: A generic label for authenticated encryption with associated data, used when the specific AEAD mode is captured elsewhere.

Key-wrapping specific modes:
- **NISTKeyWrap** / **AESKeyWrapPadding**: NIST SP 800-38F key-wrapping algorithms based on AES, providing integrity protection for key material without requiring an IV.
- **X9.102-AESKW**, **X9.102-TDKW**, **X9.102-AKW1**, **X9.102-AKW2**: ANSI X9.102 key-wrapping variants used in payment and financial systems.

## Examples

A KMIP server wrapping a symmetric key for transport to another key management system would typically use **NISTKeyWrap** or **AESKeyWrapPadding**. A TLS session key protecting a KMIP transport channel is typically derived using **GCM** mode for its AEAD properties.

## Related

- [Cryptographic Parameters](../attributes/cryptographic-parameters.md) — the structure that contains this enumeration field
- [Cryptographic Algorithm Enumeration](cryptographic-algorithm-enumeration.md) — selects the algorithm that this mode operates on
- [Padding Method Enumeration](padding-method-enumeration.md) — complements mode selection for block-size alignment
- 