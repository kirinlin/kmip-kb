---
title: Protection Storage Masks
category: structures
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "7.33"
status: reviewed
related: ["protection-storage-mask", "protection-storage-mask", "server-information", "query"]
keywords: ["protection storage masks", "supported storage configurations", "storage protection list", "query response", "server capabilities", "42015F", "ProtectionStorageMasks"]
tag_hex: "42015F"
xml_text: "ProtectionStorageMasks"
---

# Protection Storage Masks

## Overview

Protection Storage Masks is a wrapper structure (note the plural form) that carries a list of [Protection Storage Mask](../encoding/protection-storage-mask.md) values in a server's [Query](../operations/query.md) response. Where the singular Protection Storage Mask describes a single storage protection configuration, this structure advertises the full set of storage protection configurations the server supports or offers.

Clients consult this list to understand which combinations of storage protection categories — On Premise, Hardware Module, Cloud, Third Party, etc. — are available before assigning protection requirements to managed objects.

## Encoding (Tag / Type / Length / Value)

Protection Storage Masks encodes as a Structure containing one or more Protection Storage Mask integers.

| Field | Tag | XML Element | Type | Required |
|---|---|---|---|---|
| Protection Storage Mask | `420126` | `ProtectionStorageMask` | Integer | One or more |

Each Integer child is a 32-bit protection storage mask bit field.

## Fields & Structure

The repeating Protection Storage Mask children each represent one storage protection tier or combination that the server can provide. The bit-field semantics are defined in §12.2 — each bit corresponds to a protection category (On Premise, Off Premise, Hardware Module, Cloud, Client, Third Party).

A server might list several entries to indicate distinct tiers: for example, one entry for on-premise software storage (`00000001`), another for on-premise hardware module storage (`00000005`), and a third for cloud storage with hardware backing (`0000000C`). Clients can then select the appropriate tier when specifying protection requirements for newly created objects.

## Examples

A server Query response includes a Protection Storage Masks structure with three entries:
- `00000001` (On Premise)
- `00000005` (On Premise | Hardware Module)
- `00000009` (On Premise | Cloud)

A client that must satisfy a compliance requirement mandating hardware module protection knows to target the `00000005` tier when registering sensitive keys.

## Related

[Protection Storage Mask (TTLV bit field)](../encoding/protection-storage-mask.md) · [Protection Storage Mask (attribute)](../attributes/protection-storage-mask.md) · [Server Information](server-information.md) · [Query](../operations/query.md)
