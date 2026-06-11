---
title: Object Type
category: attribute
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.36"
v1_source_section: "3.3"
status: reviewed
related: ["unique-identifier", "cryptographic-algorithm"]
keywords: ["object type", "enumeration", "symmetric key", "certificate", "classification"]
tag_hex: "420057"
xml_element: "ObjectType"
---

# Object Type

## Purpose

Records which kind of managed object this is, so clients can filter
[Locate](../operations/locate.md) results and know how to interpret a
[Get](../operations/get.md) response.

## Data Type & Structure

An Enumeration. Values defined in 1.4: Certificate, Symmetric Key, Public
Key, Private Key, Split Key, Template (deprecated since 1.3), Secret Data,
Opaque Object, and PGP Key (added in 1.2), plus vendor extensions.

## Constraints

- Always present; single instance.
- Immutable: fixed when the object is created or registered, read-only for
  both sides until destruction.
- Must agree with the payload — registering a structure that is not what the
  declared type says is an error.

## Applies To (Object Types)

All managed objects (it is the attribute that *says* which type).

## Set / Modified By

Server-set, implicitly, by every object-creating operation
([Create](../operations/create.md),
[Create Key Pair](../operations/create-key-pair.md),
[Register](../operations/register.md),
[Derive Key](../operations/derive-key.md),
[Certify](../operations/certify.md),
[Re-certify](../operations/re-certify.md),
[Re-key](../operations/re-key.md),
[Re-key Key Pair](../operations/re-key-key-pair.md)). In Create and Register
the client states the intended type in the request payload, and the server
records it here.

## Related Attributes

[Unique Identifier](unique-identifier.md) ·
[Cryptographic Algorithm](cryptographic-algorithm.md)
