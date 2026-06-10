---
title: Opaque Object
category: object
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "2.3"
v1_source_section: "2.2.8"
status: draft
related: ["register", "get", "secret-data", "name"]
keywords: ["opaque object", "blob", "custom attributes", "unmanaged format"]
---

# Opaque Object

## Purpose

An Opaque Object is a managed object whose internal format the server does not
necessarily understand. It lets a client store and retrieve arbitrary data under
KMIP management — with the server treating the contents as an uninterpreted blob.
It is registered with [Register](../operations/register.md) and retrieved with
[Get](../operations/get.md).

## Structure

| Field | Required | Meaning |
|---|---|---|
| Opaque Data Type | Yes | Identifies the kind of opaque data, so a client knows how to interpret it. |
| Opaque Data Value | Yes | The raw opaque bytes the server stores without interpreting. |

## Key Attributes

Because the server cannot interpret the contents, any descriptive context is
usually attached through Custom Attributes rather than inferred from the data.
The object still carries the common managed-object attributes such as
[Unique Identifier](../attributes/unique-identifier.md),
[Object Type](../attributes/object-type.md),
[Name](../attributes/name.md), and [State](../attributes/state.md).

## Lifecycle & State

An Opaque Object follows the standard managed-object [State](../attributes/state.md)
lifecycle for registration, retrieval, and destruction, though the server does
not perform cryptographic operations on it.

## Related Objects

[Secret Data](secret-data.md) · [PGP Key](pgp-key.md)
