---
title: Digital Signature Algorithm
category: attribute
spec_version: "2.1"
spec_versions: ["1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.22"
v1_source_section: "3.16"
status: reviewed
related: ["cryptographic-algorithm", "certificate-type", "digest"]
keywords: ["digital signature algorithm", "signature", "SHA-256 with RSA", "ECDSA", "certificate signing", "4200AE", "DigitalSignatureAlgorithm"]
tag_hex: "4200AE"
xml_text: "DigitalSignatureAlgorithm"
tag_type: "Enumeration"
---

# Digital Signature Algorithm

## Purpose

Records which signature scheme signed a digitally signed object — for an
X.509 certificate, the algorithm in its signature field. Distinct from
[Cryptographic Algorithm](cryptographic-algorithm.md), which describes the
subject's own key: a certificate for an EC key signed by an RSA CA has
Cryptographic Algorithm = EC but Digital Signature Algorithm =
SHA-256 with RSA. Added in 1.1.

## Data Type & Structure

An Enumeration combining hash and signature primitive: the MD2/MD5/SHA-1/
SHA-224/SHA-256/SHA-384/SHA-512-with-RSA family (PKCS#1 v1.5), RSASSA-PSS,
DSA-with-SHA-1/224/256, ECDSA-with-SHA-1/224/256/384/512, and (1.4) the
SHA3-with-RSA variants.

## Constraints

- Always present where it applies; immutable; not client-deletable.
- Single instance for X.509 certificates; multiple instances allowed for
  PGP keys, which can carry several signatures.

## Applies To (Object Types)

Certificates and PGP keys.

## Set / Modified By

Server-set from the signed object's content during
[Certify](../operations/certify.md),
[Re-certify](../operations/re-certify.md), or
[Register](../operations/register.md).

## Related Attributes

[Cryptographic Algorithm](cryptographic-algorithm.md) ·
[Certificate Type](certificate-type.md) · [Digest](digest.md)
