---
title: Cryptographic Algorithm Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.12"
status: reviewed
related: ["cryptographic-algorithm", "cryptographic-length", "cryptographic-parameters", "key-block", "derive-key", "create", "create-key-pair"]
keywords: ["algorithm", "AES", "RSA", "ECDSA", "ECDH", "Ed25519", "3DES", "ChaCha20", "symmetric key", "asymmetric key", "cryptographic algorithm"]
tag_hex: "420028"
xml_element: "CryptographicAlgorithm"
---

# Cryptographic Algorithm Enumeration

## Overview

The Cryptographic Algorithm enumeration identifies the algorithm associated with a managed key or applied during a cryptographic operation. It is one of the most pervasive enumerations in KMIP, appearing in the [Cryptographic Algorithm attribute](../../attributes/cryptographic-algorithm.md), in [Key Block](../../structures/key-block.md) structures, in [Derivation Parameters](../../structures/derivation-parameters.md), and in operation request structures whenever the caller needs to name the algorithm. The enumeration spans the full spectrum of symmetric ciphers, asymmetric algorithms, elliptic curves, and MAC algorithms defined across the KMIP version history.

## Encoding (Tag / Type / Length / Value)

Encoded as a 4-byte integer (TTLV type `05`, Enumeration). Appears wherever an algorithm identifier is required in request or response structures.

## Fields & Structure

**Symmetric block ciphers:**
- **AES** (Advanced Encryption Standard): The dominant symmetric cipher for enterprise key management. Paired with a key length of 128, 192, or 256 bits and a block cipher mode.
- **3DES** (Triple DES, also TDEA): A legacy symmetric cipher applying DES three times for a security level of 112 effective bits. Still found in payment systems but deprecated for new designs.
- **DES**: Single DES, retained for legacy interoperability only. Considered cryptographically broken for data protection.
- **Blowfish**: A variable-key-length block cipher used in some legacy applications and VPNs.
- **Camellia**: A 128-bit block cipher from NTT and Mitsubishi, widely used in Japan and standardised by ISO/IEC.
- **IDEA**: An older 64-bit block cipher, mostly of historical interest.
- **RC2**, **RC4**, **RC5**, **RC6**: RSA Security cipher family; RC4 is a stream cipher. All are largely deprecated for modern use.
- **SEED**: A Korean national standard 128-bit block cipher.
- **ARIA**: Another Korean standard block cipher, an AES finalist.
- **SM4**: A Chinese national standard 128-bit block cipher (also called SMS4).

**Stream and authenticated ciphers:**
- **ChaCha20**: A modern stream cipher widely deployed in TLS 1.3 combined with Poly1305 for AEAD.

**Asymmetric and key-agreement algorithms:**
- **RSA**: The RSA public-key algorithm for encryption and digital signatures. Key lengths typically range from 2048 to 4096 bits.
- **DSA**: The Digital Signature Algorithm based on discrete logarithm over prime fields (FIPS 186).
- **DH** (Diffie-Hellman): The classic key-agreement algorithm over finite fields.
- **EC** (Elliptic Curve, generic): Used when the specific EC sub-algorithm is captured by context (e.g., the key format type or curve selection).
- **ECDSA** (Elliptic Curve Digital Signature Algorithm): EC-based signature algorithm, specified in combination with a recommended curve.
- **ECDH** (Elliptic Curve Diffie-Hellman): EC-based key agreement.
- **ECMQV**: An EC key agreement protocol with implicit mutual authentication.
- **Ed25519** / **Ed448**: Edwards-curve digital signature algorithms defined in RFC 8032. Ed25519 uses Curve25519 and Ed448 uses Curve448; both are modern, fast, and have strong security properties.

**Hash-based MAC algorithms:**
- **HMAC-SHA-1**, **HMAC-SHA-224**, **HMAC-SHA-256**, **HMAC-SHA-384**, **HMAC-SHA-512**: HMAC instantiations over the SHA family, used for data authentication and key derivation.

## Examples

A client creating a 256-bit AES key for database column encryption specifies **AES** as the Cryptographic Algorithm and 256 as the Cryptographic Length. A certificate signing key stored as a private key object uses **RSA** or **ECDSA** along with the key length or curve name. A Derive Key request using HKDF specifies the underlying hash algorithm (e.g., **HMAC-SHA-256**) in the Derivation Parameters.

## Related

- [Cryptographic Algorithm attribute](../../attributes/cryptographic-algorithm.md) — the per-object attribute using this enumeration
- [Cryptographic Length attribute](../../attributes/cryptographic-length.md) — specifies key size in bits, paired with this enumeration
- [Cryptographic Parameters](../../attributes/cryptographic-parameters.md) — structure that combines algorithm with mode and padding settings
- [Key Block](../../structures/key-block.md) — carries algorithm identifier for the enclosed key material
- [Recommended Curve Enumeration](recommended-curve-enumeration.md) — specifies the elliptic curve when the algorithm is EC/ECDSA/ECDH
