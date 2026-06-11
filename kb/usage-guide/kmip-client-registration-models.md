---
title: KMIP Client Registration Models
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-4.6"
status: draft
related: ["authentication", "discover-versions"]
keywords: ["client registration", "manual registration", "automated registration", "X.509 certificate", "TLS", "bootstrapping", "sub-client"]
---

# KMIP Client Registration Models

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

Establishing the initial trust relationship between a KMIP client and a KMIP server — including the exchange of X.509 certificates and other authentication material — is called client registration. KMIP defines three models: manual registration, automated registration, and sub-client registration via a trusted primary client.

## Guidance

**Manual Registration**: The server administrator creates an out-of-band package containing the client's certificate and the server's certificate (and optionally additional credential material). The administrator installs this package in the client environment. All subsequent communication uses the exchanged certificates. KMIP itself is not required to be the transport for this initial exchange.

**Automated Registration**: The client comes pre-provisioned with a bootstrap credential (e.g., a manufacturer-installed certificate). On first contact, the client uses this credential to establish an initial TLS session and sends its bootstrap certificate to the server. The server — possibly after administrator approval — returns the equivalent of a manual registration package. The client then uses the returned certificate for all subsequent connections.

The server distinguishes an automated registration initiation from a normal Register operation and handles it accordingly.

**Sub-client Registration**: A trusted primary client registers sub-clients under its identity. The server may send a tenant identifier to the primary client, which sub-clients must present along with their own credentials. The server accepts sub-clients based on the combination of the tenant identifier, the sub-client certificate, and (optionally) the sub-client's network address relative to the primary client's address.

## Implementation Notes

None of these registration workflows is specified end-to-end by KMIP, so interoperability for the initial setup phase depends on vendor-specific documentation. The Query Client Registration Methods function allows a client to discover which automated registration approaches a server supports, which is the starting point for implementing automated registration in a multi-vendor environment.

## Related Concepts

See [Authentication](authentication.md) for credential handling after registration is complete.
