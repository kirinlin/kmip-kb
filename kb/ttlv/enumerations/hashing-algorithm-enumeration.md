---
title: Hashing Algorithm Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.21"
status: reviewed
related: ["cryptographic-parameters", "derivation-parameters", "digest", "digital-signature-algorithm-enumeration", "drbg-algorithm-enumeration"]
keywords: ["hash", "SHA", "SHA-256", "SHA-3", "MD5", "RIPEMD", "Whirlpool", "hashing algorithm", "digest", "message digest"]
tag_hex: "420038"
xml_element: "HashingAlgorithm"
---

# Hashing Algorithm Enumeration

## Overview

The Hashing Algorithm enumeration identifies the cryptographic hash function to use in contexts that require a digest — for example, the underlying hash for HMAC-based key derivation, the hash used in signature algorithms, the algorithm used to compute the [Digest attribute](../../attributes/digest.md), or the hash component of Derivation Parameters. It spans a broad range of hash families from legacy algorithms (MD2, MD4, MD5, SHA-1) still needed for backward compatibility, through the current SHA-2 and SHA-3 families, to international standard hashes from Russia and other jurisdictions.

## Encoding (Tag / Type / Length / Value)

Encoded as a 4-byte integer (TTLV type `05`, Enumeration). Appears in Cryptographic Parameters, Derivation Parameters, Digest attribute structures, and anywhere else a hash function must be identified.

## Fields & Structure

**Legacy algorithms (avoid for new designs):**
- **MD2**: Produces a 128-bit digest. Considered broken; included for legacy interoperability only.
- **MD4**: Produces a 128-bit digest. Also broken; predecessor to MD5.
- **MD5**: 128-bit digest. Widely deployed but vulnerable to collision attacks; acceptable only for non-security-critical checksums or legacy MAC schemes.
- **SHA-1**: 160-bit digest. Deprecated for digital signatures and certificates; retained for legacy TLS and older code-signing workflows.

**SHA-2 family (widely recommended):**
- **SHA-224**: 224-bit truncated variant of SHA-256.
- **SHA-256**: The most widely deployed hash today; 256-bit output; the baseline choice for new designs.
- **SHA-384**: 384-bit output; truncated variant of SHA-512; used in ECDSA-384 and higher-assurance applications.
- **SHA-512**: 512-bit output; the highest-strength SHA-2 variant for symmetric-equivalent 256-bit security.
- **SHA-512/224** / **SHA-512/256**: SHA-512 with truncated outputs, providing the same performance as SHA-512 with shorter digests.

**SHA-3 family (Keccak-based, FIPS 202):**
- **SHA-3-224** / **SHA-3-256** / **SHA-3-384** / **SHA-3-512**: The SHA-3 standardised hash functions. Structurally different from SHA-2 (sponge construction), providing an independent security hedge.

**Other algorithms:**
- **RIPEMD-160**: A 160-bit hash from Europe, used in Bitcoin address derivation and some legacy TLS deployments.
- **Tiger**: A 192-bit hash designed for 64-bit platforms; used in some P2P and older network protocols.
- **Whirlpool**: A 512-bit Miyaguchi-Preneel hash recommended by NESSIE; used in some high-security European applications.
- **GOSTR3411-94**: The original Russian GOST hash standard, producing a 256-bit digest.
- **GOSTR3411-2012-256** / **GOSTR3411-2012-512**: The updated Streebog hash function from GOST R 34.11-2012, providing 256- or 512-bit outputs. Mandatory in Russian government systems.

## Examples

A Derive Key request using HKDF for TLS key material would specify **SHA-256** as the Hashing Algorithm. A KMIP server computing the Digest attribute of a certificate for lookup purposes would use **SHA-256** or **SHA-384**. A government-regulated system in Russia would use **GOSTR3411-2012-256** wherever a hash is required.

## Related

- [Cryptographic Parameters](../../attributes/cryptographic-parameters.md) — uses this enumeration to specify the hash in HMAC and signature operations
- [Derivation Parameters structure](../../structures/derivation-parameters.md) — specifies the hash for key derivation
- [Digest attribute](../../attributes/digest.md) — stores a hash of the object, recording which algorithm was used
- [Digital Signature Algorithm Enumeration](digital-signature-algorithm-enumeration.md) — compound algorithm that names the hash alongside the signature primitive
- [DRBG Algorithm Enumeration](drbg-algorithm-enumeration.md) — Hash and HMAC DRBGs require specifying a hash algorithm
