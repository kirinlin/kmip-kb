---
title: Common Attributes
category: structures
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "5.2"
status: reviewed
related: ["attribute", "private-key-attributes", "public-key-attributes", "template-attribute-structures", "unique-identifier", "object-type", "cryptographic-algorithm"]
keywords: ["common attributes", "attribute structure", "all object types", "shared attributes", "key pair attributes"]
tag_hex: "420126"
xml_element: "CommonAttributes"
---

# Common Attributes

## Overview

Common Attributes is a structure that groups the attributes applicable to all managed object types — symmetric keys, asymmetric keys, certificates, secret data, and opaque objects alike. It exists alongside the type-specific attribute structures ([Private Key Attributes](private-key-attributes.md) and [Public Key Attributes](public-key-attributes.md)) to give a clean separation between attributes every object carries and those that apply only to particular kinds of objects.

Common Attributes appears in Create Key Pair requests and responses (and in similar key-pair contexts) to carry the shared subset of attributes for both halves of the key pair in a single container. It is part of the §5 "Attribute Data Structures" group introduced in KMIP 2.0 to supersede the older Template Attribute pattern.

## Encoding (Tag / Type / Length / Value)

Common Attributes encodes as a Structure. It contains zero or more [Attribute](attribute.md) structures.

| Field | Tag | XML Element | Type | Required |
|---|---|---|---|---|
| Attribute | `420008` | `Attribute` | Structure | Zero or more |

The structure may be empty; an empty Common Attributes means no common attributes are being specified in this payload. The repeating Attribute children carry individual attribute name/value pairs.

## Fields & Structure

Each child is a complete [Attribute](attribute.md) structure with an Attribute Name and Attribute Value. Any attribute that is valid for all managed object types may appear here — examples include:

- Unique Identifier
- Name
- Object Type
- Cryptographic Algorithm
- Cryptographic Length
- State
- Digest
- Last Change Date

Attributes that apply only to private or public keys are not placed in Common Attributes; they belong in [Private Key Attributes](private-key-attributes.md) or [Public Key Attributes](public-key-attributes.md) respectively. The division mirrors the physical structure of an asymmetric key pair: both halves share a common set of properties, while each half has properties unique to it.

When a server processes a request that contains a Common Attributes structure, it applies the attributes in it to all objects being created or managed in that context — for a Create Key Pair operation, both the private and public key objects receive the common attributes.

## Examples

A Create Key Pair request might include a Common Attributes structure holding Cryptographic Algorithm = RSA, Cryptographic Length = 2048, and a Name = `"MyKeyPair"`. Both the resulting private and public key objects will inherit these attribute values. The request would also carry Private Key Attributes and Public Key Attributes structures for any key-half-specific values.

## Related

[Attribute](attribute.md) · [Private Key Attributes](private-key-attributes.md) · [Public Key Attributes](public-key-attributes.md) · [Template Attribute Structures](template-attribute-structures.md) · [Object Type](../attributes/object-type.md) · [Cryptographic Algorithm](../attributes/cryptographic-algorithm.md)
