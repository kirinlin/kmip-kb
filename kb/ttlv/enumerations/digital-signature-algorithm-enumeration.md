---
title: Digital Signature Algorithm Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.16"
status: reviewed
related: ["cryptographic-algorithm-enumeration", "hashing-algorithm-enumeration", "certify", "digest"]
keywords: ["digital signature", "signature algorithm", "RSA", "ECDSA", "DSA", "EdDSA", "HMAC", "signing"]
tag_hex: "4200AE"
xml_element: "DigitalSignatureAlgorithm"
---

# Digital Signature Algorithm Enumeration

## Overview

The Digital Signature Algorithm enumeration identifies the full signature algorithm as a combined hash-plus-key-algorithm pairing. While the [Cryptographic Algorithm Enumeration](cryptographic-algorithm-enumeration.md) names the underlying key type (RSA, EC, DSA) and the [Hashing Algorithm Enumeration](hashing-algorithm-enumeration.md) names the hash, some contexts — particularly certificate attributes and signature verification operations — require the compound identifier that ties the two together in a single value. This enumeration follows the convention used in X.509 certificate `signatureAlgorithm` OIDs, where the hash and signature primitive are named as a unit.

## Encoding (Tag / Type / Length / Value)

Encoded as a 4-byte integer (TTLV type `05`, Enumeration). Used in certificate structures, the Digital Signature Algorithm attribute, and cryptographic operation parameters where the combined algorithm must be specified unambiguously.

## Fields & Structure

**RSA-based signature algorithms:**
- **MD2 with RSA**: RSA signature with MD2 hash. Historically used in early TLS certificates; considered broken and no longer acceptable.
- **MD5 with RSA**: RSA signature with MD5 hash. Also considered insecure for certificate signing due to MD5 collision attacks.
- **SHA-1 with RSA**: RSA signature with SHA-1. Legacy; deprecated for certificate signing by most CAs and browsers.
- **SHA-224 with RSA** / **SHA-256 with RSA** / **SHA-384 with RSA** / **SHA-512 with RSA**: The current family of RSA signature algorithms. SHA-256 with RSA is the dominant choice for TLS certificates and code signing today.

**ECDSA-based signature algorithms:**
- **SHA-1 with ECDSA**: Legacy EC signature; retained for compatibility only.
- **SHA-224 with ECDSA** / **SHA-256 with ECDSA** / **SHA-384 with ECDSA** / **SHA-512 with ECDSA**: The recommended ECDSA suite. SHA-256 with ECDSA over P-256 is the most widely deployed.

**DSA-based signature algorithms:**
- **SHA-1 with DSA**: Legacy DSA signature over finite fields.
- **SHA-224 with DSA** / **SHA-256 with DSA**: Current DSA variants, used primarily in FIPS-compliant environments.

**Modern algorithms:**
- **EdDSA**: Edwards-curve Digital Signature Algorithm (Ed25519 or Ed448). No separate hash specification needed — the curve determines the hash internally.

**HMAC-based algorithms:**
- HMAC variants (e.g., HMAC-SHA-1, HMAC-SHA-256): Used in contexts where a shared-key MAC is treated as a signature-like authentication code.

## Examples

When registering a TLS certificate in KMIP, the certificate's `signatureAlgorithm` field maps to **SHA-256 with RSA** or **SHA-256 with ECDSA** for a typical modern CA. An HSM that performs code signing for firmware images would use **SHA-384 with ECDSA** to match the platform's security requirements.

## Related

- [Cryptographic Algorithm Enumeration](cryptographic-algorithm-enumeration.md) — the underlying key algorithm
- [Hashing Algorithm Enumeration](hashing-algorithm-enumeration.md) — the hash function component
- [Certify operation](../../operations/certify.md) — signs a CSR, producing a certificate with this signature algorithm
- [Digest attribute](../../attributes/digest.md) — stores a hash of the object, often using algorithms from this set
