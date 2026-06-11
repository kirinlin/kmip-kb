---
title: Certificate Server TLS 1.2 Authentication KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.19"
status: draft
related: ["tls-1-2-authentication-suite", "basic-certificate-server-kmip-profile", "certificate-client-tls-1-2-authentication-kmip-profile", "asymmetric-key-and-certificate-store-server-tls-1-2-authentication-kmip-profile"]
keywords: ["certificate", "X.509", "PKI", "TLS 1.2", "Register", "authentication suite", "server profile"]
---

# Certificate Server TLS 1.2 Authentication KMIP Profile

## Overview

The Certificate Server TLS 1.2 Authentication KMIP Profile is the TLS 1.2 variant of the [Basic Certificate Server KMIP Profile](basic-certificate-server-kmip-profile.md). It provides X.509 certificate storage and retrieval (Register, Get, Locate, Destroy on Certificate objects) with the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) mandated for transport.

The companion client profile is the [Certificate Client TLS 1.2 Authentication KMIP Profile](certificate-client-tls-1-2-authentication-kmip-profile.md). To add asymmetric key management alongside certificate storage with TLS 1.2, see [Asymmetric Key and Certificate Store Server TLS 1.2 Authentication KMIP Profile](asymmetric-key-and-certificate-store-server-tls-1-2-authentication-kmip-profile.md).

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Basic Certificate Server (Register/Get/Locate/Destroy on X.509 Certificate objects) |
| Authentication | TLS 1.2 Authentication Suite |

## Implications for Implementers

- All capability requirements from the [Basic Certificate Server](basic-certificate-server-kmip-profile.md) apply unchanged; only the transport requirements differ.
- Suitable for certificate-repository deployments where TLS 1.2 mutual authentication is a compliance requirement.

## Related Concepts

[Basic Certificate Server KMIP Profile](basic-certificate-server-kmip-profile.md) ·
[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Certificate Client TLS 1.2 Authentication KMIP Profile](certificate-client-tls-1-2-authentication-kmip-profile.md) ·
[Asymmetric Key and Certificate Store Server TLS 1.2 Authentication KMIP Profile](asymmetric-key-and-certificate-store-server-tls-1-2-authentication-kmip-profile.md)
