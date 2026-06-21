---
title: Rotate Date
category: attribute
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "4.49"
status: reviewed
related: ["rotate-automatic", "rotate-interval", "rotate-generation", "rotate-latest", "rotate-name", "rotate-offset", "re-key", "activation-date", "deactivation-date"]
keywords: ["rotate date", "key rotation date", "next rotation", "rotation schedule", "date-time", "42016D", "RotateDate"]
tag_hex: "42016D"
xml_text: "RotateDate"
tag_type: "Date-Time"
---

# Rotate Date

## Purpose

Rotate Date is a Date-Time attribute that anchors the rotation schedule to a specific calendar moment. It can express when the next rotation is due, or record when the most recent rotation was completed, depending on server implementation and how it is combined with [Rotate Interval](rotate-interval.md). Together these two attributes define a recurring rotation schedule: the initial trigger point and the recurrence period.

## Data Type & Structure

A Date-Time — a 64-bit integer count of seconds since the UNIX epoch (1970-01-01T00:00:00Z), consistent with all other Date-Time attributes in KMIP. May be set to a future date (next scheduled rotation) or a past date (last completed rotation), depending on the server's convention.

## Constraints

Single-instance. Optional. When both Rotate Date and [Rotate Interval](rotate-interval.md) are present and [Rotate Automatic](rotate-automatic.md) is `true`, the server computes subsequent rotation triggers as Rotate Date + N × Rotate Interval. Servers should update this attribute after each rotation to reflect the next due date, but exact update semantics are implementation-defined.

## Applies To (Object Types)

[Symmetric Key](../objects/symmetric-key.md), [Private Key](../objects/private-key.md), [Secret Data](../objects/secret-data.md).

## Set / Modified By

Client at creation or via [Set Attribute](../operations/set-attribute.md). Updated by the server after each automatic rotation.

## Related Attributes

[Rotate Automatic](rotate-automatic.md) · [Rotate Interval](rotate-interval.md) · [Rotate Generation](rotate-generation.md) · [Rotate Latest](rotate-latest.md) · [Activation Date](activation-date.md)
