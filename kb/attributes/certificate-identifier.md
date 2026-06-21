---
title: Certificate Identifier
category: attribute
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4"]
source_section: "del_v2"
v1_source_section: "3.13"
status: reviewed
related: ["x-509-certificate-identifier", "certificate-subject", "certificate-issuer"]
keywords: ["certificate identifier", "deprecated", "issuer", "serial number", "420014", "CertificateIdentifier"]
tag_hex: "420014"
xml_text: "CertificateIdentifier"
tag_type: "Structure"
---

# Certificate Identifier

## Purpose

The original (1.0) certificate-identity attribute: issuer and serial number
as text strings. **Deprecated since 1.1** in favor of
[X.509 Certificate Identifier](x-509-certificate-identifier.md), whose
byte-string DN encoding avoids the string-representation ambiguities that
plagued this one. Documented for compatibility with 1.0-era objects.

## Data Type & Structure

A structure of Text Strings:

| Field | Tag | XML Text | Required | Notes |
|---|---|---|---|---|
| Issuer | `42003B` | `Issuer` | Yes | Issuer DN as text; for the (also deprecated) PGP certificate type, the signing key's OpenPGP Key ID. |
| Serial Number | `420087` | `SerialNumber` | For X.509 | Absent for PGP certificates, which have no serial. |

## Constraints

- Single instance; immutable once set; not client-deletable.
- New implementations should write and query the X.509-specific attribute
  instead; servers may still populate this one for old clients.

## Applies To (Object Types)

Certificates.

## Set / Modified By

Server-set from the certificate content via
[Register](../operations/register.md), [Certify](../operations/certify.md),
or [Re-certify](../operations/re-certify.md).

## Related Attributes

[X.509 Certificate Identifier](x-509-certificate-identifier.md) (replacement) ·
[Certificate Subject](certificate-subject.md) ·
[Certificate Issuer](certificate-issuer.md)
