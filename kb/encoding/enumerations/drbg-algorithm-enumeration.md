---
title: DRBG Algorithm Enumeration
category: encoding
spec_version: "2.1"
spec_versions: ["1.2","1.3","1.4","2.0","2.1"]
source_section: "11.17"
status: reviewed
related: ["cryptographic-parameters", "rng-algorithm-enumeration", "rng-mode-enumeration", "hashing-algorithm-enumeration"]
keywords: ["DRBG", "deterministic random", "NIST SP 800-90A", "random number generator", "Dual-EC", "Hash DRBG", "HMAC DRBG", "CTR DRBG", "4200DB", "DRBGAlgorithm"]
tag_hex: "4200DB"
xml_text: "DRBGAlgorithm"
---

# DRBG Algorithm Enumeration

## Overview

The DRBG Algorithm enumeration identifies the specific deterministic random bit generator construction used when the server is generating random numbers or key material. NIST SP 800-90A defines several approved DRBG mechanisms, each with different performance, security, and hardware-implementation characteristics. The choice of DRBG algorithm matters both for compliance with specific security standards and for interoperability with systems that require a particular random source. This enumeration appears in the Cryptographic Parameters structure when the operation involves random number generation.

## Fields & Structure

| Value | Hex | XML Text | Description |
|---|---|---|---|
| Unspecified | `0x00000001` | `Unspecified` |  |
| Dual-EC | `0x00000002` | `Dual_EC` |  |
| Hash | `0x00000003` | `Hash` |  |
| HMAC | `0x00000004` | `HMAC` |  |
| CTR | `0x00000005` | `CTR` |  |

- **Unspecified**: The DRBG algorithm is not specified by the client; the server selects a suitable approved algorithm according to its policy.
- **Dual-EC**: The Dual Elliptic Curve DRBG defined in early NIST SP 800-90A. This algorithm attracted significant scrutiny due to a potential backdoor in the standardised curve parameters; it is generally avoided in new implementations, though it remains enumerated for completeness.
- **Hash**: The Hash DRBG construction, which uses a cryptographic hash function as its underlying primitive. Straightforward to implement and widely approved.
- **HMAC**: The HMAC DRBG construction, which uses HMAC over a specified hash function. Considered the most commonly recommended DRBG because of its clean security proof and resistance to related-key attacks.
- **CTR**: The CTR DRBG construction, which uses a block cipher in counter mode (typically AES-CTR) as its underlying primitive. Highly efficient in hardware and widely used in HSMs.

## Examples

An HSM implementing FIPS 140-3 would typically use **CTR** DRBG with AES-256 for key generation, as AES-CTR DRBG is well-tested in hardware and achieves the highest throughput. A software-only KMIP server might prefer **HMAC** DRBG with SHA-256 for its clean security properties and ease of implementation.

## Related

- [Cryptographic Parameters](../../attributes/cryptographic-parameters.md) — the structure that carries this enumeration
- [RNG Algorithm Enumeration](rng-algorithm-enumeration.md) — broader RNG algorithm classification
- [RNG Mode Enumeration](rng-mode-enumeration.md) — specifies the operating mode of the random number generator
- [Hashing Algorithm Enumeration](hashing-algorithm-enumeration.md) — specifies the underlying hash for Hash and HMAC DRBG
