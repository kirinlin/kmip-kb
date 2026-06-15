---
title: Modify Attribute
category: operation
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.34"
v1_source_section: "4.15"
status: reviewed
related: ["add-attribute", "delete-attribute", "get-attributes"]
keywords: ["modify attribute", "change attribute", "update value", "attribute index"]
---

# Modify Attribute

## Purpose

`Modify Attribute` changes the value of an attribute instance that already
exists on a managed object. It complements [Add Attribute](add-attribute.md),
which creates values; `Modify Attribute` only updates existing ones.

## Request Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | No | The object to change; the ID Placeholder is used when omitted. |
| Attribute | `420008` | `Attribute` | Yes | The attribute name, optional index, and new value. |

## Response Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes | The object's identifier. |
| Attribute | `420008` | `Attribute` | Yes | The attribute with its updated value. |

## Behavior & Server Requirements

Only the single instance named by the index is changed; when no index is given,
index 0 is assumed. Pointing at an index that has no attribute instance is an
error, and attributes that do not yet exist must be created with
[Add Attribute](add-attribute.md) rather than modified. The response echoes the
new value, and may omit the index when it is 0. Multiple modifications can be
batched together.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: an index that names no existing instance, modifying a non-existent or
read-only attribute, an invalid value, or insufficient permission.

## Related Operations

[Add Attribute](add-attribute.md) · [Delete Attribute](delete-attribute.md) ·
[Get Attributes](get-attributes.md)
