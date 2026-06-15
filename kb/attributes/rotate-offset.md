---
title: Rotate Offset
category: attribute
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "4.54"
status: reviewed
related: ["rotate-interval", "rotate-date", "rotate-automatic", "rotate-name", "protection-period", "activation-date", "deactivation-date"]
keywords: ["rotate offset", "rotation offset", "grace period", "lead time", "rotation adjustment", "interval"]
tag_hex: "42016C"
xml_element: "RotateOffset"
---

# Rotate Offset

## Purpose

Rotate Offset introduces a displacement from the nominal rotation trigger, enabling lead-time or grace-period behaviour. A positive offset extends the time before or after a scheduled rotation date, providing a window in which the outgoing key remains valid alongside its replacement. A negative offset (where the server supports signed semantics) causes rotation to begin before the nominal Rotate Date, pre-positioning the new key so it is ready when the old one reaches its cryptoperiod boundary.

## Data Type & Structure

An Interval — a 32-bit unsigned integer count of seconds. Whether the offset is applied before or after the nominal rotation point is implementation-defined. The most common use is a positive lead time: create the successor key this many seconds before the scheduled rotation date so that downstream systems have time to pick it up.

## Constraints

Single-instance. Optional. Only meaningful in conjunction with [Rotate Date](rotate-date.md) and/or [Rotate Interval](rotate-interval.md). Servers must document precisely how the offset is applied in their rotation scheduling logic, as ambiguous implementations can result in gaps or overlaps in key coverage.

## Applies To (Object Types)

[Symmetric Key](../objects/symmetric-key.md), [Private Key](../objects/private-key.md), [Secret Data](../objects/secret-data.md).

## Set / Modified By

Client at creation or via [Set Attribute](../operations/set-attribute.md).

## Related Attributes

[Rotate Interval](rotate-interval.md) · [Rotate Date](rotate-date.md) · [Rotate Automatic](rotate-automatic.md) · [Activation Date](activation-date.md) · [Deactivation Date](deactivation-date.md)
