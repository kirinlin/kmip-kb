---
title: Protection Storage Mask
category: encoding
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "12.2"
status: reviewed
related: ["protection-storage-masks", "protection-storage-mask", "protection-level", "protection-period", "server-information", "query"]
keywords: ["protection storage mask", "bit mask", "storage protection", "on premise", "off premise", "hardware module", "cloud storage", "third party", "42015E", "ProtectionStorageMask"]
tag_hex: "42015E"
xml_text: "ProtectionStorageMask"
---

# Protection Storage Mask

## Overview

The Protection Storage Mask is a 32-bit integer bit field defined in §12.2 of the KMIP specification. Each bit position corresponds to a category of physical or logical storage protection — where the key material is stored and under what custody model. The mask is used both as a standalone value and as the numeric representation of the [Protection Storage Mask attribute](../attributes/protection-storage-mask.md) on managed objects.

By examining the bit field a consumer can determine what protection tiers a key is stored under. This matters for regulatory compliance, where requirements may mandate hardware module storage, on-premise custody, or restrictions on cloud storage.

## Encoding (Tag / Type / Length / Value)

The Protection Storage Mask value encodes as a 32-bit Integer (tag `42015E`). It is a scalar field whose bits are interpreted individually.

| Tag | XML Text | Type | Width |
|---|---|---|---|
| `42015E` | `ProtectionStorageMask` | Integer | 32 bits |

## Fields & Structure

The defined bit positions and their storage protection categories:

| Bit | Category |
|---|---|
| 0 (0x00000001) | Software |
| 1 (0x00000002) | Hardware |
| 2 (0x00000004) | On Processor |
| 3 (0x00000008) | On System |
| 4 (0x00000010) | Off System |
| 5 (0x00000020) | Hypervisor |
| 6 (0x00000040) | Operating System |
| 7 (0x00000080) | Container |
| 8 (0x00000100) | On Premises |
| 9 (0x00000200) | Off Premises |
| 10 (0x00000400) | Self Managed |
| 11 (0x00000800) | Outsourced |
| 12 (0x00001000) | Validated |
| 13 (0x00002000) | Same Jurisdiction |

Bits 14 and above are reserved for standard use; extension values use even-numbered bit positions only. Multiple bits may be set simultaneously to indicate that a key is stored under more than one protection category (for example, an HSM-backed key at an on-premises data center would set both On Premises and Hardware).

The mask operates differently depending on context:

- On a managed object, it describes where that object's key material is currently stored.
- In a [Protection Storage Masks](../structures/protection-storage-masks.md) structure (in a Query response), it describes a storage configuration the server supports.
- As a [Protection Level](../attributes/protection-level.md) or [Protection Period](../attributes/protection-period.md) anchor, it defines the minimum required storage tier for a given object lifecycle phase.

## Examples

A key stored in an on-premises HSM carries `00000102` (On Premises | Hardware). A key hosted by a cloud provider and managed externally carries `00000A00` (Off Premises | Outsourced). A software-based key held on the local system carries `00000009` (Software | On System).

A compliance policy requiring that a key remain in on-premises hardware storage specifies `00000102` as the minimum required mask. A stricter policy that additionally mandates the key be held in a validated store specifies `00001102` (On Premises | Hardware | Validated).

## Related

[Protection Storage Masks](../structures/protection-storage-masks.md) · [Protection Storage Mask (attribute)](../attributes/protection-storage-mask.md) · [Protection Level](../attributes/protection-level.md) · [Protection Period](../attributes/protection-period.md) · [Query](../operations/query.md)
