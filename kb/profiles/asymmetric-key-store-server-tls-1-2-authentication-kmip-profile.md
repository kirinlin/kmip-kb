---
title: Asymmetric Key Store Server TLS 1.2 Authentication KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.16"
status: reviewed
related: ["tls-1-2-authentication-suite", "basic-asymmetric-key-store-server-kmip-profile", "asymmetric-key-store-client-tls-1-2-authentication-kmip-profile", "asymmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile"]
keywords: ["asymmetric key", "RSA", "key store", "TLS 1.2", "Register", "authentication suite", "server profile"]
---

# Asymmetric Key Store Server TLS 1.2 Authentication KMIP Profile

## Overview

The Asymmetric Key Store Server TLS 1.2 Authentication KMIP Profile is the TLS 1.2 variant of the [Basic Asymmetric Key Store Server KMIP Profile](basic-asymmetric-key-store-server-kmip-profile.md). It stores client-provided RSA key pairs (Register on Public Key and Private Key objects) with the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) mandated for transport.

The companion client profile is the [Asymmetric Key Store Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-store-client-tls-1-2-authentication-kmip-profile.md). For server-side key generation with TLS 1.2, see [Asymmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile.md).

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Basic Asymmetric Key Store Server (Register/Get/Locate/Activate/Revoke/Destroy, RSA Public/Private Key) |
| Authentication | TLS 1.2 Authentication Suite |

## Implications for Implementers

- Capability requirements are identical to the [Basic Asymmetric Key Store Server](basic-asymmetric-key-store-server-kmip-profile.md); only the transport layer differs.
- Particularly appropriate for deployments that handle RSA private key material — TLS 1.2 mutual authentication adds a layer of assurance that only authorized clients can deposit or retrieve private keys.

## Related Concepts

[Basic Asymmetric Key Store Server KMIP Profile](basic-asymmetric-key-store-server-kmip-profile.md) ·
[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Asymmetric Key Store Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-store-client-tls-1-2-authentication-kmip-profile.md) ·
[Asymmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile.md)
