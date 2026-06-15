---
title: RNG Algorithm Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["1.2","1.3","1.4","2.0","2.1"]
source_section: "11.49"
status: reviewed
related: ["cryptographic-parameters", "drbg-algorithm-enumeration", "rng-mode-enumeration"]
keywords: ["RNG", "random number generator", "DRBG", "NRBG", "ANSI X9.31", "FIPS 186", "random generation"]
tag_hex: "4200DA"
xml_element: "RNGAlgorithm"
---

# RNG Algorithm Enumeration

## Overview

The RNG Algorithm enumeration identifies the algorithm or standard used by a random-number or deterministic random-bit generator. It is used in [Cryptographic Parameters](../../attributes/cryptographic-parameters.md) when performing RNG-related operations (RNG Retrieve, RNG Seed) and in Query responses advertising the server's RNG capabilities. The enumeration distinguishes true random generators from deterministic ones and from algorithm-standard-specific instantiations.

## Encoding (Tag / Type / Length / Value)

Encoded as a 4-byte integer (TTLV type `05`, Enumeration).

## Fields & Structure

- **Unspecified**: The algorithm is not identified or is implementation-defined.
- **FIPS 186-2**: The DSA-based random-number generation method from FIPS 186-2. Largely superseded by SP 800-90A DRBGs.
- **DRBG**: A deterministic random bit generator, typically one of the SP 800-90A constructions (Hash_DRBG, HMAC_DRBG, CTR_DRBG). The specific DRBG construction is further identified by the [DRBG Algorithm Enumeration](drbg-algorithm-enumeration.md).
- **NRBG**: A non-deterministic (true) random bit generator seeded from physical entropy sources. Provides the highest randomness quality but may be slower.
- **ANSI X9.31**: The ANSI X9.31 RNG method for financial applications, based on 3DES or AES.
- **ANSI X9.62**: The ANSI X9.62 random-number generation method defined for ECDSA key generation.

## Examples

A server advertising its RNG capabilities in a Query response might list **NRBG** (hardware entropy) and **DRBG** (HMAC_DRBG seeded from the NRBG). An RNG Retrieve request for a session key seed specifies **DRBG** to get FIPS-approved deterministic output.

## Related

[Cryptographic Parameters](../../attributes/cryptographic-parameters.md) · [DRBG Algorithm Enumeration](drbg-algorithm-enumeration.md) · [RNG Mode Enumeration](rng-mode-enumeration.md)
