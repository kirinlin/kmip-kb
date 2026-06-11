---
title: X.509 Certificate Identifier
category: attribute
spec_version: "2.1"
spec_versions: ["1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.61"
v1_source_section: "3.10"
status: draft
related: ["x-509-certificate-subject", "x-509-certificate-issuer", "certificate-identifier"]
keywords: ["X.509 certificate identifier", "issuer distinguished name", "serial number"]
tag_hex: "4200B5"
xml_element: "X_509CertificateIdentifier"
---

# X.509 Certificate Identifier

## Purpose

The PKI-world identity of an X.509 certificate: issuer DN plus serial number,
the pair that uniquely names a certificate across all of PKI (every CA must
issue unique serials). Lets clients [Locate](../operations/locate.md) a
stored certificate from data found in, say, a TLS handshake or a CRL entry.
Added in 1.1 to replace the text-based
[Certificate Identifier](certificate-identifier.md).

## Data Type & Structure

A structure of two required Byte Strings, both taken verbatim (DER) from the
certificate:

| Field | Source |
|---|---|
| Issuer Distinguished Name | The certificate's Issuer field. |
| Certificate Serial Number | The certificate's Serial Number field. |

## Constraints

- Always present on X.509 certificates (1.1+); single instance; immutable
  and not client-deletable — it is derived from the certificate bytes.

## Applies To (Object Types)

X.509 certificates.

## Set / Modified By

Extracted and set by the server when the certificate arrives — implicitly via
[Register](../operations/register.md), [Certify](../operations/certify.md),
or [Re-certify](../operations/re-certify.md).

## Related Attributes

[X.509 Certificate Subject](x-509-certificate-subject.md) ·
[X.509 Certificate Issuer](x-509-certificate-issuer.md) ·
[Certificate Identifier](certificate-identifier.md) (deprecated predecessor)
