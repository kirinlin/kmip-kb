---
title: Cryptographic Algorithm
category: attribute
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "3.4"
status: draft
related: ["cryptographic-length", "cryptographic-parameters", "digital-signature-algorithm", "cryptographic-usage-mask"]
keywords: ["cryptographic algorithm", "AES", "RSA", "algorithm enumeration"]
---

# Cryptographic Algorithm

## Purpose

Identifies the algorithm the object's key material belongs to — AES, RSA,
ECDSA, HMAC-SHA256, and so on. For a [Certificate](../objects/certificate.md)
it describes the *public key inside* the certificate; the algorithm that
signed the certificate is a separate attribute
([Digital Signature Algorithm](digital-signature-algorithm.md)).

## Data Type & Structure

An Enumeration. The 1.4 list spans symmetric ciphers (DES, 3DES, AES,
Blowfish, Camellia, ChaCha20, ...), asymmetric algorithms (RSA, DSA, DH, EC
variants), HMACs, and 1.4 additions such as ChaCha20Poly1305, the SHA-3
family, and SHAKE. The generic `EC` value (1.1+) is preferred over the older
per-scheme ECDSA/ECDH/ECMQV values.

## Constraints

- Always present for objects it applies to; single instance.
- Immutable once the object exists; not deletable.
- Must be consistent with the same field in the object's
  [Key Block](../ttlv/key-block.md).

## Applies To (Object Types)

Keys (symmetric, public, private, split), certificates (describing the
embedded public key), and — historically — templates.

## Set / Modified By

Server-set at creation or registration, implicitly via
[Create](../operations/create.md),
[Create Key Pair](../operations/create-key-pair.md),
[Register](../operations/register.md),
[Derive Key](../operations/derive-key.md),
[Certify](../operations/certify.md) /
[Re-certify](../operations/re-certify.md),
[Re-key](../operations/re-key.md) /
[Re-key Key Pair](../operations/re-key-key-pair.md). In Create the client
supplies it as a requested attribute; the server adopts it.

## Related Attributes

[Cryptographic Length](cryptographic-length.md) ·
[Cryptographic Parameters](cryptographic-parameters.md) ·
[Cryptographic Usage Mask](cryptographic-usage-mask.md) ·
[Digital Signature Algorithm](digital-signature-algorithm.md)
