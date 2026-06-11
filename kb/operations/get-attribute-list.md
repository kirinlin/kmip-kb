---
title: Get Attribute List
category: operation
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.21"
v1_source_section: "4.13"
status: reviewed
related: ["get-attributes", "get"]
keywords: ["get attribute list", "attribute names", "list attributes", "metadata"]
---

# Get Attribute List

## Purpose

`Get Attribute List` reports which attributes are present on a managed object,
returning their names but not their values. A client typically calls it to
discover what is available, then calls [Get Attributes](get-attributes.md) for
the values it wants.

## Request Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | No | The object to inspect; the ID Placeholder is used when omitted. |

## Response Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | Yes | The object's identifier. |
| Attribute Name | Yes (may repeat) | The name of each attribute currently set on the object. |

## Behavior & Server Requirements

The server returns the names of the attributes that currently have a value on
the object. The companion operation [Get Attributes](get-attributes.md) then
retrieves the values for any of those names.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: an unknown object, or insufficient permission.

## Related Operations

[Get Attributes](get-attributes.md) · [Get](get.md)
