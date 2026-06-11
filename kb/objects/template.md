---
title: Template
category: object
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4"]
source_section: "del_v2"
v1_source_section: "2.2.6"
status: draft
related: ["register", "create", "create-key-pair", "name", "get"]
keywords: ["template", "deprecated", "attributes", "named object"]
tag_hex: "420090"
xml_element: "Template"
---

# Template

## Purpose

A Template is a named managed object that bundles a set of client-settable
attributes so they can be reused when creating new managed cryptographic
objects. Instead of listing every attribute on each request, a client could
register a Template once and then reference it by name from the
Template-Attribute structures of operations like
[Create](../operations/create.md) and
[Create Key Pair](../operations/create-key-pair.md).

> **Deprecated as of KMIP 1.3.** The Template object is deprecated and may be
> removed from later versions. Supply individual attributes directly in the
> Template-Attribute structures instead. This entry documents it for
> completeness and for interoperability with older deployments.

## Structure

| Field | Required | Meaning |
|---|---|---|
| Attribute | Yes (repeatable) | One or more attribute objects that the template carries and that get applied to objects referencing it. |

## Key Attributes

A Template is itself named via the [Name](../attributes/name.md) attribute,
supplied in the Template-Attribute structure of the
[Register](../operations/register.md) operation that creates it; that name is
how other operations reference the template. The attributes it contains are the
client-settable attributes appropriate to the object type being created.

## Lifecycle & State

A Template is registered like any other managed object and referenced by name
thereafter. Because it has been deprecated since version 1.3, new
implementations should prefer passing attributes individually rather than
maintaining template objects.

## Related Objects

[Symmetric Key](symmetric-key.md) · [Public Key](public-key.md) · [Private Key](private-key.md)
