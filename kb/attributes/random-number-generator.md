---
title: Random Number Generator
category: attribute
spec_version: "2.1"
spec_versions: ["1.3", "1.4", "2.0", "2.1"]
source_section: "4.46"
v1_source_section: "3.44"
status: reviewed
related: ["original-creation-date", "cryptographic-algorithm", "rng-parameters"]
keywords: ["random number generator", "RNG", "DRBG", "entropy provenance", "FIPS", "4200DE", "RandomNumberGenerator"]
tag_hex: "4200DE"
xml_text: "RandomNumberGenerator"
---

# Random Number Generator

## Purpose

Provenance for the randomness behind a key: which RNG produced it. Added in
1.3 for compliance regimes that care whether key material came from an
approved DRBG. Clients can also use it prescriptively — requesting that a
key be generated only by an RNG matching given parameters.

## Data Type & Structure

The value is an [RNG Parameters](../structures/rng-parameters.md) structure: a
mandatory RNG Algorithm (Unspecified, FIPS 186-2, DRBG, NRBG, ANSI X9.31,
ANSI X9.62) plus optional detail — cryptographic algorithm and length,
hashing algorithm, DRBG flavor (Hash/HMAC/CTR/Dual-EC), recommended curve,
FIPS 186 variation, and a prediction-resistance flag.

## Constraints

- Mandatory (server-set) for server-generated objects; if the server cannot
  or will not disclose details, it must still set the attribute with RNG
  Algorithm = Unspecified.
- Optional (client-set) for registered objects, at Register time or later
  via [Add Attribute](../operations/add-attribute.md).
- If a create-style request carries one or more Random Number Generator
  values among its requested attributes, the server must generate with a
  matching RNG or fail the request.
- Single instance; immutable and not deletable once set; never copied to a
  re-keyed successor (which gets its own provenance).

## Applies To (Object Types)

All cryptographic objects.

## Set / Modified By

Server (generated objects) or client (registered objects); implicitly set by
[Create](../operations/create.md),
[Create Key Pair](../operations/create-key-pair.md),
[Derive Key](../operations/derive-key.md),
[Re-key](../operations/re-key.md),
[Re-key Key Pair](../operations/re-key-key-pair.md).

## Related Attributes

[Original Creation Date](original-creation-date.md) ·
[Cryptographic Algorithm](cryptographic-algorithm.md)
