---
title: Certificate Type
category: attribute
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4"]
source_section: "3.8"
status: draft
related: ["certificate-length", "x-509-certificate-identifier", "digital-signature-algorithm"]
keywords: ["certificate type", "X.509", "PGP", "certificate"]
---

# Certificate Type

## Purpose

Says what flavor of certificate a [Certificate](../objects/certificate.md)
object holds, so a client knows how to parse the Certificate Value bytes.

## Data Type & Structure

An Enumeration with two defined values: `X.509` and `PGP`. The PGP value is
deprecated since 1.2 — OpenPGP material belongs in the
[PGP Key](../objects/pgp-key.md) object instead — leaving X.509 as the only
type in practical use.

## Constraints

- Always present on certificates; single instance; immutable and not
  deletable once set.
- Mirrors the Certificate Type field inside the Certificate object structure.

## Applies To (Object Types)

Certificates only.

## Set / Modified By

Server-set when the certificate enters the system, implicitly via
[Register](../operations/register.md), [Certify](../operations/certify.md),
or [Re-certify](../operations/re-certify.md), based on what the server finds
in (or knows about) the certificate payload.

## Related Attributes

[Certificate Length](certificate-length.md) ·
[X.509 Certificate Identifier](x-509-certificate-identifier.md) ·
[Digital Signature Algorithm](digital-signature-algorithm.md)
