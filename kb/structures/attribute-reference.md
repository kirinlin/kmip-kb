---
title: Attribute Reference
category: structures
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "5.5"
status: reviewed
related: ["attribute", "current-attribute", "new-attribute", "set-attribute", "delete-attribute", "adjust-attribute", "constraint"]
keywords: ["attribute reference", "attribute name", "attribute index", "attribute pointer", "attribute identification", "42013B", "AttributeReference"]
tag_hex: "42013B"
xml_text: "AttributeReference"
---

# Attribute Reference

## Overview

An Attribute Reference names an attribute without carrying its value. Where older KMIP versions required a full Attribute structure — name plus value — even in contexts where only identification was needed, the Attribute Reference offers a lighter form that carries just the attribute name and, when relevant, an index to distinguish among multiple instances of the same multi-valued attribute.

The structure appears in operation payloads such as [Set Attribute](../operations/set-attribute.md), [Delete Attribute](../operations/delete-attribute.md), and [Adjust Attribute](../operations/adjust-attribute.md). It also appears inside [Constraint](constraint.md) entries, where the reference identifies which attribute a policy rule governs without binding the rule to a particular value.

## Encoding (Tag / Type / Length / Value)

Attribute Reference encodes as a Structure.

| Field | Tag | XML Text | Type | Required |
|---|---|---|---|---|
| Attribute Name | `420009` | `AttributeName` | Text String | Yes |
| Attribute Index | `42000A` | `AttributeIndex` | Integer | No |

The Attribute Name is the canonical string name exactly as defined in the spec — for example `"Cryptographic Algorithm"` or `"Name"`. Attribute Index is omitted for single-valued attributes and, when present, selects a specific instance of a repeating attribute.

## Fields & Structure

**Attribute Name** is a case-sensitive Text String that must match one of the attribute names defined in the KMIP specification. Using the exact canonical form (title-case with spaces) is required for interoperability; vendor-prefixed names follow the `"x-<vendor>-<name>"` convention.

**Attribute Index** is a zero-based Integer. It is only meaningful for attributes that can appear multiple times on an object, such as Name or Link. When absent in a context that requires disambiguation, behavior is server-defined but typically defaults to the first occurrence (index 0).

The Attribute Reference pattern was introduced to replace the awkward practice of sending a full Attribute value just to indicate "act on this attribute." Because the value is not included, the reference is smaller and cannot accidentally carry stale data.

## Examples

A client wishes to delete the second Name attribute (index 1) from an object. The Delete Attribute request payload contains an Attribute Reference with Attribute Name = `"Name"` and Attribute Index = `1`. No name string value is transmitted — the reference alone is sufficient.

In a Constraint applied via [Set Constraints](../operations/set-constraints.md), an Attribute Reference pointing to `"Cryptographic Algorithm"` scopes the rule to that attribute without fixing which algorithm values are acceptable. The rule's logic is expressed separately in the enclosing Constraint structure.

## Related

[Attribute](attribute.md) · [Current Attribute](current-attribute.md) · [New Attribute](new-attribute.md) · [Constraint](constraint.md) · [Set Attribute](../operations/set-attribute.md) · [Delete Attribute](../operations/delete-attribute.md) · [Adjust Attribute](../operations/adjust-attribute.md)
