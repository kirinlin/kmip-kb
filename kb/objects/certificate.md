---
title: Certificate
category: object
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "2.1"
v1_source_section: "2.2.1"
status: draft
related: ["certify", "re-certify", "register", "get", "public-key", "certificate-type", "x-509-certificate-identifier", "digest"]
keywords: ["certificate", "X.509", "DER", "public key certificate", "PKI"]
---

# Certificate

## Purpose

A Certificate is a managed cryptographic object that holds a public-key
certificate binding a public key to an identity. In KMIP 1.x it is a
DER-encoded X.509 certificate. Certificates are produced by
[Certify](../operations/certify.md) and [Re-certify](../operations/re-certify.md),
or handed to the server with [Register](../operations/register.md).

## Structure

| Field | Required | Meaning |
|---|---|---|
| Certificate Type | Yes | Identifies the certificate encoding; in 1.x this is X.509 (see [Certificate Type](../attributes/certificate-type.md)). |
| Certificate Value | Yes | The raw DER-encoded certificate bytes. |

The older PGP certificate type was deprecated as of version 1.2; the dedicated
[PGP Key](pgp-key.md) object should be used for PGP material instead.

## Key Attributes

A certificate is described by certificate-specific attributes the server can
derive from the encoded value, including
[Certificate Type](../attributes/certificate-type.md),
[Certificate Length](../attributes/certificate-length.md),
[X.509 Certificate Identifier](../attributes/x-509-certificate-identifier.md),
[X.509 Certificate Subject](../attributes/x-509-certificate-subject.md), and
[X.509 Certificate Issuer](../attributes/x-509-certificate-issuer.md). It also
carries the common [Unique Identifier](../attributes/unique-identifier.md),
[State](../attributes/state.md), and a [Digest](../attributes/digest.md) of the
certificate value.

## Lifecycle & State

A certificate follows the managed-object lifecycle via its
[State](../attributes/state.md). It is typically [Linked](../attributes/link.md)
to the [Public Key](public-key.md) it certifies (and through that, to the
matching [Private Key](private-key.md)). [Revoke](../operations/revoke.md) marks
it revoked or compromised, and [Destroy](../operations/destroy.md) removes its
material.

## Related Objects

[Public Key](public-key.md) · [Private Key](private-key.md) · [PGP Key](pgp-key.md)
