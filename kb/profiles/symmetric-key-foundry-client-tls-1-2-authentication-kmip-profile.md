---
title: Symmetric Key Foundry Client TLS 1.2 Authentication KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.35"
status: draft
related: ["tls-1-2-authentication-suite", "basic-symmetric-key-foundry-client-kmip-profile", "symmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile", "symmetric-key-store-client-tls-1-2-authentication-kmip-profile"]
keywords: ["symmetric key", "Create", "TLS 1.2", "AES", "key generation", "authentication suite", "client profile"]
---

# Symmetric Key Foundry Client TLS 1.2 Authentication KMIP Profile

## Overview

The Symmetric Key Foundry Client TLS 1.2 Authentication KMIP Profile is the TLS 1.2 variant of the [Basic Symmetric Key Foundry Client KMIP Profile](basic-symmetric-key-foundry-client-kmip-profile.md). It provides Create and Get on AES Symmetric Key objects (server-side key generation), with the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) mandated for transport.

The companion server profile is the [Symmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile](symmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile.md). For TLS 1.2 key storage (no generation), see [Symmetric Key Store Client TLS 1.2 Authentication KMIP Profile](symmetric-key-store-client-tls-1-2-authentication-kmip-profile.md).

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Basic Symmetric Key Foundry Client (Create/Get on AES Symmetric Key objects) |
| Authentication | TLS 1.2 Authentication Suite |

## Implications for Implementers

- Capability requirements are unchanged from the [Basic Symmetric Key Foundry Client](basic-symmetric-key-foundry-client-kmip-profile.md); only the transport requirements differ.
- Server-side key generation over a TLS 1.2 mutually authenticated channel is the secure pattern for environments where symmetric keys must never traverse unprotected connections.

## Related Concepts

[Basic Symmetric Key Foundry Client KMIP Profile](basic-symmetric-key-foundry-client-kmip-profile.md) ·
[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Symmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile](symmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile.md) ·
[Symmetric Key Store Client TLS 1.2 Authentication KMIP Profile](symmetric-key-store-client-tls-1-2-authentication-kmip-profile.md)
