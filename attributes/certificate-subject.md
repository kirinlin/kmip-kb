---
title: Certificate Subject
category: attribute
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4"]
source_section: "3.14"
status: draft
related: ["x-509-certificate-subject", "certificate-identifier", "certificate-issuer"]
keywords: ["certificate subject", "deprecated", "subject distinguished name"]
---

# Certificate Subject

## Purpose

The 1.0-era subject-identity attribute, holding the subject DN and
alternative names as text. **Deprecated since 1.1**;
[X.509 Certificate Subject](x-509-certificate-subject.md) replaces it with
DER byte strings. For PGP certificates it held the first User ID packet's
content.

## Data Type & Structure

A structure of Text Strings:

| Field | Required | Notes |
|---|---|---|
| Certificate Subject Distinguished Name | Yes, may be empty | Empty is allowed when a critical SAN extension carries the identity. |
| Certificate Subject Alternative Name | No; repeatable | Email, DNS, IP, etc. |

## Constraints

- Single structure instance; immutable; not client-deletable — extracted
  from the certificate.
- Prefer the X.509-specific replacement in anything written today.

## Applies To (Object Types)

Certificates.

## Set / Modified By

Server-set from certificate content during
[Register](../operations/register.md), [Certify](../operations/certify.md),
or [Re-certify](../operations/re-certify.md).

## Related Attributes

[X.509 Certificate Subject](x-509-certificate-subject.md) (replacement) ·
[Certificate Identifier](certificate-identifier.md) ·
[Certificate Issuer](certificate-issuer.md)
