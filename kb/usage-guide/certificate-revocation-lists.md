---
title: Certificate Revocation Lists
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.42"
status: draft
related: ["certify-and-re-certify"]
keywords: ["CRL", "Certificate Revocation List", "revocation checking", "client responsibility", "Register", "Re-key"]
---

# Certificate Revocation Lists

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

KMIP assigns revocation checking responsibility entirely to the client. Before submitting a Register or Re-key request, the client must verify the revocation status of any involved certificate; the protocol places no obligation on the server to do so. KMIP does not define a server-side CRL checking obligation.

## Guidance

The client is responsible for obtaining and validating the relevant CRL (or OCSP response) for any certificate involved in a KMIP operation before submitting the request. If the client registers a certificate that the CRL shows as revoked, or attempts to re-key a key pair associated with a revoked certificate, the KMIP server has no protocol-level obligation to detect and reject this.

## Implementation Notes

Deployments that need server-side revocation checking must implement it as server policy outside the KMIP protocol specification. Clients that rely on KMIP for PKI workflows should build CRL and OCSP checking into their pre-submission logic, particularly for Certificate Register and Certify operations involving externally issued certificates.

## Related Concepts

See [Certify and Re-certify](certify-and-re-certify.md) and [Compromised Objects](compromised-objects.md).
