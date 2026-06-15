---
title: New Attribute
category: structures
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "5.7"
status: reviewed
related: ["attribute", "current-attribute", "attribute-reference", "set-attribute", "adjust-attribute"]
keywords: ["new attribute", "updated attribute", "replacement attribute value", "attribute modification", "42013D", "NewAttribute"]
tag_hex: "42013D"
xml_text: "NewAttribute"
---

# New Attribute

## Overview

New Attribute is a structure that carries the replacement value of an attribute in a modification operation. It is the "after" counterpart to [Current Attribute](current-attribute.md), which carries the "before" value. Together, the pair allows a client to express an atomic conditional update: "change the attribute from this value to that value."

New Attribute appears in [Set Attribute](../operations/set-attribute.md) and [Adjust Attribute](../operations/adjust-attribute.md) request payloads. In Set Attribute it holds the value to be stored. In Adjust Attribute it holds the computed target value — the value that should exist after the adjustment is applied.

## Encoding (Tag / Type / Length / Value)

New Attribute encodes as a Structure containing a single Attribute.

| Field | Tag | XML Element | Type | Required |
|---|---|---|---|---|
| Attribute | `420008` | `Attribute` | Structure | Yes |

The inner Attribute follows the standard encoding with Attribute Name and Attribute Value sub-fields. There is exactly one Attribute child.

## Fields & Structure

The single child [Attribute](attribute.md) carries the full name and the new value to be stored. The Attribute Name must match the name of an existing or creatable attribute on the target object. The Attribute Value must be correctly typed for that attribute.

When New Attribute is used alongside [Current Attribute](current-attribute.md), the server performs an optimistic concurrency check before applying the new value. When it is used alone (without a Current Attribute in the same request), the server applies the update unconditionally, replacing whatever value was previously stored for that attribute.

For multi-valued attributes the combination of Attribute Name and, where applicable, Attribute Index in the [Attribute Reference](attribute-reference.md) determines which instance is being replaced; the New Attribute value provides the replacement content.

## Examples

A client wants to change an object's Name from `"OldKeyName"` to `"NewKeyName"`. It sends a Set Attribute request with New Attribute containing Attribute Name = `"Name"` and Attribute Value = `"NewKeyName"`. If the request also includes a Current Attribute with Name = `"OldKeyName"`, the server first verifies the existing value before applying the change.

In an Adjust Attribute request for Cryptographic Usage Mask, New Attribute carries the full updated mask value (not a delta). The server stores this value directly.

## Related

[Attribute](attribute.md) · [Current Attribute](current-attribute.md) · [Attribute Reference](attribute-reference.md) · [Set Attribute](../operations/set-attribute.md) · [Adjust Attribute](../operations/adjust-attribute.md)
