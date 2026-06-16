---
title: Key Format Type Enumeration
category: encoding
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.25"
status: reviewed
related: ["key-block", "key-format-type", "get", "register", "key-value"]
keywords: ["key format", "PKCS#1", "PKCS#8", "X.509", "raw", "transparent", "key encoding", "ECPrivateKey", "PKCS#12", "420042", "KeyFormatType"]
tag_hex: "420042"
xml_text: "KeyFormatType"
---

# Key Format Type Enumeration

## Overview

The Key Format Type enumeration specifies the encoding or serialisation format of the key material stored inside a [Key Block](../../structures/key-block.md). Different applications, protocols, and hardware require keys in different wire formats: a TLS library expects PKCS#8 or ECPrivateKey for private keys; an HSM API may require PKCS#1 for RSA; a key escrow system may need raw transparent key structures; and a PKCS#12 archive bundles a private key with its certificate chain. The key format type tells consumers exactly how to interpret and parse the key bytes they receive. It also controls what the client receives from a [Get](../../operations/get.md) operation when a specific format is requested.

## Fields & Structure

| Value | Hex | XML Text | Description |
|---|---|---|---|
| Raw | `0x00000001` | `Raw` |  |
| Opaque | `0x00000002` | `Opaque` |  |
| PKCS#1 | `0x00000003` | `PKCS_1` |  |
| PKCS#8 | `0x00000004` | `PKCS_8` |  |
| X.509 | `0x00000005` | `X_509` |  |
| ECPrivateKey | `0x00000006` | `ECPrivateKey` |  |
| Transparent Symmetric Key | `0x00000007` | `TransparentSymmetricKey` |  |
| Transparent DSA Private Key | `0x00000008` | `TransparentDSAPrivateKey` |  |
| Transparent DSA Public Key | `0x00000009` | `TransparentDSAPublicKey` |  |
| Transparent RSA Private Key | `0x0000000A` | `TransparentRSAPrivateKey` |  |
| Transparent RSA Public Key | `0x0000000B` | `TransparentRSAPublicKey` |  |
| Transparent DH Private Key | `0x0000000C` | `TransparentDHPrivateKey` |  |
| Transparent DH Public Key | `0x0000000D` | `TransparentDHPublicKey` |  |
| Transparent EC Private Key | `0x00000014` | `TransparentECPrivateKey` |  |
| Transparent EC Public Key | `0x00000015` | `TransparentECPublicKey` |  |
| PKCS#12 | `0x00000016` | `PKCS_12` |  |
| PKCS#10 | `0x00000017` | `PKCS_10` |  |

**Format-agnostic and opaque:**
- **Raw**: The key material is an unformatted sequence of bytes — just the key value itself with no ASN.1, no headers. Used for symmetric keys and raw shared secrets.
- **Opaque**: The format is vendor-defined or not otherwise specified. The server stores the bytes as-is without interpreting them.

**ASN.1/DER-based formats:**
- **PKCS#1**: RSA private or public key encoded according to PKCS#1 (RFC 8017). RSA private keys use the `RSAPrivateKey` ASN.1 structure; public keys use `RSAPublicKey`.
- **PKCS#8**: An algorithm-agnostic private key format (RFC 5958) that wraps the key in a `PrivateKeyInfo` or `OneAsymmetricKey` structure. Supports RSA, EC, DSA, and Ed25519/Ed448 private keys; can optionally be encrypted (`EncryptedPrivateKeyInfo`). The most portable private key format.
- **X.509**: A public key encoded in the SubjectPublicKeyInfo DER structure (RFC 5280 §4.1.2.7). Algorithm-agnostic: covers RSA, EC, DSA, and Ed25519/Ed448 public keys.
- **ECPrivateKey**: An EC private key in the SEC 1 format (RFC 5915), which is the `ECPrivateKey` ASN.1 structure. Optionally includes the public key and the named curve OID.

**KMIP transparent structures:**
- **TransparentSymmetricKey**: The symmetric key value as a TTLV Big Integer, suitable for key archiving and explicit inspection.
- **TransparentDSAPrivateKey** / **TransparentDSAPublicKey**: DSA key components (p, q, g, x/y) as individual TTLV fields.
- **TransparentRSAPrivateKey** / **TransparentRSAPublicKey**: RSA key components (n, e, d, p, q, etc.) as individual TTLV fields. Enables key component inspection and archival.
- **TransparentDHPrivateKey** / **TransparentDHPublicKey**: Diffie-Hellman key components as TTLV fields.
- **TransparentECPrivateKey** / **TransparentECPublicKey**: EC private scalar and public point as TTLV fields, with the recommended curve identified separately.

**Container formats:**
- **PKCS#12**: A DER-encoded archive that bundles a private key with its certificate and optionally its certificate chain and additional attributes. Used for portability between applications (e.g., browser import/export).

## Examples

An application using Java's KeyStore API requests a private key in **PKCS#8** format, which it can load directly into a `PKCS8EncodedKeySpec`. An HSM backup procedure retrieves all symmetric keys as **TransparentSymmetricKey** for escrow purposes, storing the raw key bytes alongside their algorithm attributes. A certificate migration tool exports keys as **PKCS#12** so that both the key and its certificate travel together.

## Related

- [Key Block structure](../../structures/key-block.md) — the container that holds key material with this format type field
- [Key Format Type attribute](../../attributes/key-format-type.md) — the per-object attribute recording the stored format
- [Get operation](../../operations/get.md) — clients can request a specific format type when retrieving a key
- [Register operation](../../operations/register.md) — clients specify the format of key material being imported
