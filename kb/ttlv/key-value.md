---
title: Key Value
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "3.2"
v1_source_section: "2.1.4"
status: reviewed
related: ["key-block", "key-wrapping-data", "transparent-key-structures", "attribute"]
keywords: ["key value", "key material", "wrapped key", "encapsulated attributes"]
tag_hex: "420045"
xml_element: "KeyValue"
---

# Key Value

## Overview

The innermost payload of a [Key Block](key-block.md): the key material
itself, optionally bundled with attributes that travel (and get wrapped)
*with* the key. It appears in exactly one place — inside a Key Block — and
takes one of two shapes depending on whether the key is wrapped.

## Encoding (Tag / Type / Length / Value)

Tag `420045`. Two encodings:

- **Plaintext**: a Structure containing Key Material (`420043`) plus zero or
  more [Attribute](attribute.md) structures.
- **Wrapped**: a Byte String — the ciphertext of either the TTLV-encoded Key
  Value structure or the bare Key Material bytes, per the
  [Encoding Option](key-wrapping-data.md).

| Field | Tag | XML Element | Type | Required |
|---|---|---|---|---|
| Key Material | `420043` | `KeyMaterial` | Byte String for Raw/Opaque/PKCS#1/PKCS#8/ECPrivateKey formats; Structure for Transparent formats | Yes |
| Attribute | `420008` | `Attribute` | Structure | No; repeatable |

## Fields & Structure

The encapsulated attributes are the same attributes readable via
[Get Attributes](../operations/get-attributes.md) — the only difference is
that here they ride inside (and can be cryptographically bound to) the key
material. A [Key Wrapping Specification](key-wrapping-specification.md) lists
which attribute names to include when asking for a wrapped key; with the
No Encoding option, no attributes may be included at all (there is no
structure to put them in).

## Examples

A plaintext AES key: Key Value structure containing a 32-byte Key Material
byte string. The same key wrapped with AES key wrap, TTLV encoding option:
Key Value as one byte string whose plaintext is the TTLV encoding of that
structure.

## Related

[Key Block](key-block.md) · [Key Wrapping Data](key-wrapping-data.md) ·
[Transparent Key Structures](transparent-key-structures.md) ·
[Attribute](attribute.md)
