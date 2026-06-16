---
title: Key Format Type (Attribute)
category: attribute
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "4.26"
tag_hex: "420042"
xml_text: "KeyFormatType"
status: reviewed
related: ["cryptographic-algorithm", "cryptographic-length", "key-block", "symmetric-key", "public-key", "private-key"]
keywords: ["key format type", "key format", "raw", "pkcs1", "pkcs8", "transparent", "opaque key", "stored format", "420042", "KeyFormatType"]
---

# Key Format Type (Attribute)

## Purpose

Key Format Type records the encoding format in which the key material is persisted on the server. This top-level attribute, introduced in v2.1, makes it possible to query or locate objects by their stored format without retrieving the key material itself. It is distinct from — but consistent with — the Key Format Type field embedded inside the [Key Block](../structures/key-block.md), which has existed since v1.0.

## Data Type & Structure

| Field | Tag | XML Element | Type |
|---|---|---|---|
| Key Format Type | `420042` | `KeyFormatType` | Enumeration — [Key Format Type Enumeration](../enumerations/key-format-type-enumeration.md) |

Values include Raw, Opaque, PKCS#1, PKCS#8, PKCS#10, PKCS#12, X.509, ECPrivateKey, TransparentSymmetricKey, TransparentDSAPrivateKey, TransparentDSAPublicKey, TransparentDHPrivateKey, TransparentDHPublicKey, TransparentECPrivateKey, TransparentECPublicKey, TransparentRSAPrivateKey, TransparentRSAPublicKey, and vendor Extension types. The value reflects the format in which the key material is actually stored or was supplied.

## Attribute Rules

| Rule | Value |
|---|---|
| SHALL always have a value | Yes |
| Initially set by | Server |
| Modifiable by server | No |
| Modifiable by client | No |
| Deletable by client | No |
| Multiple instances permitted | No |
| Applies to Object Types | All Objects |

The client may _request_ a particular format on operations where the server generates key material ([Create](../operations/create.md), [Create Key Pair](../operations/create-key-pair.md), [Create Split Key](../operations/create-split-key.md), [Re-key](../operations/re-key.md), [Derive Key](../operations/derive-key.md)). If specified, the server must honour the request or fail the operation. On [Register](../operations/register.md) or [Import](../operations/import.md), the value is inferred from the supplied key material; it cannot be overridden by the client after creation.

## Default Key Format Type by Object

When the client does not request a specific format, the server stores the object in its default Key Format Type:

| Object | Default Key Format Type |
|---|---|
| Certificate | X.509 |
| Certificate Request | PKCS#10 |
| Opaque Object | Opaque |
| PGP Key | Raw |
| Secret Data | Raw |
| Symmetric Key | Raw |
| Split Key | Raw |
| RSA Private Key | PKCS#1 |
| RSA Public Key | PKCS#1 |
| EC Private Key | Transparent EC Private Key |
| EC Public Key | Transparent EC Public Key |
| DSA Private Key | Transparent DSA Private Key |
| DSA Public Key | Transparent DSA Public Key |

## Digest Interaction

When the server computes a [Digest](digest.md) for an object, it calculates the digest over the data in the assigned Key Format Type. If the assigned format differs from the KMIP default for that object type and algorithm, the server additionally computes a digest in the default format, so both are stored.

## Related Attributes

[Cryptographic Algorithm](cryptographic-algorithm.md) · [Cryptographic Length](cryptographic-length.md) · [Digest](digest.md)
