---
title: Digest
category: attribute
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4"]
source_section: "3.17"
status: draft
related: ["unique-identifier", "key-value-present", "digital-signature-algorithm"]
keywords: ["digest", "hash", "SHA-256", "fingerprint", "key material integrity"]
---

# Digest

## Purpose

A server-computed fingerprint of the object's actual material — the key
bytes, certificate value, secret data, or opaque payload. Clients use it to
verify that retrieved material is intact, to deduplicate, or to match a key
held locally against one on the server without fetching it.

## Data Type & Structure

A structure:

| Field | Type | Required |
|---|---|---|
| Hashing Algorithm | Enumeration | Yes |
| Digest Value | Byte String | Yes, when the server has the material (or was given the digest out of band) |
| Key Format Type | Enumeration | Yes for keys and secret data — the format the digested bytes were in |

What gets hashed: the raw Key Material byte string, or — when the material is
a transparent structure — its TTLV encoding; for certificates the
Certificate Value; for opaque objects the Opaque Data Value.

## Constraints

- Multi-instance: additional digests may exist for other hash algorithms or
  key formats, but one instance computed with **SHA-256 is mandatory**
  whenever the attribute exists at all.
- For client-registered objects the mandatory instance uses the registered
  Key Format Type; for server-generated objects the server picks any format
  it can also serve the object in.
- Static once computed; read-only for everyone; not deletable.

## Applies To (Object Types)

All cryptographic objects, plus opaque objects.

## Set / Modified By

Server-set, implicitly, whenever an object with accessible material is
created or registered: [Create](../operations/create.md),
[Create Key Pair](../operations/create-key-pair.md),
[Register](../operations/register.md),
[Derive Key](../operations/derive-key.md),
[Certify](../operations/certify.md) /
[Re-certify](../operations/re-certify.md),
[Re-key](../operations/re-key.md) /
[Re-key Key Pair](../operations/re-key-key-pair.md). If the server never
sees the material (registered without a key value), the digest may be absent.

## Related Attributes

[Key Value Present](key-value-present.md) ·
[Digital Signature Algorithm](digital-signature-algorithm.md) ·
[Unique Identifier](unique-identifier.md)
