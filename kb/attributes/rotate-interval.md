---
title: Rotate Interval
category: attribute
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "4.51"
status: reviewed
related: ["rotate-automatic", "rotate-date", "rotate-generation", "rotate-latest", "rotate-name", "rotate-offset", "protection-period", "re-key"]
keywords: ["rotate interval", "rotation interval", "cryptoperiod", "key rotation period", "interval attribute", "42016A", "RotateInterval"]
tag_hex: "42016A"
xml_text: "RotateInterval"
tag_type: "Interval"
---

# Rotate Interval

## Purpose

Rotate Interval sets the recurring period between key rotations as a duration. In combination with [Rotate Date](rotate-date.md), it defines a complete rotation schedule: starting from the anchor date, the key should be rotated every Rotate Interval seconds. This approach keeps the rotation schedule self-describing within the key's own attributes rather than in external configuration.

## Data Type & Structure

An Interval — a 32-bit unsigned integer count of seconds. Typical values map to common cryptoperiods: 7776000 (90 days), 15552000 (180 days), 31536000 (1 year). An interval of zero may indicate that interval-based rotation is not applicable, with rotation instead triggered by date or generation count.

## Constraints

Single-instance. Optional. Most meaningful when [Rotate Automatic](rotate-automatic.md) is `true` and [Rotate Date](rotate-date.md) provides the starting point. Without an anchor date, the interval alone is ambiguous. Servers must document how they compute the next rotation time if Rotate Date is absent.

## Applies To (Object Types)

[Symmetric Key](../objects/symmetric-key.md), [Private Key](../objects/private-key.md), [Secret Data](../objects/secret-data.md).

## Set / Modified By

Client at creation or via [Set Attribute](../operations/set-attribute.md). May be set by the server based on object-type policy defaults.

## Related Attributes

[Rotate Automatic](rotate-automatic.md) · [Rotate Date](rotate-date.md) · [Rotate Offset](rotate-offset.md) · [Protection Period](protection-period.md)
