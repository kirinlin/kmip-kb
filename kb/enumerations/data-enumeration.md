---
title: Data Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["2.0","2.1"]
source_section: "11.13"
status: reviewed
related: ["process"]
keywords: ["data type", "process operation", "encrypt input", "decrypt input", "sign input", "verify input", "data payload", "4200C2", "Data"]
tag_hex: "4200C2"
xml_text: "Data"
---

# Data Enumeration

## Overview

The Data enumeration discriminates the role of a data payload within the [Process](../operations/process.md) operation, which provides a generic cryptographic processing interface for applying key-based operations to raw data. Because Process can perform multiple cryptographic functions — encryption, decryption, signing, and signature verification — the Data enumeration tells the server which role the accompanying byte string plays. This avoids ambiguity when the same operation supports multiple data inputs or when a pipeline processes data in stages.

## Fields & Structure

| Value | Hex | XML Text | Description |
|---|---|---|---|
| Decrypt | `0x00000001` | `Decrypt` |  |
| Encrypt | `0x00000002` | `Encrypt` |  |
| Hash | `0x00000003` | `Hash` |  |
| MAC MAC Data | `0x00000004` | `MACMACData` |  |
| RNG Retrieve | `0x00000005` | `RNGRetrieve` |  |
| Sign Signature Data | `0x00000006` | `SignSignatureData` |  |
| Signature Verify | `0x00000007` | `SignatureVerify` |  |

- **Encrypt Input**: The plaintext bytes to be encrypted using the referenced key and algorithm parameters. The output will be ciphertext.
- **Decrypt Input**: The ciphertext bytes to be decrypted. The output will be plaintext.
- **Sign Input**: The message or hash bytes to be signed. The output will be a digital signature.
- **Verify Input**: Data submitted for signature verification alongside a signature value; the result indicates whether the signature is valid.

Additional values may be defined for other process functions such as MAC generation and verification, hash computation, and random number generation, allowing the Process operation to be extended without adding new operation codes.

## Examples

A client calling Process to sign a software artefact submits the artefact hash as **Sign Input** along with a reference to the signing key. A client calling Process to authenticate a message provides the received ciphertext as **Decrypt Input** and separately provides the authentication tag, if required by the mode.

## Related

- [Process operation](../operations/process.md) — the operation that uses this enumeration
- 