---
title: RNG Parameters
category: structures
spec_version: "2.1"
spec_versions: ["1.3", "1.4", "2.0", "2.1"]
source_section: "7.36"
v1_source_section: "2.1.18"
status: reviewed
related: ["random-number-generator", "capability-information", "validation-information"]
keywords: ["RNG parameters", "DRBG", "NRBG", "prediction resistance", "randomness", "4200D9", "RNGParameters"]
tag_hex: "4200D9"
xml_text: "RNGParameters"
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

| Field | Tag | XML Text | Type | Required |
|---|---|---|---|---|
| RNG Algorithm | `4200DA` | `RNGAlgorithm` | Enumeration | Yes — Unspecified, FIPS 186-2, DRBG, NRBG, ANSI X9.31, ANSI X9.62 |
| Cryptographic Algorithm | `420028` | `CryptographicAlgorithm` | Enumeration | No |
| Cryptographic Length | `42002A` | `CryptographicLength` | Integer | No |
| Hashing Algorithm | `420038` | `HashingAlgorithm` | Enumeration | No |
| DRBG Algorithm | `4200DB` | `DRBGAlgorithm` | Enumeration | No — Hash, HMAC, CTR, Dual-EC, Unspecified |
| Recommended Curve | `420075` | `RecommendedCurve` | Enumeration | No |
| FIPS186 Variation | `4200DC` | `FIPS186Variation` | Enumeration | No |
| Prediction Resistance | `4200DD` | `PredictionResistance` | Boolean | No |

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
