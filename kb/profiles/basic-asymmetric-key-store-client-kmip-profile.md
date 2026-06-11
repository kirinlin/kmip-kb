---
title: Basic Asymmetric Key Store Client KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.26"
status: draft
related: ["basic-authentication-suite", "basic-asymmetric-key-store-server-kmip-profile", "asymmetric-key-store-client-tls-1-2-authentication-kmip-profile", "basic-asymmetric-key-foundry-client-kmip-profile"]
keywords: ["asymmetric key", "RSA", "public key", "private key", "Register", "Basic Authentication Suite", "client profile"]
---

# Basic Asymmetric Key Store Client KMIP Profile

## Overview

The Basic Asymmetric Key Store Client KMIP Profile defines client requirements for storing and retrieving asymmetric key pairs at a KMIP v1.1 server, using the [Basic Authentication Suite](basic-authentication-suite.md). A client claiming this profile provides Public Key and Private Key objects to the server via Register and retrieves them via Get. The companion server profile is the [Basic Asymmetric Key Store Server KMIP Profile](basic-asymmetric-key-store-server-kmip-profile.md).

For the TLS 1.2 variant, see [Asymmetric Key Store Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-store-client-tls-1-2-authentication-kmip-profile.md).

## Required Operations

The client must support Register and Get on Public Key and Private Key objects. RSA is the mandatory algorithm; key format support must include PKCS#1 (public keys) and PKCS#8 (private keys) at minimum.

## Implications for Implementers

- Clients in this profile typically import externally generated key pairs (HSM-generated keys, CA key pairs, TLS key pairs) into KMIP for centralized lifecycle management.
- Use distinct `Cryptographic Usage Mask` values for the public and private key to reflect their respective roles (e.g., public key for encryption and signature verification; private key for decryption and signing).
- To request server-generated key pairs instead of storing imported material, use the [Basic Asymmetric Key Foundry Client KMIP Profile](basic-asymmetric-key-foundry-client-kmip-profile.md).

## Related Concepts

[Basic Authentication Suite](basic-authentication-suite.md) ·
[Basic Asymmetric Key Store Server KMIP Profile](basic-asymmetric-key-store-server-kmip-profile.md) ·
[Basic Asymmetric Key Foundry Client KMIP Profile](basic-asymmetric-key-foundry-client-kmip-profile.md) ·
[Asymmetric Key Store Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-store-client-tls-1-2-authentication-kmip-profile.md)
