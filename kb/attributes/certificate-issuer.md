---
title: Certificate Issuer
category: attribute
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4"]
source_section: "del_v2"
v1_source_section: "3.15"
status: reviewed
related: ["x-509-certificate-issuer", "certificate-identifier", "certificate-subject"]
keywords: ["certificate issuer", "deprecated", "issuer distinguished name", "420015", "CertificateIssuer"]
tag_hex: "420015"
xml_text: "CertificateIssuer"
---

# Certificate Issuer

## Purpose

The 1.0-era issuer-identity attribute: the signing CA's DN and alternative
names as text. **Deprecated since 1.1** in favor of
[X.509 Certificate Issuer](x-509-certificate-issuer.md), which stores the
DER-encoded DN bytes instead of a lossy string rendering.

## Data Type & Structure

A structure of Text Strings:

| Field | Tag | XML Text | Required |
|---|---|---|---|
| Certificate Issuer Distinguished Name | `420017` | `CertificateIssuerDistinguishedName` | Yes |
| Certificate Issuer Alternative Name | `420016` | `CertificateIssuerAlternativeName` | No; repeatable |

## Constraints

- Single structure instance; immutable; not client-deletable — derived from
  the certificate itself.
- Retained by servers for 1.0-compatible clients; new code should use the
  X.509-specific attribute.

## Applies To (Object Types)

Certificates.

## Set / Modified By

Server-set from certificate content during
[Register](../operations/register.md), [Certify](../operations/certify.md),
or [Re-certify](../operations/re-certify.md).

## Related Attributes

[X.509 Certificate Issuer](x-509-certificate-issuer.md) (replacement) ·
[Certificate Identifier](certificate-identifier.md) ·
[Certificate Subject](certificate-subject.md)
