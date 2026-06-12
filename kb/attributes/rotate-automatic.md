---
title: Rotate Automatic
category: attribute
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "4.48"
status: reviewed
related: ["rotate-interval", "rotate-date", "rotate-generation", "rotate-latest", "rotate-name", "rotate-offset", "re-key", "deactivation-date"]
keywords: ["rotate automatic", "key rotation", "automatic rotation", "auto-rotate", "rotation policy", "boolean"]
---

# Rotate Automatic

## Purpose

Rotate Automatic is a Boolean attribute that enables server-driven automatic key rotation. When set to `true`, the server will initiate a rotation operation — equivalent in effect to a client-issued [Re-key](../operations/re-key.md) — when the conditions defined by the rotation policy attributes are met. This allows keys to be rotated on schedule without requiring a client to poll expiry dates or issue explicit rotation requests.

## Data Type & Structure

A Boolean. `true` enables automatic rotation; `false` (or absence of the attribute) means rotation must be initiated explicitly by a client.

## Constraints

Single-instance. Optional. Meaningful only when at least one rotation-trigger attribute is also present — typically [Rotate Interval](rotate-interval.md) or [Rotate Date](rotate-date.md). Servers that do not support server-initiated rotation should return an error or ignore this attribute, and implementations should document their behaviour. Automatic rotation generates a new key object linked to the original via linked-object semantics; the predecessor is deactivated according to server policy.

## Applies To (Object Types)

[Symmetric Key](../objects/symmetric-key.md), [Private Key](../objects/private-key.md), [Secret Data](../objects/secret-data.md).

## Set / Modified By

Client at creation or via [Set Attribute](../operations/set-attribute.md). May also be set by the server as part of a policy template.

## Related Attributes

[Rotate Interval](rotate-interval.md) · [Rotate Date](rotate-date.md) · [Rotate Generation](rotate-generation.md) · [Rotate Latest](rotate-latest.md) · [Rotate Name](rotate-name.md) · [Rotate Offset](rotate-offset.md)
