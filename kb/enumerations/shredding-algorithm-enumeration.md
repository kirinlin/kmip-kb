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
tag_type: "Enumeration"
---

# Shredding Algorithm Enumeration

## Overview

The Shredding Algorithm enumeration specifies how the physical storage medium holding key material should be sanitised when a managed object is destroyed. Not all destruction requests require or trigger physical sanitisation — a software delete may suffice depending on policy — but when sanitisation is required this enumeration identifies the method. It is used in conjunction with the [Destroy Action Enumeration](destroy-action-enumeration.md) in the Revoke or Destroy flow.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Unspecified | `00000001` | `Unspecified` | The shredding method is not specified or is implementation-defined. The server uses its default sanitisation policy. |
| Cryptographic | `00000002` | `Cryptographic` | Cryptographic erasure: the key material was stored encrypted under a wrapping key, and destroying that wrapping key renders the protected data unrecoverable without any physical media overwrite. Equivalent to NIST SP 800-88 Cryptographic Erase. |
| Unsupported | `00000003` | `Unsupported` | The server does not support physical sanitisation of the storage medium. Destruction deletes logical references only; no hardware-level shredding is performed. Servers advertise this value in Capability Information when they lack the ability to sanitise storage. |

## Examples

An HSM that destroys an RSA private key uses **Cryptographic Erase** because the key was stored encrypted and deleting the KEK is instant and provably complete. A software key manager destroying a key on a conventional SSD uses **Overwrite** with a single pass, accepting that the SSD controller may have additional copies in wear-leveling sectors.

## Related

[Destroy Action Enumeration](destroy-action-enumeration.md) · [Destroy](../operations/destroy.md)
