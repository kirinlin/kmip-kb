---
title: Secret Data Server TLS 1.2 Authentication KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.13"
status: reviewed
related: ["tls-1-2-authentication-suite", "basic-secret-data-server-kmip-profile", "secret-data-client-tls-1-2-authentication-kmip-profile", "secret-data-tls-1-2-authentication-kmip-profile"]
keywords: ["secret data", "TLS 1.2", "password", "token", "authentication suite", "server profile"]
---

# Secret Data Server TLS 1.2 Authentication KMIP Profile

## Overview

The Secret Data Server TLS 1.2 Authentication KMIP Profile is the TLS 1.2 variant of the [Basic Secret Data Server KMIP Profile](basic-secret-data-server-kmip-profile.md). It adds Secret Data object support (Register, Get, Locate, Destroy on opaque secrets such as passwords, tokens, and PINs) to the baseline server capability, with the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) mandated for transport.

The companion client profile is the [Secret Data Client TLS 1.2 Authentication KMIP Profile](secret-data-client-tls-1-2-authentication-kmip-profile.md). The v1.0 combined predecessor using TLS 1.2 is the [Secret Data TLS 1.2 Authentication KMIP Profile](secret-data-tls-1-2-authentication-kmip-profile.md).

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Basic Secret Data Server (Register/Get/Locate/Destroy on Secret Data objects) |
| Authentication | TLS 1.2 Authentication Suite |

## Implications for Implementers

- All capability requirements from the [Basic Secret Data Server](basic-secret-data-server-kmip-profile.md) apply unchanged; only the transport layer differs.
- This profile is appropriate for credential-management deployments where TLS 1.2 mutual authentication is a compliance requirement.

## Related Concepts

[Basic Secret Data Server KMIP Profile](basic-secret-data-server-kmip-profile.md) ·
[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Secret Data Client TLS 1.2 Authentication KMIP Profile](secret-data-client-tls-1-2-authentication-kmip-profile.md) ·
[Secret Data TLS 1.2 Authentication KMIP Profile](secret-data-tls-1-2-authentication-kmip-profile.md)
