---
title: Object Type Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.34"
status: reviewed
related: ["object-type", "symmetric-key", "public-key", "private-key", "split-key", "secret-data", "certificate", "opaque-object", "certificate-request"]
keywords: ["object type", "managed object type", "key type", "certificate", "secret data", "opaque object", "420057", "ObjectType"]
tag_hex: "420057"
xml_text: "ObjectType"
---

# Object Type Enumeration

## Overview

The Object Type enumeration identifies which kind of managed cryptographic object is being created, registered, or operated on. It is one of the most fundamental enumerations in KMIP, appearing in virtually every request or response that targets or returns a managed object. Servers use it to determine storage format, applicable attributes, and permitted operations; clients use it in Locate filters and Create/Register requests.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Certificate | `00000001` | `Certificate` |  |
| Symmetric Key | `00000002` | `SymmetricKey` |  |
| Public Key | `00000003` | `PublicKey` |  |
| Private Key | `00000004` | `PrivateKey` |  |
| Split Key | `00000005` | `SplitKey` |  |
| Secret Data | `00000007` | `SecretData` |  |
| Opaque Object | `00000008` | `OpaqueObject` |  |
| PGP Key | `00000009` | `PGPKey` |  |
| Certificate Request | `0000000A` | `CertificateRequest` |  |

- **Certificate**: An X.509 or PGP certificate. The most common managed non-key object. Holds encoded certificate material and a Certificate Type sub-classification.
- **Symmetric Key**: A secret key for symmetric cipher algorithms (AES, 3DES, ChaCha20, etc.).
- **Public Key**: The public half of an asymmetric key pair (RSA, EC, DSA, etc.).
- **Private Key**: The private half of an asymmetric key pair. The most access-controlled object type.
- **Split Key**: One share of a key that has been divided using XOR, Shamir, or Blakley secret sharing.
- **Secret Data**: Non-key secrets — passwords, seeds, PINs, API tokens — that need lifecycle management without cryptographic algorithm semantics.
- **Opaque Object**: An arbitrary byte blob whose content the server does not interpret. Sub-classified by Opaque Data Type.
- **PGP Key**: A PGP public or private key packet. Added to cover PGP workflows alongside the X.509/asymmetric key model.
- **Certificate Request** *(v2.1)*: A certificate signing request (CSR) — PKCS#10, PEM, CRMF, or CMC — promoted to a first-class managed object in v2.1.

## Examples

A Create request specifying **Symmetric Key** produces an AES key stored on the server. A Register request with **Certificate** registers an externally issued X.509 certificate. A Locate filter using **Private Key** restricts results to asymmetric private keys only.

## Related

[Object Type attribute](../attributes/object-type.md) · [Symmetric Key](../objects/symmetric-key.md) · [Certificate](../objects/certificate.md) · [Certificate Request](../objects/certificate-request.md)
