---
title: RNG Parameters
category: ttlv
spec_version: "1.4"
spec_versions: ["1.3", "1.4"]
source_section: "2.1.18"
status: draft
related: ["random-number-generator", "capability-information", "validation-information"]
keywords: ["RNG parameters", "DRBG", "NRBG", "prediction resistance", "randomness"]
---

# RNG Parameters

## Overview

A structured description of a random number generator, added in 1.3. Used in
two places: as the value of the
[Random Number Generator](../attributes/random-number-generator.md)
attribute (provenance of a key's randomness) and in
[Query](../operations/query.md) responses listing the RNGs an implementation
offers.

## Encoding (Tag / Type / Length / Value)

Structure, tag `4200D9`:

| Field | Tag | Type | Required |
|---|---|---|---|
| RNG Algorithm | `4200DA` | Enumeration | Yes — Unspecified, FIPS 186-2, DRBG, NRBG, ANSI X9.31, ANSI X9.62 |
| Cryptographic Algorithm | `420028` | Enumeration | No |
| Cryptographic Length | `42002A` | Integer | No |
| Hashing Algorithm | `420038` | Enumeration | No |
| DRBG Algorithm | `4200DB` | Enumeration | No — Hash, HMAC, CTR, Dual-EC, Unspecified |
| Recommended Curve | `420075` | Enumeration | No |
| FIPS186 Variation | `4200DC` | Enumeration | No |
| Prediction Resistance | `4200DD` | Boolean | No |

## Fields & Structure

Only the RNG Algorithm is mandatory; an implementation unwilling or unable to
disclose details uses `Unspecified` and stops there. The optional fields
describe the construction's building blocks — e.g. a CTR-DRBG over AES-256
fills in DRBG Algorithm = CTR, Cryptographic Algorithm = AES, Cryptographic
Length = 256. Several listed algorithm choices (Dual-EC, X9.31) are
historic and discouraged; they exist so legacy hardware can be described
honestly.

## Examples

A FIPS-validated appliance answers Query (RNGs) with RNG Parameters { RNG
Algorithm = DRBG, DRBG Algorithm = HMAC, Hashing Algorithm = SHA-256,
Prediction Resistance = True }.

## Related

[Random Number Generator attribute](../attributes/random-number-generator.md) ·
[Capability Information](capability-information.md) ·
[Query](../operations/query.md)
