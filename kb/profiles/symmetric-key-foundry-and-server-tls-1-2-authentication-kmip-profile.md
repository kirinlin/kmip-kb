---
title: Symmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.15"
status: reviewed
related: ["tls-1-2-authentication-suite", "basic-symmetric-key-foundry-and-server-kmip-profile", "symmetric-key-foundry-client-tls-1-2-authentication-kmip-profile", "symmetric-key-store-and-server-tls-1-2-authentication-kmip-profile"]
keywords: ["symmetric key", "key generation", "Create", "TLS 1.2", "AES", "authentication suite", "server profile"]
---

# Symmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile

## Overview

The Symmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile is the TLS 1.2 variant of the [Basic Symmetric Key Foundry and Server KMIP Profile](basic-symmetric-key-foundry-and-server-kmip-profile.md). It adds server-side AES key generation (Create) to the symmetric key store capability, with the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) mandated for transport.

The companion client profile is the [Symmetric Key Foundry Client TLS 1.2 Authentication KMIP Profile](symmetric-key-foundry-client-tls-1-2-authentication-kmip-profile.md). For storage-only with TLS 1.2, see [Symmetric Key Store and Server TLS 1.2 Authentication KMIP Profile](symmetric-key-store-and-server-tls-1-2-authentication-kmip-profile.md).

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Symmetric Key Foundry and Server (Create/Register/Get/Locate/Activate/Revoke/Destroy, AES Symmetric Key) |
| Authentication | TLS 1.2 Authentication Suite |

## Implications for Implementers

- Capability requirements are identical to the [Basic Symmetric Key Foundry and Server](basic-symmetric-key-foundry-and-server-kmip-profile.md); only the transport layer differs.
- The TLS 1.2 channel provides mutual authentication before any key material is generated or exchanged — this is particularly important for the Create operation, where the server generates key material that may never leave the secure boundary.

## Related Concepts

[Basic Symmetric Key Foundry and Server KMIP Profile](basic-symmetric-key-foundry-and-server-kmip-profile.md) ·
[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Symmetric Key Foundry Client TLS 1.2 Authentication KMIP Profile](symmetric-key-foundry-client-tls-1-2-authentication-kmip-profile.md) ·
[Symmetric Key Store and Server TLS 1.2 Authentication KMIP Profile](symmetric-key-store-and-server-tls-1-2-authentication-kmip-profile.md)
