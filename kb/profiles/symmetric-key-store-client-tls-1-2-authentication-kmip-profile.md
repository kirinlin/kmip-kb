---
title: Symmetric Key Store Client TLS 1.2 Authentication KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.34"
status: draft
related: ["tls-1-2-authentication-suite", "basic-symmetric-key-store-client-kmip-profile", "symmetric-key-store-and-server-tls-1-2-authentication-kmip-profile", "symmetric-key-foundry-client-tls-1-2-authentication-kmip-profile"]
keywords: ["symmetric key", "key store", "TLS 1.2", "AES", "Register", "authentication suite", "client profile"]
---

# Symmetric Key Store Client TLS 1.2 Authentication KMIP Profile

## Overview

The Symmetric Key Store Client TLS 1.2 Authentication KMIP Profile is the TLS 1.2 variant of the [Basic Symmetric Key Store Client KMIP Profile](basic-symmetric-key-store-client-kmip-profile.md). It provides Register and Get on AES Symmetric Key objects, with the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) mandated for transport.

The companion server profile is the [Symmetric Key Store and Server TLS 1.2 Authentication KMIP Profile](symmetric-key-store-and-server-tls-1-2-authentication-kmip-profile.md). For TLS 1.2 key generation, see [Symmetric Key Foundry Client TLS 1.2 Authentication KMIP Profile](symmetric-key-foundry-client-tls-1-2-authentication-kmip-profile.md).

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Basic Symmetric Key Store Client (Register/Get on AES Symmetric Key objects) |
| Authentication | TLS 1.2 Authentication Suite |

## Implications for Implementers

- Capability requirements are unchanged from the [Basic Symmetric Key Store Client](basic-symmetric-key-store-client-kmip-profile.md); only the transport requirements differ.
- Use this profile when depositing or retrieving symmetric keys must occur over a TLS 1.2 mutually authenticated channel per organizational policy.

## Related Concepts

[Basic Symmetric Key Store Client KMIP Profile](basic-symmetric-key-store-client-kmip-profile.md) ·
[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Symmetric Key Store and Server TLS 1.2 Authentication KMIP Profile](symmetric-key-store-and-server-tls-1-2-authentication-kmip-profile.md) ·
[Symmetric Key Foundry Client TLS 1.2 Authentication KMIP Profile](symmetric-key-foundry-client-tls-1-2-authentication-kmip-profile.md)
