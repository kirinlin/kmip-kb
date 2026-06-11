---
title: Basic Symmetric Key Foundry Client KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.25"
status: draft
related: ["basic-authentication-suite", "basic-symmetric-key-foundry-and-server-kmip-profile", "symmetric-key-foundry-client-tls-1-2-authentication-kmip-profile", "basic-symmetric-key-store-client-kmip-profile"]
keywords: ["symmetric key", "key generation", "Create", "AES", "Basic Authentication Suite", "client profile"]
---

# Basic Symmetric Key Foundry Client KMIP Profile

## Overview

The Basic Symmetric Key Foundry Client KMIP Profile defines client requirements for requesting server-side symmetric key generation in KMIP v1.1, using the [Basic Authentication Suite](basic-authentication-suite.md). A client claiming this profile can invoke Create to request an AES key from the server rather than supplying its own material via Register. The server side is the [Basic Symmetric Key Foundry and Server KMIP Profile](basic-symmetric-key-foundry-and-server-kmip-profile.md).

For the TLS 1.2 variant, see [Symmetric Key Foundry Client TLS 1.2 Authentication KMIP Profile](symmetric-key-foundry-client-tls-1-2-authentication-kmip-profile.md).

## Required Operations

The client must support Create on Symmetric Key objects, specifying at minimum the cryptographic algorithm and key length. Get is required to retrieve the generated key. Locate, Activate, Revoke, and Destroy may be used for lifecycle management.

## Implications for Implementers

- Clients that only claim this profile but not the Store variant can still Register keys — the Foundry profile builds on the Store capability. Pair both if your client needs both paths.
- When invoking Create, always specify `Cryptographic Algorithm` (AES), `Cryptographic Length`, and `Cryptographic Usage Mask` explicitly rather than relying on server defaults, since defaults vary between implementations.
- If TLS 1.2 mutual authentication is required, use [Symmetric Key Foundry Client TLS 1.2 Authentication KMIP Profile](symmetric-key-foundry-client-tls-1-2-authentication-kmip-profile.md).

## Related Concepts

[Basic Authentication Suite](basic-authentication-suite.md) ·
[Basic Symmetric Key Foundry and Server KMIP Profile](basic-symmetric-key-foundry-and-server-kmip-profile.md) ·
[Basic Symmetric Key Store Client KMIP Profile](basic-symmetric-key-store-client-kmip-profile.md) ·
[Symmetric Key Foundry Client TLS 1.2 Authentication KMIP Profile](symmetric-key-foundry-client-tls-1-2-authentication-kmip-profile.md)
