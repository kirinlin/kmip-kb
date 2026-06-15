---
title: X.509 Certificate Subject
category: attribute
spec_version: "2.1"
spec_versions: ["1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.63"
v1_source_section: "3.11"
status: reviewed
related: ["x-509-certificate-identifier", "x-509-certificate-issuer", "certificate-subject"]
keywords: ["X.509 certificate subject", "subject distinguished name", "subject alternative name", "SAN"]
tag_hex: "4200B7"
xml_element: "X_509CertificateSubject"
---

# X.509 Certificate Subject

## Purpose

Who the certificate is *for*: the subject DN and any subject alternative
names (DNS names, email addresses, IPs) pulled out of the certificate so
clients can search by identity without parsing DER themselves. Added in 1.1,
superseding the text-based [Certificate Subject](certificate-subject.md).

## Data Type & Structure

A structure of Byte Strings:

| Field | Tag | XML Element | Required | Source |
|---|---|---|---|---|
| Subject Distinguished Name | `4200B4` | `SubjectDistinguishedName` | Yes, but may be empty | The Subject field. |
| Subject Alternative Name | `4200B3` | `SubjectAlternativeName` | Required when the DN is empty; repeatable | The SAN extension entries. |

An empty subject DN is legitimate X.509 practice when a critical SAN
extension carries the identity instead — hence the conditional requirement.

## Constraints

- Always present on X.509 certificates (1.1+); single instance of the
  structure (the SAN field repeats *inside* it); immutable; not deletable.

## Applies To (Object Types)

X.509 certificates.

## Set / Modified By

Set by the server from the certificate content during
[Register](../operations/register.md), [Certify](../operations/certify.md),
or [Re-certify](../operations/re-certify.md). Clients never write it.

## Related Attributes

[X.509 Certificate Identifier](x-509-certificate-identifier.md) ·
[X.509 Certificate Issuer](x-509-certificate-issuer.md) ·
[Certificate Subject](certificate-subject.md) (deprecated predecessor)
