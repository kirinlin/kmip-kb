---
title: Certificate Length
category: attribute
spec_version: "2.1"
spec_versions: ["1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.8"
v1_source_section: "3.9"
status: draft
related: ["certificate-type", "cryptographic-length"]
keywords: ["certificate length", "bytes", "DER size"]
---

# Certificate Length

## Purpose

The size, in bytes, of the certificate object — i.e. of the DER-encoded
certificate blob. Useful for clients that must budget storage or transport
buffers before fetching the certificate itself. Added in KMIP 1.1.

## Data Type & Structure

A single Integer counting bytes. Contrast with
[Cryptographic Length](cryptographic-length.md), which is the *bit* length of
the public key inside the certificate.

## Constraints

- Always present on certificates (from 1.1 on); single instance.
- Immutable and not client-deletable: a certificate's bytes never change
  in place, so neither does this.

## Applies To (Object Types)

Certificates only.

## Set / Modified By

Computed and set by the server when the certificate is registered or issued —
implicitly via [Register](../operations/register.md),
[Certify](../operations/certify.md), or
[Re-certify](../operations/re-certify.md).

## Related Attributes

[Certificate Type](certificate-type.md) ·
[Cryptographic Length](cryptographic-length.md)
