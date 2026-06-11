---
title: Key Value Present
category: attribute
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.28"
v1_source_section: "3.41"
status: draft
related: ["key-value-location", "digest", "fresh"]
keywords: ["key value present", "metadata-only registration", "key value absent", "registry"]
tag_hex: "4200BB"
xml_element: "KeyValuePresent"
---

# Key Value Present

## Purpose

Marks an object that was registered *without* its key material. KMIP 1.2
allowed [Register](../operations/register.md) to omit the
[Key Value](../ttlv/key-value.md) from the [Key Block](../ttlv/key-block.md),
so a server can act as a pure metadata registry for keys stored elsewhere
(an HSM, a tape silo). This attribute is how that condition is recorded and
queried.

## Data Type & Structure

A Boolean. Slightly counter-intuitively, the server creates the attribute
when the key value is **absent** at registration; an ordinary object with
material typically has no instance of this attribute at all.

## Constraints

- Optional; single instance; entirely server-managed — clients must not
  supply it in Register, and neither side ever modifies or deletes it.
- Usable as a [Locate](../operations/locate.md) predicate to find
  metadata-only objects.
- A [Get](../operations/get.md) on such an object fails with the
  `Key Value Not Present` result reason (added alongside this attribute).

## Applies To (Object Types)

Symmetric keys, private keys, split keys, and secret data — the types whose
key block can meaningfully omit material. Not certificates, public keys,
opaque objects, or templates.

## Set / Modified By

Server only, implicitly during [Register](../operations/register.md).

## Related Attributes

[Key Value Location](key-value-location.md) · [Digest](digest.md) ·
[Fresh](fresh.md)
