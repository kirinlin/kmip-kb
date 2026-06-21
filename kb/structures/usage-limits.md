---
title: Usage Limits
category: structures
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "7.40"
status: reviewed
related: ["get-attributes", "locate", "state", "cryptographic-usage-mask"]
keywords: ["usage limits", "usage count", "usage total", "usage limits unit", "key usage enforcement", "byte count", "object count", "420095", "UsageLimits"]
tag_hex: "420095"
xml_text: "UsageLimits"
tag_type: "Structure"
---

# Usage Limits

## Overview

Usage Limits is a structure that encodes quantitative restrictions on how many times — or for how much data — a managed object may be used. When a server enforces usage limits, it tracks consumption against these bounds and may transition an object to the Deactivated state once the limits are exhausted. The structure is used as an attribute on managed objects (primarily symmetric keys) and is carried in operation payloads when reading or setting usage limit information.

Usage limits are a complement to the [Cryptographic Usage Mask](../encoding/cryptographic-usage-mask.md) (which controls what operations a key may perform) and the [State](../attributes/state.md) machine (which tracks lifecycle). They add a *quantity* dimension: a key might be permitted to encrypt, but only for up to 1 billion bytes.

## Encoding (Tag / Type / Length / Value)

Usage Limits encodes as a Structure.

| Field | Tag | XML Text | Type | Required |
|---|---|---|---|---|
| Usage Limits Count | `42009A` | `UsageLimitsCount` | Long Integer | Yes |
| Usage Limits Total | `42009B` | `UsageLimitsTotal` | Long Integer | Yes |
| Usage Limits Unit | `42009C` | `UsageLimitsUnit` | Enumeration | Yes |

All three fields are required.

## Fields & Structure

**Usage Limits Count** is the remaining allowed usage — the current "balance" that decrements as the object is used. At creation or registration it equals Usage Limits Total; each use reduces it by the quantity consumed (one unit per operation, or the byte count of data processed, depending on the Unit).

**Usage Limits Total** is the initial limit — the total allowed usage set at creation or last authorized replenishment. It serves as the upper bound for Count. The server uses this to enforce a cap on how much the key can be used over its entire lifetime.

**Usage Limits Unit** is an Enumeration that defines what "one unit" means when decrementing the count:

- *Byte* — each use decrements Count by the number of bytes processed in the cryptographic operation (useful for tracking data volume encrypted with a key).
- *Object* — each invocation of a key-using operation decrements Count by one, regardless of data size.

When Usage Limits Count reaches zero the server should prevent further use of the object and may automatically transition it away from the Active state. The Get Usage Allocation operation allows a client to pre-allocate a portion of the remaining count for a batch of anticipated operations.

## Examples

A key intended for bulk encryption with a hard limit of 10 GB of plaintext might be registered with Usage Limits Total = 10,737,418,240 (bytes), Usage Limits Count = 10,737,418,240, Unit = Byte. After encrypting 1 GB of data the Count decrements to 9,663,676,416. After the full 10 GB are processed the Count reaches zero and the server refuses further encrypt operations on that key.

A one-time-use symmetric key would be registered with Total = 1, Count = 1, Unit = Object. The first (and only) encryption operation decrements Count to zero and the key is automatically retired.

## Related

[Cryptographic Usage Mask](../encoding/cryptographic-usage-mask.md) · [State](../attributes/state.md) · [Get Attributes](../operations/get-attributes.md) · [Locate](../operations/locate.md)
