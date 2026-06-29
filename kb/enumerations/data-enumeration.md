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
tag_type: "Enumeration"
---

# Data Enumeration

## Overview

The Data enumeration discriminates the role of a data payload within the [Process](../operations/process.md) operation, which provides a generic cryptographic processing interface for applying key-based operations to raw data. Because Process can perform multiple cryptographic functions — encryption, decryption, signing, and signature verification — the Data enumeration tells the server which role the accompanying byte string plays. This avoids ambiguity when the same operation supports multiple data inputs or when a pipeline processes data in stages.

## Fields & Structure

| Name | Value | XML Text |
|---|---|---|
| Decrypt | `00000001` | `Decrypt` |
| Encrypt | `00000002` | `Encrypt` |
| Hash | `00000003` | `Hash` |
| MAC MAC Data | `00000004` | `MACMACData` |
| RNG Retrieve | `00000005` | `RNGRetrieve` |
| Sign Signature Data | `00000006` | `SignSignatureData` |
| Signature Verify | `00000007` | `SignatureVerify` |

## Examples

A client calling Process to sign a software artefact submits the artefact hash as **Sign Input** along with a reference to the signing key. A client calling Process to authenticate a message provides the received ciphertext as **Decrypt Input** and separately provides the authentication tag, if required by the mode.

## Related

- [Process operation](../operations/process.md) — the operation that uses this enumeration
- 