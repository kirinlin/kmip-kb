---
title: Add Attribute
category: operation
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.2"
v1_source_section: "4.14"
status: reviewed
related: ["modify-attribute", "delete-attribute", "get-attributes"]
keywords: ["add attribute", "set attribute", "attribute instance", "attribute index"]
xml_text: "AddAttribute"
---

# Add Attribute

## Purpose

`Add Attribute` attaches a new attribute value to a managed object. It is how an
attribute first gets a value: for single-valued attributes it sets the one
value, and for multi-valued attributes it creates the first and each subsequent
value. Changing a value that already exists is the job of
[Modify Attribute](modify-attribute.md).

## Request Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | No | The object to add to; the ID Placeholder is used when omitted. |
| Attribute | `420008` | `Attribute` | Yes | The attribute name and value to attach. |

## Response Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes | The object's identifier. |
| Attribute | `420008` | `Attribute` | Yes | The attribute that was added, including its assigned index. |

## Behavior & Server Requirements

The client supplies the attribute name and value but not the index — the server
assigns the index of the new instance and reports it back (the index may be left
out of the response when it is 0). Read-only attributes cannot be added this way.
Several `Add Attribute` requests can be combined in one batch to populate
multiple attributes at once.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: attempting to add a read-only attribute, supplying an index, adding a
value to a single-valued attribute that already has one, an invalid value, or
insufficient permission.

## Related Operations

[Modify Attribute](modify-attribute.md) · [Delete Attribute](delete-attribute.md) ·
[Get Attributes](get-attributes.md)
