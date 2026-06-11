---
title: Certify and Re-certify
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.39"
status: draft
related: ["certificate-renewal-update-and-re-key", "private-key"]
keywords: ["Certify", "Re-certify", "CA", "certificate request", "PKCS#10", "PEM", "CRMF", "Proof-of-Possession"]
---

# Certify and Re-certify

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

The Certify operation submits a certificate request to the KMIP server (which may embed a CA or proxy to an external CA), and the Re-certify operation renews or replaces an existing certificate. The server's handling of the CA function — whether it is embedded or proxied — is vendor-defined.

## Guidance

KMIP supports three certificate request formats: PKCS#10, PEM-encoded requests, and CRMF. All three formats support Proof-of-Possession (POP), which establishes that the requestor controls the private counterpart to the submitted public key. However, some CAs do not support POP via CRMF and rely on the surrounding certificate management protocol (CMP or CMC) instead. In such deployments, PKCS#10 or PEM is the appropriate format choice.

When a KMIP server hosts multiple CAs, the client can name a specific CA by setting the X.509 Certificate Issuer attribute on the request. If left unset, the server routes to whichever CA its policy designates.

## Implementation Notes

The choice of CA and its support for specific request formats is typically a deployment configuration decision made out-of-band. Clients in diverse environments should query the server for supported operations and test certificate workflows before production deployment. Re-certify renews an existing certificate while keeping the same key pair. When a new key pair is needed, the client should invoke Re-key Key Pair and then Certify to cover that case.

## Related Concepts

See [Certificate Renewal, Update, and Re-key](certificate-renewal-update-and-re-key.md) for the terminology and workflow details.
