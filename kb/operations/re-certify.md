---
title: Re-certify
category: operation
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.45"
v1_source_section: "4.8"
status: reviewed
related: ["certify", "create-key-pair", "certificate", "public-key", "link"]
keywords: ["re-certify", "recertify", "certificate renewal", "X.509", "certificate update"]
---

# Re-certify

## Purpose

`Re-certify` issues a replacement certificate for a key pair whose certificate
is being renewed. It is the certificate analogue of [Re-key](re-key.md).
One certificate is renewed per request, and server support is optional — an
unsupporting server returns an error.

## Request Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | No | The [Certificate](../objects/certificate.md) being renewed. If omitted, the ID Placeholder is used. |
| Certificate Request Type | `420019` | `CertificateRequestType` | No | An enumeration naming the request format; required when a Certificate Request is included. |
| Certificate Request | `420018` | `CertificateRequest` | No | A byte string carrying the request itself (PKCS#10, PEM, etc.). |
| Offset | `420058` | `Offset` | No | An interval giving the gap between the new certificate's initial date and its activation date. |
| Template-Attribute | `420091` | `TemplateAttribute` | No | Desired attributes for the new certificate. In KMIP 2.0+ this wrapper is replaced by the flat [Attributes](../ttlv/template-attribute-structures.md) structure. |

If the Certificate Request and its type are both omitted and no certificate type
is given via the template-attribute, the new certificate keeps the type of the
existing one.

## Response Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes | Identifier of the new certificate. |
| Template-Attribute | `420091` | `TemplateAttribute` | No | Attributes the server set implicitly. |

## Behavior & Server Requirements

The server issues the new certificate, sets the ID Placeholder to its
identifier, and rewires the links: the old certificate gets a [Link](../attributes/link.md)
of type Replacement to the new one, the new certificate gets a Replaced link
back, and the public key's Certificate link is moved to point at the new
certificate. Where the Certificate Request conflicts with the template-attribute,
the request wins. The existing certificate's name(s) transfer to the new one, so
a certificate should only be re-certified once. Initial and last-change dates are
set to now; destroy and revocation dates are not carried over; a fresh
identifier is generated and the [Digest](../attributes/digest.md) is recomputed.
When an Offset is supplied, the new certificate's activation and deactivation
dates derive from the existing certificate's dates shifted by the offset.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: the operation not being supported, a missing Certificate Request Type
when a request is present, an unknown certificate, or insufficient permission.

## Related Operations

[Certify](certify.md) · [Re-key Key Pair](re-key-key-pair.md) · [Get](get.md)
