---
title: Attribute
category: structures
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "5.1"
v1_source_section: "2.1.1"
status: reviewed
related: ["template-attribute-structures", "custom-attribute", "ttlv-encoding"]
keywords: ["attribute structure", "attribute name", "attribute index", "attribute value"]
tag_hex: "420008"
xml_element: "Attribute"
---

# Attribute

## Overview

The wire container for any attribute crossing the protocol: a name, an
optional instance index, and the value. Operations that move attributes
around — [Get Attributes](../operations/get-attributes.md),
[Add](../operations/add-attribute.md) /
[Modify](../operations/modify-attribute.md) /
[Delete Attribute](../operations/delete-attribute.md),
[Locate](../operations/locate.md) predicates, Template-Attribute payloads —
all carry their attributes in this envelope.

## Encoding (Tag / Type / Length / Value)

Structure, tag `420008`. Inside:

| Field | Tag | XML Element | Type | Required |
|---|---|---|---|---|
| Attribute Name | `42000A` | `AttributeName` | Text String | Yes |
| Attribute Index | `420009` | `AttributeIndex` | Integer | No (defaults to 0) |
| Attribute Value | `42000B` | `AttributeValue` | varies | Yes, except in [Notify](../operations/server-to-client/notify.md), where a value-less Attribute signals deletion |

## Fields & Structure

The **name** is the canonical attribute name from the spec's attributes
chapter (v2.1 §4; v1.x §3) (e.g.
`Cryptographic Algorithm`, or an `x-`/`y-` prefixed
[custom attribute](../attributes/custom-attribute.md) name). The **index**
distinguishes instances of multi-instance attributes: numbering starts at 0,
an instance keeps its index even when siblings are added or removed, and
single-instance attributes always sit at index 0. The **value**'s TTLV type
depends on the attribute — primitive for simple attributes, a nested
structure for things like [Link](../attributes/link.md) or
[Name](../attributes/name.md).

## Examples

Modifying the second name on an object: an Attribute structure with
Attribute Name = `"Name"`, Attribute Index = 1, and an Attribute Value
holding a Name structure (Name Value `"backup-key"`, Name Type
Uninterpreted Text String).

## Related

[Template-Attribute Structures](template-attribute-structures.md) ·
[Custom Attribute](../attributes/custom-attribute.md) ·
[attributes/ index](../attributes/index.md)
