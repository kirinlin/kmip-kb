---
title: Key Format Type Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.25"
status: reviewed
related: ["key-block", "key-format-type", "get", "register", "key-value"]
keywords: ["key format", "PKCS#1", "PKCS#8", "X.509", "raw", "transparent", "key encoding", "ECPrivateKey", "PKCS#12", "420042", "KeyFormatType"]
tag_hex: "420042"
xml_text: "KeyFormatType"
tag_type: "Enumeration"
---

# Key Format Type Enumeration

## Overview

The Key Format Type enumeration specifies the encoding or serialisation format of the key material stored inside a [Key Block](../structures/key-block.md). Different applications, protocols, and hardware require keys in different wire formats: a TLS library expects PKCS#8 or ECPrivateKey for private keys; an HSM API may require PKCS#1 for RSA; a key escrow system may need raw transparent key structures; and a PKCS#12 archive bundles a private key with its certificate chain. The key format type tells consumers exactly how to interpret and parse the key bytes they receive. It also controls what the client receives from a [Get](../operations/get.md) operation when a specific format is requested.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Raw | `00000001` | `Raw` | The key material is an unformatted sequence of bytes — just the key value itself with no ASN.1, no headers. Used for symmetric keys and raw shared secrets. |
| Opaque | `00000002` | `Opaque` | The format is vendor-defined or not otherwise specified. The server stores the bytes as-is without interpreting them. |
| PKCS#1 | `00000003` | `PKCS_1` | RSA private or public key encoded according to PKCS#1 (RFC 8017). RSA private keys use the `RSAPrivateKey` ASN.1 structure; public keys use `RSAPublicKey`. |
| PKCS#8 | `00000004` | `PKCS_8` | An algorithm-agnostic private key format (RFC 5958) that wraps the key in a `PrivateKeyInfo` or `OneAsymmetricKey` structure. Supports RSA, EC, DSA, and Ed25519/Ed448 private keys; can optionally be encrypted (`EncryptedPrivateKeyInfo`). The most portable private key format. |
| X.509 | `00000005` | `X_509` | A public key encoded in the SubjectPublicKeyInfo DER structure (RFC 5280 §4.1.2.7). Algorithm-agnostic: covers RSA, EC, DSA, and Ed25519/Ed448 public keys. |
| ECPrivateKey | `00000006` | `ECPrivateKey` | An EC private key in the SEC 1 format (RFC 5915), which is the `ECPrivateKey` ASN.1 structure. Optionally includes the public key and the named curve OID. |
| Transparent Symmetric Key | `00000007` | `TransparentSymmetricKey` | A KMIP-native structure that exposes the raw key bytes of a symmetric key as a named `Key` field, without any external encoding wrapper. Used for key escrow, key import/export, and split-key operations where the exact key material must be accessible by value. |
| Transparent DSA Private Key | `00000008` | `TransparentDSAPrivateKey` | A KMIP-native structure holding a DSA private key by its mathematical components: domain parameters p (prime modulus), q (prime divisor), g (generator), and the private key integer x. Avoids any ASN.1 wrapper and makes each parameter individually addressable. |
| Transparent DSA Public Key | `00000009` | `TransparentDSAPublicKey` | A KMIP-native structure holding a DSA public key by its components: domain parameters p, q, g, and the public key integer y. Mirrors TransparentDSAPrivateKey at the public side. |
| Transparent RSA Private Key | `0000000A` | `TransparentRSAPrivateKey` | A KMIP-native structure that exposes an RSA private key as named integer fields: modulus n, public exponent e, private exponent d, and optionally the CRT components (prime1, prime2, exponent1, exponent2, coefficient). Provides direct access to each RSA component without DER encoding. |
| Transparent RSA Public Key | `0000000B` | `TransparentRSAPublicKey` | A KMIP-native structure holding an RSA public key as two named integer fields: the modulus n and the public exponent e. Complements TransparentRSAPrivateKey at the public side. |
| Transparent DH Private Key | `0000000C` | `TransparentDHPrivateKey` | A KMIP-native structure holding a Diffie-Hellman private key by its components: group parameters p, q (optional), g, and the private integer x. Useful for DH key agreement escrow without wrapping the value in PKCS#3 or other encodings. |
| Transparent DH Public Key | `0000000D` | `TransparentDHPublicKey` | A KMIP-native structure holding a Diffie-Hellman public key by its group parameters p, q (optional), g, and the public integer y. Mirrors TransparentDHPrivateKey at the public side. |
| Transparent EC Private Key | `00000014` | `TransparentECPrivateKey` | A KMIP-native structure for an elliptic-curve private key containing the recommended curve identifier and the scalar private value d. Optionally includes the corresponding public key point Q. Does not use SEC 1 or PKCS#8 encoding. |
| Transparent EC Public Key | `00000015` | `TransparentECPublicKey` | A KMIP-native structure for an elliptic-curve public key containing the recommended curve identifier and the public key point Q as a byte string (typically uncompressed or compressed form per SEC 1). Complements TransparentECPrivateKey. |
| PKCS#12 | `00000016` | `PKCS_12` | A DER-encoded archive that bundles a private key with its certificate and optionally its certificate chain and additional attributes. Used for portability between applications (e.g., browser import/export). |
| PKCS#10 | `00000017` | `PKCS_10` | A Certificate Signing Request (CSR) encoded per PKCS#10 (RFC 2986). Contains a public key and subject identifying information, signed by the corresponding private key, and submitted to a CA to obtain a certificate. |

## Examples

An application using Java's KeyStore API requests a private key in **PKCS#8** format, which it can load directly into a `PKCS8EncodedKeySpec`. An HSM backup procedure retrieves all symmetric keys as **TransparentSymmetricKey** for escrow purposes, storing the raw key bytes alongside their algorithm attributes. A certificate migration tool exports keys as **PKCS#12** so that both the key and its certificate travel together.

## Related

- [Key Block structure](../structures/key-block.md) — the container that holds key material with this format type field
- [Key Format Type attribute](../attributes/key-format-type.md) — the per-object attribute recording the stored format
- [Get operation](../operations/get.md) — clients can request a specific format type when retrieving a key
- [Register operation](../operations/register.md) — clients specify the format of key material being imported
