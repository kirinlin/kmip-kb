---
title: RNG Mode Enumeration
category: encoding
spec_version: "2.1"
spec_versions: ["1.2","1.3","1.4","2.0","2.1"]
source_section: "11.50"
status: reviewed
related: ["cryptographic-parameters", "rng-algorithm-enumeration", "drbg-algorithm-enumeration"]
keywords: ["RNG mode", "prediction resistance", "reseeding", "non-reseeding", "random generation mode", "4200F5", "RNGMode"]
tag_hex: "4200F5"
xml_text: "RNGMode"
---

# RNG Mode Enumeration

## Overview

The RNG Mode enumeration controls the reseeding and prediction-resistance behaviour of a deterministic random bit generator (DRBG) as defined in NIST SP 800-90A. It is carried in [Cryptographic Parameters](../../attributes/cryptographic-parameters.md) alongside the [RNG Algorithm](rng-algorithm-enumeration.md) to fully specify how the RNG should operate when a security requirement calls for prediction resistance or controlled reseeding.

## Fields & Structure

| Value | Hex | XML Text | Description |
|---|---|---|---|
| Unspecified | `0x00000001` | `Unspecified` |  |
| Shared Instantiation | `0x00000002` | `SharedInstantiation` |  |
| Non-Shared Instantiation | `0x00000003` | `NonSharedInstantiation` |  |

- **Unspecified**: The mode is not constrained; the server uses its default reseeding policy.
- **Non-Reseeding**: The DRBG is instantiated without reseeding support. The internal state evolves from its initial seed without injecting additional entropy. Suitable when the seed is trusted and state exhaustion is not a concern.
- **Prediction Resistance**: Fresh entropy is injected before every generate call, ensuring that even if the internal state were compromised at time T, outputs before T are still unpredictable. Required for the highest-security applications.
- **Reseeding**: The DRBG is reseeded periodically (after a defined number of generate calls or by explicit request) but not for every individual call. A balance between performance and forward security.

## Examples

A key-generation service that must comply with FIPS 140-2 Level 3 requirements and cannot tolerate state compromise specifies **Prediction Resistance** in its Cryptographic Parameters for RNG operations. A batch key-generation job that generates thousands of keys rapidly might use **Reseeding** to amortise entropy-injection overhead.

## Related

[Cryptographic Parameters](../../attributes/cryptographic-parameters.md) · [RNG Algorithm Enumeration](rng-algorithm-enumeration.md) · [DRBG Algorithm Enumeration](drbg-algorithm-enumeration.md)
