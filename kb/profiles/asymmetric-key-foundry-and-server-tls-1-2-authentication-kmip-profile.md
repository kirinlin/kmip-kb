---
title: Asymmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.18"
status: draft
related: ["tls-1-2-authentication-suite", "basic-asymmetric-key-foundry-and-server-kmip-profile", "asymmetric-key-foundry-client-tls-1-2-authentication-kmip-profile", "asymmetric-key-and-certificate-store-server-tls-1-2-authentication-kmip-profile"]
keywords: ["asymmetric key", "Create Key Pair", "RSA", "TLS 1.2", "key generation", "authentication suite", "server profile"]
---

# Asymmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile

## Overview

The Asymmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile is the TLS 1.2 variant of the [Basic Asymmetric Key Foundry and Server KMIP Profile](basic-asymmetric-key-foundry-and-server-kmip-profile.md). It adds server-side RSA key-pair generation (Create Key Pair) to the asymmetric key store capability, with the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) mandated for transport.

The companion client profile is the [Asymmetric Key Foundry Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-client-tls-1-2-authentication-kmip-profile.md). To add certificate storage alongside key generation with TLS 1.2, see [Asymmetric Key Foundry and Certificate Server TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-and-certificate-server-tls-1-2-authentication-kmip-profile.md).

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Basic Asymmetric Key Foundry and Server (Create Key Pair + Register/Get/Locate/Activate/Revoke/Destroy, RSA) |
| Authentication | TLS 1.2 Authentication Suite |

## Implications for Implementers

- Capability requirements are identical to the [Basic Asymmetric Key Foundry and Server](basic-asymmetric-key-foundry-and-server-kmip-profile.md); only the transport requirements differ.
- TLS 1.2 mutual authentication is especially valuable here: private key material generated inside the server should only be accessible to authenticated, authorized clients.

## Related Concepts

[Basic Asymmetric Key Foundry and Server KMIP Profile](basic-asymmetric-key-foundry-and-server-kmip-profile.md) ·
[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Asymmetric Key Foundry Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-client-tls-1-2-authentication-kmip-profile.md) ·
[Asymmetric Key Foundry and Certificate Server TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-and-certificate-server-tls-1-2-authentication-kmip-profile.md)
