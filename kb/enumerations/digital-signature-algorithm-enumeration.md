---
title: Digital Signature Algorithm Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.16"
status: reviewed
related: ["cryptographic-algorithm-enumeration", "hashing-algorithm-enumeration", "certify", "digest"]
keywords: ["digital signature", "signature algorithm", "RSA", "ECDSA", "DSA", "EdDSA", "HMAC", "signing", "4200AE", "DigitalSignatureAlgorithm"]
tag_hex: "4200AE"
xml_text: "DigitalSignatureAlgorithm"
tag_type: "Enumeration"
---

# Digital Signature Algorithm Enumeration

## Overview

The Digital Signature Algorithm enumeration identifies the full signature algorithm as a combined hash-plus-key-algorithm pairing. While the [Cryptographic Algorithm Enumeration](cryptographic-algorithm-enumeration.md) names the underlying key type (RSA, EC, DSA) and the [Hashing Algorithm Enumeration](hashing-algorithm-enumeration.md) names the hash, some contexts — particularly certificate attributes and signature verification operations — require the compound identifier that ties the two together in a single value. This enumeration follows the convention used in X.509 certificate `signatureAlgorithm` OIDs, where the hash and signature primitive are named as a unit.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| MD2 with RSA Encryption | `00000001` | `MD2WithRSAEncryption` |  |
| MD5 with RSA Encryption | `00000002` | `MD5WithRSAEncryption` |  |
| SHA-1 with RSA Encryption | `00000003` | `SHA_1WithRSAEncryption` |  |
| SHA-224 with RSA Encryption | `00000004` | `SHA_224WithRSAEncryption` |  |
| SHA-256 with RSA Encryption | `00000005` | `SHA_256WithRSAEncryption` |  |
| SHA-384 with RSA Encryption | `00000006` | `SHA_384WithRSAEncryption` |  |
| SHA-512 with RSA Encryption | `00000007` | `SHA_512WithRSAEncryption` |  |
| RSASSA-PSS | `00000008` | `RSASSA_PSS` |  |
| DSA with SHA-1 | `00000009` | `DSAWithSHA_1` |  |
| DSA with SHA224 | `0000000A` | `DSAWithSHA224` |  |
| DSA with SHA256 | `0000000B` | `DSAWithSHA256` |  |
| ECDSA with SHA-1 | `0000000C` | `ECDSAWithSHA_1` |  |
| ECDSA with SHA224 | `0000000D` | `ECDSAWithSHA224` |  |
| ECDSA with SHA256 | `0000000E` | `ECDSAWithSHA256` |  |
| ECDSA with SHA384 | `0000000F` | `ECDSAWithSHA384` |  |
| ECDSA with SHA512 | `00000010` | `ECDSAWithSHA512` |  |
| SHA3-256 with RSA Encryption | `00000011` | `SHA3_256WithRSAEncryption` |  |
| SHA3-384 with RSA Encryption | `00000012` | `SHA3_384WithRSAEncryption` |  |
| SHA3-512 with RSA Encryption | `00000013` | `SHA3_512WithRSAEncryption` |  |

## Examples

When registering a TLS certificate in KMIP, the certificate's `signatureAlgorithm` field maps to **SHA-256 with RSA** or **SHA-256 with ECDSA** for a typical modern CA. An HSM that performs code signing for firmware images would use **SHA-384 with ECDSA** to match the platform's security requirements.

## Related

- [Cryptographic Algorithm Enumeration](cryptographic-algorithm-enumeration.md) — the underlying key algorithm
- [Hashing Algorithm Enumeration](hashing-algorithm-enumeration.md) — the hash function component
- [Certify operation](../operations/certify.md) — signs a CSR, producing a certificate with this signature algorithm
- [Digest attribute](../attributes/digest.md) — stores a hash of the object, often using algorithms from this set
