---
title: Protection Period
category: attribute
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "4.43"
status: reviewed
related: ["protection-level", "protection-storage-mask", "activation-date", "deactivation-date", "rotate-interval"]
keywords: ["protection period", "key lifetime", "protection duration", "interval", "cryptoperiod"]
tag_hex: "420146"
xml_element: "ProtectionPeriod"
---

# Protection Period

## Purpose

Protection Period specifies the duration for which a key or secret object's protection requirements must remain in effect. It provides a time-bounded policy anchor: once the interval expires, the server or client may reassess the protection level, initiate rotation, or deactivate the object. This complements the point-in-time lifecycle dates (Activation Date, Deactivation Date) with a forward-looking duration expression.

## Data Type & Structure

An Interval — a 32-bit unsigned integer count of seconds. The period begins from a reference point defined by server policy (typically the Activation Date or the date the attribute was last set). An interval of zero may indicate an indefinite or policy-defined period, depending on implementation.

## Constraints

Single-instance. Optional. May be set at creation or updated via [Set Attribute](../operations/set-attribute.md). The attribute does not itself trigger any automatic action; external policy engines or the [Rotate Interval](rotate-interval.md) attribute carry the operational logic.

## Applies To (Object Types)

[Symmetric Key](../objects/symmetric-key.md), [Private Key](../objects/private-key.md), [Secret Data](../objects/secret-data.md), and any object with a defined protection requirement duration.

## Set / Modified By

Client at creation or registration. Updateable via [Set Attribute](../operations/set-attribute.md).

## Related Attributes

[Protection Level](protection-level.md) · [Protection Storage Mask](protection-storage-mask.md) · [Rotate Interval](rotate-interval.md) · [Activation Date](activation-date.md) · [Deactivation Date](deactivation-date.md)
