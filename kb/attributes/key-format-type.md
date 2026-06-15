---
title: Key Format Type (Attribute)
category: attribute
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "4.26"
status: reviewed
related: ["cryptographic-algorithm", "cryptographic-length", "key-block", "symmetric-key", "public-key", "private-key"]
keywords: ["key format type", "key format", "raw", "pkcs1", "pkcs8", "transparent", "opaque key", "stored format"]
---

# Key Format Type (Attribute)

## Purpose

Key Format Type records the encoding format in which the key material is persisted on the server. This top-level attribute, introduced in v2.1, makes it possible to query or locate objects by their stored format without retrieving the key material itself. It is distinct from — but consistent with — the Key Format Type field embedded inside the [Key Block](../structures/key-block.md), which has existed since v1.0.

## Data Type & Structure

An Enumeration drawn from the Key Format Type enumeration. Representative values include Raw, Opaque, PKCS#1, PKCS#8, X.509, ECPrivateKey, TransparentSymmetricKey, TransparentDSAPrivateKey, TransparentDHPrivateKey, TransparentECPrivateKey, and their public-key counterparts. The exact value is determined by the format the server used when storing or accepting the key.

## Constraints

Single-instance. Read-only from the client perspective; the server sets it based on the format supplied at creation or import time. Changing the stored key format (e.g., converting from PKCS#8 to transparent) would require a new import or re-key operation, not a direct attribute update.

## Applies To (Object Types)

[Symmetric Key](../objects/symmetric-key.md), [Public Key](../objects/public-key.md), [Private Key](../objects/private-key.md), [Split Key](../objects/split-key.md), [Secret Data](../objects/secret-data.md).

## Set / Modified By

Set by the server at [Create](../operations/create.md), [Create Key Pair](../operations/create-key-pair.md), [Register](../operations/register.md), [Import](../operations/import.md), or [Derive Key](../operations/derive-key.md) time. Not directly modifiable by clients.

## Related Attributes

[Cryptographic Algorithm](cryptographic-algorithm.md) · [Cryptographic Length](cryptographic-length.md)
