---
title: Name
category: attribute
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.32"
v1_source_section: "3.2"
status: draft
related: ["unique-identifier", "alternative-name", "object-group"]
keywords: ["name", "human-readable label", "locate by name", "name type"]
---

# Name

## Purpose

The client-chosen, human-meaningful handle for an object — the label an
application uses to find a key again via [Locate](../operations/locate.md)
without storing the server-assigned
[Unique Identifier](unique-identifier.md). Templates (while they existed)
were also referenced by their Name.

## Data Type & Structure

A structure with two required fields:

| Field | Type | Notes |
|---|---|---|
| Name Value | Text String | The label itself. |
| Name Type | Enumeration | `Uninterpreted Text String` or `URI`. |

## Constraints

- Optional, multi-instance: one object can carry several names.
- Each Name must be unique within the server's management domain (unlike
  [Alternative Name](alternative-name.md), which has no uniqueness rule);
  global uniqueness is not expected.
- Servers may impose naming rules; KMIP gives no in-band way to learn them.

## Applies To (Object Types)

All managed objects.

## Set / Modified By

Initially set by the client ([Add Attribute](../operations/add-attribute.md)
or at create/register time); both client and server may modify, and the
client may delete instances. Set implicitly by
[Re-key](../operations/re-key.md),
[Re-key Key Pair](../operations/re-key-key-pair.md), and
[Re-certify](../operations/re-certify.md), which transfer the name(s) to the
replacement object.

## Related Attributes

[Unique Identifier](unique-identifier.md) ·
[Alternative Name](alternative-name.md) · [Object Group](object-group.md)
