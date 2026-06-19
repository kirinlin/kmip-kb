---
title: Public Key Attributes
category: structures
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "5.4"
status: reviewed
related: ["common-attributes", "private-key-attributes", "attribute", "template-attribute-structures", "create-key-pair", "public-key"]
keywords: ["public key attributes", "asymmetric key attributes", "key pair attributes", "public key specific", "attribute structure", "420128", "PublicKeyAttributes"]
tag_hex: "420128"
xml_text: "PublicKeyAttributes"
---

# Public Key Attributes

## Overview

Public Key Attributes is a structure encoding the attributes that apply specifically to the public key half of an asymmetric key pair. It parallels [Private Key Attributes](private-key-attributes.md) and both exist alongside [Common Attributes](common-attributes.md) in the §5 "Attribute Data Structures" group. The design ensures that shared properties go into Common Attributes while each key half carries its own distinct attributes in the appropriate typed structure.

Public Key Attributes appears in Create Key Pair requests and responses to carry public-key-specific attribute values independently of private-key values.

## Encoding (Tag / Type / Length / Value)

Public Key Attributes encodes as a Structure. It contains zero or more [Attribute](attribute.md) structures.

| Field | Tag | XML Text | Type | Required |
|---|---|---|---|---|
| Attribute | `420008` | `Attribute` | Structure | Zero or more |

An empty Public Key Attributes structure is valid and means no public-key-specific attributes are being specified in this payload.

## Fields & Structure

Each child Attribute follows the standard encoding with Attribute Name and Attribute Value. Attributes that belong here are those applicable exclusively or primarily to public key objects. Examples include:

- Public Key Unique Identifier — when the public key should have a specific identifier
- Name attributes specific to the public key (separate from the private key's name)
- Cryptographic Usage Mask values appropriate for public-key operations: Verify, Encrypt (for asymmetric encryption), Wrap Key, Certificate Sign, CRL Sign

Attributes meaningful for both key halves — Algorithm, Length, etc. — belong in [Common Attributes](common-attributes.md).

The server applies the values in this structure only to the public key object created by the operation. The paired private key receives values from [Private Key Attributes](private-key-attributes.md) and the shared Common Attributes.

## Examples

A Create Key Pair request for a TLS certificate CA key pair might carry Common Attributes (Algorithm = EC, Length = 384) plus Private Key Attributes (Usage Mask = Certificate Sign | CRL Sign, Name = `"ca-key-private"`) and Public Key Attributes (Usage Mask = Certificate Sign | CRL Sign, Name = `"ca-key-public"`). The two name attributes allow the key halves to be found independently by name while sharing the algorithm and length defaults.

## Related

[Common Attributes](common-attributes.md) · [Private Key Attributes](private-key-attributes.md) · [Attribute](attribute.md) · [Template Attribute Structures](template-attribute-structures.md) · [Create Key Pair](../operations/create-key-pair.md) · [Public Key](../objects/public-key.md)
