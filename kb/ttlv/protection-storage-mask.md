---
title: Protection Storage Mask
category: ttlv
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "12.2"
status: reviewed
related: ["protection-storage-masks", "protection-storage-mask", "protection-level", "protection-period", "server-information", "query"]
keywords: ["protection storage mask", "bit mask", "storage protection", "on premise", "off premise", "hardware module", "cloud storage", "third party"]
---

# Protection Storage Mask

## Overview

The Protection Storage Mask is a 32-bit integer bit field defined in §12.2 of the KMIP specification. Each bit position corresponds to a category of physical or logical storage protection — where the key material is stored and under what custody model. The mask is used both as a standalone value and as the numeric representation of the [Protection Storage Mask attribute](../attributes/protection-storage-mask.md) on managed objects.

By examining the bit field a consumer can determine what protection tiers a key is stored under. This matters for regulatory compliance, where requirements may mandate hardware module storage, on-premise custody, or restrictions on cloud storage.

## Encoding (Tag / Type / Length / Value)

The Protection Storage Mask value encodes as a 32-bit Integer (tag `420126`). It is a scalar field whose bits are interpreted individually.

| Tag | Type | Width |
|---|---|---|
| `420126` | Integer | 32 bits |

## Fields & Structure

The defined bit positions and their storage protection categories:

| Bit | Category |
|---|---|
| 0 (0x00000001) | On Premise |
| 1 (0x00000002) | Off Premise |
| 2 (0x00000004) | Hardware Module |
| 3 (0x00000008) | Cloud |
| 4 (0x00000010) | Client |
| 5 (0x00000020) | Third Party |

Higher bits are reserved. Multiple bits may be set simultaneously to indicate that a key is stored under more than one protection category (for example, an HSM-backed key at an on-premise data center would set both On Premise and Hardware Module).

The mask operates differently depending on context:

- On a managed object, it describes where that object's key material is currently stored.
- In a [Protection Storage Masks](../structures/protection-storage-masks.md) structure (in a Query response), it describes a storage configuration the server supports.
- As a [Protection Level](../attributes/protection-level.md) or [Protection Period](../attributes/protection-period.md) anchor, it defines the minimum required storage tier for a given object lifecycle phase.

## Examples

A key stored on an on-premise HSM would carry a Protection Storage Mask of `0x00000005` (On Premise | Hardware Module). A key stored by a cloud key management service would carry `0x00000008` (Cloud). A policy requiring that a key remain on premise in hardware at all times would specify a mask of `0x00000005` as the required minimum.

## Related

[Protection Storage Masks](../structures/protection-storage-masks.md) · [Protection Storage Mask (attribute)](../attributes/protection-storage-mask.md) · [Protection Level](../attributes/protection-level.md) · [Protection Period](../attributes/protection-period.md) · [Query](../operations/query.md)
