---
title: Adjustment Type Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "11.1"
status: reviewed
related: ["adjust-attribute", "rotate-generation", "rotate-interval", "rotate-offset"]
keywords: ["adjustment type", "numeric delta", "adjust attribute", "arithmetic operation", "420158", "AdjustmentType"]
tag_hex: "420158"
xml_text: "AdjustmentType"
---

# Adjustment Type Enumeration

## Overview

The Adjustment Type enumeration controls how the [Adjust Attribute](../operations/adjust-attribute.md) operation modifies the current value of a numeric attribute. Rather than always replacing a value outright, this enumeration lets a client express an intent — increment, decrement, scale, or overwrite — and lets the server apply that intent atomically on the stored value. This is particularly useful for counters and rotation-related attributes where the client may not know the current value but needs to nudge it in a specific direction.

## Fields & Structure

| Value | Hex | XML Text | Description |
|---|---|---|---|
| Increment | `0x00000001` | `Increment` |  |
| Decrement | `0x00000002` | `Decrement` |  |
| Negate | `0x00000003` | `Negate` |  |

- **Add**: Increases the existing numeric attribute value by the supplied adjustment amount. Used when incrementing counters such as a rotate-generation counter or a usage count.
- **Subtract**: Decreases the existing numeric attribute value by the supplied adjustment amount. Mirrors Add but in the opposite direction; useful for releasing reserved usage allocations.
- **Multiply**: Multiplies the existing value by the adjustment amount. Less common but available for scaling operations.
- **Replace**: Overwrites the attribute with the supplied value regardless of what the current value is. Functionally equivalent to a Set Attribute but expressed through the Adjust Attribute path, and useful when the caller has authoritative knowledge of the correct final value.

## Examples

A client maintaining a rotation-generation counter can issue an Adjust Attribute request with type **Add** and a value of 1 each time a key generation is recorded, without needing to read the current counter first. If a management operation determines the counter has drifted, **Replace** lets it reset the attribute to an authoritative value in a single round trip.

## Related

- [Adjust Attribute](../operations/adjust-attribute.md) — the operation that consumes this enumeration
- [Rotate Generation](../attributes/rotate-generation.md) — example of a numeric attribute adjusted with Add
- [Rotate Interval](../attributes/rotate-interval.md) — another rotation attribute that may be adjusted
