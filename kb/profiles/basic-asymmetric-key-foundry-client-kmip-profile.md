---
title: Basic Asymmetric Key Foundry Client KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.28"
status: reviewed
related: ["basic-authentication-suite", "basic-asymmetric-key-foundry-and-server-kmip-profile", "asymmetric-key-foundry-client-tls-1-2-authentication-kmip-profile", "basic-asymmetric-key-store-client-kmip-profile"]
keywords: ["asymmetric key", "Create Key Pair", "RSA", "Basic Authentication Suite", "client profile", "key generation"]
---

# Basic Asymmetric Key Foundry Client KMIP Profile

## Overview

The Basic Asymmetric Key Foundry Client KMIP Profile defines client requirements for requesting server-side RSA key-pair generation in KMIP v1.1, using the [Basic Authentication Suite](basic-authentication-suite.md). A client claiming this profile invokes Create Key Pair on a server that claims the [Basic Asymmetric Key Foundry and Server KMIP Profile](basic-asymmetric-key-foundry-and-server-kmip-profile.md). The private key material is generated inside the server and never exposed to the client unless explicitly retrieved.

For the TLS 1.2 variant, see [Asymmetric Key Foundry Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-client-tls-1-2-authentication-kmip-profile.md).

## Required Operations

The client must support Create Key Pair, specifying cryptographic algorithm, key length, and usage mask. Get is needed to retrieve the public key (and optionally the private key). The response to Create Key Pair includes both `Private Key Unique Identifier` and `Public Key Unique Identifier`.

## Implications for Implementers

- Server-side key generation (Foundry model) is preferred when the private key must never leave the secure boundary. The client requests generation and uses the resulting identifiers for subsequent operations without ever possessing the raw private key material.
- Always specify RSA key size explicitly in Create Key Pair. RSA-2048 is the minimum; RSA-3072 or RSA-4096 is recommended for new deployments.
- To also manage certificates associated with generated key pairs, use the [Basic Asymmetric Key Foundry and Certificate Client profile](basic-asymmetric-key-foundry-and-certificate-client-kmip-profile.md).

## Related Concepts

[Basic Authentication Suite](basic-authentication-suite.md) ·
[Basic Asymmetric Key Foundry and Server KMIP Profile](basic-asymmetric-key-foundry-and-server-kmip-profile.md) ·
[Basic Asymmetric Key Store Client KMIP Profile](basic-asymmetric-key-store-client-kmip-profile.md) ·
[Asymmetric Key Foundry Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-client-tls-1-2-authentication-kmip-profile.md)
