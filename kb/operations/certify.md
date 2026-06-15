---
title: Certify
category: operation
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.6"
v1_source_section: "4.7"
status: reviewed
related: ["re-certify", "create-key-pair", "register", "certificate", "public-key", "link"]
keywords: ["certify", "certificate", "X.509", "PKCS#10", "certificate signing request", "CSR"]
---

# Certify

## Purpose

`Certify` asks the server to produce a [Certificate](../objects/certificate.md)
object for a public key. It covers both certifying a brand-new public key and
re-certifying one that already has a certificate. Exactly one certificate is
produced per request, and server support for the operation is optional — a
server that does not implement it returns an error.

## Request Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | No | The [Public Key](../objects/public-key.md) to certify. If omitted, the ID Placeholder is used. |
| Certificate Request Type | `420019` | `CertificateRequestType` | No | An enumeration naming the request format; required when a Certificate Request is included. |
| Certificate Request | `420018` | `CertificateRequest` | No | A byte string carrying the request itself (for example PKCS#10 or PEM). |
| Template-Attribute | `420091` | `TemplateAttribute` | No | Desired attributes for the resulting certificate. In KMIP 2.0+ this wrapper is replaced by the flat [Attributes](../structures/template-attribute-structures.md) structure. |

When no Certificate Request is supplied, the public key is named only by its
Unique Identifier and the desired certificate type comes from the
template-attribute. Carrying the request as a byte string lets clients submit
any of several X.509 request encodings.

## Response Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes | Identifier of the certificate that was produced. |
| Template-Attribute | `420091` | `TemplateAttribute` | No | Attributes the server set implicitly. |

## Behavior & Server Requirements

The server creates the certificate, assigns it a [Unique Identifier](../attributes/unique-identifier.md),
sets the ID Placeholder to it, and cross-links it with the public key —
[Link](../attributes/link.md) of type Certificate on the key and Public Key on
the certificate. When the request and the template-attribute disagree, the
Certificate Request wins. Because the new certificate's
identifier flows through the ID Placeholder, a client can fetch it with a
[Get](get.md) batched after the Certify.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: the operation not being supported by the server, a missing
Certificate Request Type when a request is present, an unknown public key, or
insufficient permission.

## Related Operations

[Re-certify](re-certify.md) · [Create Key Pair](create-key-pair.md) ·
[Register](register.md) · [Get](get.md)
