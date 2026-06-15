---
title: Custom Attribute
category: attribute
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.60"
v1_source_section: "3.39"
status: reviewed
related: ["application-specific-information", "description", "comment"]
keywords: ["custom attribute", "x- prefix", "y- prefix", "vendor extension", "client-defined attribute", "42002D", "CustomAttribute"]
tag_hex: "42002D"
xml_text: "CustomAttribute"
---

# Custom Attribute

## Purpose

The escape hatch for metadata KMIP did not anticipate. Clients and servers
can attach arbitrarily named values to objects, partitioned by a naming
convention: client-created names start `x-`, server-created names start
`y-`. The other side stores them without interpreting them.

## Data Type & Structure

Any TTLV data type, including a structure — but a structure value must stay
flat (no nested sub-structures). Because the Custom Attribute tag itself says
nothing about *which* custom attribute it is, the value only ever travels
inside an [Attribute structure](../structures/attribute.md) where the Attribute
Name disambiguates it.

## Constraints

- Optional; multi-instance (different names, and multiple instances per
  name).
- Namespace enforcement is mandatory: a server rejects any client attempt to
  create or modify a `y-` attribute.
- Each side may only modify/delete its own: clients manage `x-` attributes,
  servers manage `y-` attributes.
- [Locate](../operations/locate.md) can match on custom attributes.

## Applies To (Object Types)

All managed objects.

## Set / Modified By

Client (`x-`) or server (`y-`); implicitly set by the create/register
family, [Activate](../operations/activate.md),
[Revoke](../operations/revoke.md), [Destroy](../operations/destroy.md), and
the certify/re-key families (e.g. copied to successors).

## Related Attributes

[Application Specific Information](application-specific-information.md) ·
[Description](description.md) · [Comment](comment.md)
