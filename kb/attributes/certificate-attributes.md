---
title: Certificate Attributes
category: attribute
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "4.6"
status: reviewed
related: ["certificate-type", "certificate-length", "digital-signature-algorithm", "certificate", "digest"]
keywords: ["certificate attributes", "x.509", "der", "certificate type", "certificate length", "compound attribute"]
---

# Certificate Attributes

## Purpose

Certificate Attributes is a compound structure attribute introduced in v2.1 that consolidates certificate-specific metadata into a single attribute. Rather than requiring a client to fetch Certificate Type, Certificate Length, and Digital Signature Algorithm as separate attributes, this structure groups them in one retrievable unit, reducing round-trips when inspecting certificate objects.

## Data Type & Structure

A Structure containing up to three fields: Certificate Type (Enumeration), Certificate Length (Integer), and optionally Digital Signature Algorithm (Enumeration). The Certificate Type and Certificate Length sub-fields carry the same semantics as their standalone counterparts, but are bundled here for convenience. The Digital Signature Algorithm sub-field identifies the signature algorithm used to sign the certificate itself, which may differ from any key algorithm the certificate carries.

## Constraints

Single-instance attribute. Applies only to Certificate managed objects. The server populates it at registration or certification time; clients do not typically set it directly. If individual top-level Certificate Type or Certificate Length attributes are also present, they must be consistent with the values here.

## Applies To (Object Types)

[Certificate](../objects/certificate.md) only.

## Set / Modified By

Set by the server when a Certificate object is registered via [Register](../operations/register.md) or created via [Certify](../operations/certify.md). Updated if the certificate is replaced.

## Related Attributes

[Certificate Type](certificate-type.md) · [Certificate Length](certificate-length.md) · [Digital Signature Algorithm](digital-signature-algorithm.md) · [Digest](digest.md)
