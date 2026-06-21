---
title: Private Key Attributes
category: structures
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "5.3"
status: reviewed
related: ["common-attributes", "public-key-attributes", "attribute", "template-attribute-structures", "create-key-pair", "private-key"]
keywords: ["private key attributes", "asymmetric key attributes", "key pair attributes", "private key specific", "attribute structure", "420127", "PrivateKeyAttributes"]
tag_hex: "420127"
xml_text: "PrivateKeyAttributes"
tag_type: "Structure"
---

# Private Key Attributes

## Overview

Private Key Attributes is a structure encoding the attributes that apply specifically to the private key half of an asymmetric key pair. It exists alongside [Common Attributes](common-attributes.md) and [Public Key Attributes](public-key-attributes.md) in the §5 "Attribute Data Structures" group. The separation ensures that attributes shared by both key halves go into Common Attributes, while private-key-specific properties are kept in this structure.

Private Key Attributes appears in Create Key Pair requests and responses to carry private-key-specific attribute values without conflating them with public-key values.

## Encoding (Tag / Type / Length / Value)

Private Key Attributes encodes as a Structure. It contains zero or more [Attribute](attribute.md) structures.

| Field | Tag | XML Text | Type | Required |
|---|---|---|---|---|
| Attribute | `420008` | `Attribute` | Structure | Zero or more |

An empty Private Key Attributes structure is valid and means no private-key-specific attributes are being specified in this payload.

## Fields & Structure

Each child Attribute follows the standard encoding with Attribute Name and Attribute Value. Attributes that belong here are those defined in the spec as applying exclusively or primarily to private key objects. Examples may include:

- Private Key Unique Identifier — when the private key needs a specific identifier distinct from the auto-generated one
- Name attributes specific to the private key
- Cryptographic Usage Mask values restricted to private-key operations (Sign, Decrypt, Unwrap Key, Key Agreement)

Attributes that are meaningful for both key halves — such as Cryptographic Algorithm or Cryptographic Length — belong in [Common Attributes](common-attributes.md) rather than here.

The server applies the values in this structure only to the private key object created by the operation. The paired public key object receives values from [Public Key Attributes](public-key-attributes.md) and the shared Common Attributes.

## Examples

A Create Key Pair request for an RSA signing key pair might carry Common Attributes (Algorithm = RSA, Length = 3072) plus Private Key Attributes containing a Cryptographic Usage Mask = Sign and a Name = `"signing-key-private"`. The Public Key Attributes structure would carry a separate Cryptographic Usage Mask = Verify and Name = `"signing-key-public"`.

## Related

[Common Attributes](common-attributes.md) · [Public Key Attributes](public-key-attributes.md) · [Attribute](attribute.md) · [Template Attribute Structures](template-attribute-structures.md) · [Create Key Pair](../operations/create-key-pair.md) · [Private Key](../objects/private-key.md)
