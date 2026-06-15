---
title: Certificate Request
category: object
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "2.2"
status: reviewed
related: ["certificate", "private-key", "public-key", "certify", "re-certify", "register", "create-key-pair", "unique-identifier"]
keywords: ["certificate request", "csr", "pkcs10", "pem", "crmf", "cmc", "certificate signing request", "managed object", "420018", "CertificateRequest"]
tag_hex: "420018"
xml_text: "CertificateRequest"
---

# Certificate Request

## Purpose

Certificate Request is a managed object type introduced in v2.1 that represents a certificate signing request (CSR) as a first-class KMIP object. Before v2.1, clients submitting a CSR had to use [Certify](../operations/certify.md) or [Re-certify](../operations/re-certify.md) directly, passing the request inline. Promoting the CSR to a managed object lets clients register a request once and reference it by Unique Identifier in subsequent operations, supports the normal KMIP attribute and lifecycle machinery, and allows the server to track the request's state through its certification workflow.

## Structure

A Certificate Request object consists of:

- **Certificate Request Type** — an Enumeration indicating the encoding format of the request material: PKCS#10 (the most common, a DER-encoded CertificationRequest), PEM (the base64-armoured form), CRMF (Certificate Request Message Format, used in CMP), CMC (Certificate Management over CMS), and optionally vendor-defined types.
- **Certificate Request Value** — a Byte String containing the actual request data in the format indicated by Certificate Request Type.

Standard KMIP attributes — Name, Object Type, Unique Identifier, Cryptographic Algorithm, State, and others — apply to Certificate Request objects in the same way they apply to other managed objects.

## Key Attributes

Relevant attributes include:

- [Object Type](../attributes/object-type.md) — set to Certificate Request.
- [Name](../attributes/name.md) — optional human-readable label.
- [Cryptographic Algorithm](../attributes/cryptographic-algorithm.md) — algorithm of the key pair underlying the request.
- [Cryptographic Length](../attributes/cryptographic-length.md) — length of the subject key.
- [State](../attributes/state.md) — follows the standard object lifecycle; newly registered requests begin Pre-Active.
- [Unique Identifier](../attributes/unique-identifier.md) — server-assigned identifier used to reference the request in subsequent operations.

## Lifecycle & State

Certificate Request objects participate in the standard [State](../attributes/state.md). A newly registered request enters Pre-Active. The server or client may Activate it when it is ready for submission to a CA, at which point it transitions to Active. Once the CA issues the certificate — or the request is cancelled or superseded — the object can be Revoked or Destroyed. An issued certificate is typically a separate [Certificate](certificate.md) object linked to the request.

Clients create Certificate Request objects via [Register](../operations/register.md) (submitting an externally generated CSR) or may generate the underlying key pair and the request together using [Create Key Pair](../operations/create-key-pair.md) when the server supports inline CSR generation.

## Related Objects

[Certificate](certificate.md) · [Private Key](private-key.md) · [Public Key](public-key.md)
