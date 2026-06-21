---
title: Certificate Type Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.9"
status: reviewed
related: ["certificate", "certify", "certificate-request-type-enumeration", "object-type-enumeration"]
keywords: ["certificate", "X.509", "PGP", "certificate type", "public key certificate", "42001D", "CertificateType"]
tag_hex: "42001D"
xml_text: "CertificateType"
tag_type: "Enumeration"
---

# Certificate Type Enumeration

## Overview

The Certificate Type enumeration classifies the format of a certificate object managed by the KMIP server. Certificates in KMIP are first-class managed objects alongside keys, and they may come from different PKI ecosystems with different encoding formats. The type field allows the server and its clients to distinguish standard X.509 public key infrastructure certificates from OpenPGP certificates, and ensures that certificate consumers know which parser and trust model to apply.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| X.509 | `00000001` | `X_509` |  |
| PGP | `00000002` | `PGP` |  |

- **X.509**: An ASN.1/DER-encoded X.509v3 public key certificate as defined in RFC 5280. This is the dominant certificate format for TLS, code signing, and most enterprise PKI deployments. X.509 certificates carry a subject distinguished name, public key, validity period, extensions such as Subject Alternative Names and Key Usage, and a CA signature.
- **PGP**: An OpenPGP certificate as defined in RFC 4880 or its successor RFC 9580. PGP certificates use a web-of-trust model rather than a hierarchical CA chain, and the encoding is based on PGP packet format rather than ASN.1. Used in email encryption and software signing workflows.

## Examples

When a KMIP client submits a PEM-encoded TLS certificate obtained from a corporate CA, it registers an object of type **X.509**. A software publishing workflow that signs release artefacts with developer keys might register **PGP** certificates for the developers' public keys.

## Related

- [Certificate object](../objects/certificate.md) — the managed object that stores certificate data
- [Certify operation](../operations/certify.md) — issues a certificate from a signing request
- [Certificate Request Type Enumeration](certificate-request-type-enumeration.md) — classifies the request format leading to a certificate
- [Object Type Enumeration](object-type-enumeration.md) — the top-level object type discriminator, of which Certificate is one value
