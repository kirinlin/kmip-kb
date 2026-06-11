---
title: Certificate Client TLS 1.2 Authentication KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.39"
status: draft
related: ["tls-1-2-authentication-suite", "basic-certificate-client-kmip-profile", "certificate-server-tls-1-2-authentication-kmip-profile", "asymmetric-key-and-certificate-store-client-tls-1-2-authentication-kmip-profile"]
keywords: ["certificate", "X.509", "PKI", "TLS 1.2", "Register", "authentication suite", "client profile"]
---

# Certificate Client TLS 1.2 Authentication KMIP Profile

## Overview

The Certificate Client TLS 1.2 Authentication KMIP Profile is the TLS 1.2 variant of the [Basic Certificate Client KMIP Profile](basic-certificate-client-kmip-profile.md). It provides Register and Get on X.509 Certificate objects, with the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) mandated for transport.

The companion server profile is the [Certificate Server TLS 1.2 Authentication KMIP Profile](certificate-server-tls-1-2-authentication-kmip-profile.md). To also manage key pairs with TLS 1.2, see [Asymmetric Key and Certificate Store Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-and-certificate-store-client-tls-1-2-authentication-kmip-profile.md).

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Basic Certificate Client (Register/Get/Locate on X.509 Certificate objects) |
| Authentication | TLS 1.2 Authentication Suite |

## Implications for Implementers

- Capability requirements are unchanged from the [Basic Certificate Client](basic-certificate-client-kmip-profile.md); only the transport requirements differ.
- Use this profile for certificate-repository clients in regulated environments where TLS 1.2 mutual authentication is mandated.

## Related Concepts

[Basic Certificate Client KMIP Profile](basic-certificate-client-kmip-profile.md) ·
[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Certificate Server TLS 1.2 Authentication KMIP Profile](certificate-server-tls-1-2-authentication-kmip-profile.md) ·
[Asymmetric Key and Certificate Store Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-and-certificate-store-client-tls-1-2-authentication-kmip-profile.md)
