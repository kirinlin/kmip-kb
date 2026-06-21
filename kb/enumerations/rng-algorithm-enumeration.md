---
title: RNG Algorithm Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.2","1.3","1.4","2.0","2.1"]
source_section: "11.49"
status: reviewed
related: ["cryptographic-parameters", "drbg-algorithm-enumeration", "rng-mode-enumeration"]
keywords: ["RNG", "random number generator", "DRBG", "NRBG", "ANSI X9.31", "FIPS 186", "random generation", "4200DA", "RNGAlgorithm"]
tag_hex: "4200DA"
xml_text: "RNGAlgorithm"
tag_type: "Enumeration"
---

# RNG Algorithm Enumeration

## Overview

The RNG Algorithm enumeration identifies the algorithm or standard used by a random-number or deterministic random-bit generator. It is used in [Cryptographic Parameters](../attributes/cryptographic-parameters.md) when performing RNG-related operations (RNG Retrieve, RNG Seed) and in Query responses advertising the server's RNG capabilities. The enumeration distinguishes true random generators from deterministic ones and from algorithm-standard-specific instantiations.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Unspecified | `00000001` | `Unspecified` |  |
| FIPS 186-2 | `00000002` | `FIPS186_2` |  |
| DRBG | `00000003` | `DRBG` |  |
| NRBG | `00000004` | `NRBG` |  |
| ANSI X9.31 | `00000005` | `ANSIX9_31` |  |
| ANSI X9.62 | `00000006` | `ANSIX9_62` |  |

- **Unspecified**: The algorithm is not identified or is implementation-defined.
- **FIPS 186-2**: The DSA-based random-number generation method from FIPS 186-2. Largely superseded by SP 800-90A DRBGs.
- **DRBG**: A deterministic random bit generator, typically one of the SP 800-90A constructions (Hash_DRBG, HMAC_DRBG, CTR_DRBG). The specific DRBG construction is further identified by the [DRBG Algorithm Enumeration](drbg-algorithm-enumeration.md).
- **NRBG**: A non-deterministic (true) random bit generator seeded from physical entropy sources. Provides the highest randomness quality but may be slower.
- **ANSI X9.31**: The ANSI X9.31 RNG method for financial applications, based on 3DES or AES.
- **ANSI X9.62**: The ANSI X9.62 random-number generation method defined for ECDSA key generation.

## Examples

A server advertising its RNG capabilities in a Query response might list **NRBG** (hardware entropy) and **DRBG** (HMAC_DRBG seeded from the NRBG). An RNG Retrieve request for a session key seed specifies **DRBG** to get FIPS-approved deterministic output.

## Related

[Cryptographic Parameters](../attributes/cryptographic-parameters.md) · [DRBG Algorithm Enumeration](drbg-algorithm-enumeration.md) · [RNG Mode Enumeration](rng-mode-enumeration.md)
