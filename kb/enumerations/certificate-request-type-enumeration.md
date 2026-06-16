---
title: Certificate Request Type Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.8"
status: reviewed
related: ["certify", "certificate-type-enumeration", "certificate-request", "certificate"]
keywords: ["certificate request", "CSR", "PKCS#10", "CRMF", "PEM", "PGP", "certify", "420019", "CertificateRequestType"]
tag_hex: "420019"
xml_text: "CertificateRequestType"
---

# Certificate Request Type Enumeration

## Overview

The Certificate Request Type enumeration identifies the format of the certificate signing request (CSR) data submitted to a KMIP server via the [Certify](../operations/certify.md) operation. Different PKI ecosystems use different CSR formats with varying capabilities for expressing certificate policy, key usage, and subject attributes. Specifying the correct type allows the server (or the CA it proxies) to parse the request correctly and validate its signature.

## Fields & Structure

| Value | Hex | XML Text | Description |
|---|---|---|---|
| CRMF | `0x00000001` | `CRMF` |  |
| PKCS#10 | `0x00000002` | `PKCS_10` |  |
| PEM | `0x00000003` | `PEM` |  |

- **CRMF** (Certificate Request Message Format, RFC 4211): An ASN.1-based format used in Certificate Management over CMS (CMC) and the Certificate Management Protocol (CMP). More expressive than PKCS#10, allowing proof-of-possession and certificate template constraints to be specified.
- **PKCS#10** (RFC 2986): The most widely deployed CSR format, consisting of a DER-encoded CertificationRequest structure signed by the private key corresponding to the public key being certified. Supported by virtually all CAs and PKI toolkits.
- **PEM**: A base64-encoded DER format with `-----BEGIN CERTIFICATE REQUEST-----` headers, commonly used in file-based CA workflows. Typically wraps a PKCS#10 structure.
- **PGP**: An OpenPGP key certification request, used when obtaining a PGP certificate rather than an X.509 certificate.

## Examples

A client generating a TLS server certificate submits a **PKCS#10** CSR containing the server's public key and a Subject Alternative Name extension listing its hostnames. An enterprise PKI using SCEP or CMP might use **CRMF** to express certificate policy OIDs and proof-of-possession challenges.

## Related

- [Certify operation](../operations/certify.md) — the operation that processes a certificate request
- [Certificate Request object](../objects/certificate-request.md) — the managed object that can hold a stored CSR
- [Certificate Type Enumeration](certificate-type-enumeration.md) — classifies the resulting certificate format
- [Certificate object](../objects/certificate.md) — the resulting managed object produced by certification
