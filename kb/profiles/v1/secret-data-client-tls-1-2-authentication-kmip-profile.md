---
title: Secret Data Client TLS 1.2 Authentication KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.33"
status: reviewed
related: ["tls-1-2-authentication-suite", "basic-secret-data-client-kmip-profile", "secret-data-server-tls-1-2-authentication-kmip-profile"]
keywords: ["secret data", "TLS 1.2", "password", "token", "authentication suite", "client profile"]
---

# Secret Data Client TLS 1.2 Authentication KMIP Profile

## Overview

The Secret Data Client TLS 1.2 Authentication KMIP Profile is the TLS 1.2 variant of the [Basic Secret Data Client KMIP Profile](basic-secret-data-client-kmip-profile.md). It provides the same capability — Register and Get on Secret Data objects (passwords, tokens, PINs) — with the [TLS 1.2 Authentication Suite](../authentication/tls-1-2-authentication-suite.md) mandated for transport.

The companion server profile is the [Secret Data Server TLS 1.2 Authentication KMIP Profile](secret-data-server-tls-1-2-authentication-kmip-profile.md).

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Basic Secret Data Client (Register/Get on Secret Data objects) |
| Authentication | TLS 1.2 Authentication Suite |

## Implications for Implementers

- All capability requirements from the [Basic Secret Data Client](basic-secret-data-client-kmip-profile.md) apply unchanged; only the transport requirements differ.
- Credential management is a security-sensitive workload; TLS 1.2 mutual authentication ensures that both the server's identity and the client's identity are verified before any secret material is exchanged.

## Related Concepts

[Basic Secret Data Client KMIP Profile](basic-secret-data-client-kmip-profile.md) ·
[TLS 1.2 Authentication Suite](../authentication/tls-1-2-authentication-suite.md) ·
[Secret Data Server TLS 1.2 Authentication KMIP Profile](secret-data-server-tls-1-2-authentication-kmip-profile.md)
