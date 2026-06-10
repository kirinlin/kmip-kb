---
title: Delete Attribute
category: operation
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.16"
status: draft
related: ["add-attribute", "modify-attribute", "get-attributes"]
keywords: ["delete attribute", "remove attribute", "attribute index"]
---

# Delete Attribute

## Purpose

`Delete Attribute` removes an attribute instance from a managed object. It is the
counterpart to [Add Attribute](add-attribute.md).

## Request Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | No | The object to change; the ID Placeholder is used when omitted. |
| Attribute Name | Yes | The name of the attribute to remove. |
| Attribute Index | No | Which instance to remove; index 0 is assumed when omitted. |

## Response Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | Yes | The object's identifier. |
| Attribute | Yes | The attribute instance that was removed. |

## Behavior & Server Requirements

Attributes that are always required to hold a value cannot be removed. Naming an
attribute that is not set, or an index with no corresponding value, is an error.
The response returns the removed instance and may omit the index when it is 0.
Several deletions can be carried in a single batch.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: deleting a required attribute, naming a non-existent attribute or index,
or insufficient permission.

## Related Operations

[Add Attribute](add-attribute.md) · [Modify Attribute](modify-attribute.md) ·
[Get Attributes](get-attributes.md)
