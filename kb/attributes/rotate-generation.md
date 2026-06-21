---
title: Rotate Generation
category: attribute
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "4.50"
status: reviewed
related: ["rotate-automatic", "rotate-date", "rotate-interval", "rotate-latest", "rotate-name", "rotate-offset", "re-key"]
keywords: ["rotate generation", "key generation", "rotation count", "generation number", "key versioning", "42016E", "RotateGeneration"]
tag_hex: "42016E"
xml_text: "RotateGeneration"
tag_type: "Integer"
---

# Rotate Generation

## Purpose

Rotate Generation tracks how many times a key has been rotated since its original creation. Generation 0 (or 1, depending on server convention) is the original key; each successful rotation increments the counter. This provides a compact audit trail for key lineage and enables policies that retire a key family after a maximum number of rotations rather than (or in addition to) a time-based policy.

## Data Type & Structure

An Integer. Non-negative. The starting value and increment behaviour (whether 0-based or 1-based, whether it counts the original key or only rotations) are implementation-defined but should be consistent within a single server.

## Constraints

Single-instance. Optional but server-maintained when rotation is in use. Clients should treat this as read-only in practice; the server increments it after each [Re-key](../operations/re-key.md) or automatic rotation. Writing it directly via [Set Attribute](../operations/set-attribute.md) may be restricted by policy.

## Applies To (Object Types)

[Symmetric Key](../objects/symmetric-key.md), [Private Key](../objects/private-key.md), [Secret Data](../objects/secret-data.md).

## Set / Modified By

Set and incremented by the server on each rotation. May optionally be initialized by the client at registration for imported key lineages.

## Related Attributes

[Rotate Automatic](rotate-automatic.md) · [Rotate Latest](rotate-latest.md) · [Rotate Name](rotate-name.md)
