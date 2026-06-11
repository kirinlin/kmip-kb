---
title: Cryptographic Length of Asymmetric Keys
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.20"
status: draft
related: ["private-key", "public-key"]
keywords: ["Cryptographic Length", "RSA", "key length", "modulus", "asymmetric", "key size"]
---

# Cryptographic Length of Asymmetric Keys

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

For asymmetric keys, the KMIP Cryptographic Length attribute records the length of the key's defining parameter (such as the RSA modulus), not the total size of all the mathematical components that make up the full key structure. Implementations must not infer actual memory or storage requirements from this value alone.

## Guidance

For RSA, Cryptographic Length records the size of the modulus in bits. The full RSA public key includes both the modulus and the public exponent; the full private key includes the modulus, public exponent, private exponent, two primes, and three additional derived values — all encoded, typically in ASN.1/DER. The total encoded length is significantly larger than 2048 bits even for a 2048-bit RSA key.

For elliptic curve keys, the Cryptographic Length refers to the bit length of the curve's field prime or order, not the full encoded point coordinates.

## Implementation Notes

Implementations that allocate buffers or plan serialisation based on key length must account for the full encoding overhead of the key format in use (raw, PKCS#8, X.509 SubjectPublicKeyInfo, etc.). Using Cryptographic Length directly as a buffer size for asymmetric key material is a common implementation bug that can cause buffer overflows or truncation.

## Related Concepts

See [Private Key](../objects/private-key.md) and [Public Key](../objects/public-key.md) for the full key object structures.
