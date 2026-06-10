---
title: X.509 Certificate Issuer
category: attribute
spec_version: "1.4"
spec_versions: ["1.1", "1.2", "1.3", "1.4"]
source_section: "3.12"
status: draft
related: ["x-509-certificate-identifier", "x-509-certificate-subject", "certificate-issuer"]
keywords: ["X.509 certificate issuer", "issuer distinguished name", "issuer alternative name", "CA"]
---

# X.509 Certificate Issuer

## Purpose

Who *signed* the certificate: the issuing CA's DN and any issuer alternative
names, extracted for searchability — e.g. "find every certificate issued by
this CA" ahead of a CA rotation. Added in 1.1, superseding the text-based
[Certificate Issuer](certificate-issuer.md).

## Data Type & Structure

A structure of Byte Strings:

| Field | Required | Source |
|---|---|---|
| Issuer Distinguished Name | Yes | The Issuer field. |
| Issuer Alternative Name | No; repeatable | The Issuer Alternative Name extension entries. |

## Constraints

- Always present on X.509 certificates (1.1+); single structure instance;
  immutable; not deletable — derived data.

## Applies To (Object Types)

X.509 certificates.

## Set / Modified By

Set by the server from the certificate during
[Register](../operations/register.md), [Certify](../operations/certify.md),
or [Re-certify](../operations/re-certify.md).

## Related Attributes

[X.509 Certificate Identifier](x-509-certificate-identifier.md) ·
[X.509 Certificate Subject](x-509-certificate-subject.md) ·
[Certificate Issuer](certificate-issuer.md) (deprecated predecessor)
