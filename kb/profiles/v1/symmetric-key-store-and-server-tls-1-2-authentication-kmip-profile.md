---
title: Symmetric Key Store and Server TLS 1.2 Authentication KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.14"
status: reviewed
related: ["tls-1-2-authentication-suite", "basic-symmetric-key-store-and-server-kmip-profile", "symmetric-key-store-client-tls-1-2-authentication-kmip-profile", "symmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile"]
keywords: ["symmetric key", "key store", "TLS 1.2", "AES", "Register", "authentication suite", "server profile"]
---

# Symmetric Key Store and Server TLS 1.2 Authentication KMIP Profile

## Overview

The Symmetric Key Store and Server TLS 1.2 Authentication KMIP Profile is the TLS 1.2 variant of the [Basic Symmetric Key Store and Server KMIP Profile](basic-symmetric-key-store-and-server-kmip-profile.md). It provides symmetric key storage (client-provided via Register, no server-side generation) with the [TLS 1.2 Authentication Suite](../authentication/tls-1-2-authentication-suite.md) mandated for transport.

The companion client profile is the [Symmetric Key Store Client TLS 1.2 Authentication KMIP Profile](symmetric-key-store-client-tls-1-2-authentication-kmip-profile.md). For server-side key generation with TLS 1.2, see [Symmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile](symmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile.md).

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Symmetric Key Store and Server (Register/Get/Locate/Activate/Revoke/Destroy, AES Symmetric Key) |
| Authentication | TLS 1.2 Authentication Suite |

## Implications for Implementers

- Capability requirements are identical to the [Basic Symmetric Key Store and Server](basic-symmetric-key-store-and-server-kmip-profile.md); only the transport layer differs.
- Use this profile in enterprise environments where TLS 1.2 mutual authentication is required for symmetric key management operations.

## Related Concepts

[Basic Symmetric Key Store and Server KMIP Profile](basic-symmetric-key-store-and-server-kmip-profile.md) ·
[TLS 1.2 Authentication Suite](../authentication/tls-1-2-authentication-suite.md) ·
[Symmetric Key Store Client TLS 1.2 Authentication KMIP Profile](symmetric-key-store-client-tls-1-2-authentication-kmip-profile.md) ·
[Symmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile](symmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile.md)
