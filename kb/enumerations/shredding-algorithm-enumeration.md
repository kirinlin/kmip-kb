---
title: Shredding Algorithm Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["2.0","2.1"]
source_section: "11.53"
status: reviewed
related: ["destroy", "destroy-action-enumeration"]
keywords: ["shredding", "key destruction", "secure erase", "overwrite", "cryptographic erase", "4200F4", "ShreddingAlgorithm"]
tag_hex: "4200F4"
xml_text: "ShreddingAlgorithm"
---

# Shredding Algorithm Enumeration

## Overview

The Shredding Algorithm enumeration specifies how the physical storage medium holding key material should be sanitised when a managed object is destroyed. Not all destruction requests require or trigger physical sanitisation — a software delete may suffice depending on policy — but when sanitisation is required this enumeration identifies the method. It is used in conjunction with the [Destroy Action Enumeration](destroy-action-enumeration.md) in the Revoke or Destroy flow.

## Fields & Structure

| Value | Hex | XML Text | Description |
|---|---|---|---|
| Unspecified | `0x00000001` | `Unspecified` |  |
| Cryptographic | `0x00000002` | `Cryptographic` |  |
| Unsupported | `0x00000003` | `Unsupported` |  |

- **Unspecified**: The shredding method is not specified or is implementation-defined. The server uses its default sanitisation policy.
- **Cryptographic Erase**: The key material is deleted by discarding the encryption key that protects it, rendering the stored ciphertext unrecoverable without key recovery. Fast and effective when the key truly cannot be recovered.
- **Overwrite** (single pass): The storage blocks holding key material are overwritten once with zeros, ones, or a pseudo-random pattern before the space is released. Meets common data sanitisation requirements for non-volatile storage.
- **Overwrite** (multiple passes): Multiple overwrite passes with varying patterns (e.g., DoD 5220.22-M or Gutmann method). Intended to defeat advanced forensic recovery techniques on magnetic media.

## Examples

An HSM that destroys an RSA private key uses **Cryptographic Erase** because the key was stored encrypted and deleting the KEK is instant and provably complete. A software key manager destroying a key on a conventional SSD uses **Overwrite** with a single pass, accepting that the SSD controller may have additional copies in wear-leveling sectors.

## Related

[Destroy Action Enumeration](destroy-action-enumeration.md) · [Destroy](../operations/destroy.md)
