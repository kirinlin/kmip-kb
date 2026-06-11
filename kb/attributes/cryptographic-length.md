---
title: Cryptographic Length
category: attribute
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.15"
v1_source_section: "3.5"
status: draft
related: ["cryptographic-algorithm", "certificate-length", "cryptographic-domain-parameters"]
keywords: ["cryptographic length", "key size", "bits", "key length"]
---

# Cryptographic Length

## Purpose

The key size in bits: for keys, the length of the plaintext key material; for
certificates, the size of the public key the certificate contains. Together
with [Cryptographic Algorithm](cryptographic-algorithm.md) it pins down what
the object actually is (AES-256 vs AES-128, RSA-2048 vs RSA-3072).

## Data Type & Structure

A single Integer, in bits — not bytes, and not the size of any encoded blob
(that, for certificates, is [Certificate Length](certificate-length.md)).

## Constraints

- Always present where applicable; single instance; immutable and not
  deletable once the object exists.
- Must match the key material and the corresponding
  [Key Block](../ttlv/key-block.md) field.
- For DSA/DH the value is the length of the prime P; the subgroup size Q is
  requested separately via
  [Cryptographic Domain Parameters](cryptographic-domain-parameters.md).

## Applies To (Object Types)

Keys and certificates (and formerly templates). Not meaningful for opaque
objects; for [Secret Data](../objects/secret-data.md) the key block carries
no algorithm/length pair.

## Set / Modified By

Server-set at create/register time, implicitly by the same operations that
set the algorithm: [Create](../operations/create.md),
[Create Key Pair](../operations/create-key-pair.md),
[Register](../operations/register.md),
[Derive Key](../operations/derive-key.md),
[Certify](../operations/certify.md) /
[Re-certify](../operations/re-certify.md),
[Re-key](../operations/re-key.md) /
[Re-key Key Pair](../operations/re-key-key-pair.md).

## Related Attributes

[Cryptographic Algorithm](cryptographic-algorithm.md) ·
[Certificate Length](certificate-length.md) ·
[Cryptographic Domain Parameters](cryptographic-domain-parameters.md)
