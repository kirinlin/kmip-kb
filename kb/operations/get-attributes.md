---
title: Get Attributes
category: operation
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.20"
v1_source_section: "4.12"
status: reviewed
related: ["get-attribute-list", "get", "add-attribute", "modify-attribute"]
keywords: ["get attributes", "read attributes", "attribute values", "metadata"]
---

# Get Attributes

## Purpose

`Get Attributes` reads the values of one or more attributes of a managed object.
Where [Get Attribute List](get-attribute-list.md) returns just the names of the
attributes present, this operation returns their actual values.

## Request Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | No | The object to read; the ID Placeholder is used when omitted. |
| Attribute Name | No (may repeat) | The name of an attribute to return. A given name must not appear more than once. |

## Response Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | Yes | The object's identifier. |
| Attribute | No (may repeat) | A requested attribute and its value. |

## Behavior & Server Requirements

When an attribute has several instances, all of them are returned. An attribute
that has no value is simply absent from the response rather than returned empty,
so a request for attributes that all turn out to be unset yields a response
carrying only the identifier. Supplying no attribute names is shorthand for
"return everything" — the server treats every attribute as requested.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: an unknown object, a duplicated attribute name in the request, or
insufficient permission.

## Related Operations

[Get Attribute List](get-attribute-list.md) · [Get](get.md) ·
[Modify Attribute](modify-attribute.md)
