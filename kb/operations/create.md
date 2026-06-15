---
title: Create
category: operation
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.8"
v1_source_section: "4.1"
status: reviewed
related: ["create-key-pair", "register", "derive-key", "get", "symmetric-key", "cryptographic-algorithm", "cryptographic-usage-mask"]
keywords: ["create", "symmetric key", "generate key", "provisioning", "key generation"]
---

# Create

## Purpose

`Create` asks the server to generate a brand-new symmetric key and place it
under management as a cryptographic object. It is the usual way to provision
freshly generated secret-key material when the client wants the server (rather
than the client) to produce the random key. Use [Register](register.md) instead
when the client already holds the key material, and [Create Key Pair](create-key-pair.md)
for asymmetric keys. `Create` is not used to build Template objects.

## Request Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Object Type | `420057` | `ObjectType` | Yes | The kind of object to generate — a [Symmetric Key](../objects/symmetric-key.md). |
| Template-Attribute | `420091` | `TemplateAttribute` | Yes | The attributes the new key should carry, given as individual attributes and/or by referencing server-side Template objects by name. Template objects have been deprecated since version 1.3, so attributes are better supplied individually. |

*Version note:* KMIP 2.0 replaced the Template-Attribute wrapper with the flat
[Attributes](../ttlv/template-attribute-structures.md) structure; the attribute
payload it carries is unchanged.

At minimum the request must convey a [Cryptographic Algorithm](../attributes/cryptographic-algorithm.md)
and a [Cryptographic Usage Mask](../attributes/cryptographic-usage-mask.md);
[Cryptographic Length](../attributes/cryptographic-length.md) is normally
supplied as well so the server knows the key size to generate.

## Response Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Object Type | `420057` | `ObjectType` | Yes | Echoes the type of object that was generated. |
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes | The server-assigned identifier for the new key, used to reference it in later operations. |
| Template-Attribute | `420091` | `TemplateAttribute` | No | Any attributes the server set on its own initiative that the client did not specify. |

## Behavior & Server Requirements

The server generates key material for the requested algorithm and length,
assigns a fresh [Unique Identifier](../attributes/unique-identifier.md), and
records the supplied attributes on the new object. It then writes that
identifier into the batch ID Placeholder, so a subsequent operation in the same
batch (for example a [Get](get.md)) can refer to the new key implicitly instead
of repeating the identifier. The new object normally starts in the Pre-Active
[state](../attributes/state.md) until it is activated or its activation date
arrives.

## Errors

`Create` follows the protocol's centralized [error handling](../concepts/error-handling.md).
Common failure causes include omitting a required attribute, supplying an
invalid or unsupported algorithm/length combination, providing a read-only or
otherwise invalid attribute, or lacking permission to create objects.

## Examples

Conceptually, a client requests "generate an AES-256 key usable for Encrypt and
Decrypt": Object Type = Symmetric Key, with Cryptographic Algorithm = AES,
Cryptographic Length = 256, and a Cryptographic Usage Mask selecting Encrypt and
Decrypt. The response returns the new key's Unique Identifier, which the client
then uses with [Activate](activate.md) and [Get](get.md).

## Related Operations

[Create Key Pair](create-key-pair.md) · [Register](register.md) ·
[Derive Key](derive-key.md) · [Activate](activate.md) · [Get](get.md)
