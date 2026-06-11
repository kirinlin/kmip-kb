---
title: Basic Asymmetric Key Foundry and Server KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.8"
status: draft
related: ["basic-authentication-suite", "basic-asymmetric-key-store-server-kmip-profile", "basic-asymmetric-key-foundry-client-kmip-profile", "asymmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile", "asymmetric-key-lifecycle-profiles"]
keywords: ["asymmetric key", "key generation", "Create Key Pair", "RSA", "Basic Authentication Suite", "key foundry"]
---

# Basic Asymmetric Key Foundry and Server KMIP Profile

## Overview

The Basic Asymmetric Key Foundry and Server KMIP Profile extends the [Basic Asymmetric Key Store Server](basic-asymmetric-key-store-server-kmip-profile.md) with server-side key-pair generation. The "Foundry" designation means the server can generate RSA key pairs on demand via Create Key Pair, rather than only storing externally supplied material. It uses the [Basic Authentication Suite](basic-authentication-suite.md).

The companion client profile is the [Basic Asymmetric Key Foundry Client KMIP Profile](basic-asymmetric-key-foundry-client-kmip-profile.md). For the TLS 1.2 variant, see [Asymmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile.md).

## Required Operations and Objects

All requirements of the [Basic Asymmetric Key Store Server](basic-asymmetric-key-store-server-kmip-profile.md) apply, plus Create Key Pair. The server must generate RSA key pairs and correctly distribute the resulting `Private Key Unique Identifier` and `Public Key Unique Identifier` in the Create Key Pair response. Key format support must include PKCS#1, PKCS#8, and Transparent RSA formats.

## Implications for Implementers

- A Foundry server is the preferred pattern when the environment requires that private key material never leave the secure boundary — the private key is generated inside the server and clients never see the raw material unless they explicitly retrieve it.
- Create Key Pair must support at least the key sizes required by the [Asymmetric Key Lifecycle Profiles](asymmetric-key-lifecycle-profiles.md) (RSA-2048 minimum; RSA-3072 or RSA-4096 recommended for new keys).
- If certificates for generated keys must also be stored, upgrade to the [Basic Asymmetric Key Foundry and Certificate Server](basic-asymmetric-key-foundry-and-certificate-server-kmip-profile.md) profile.

## Related Concepts

[Basic Authentication Suite](basic-authentication-suite.md) ·
[Basic Asymmetric Key Store Server KMIP Profile](basic-asymmetric-key-store-server-kmip-profile.md) ·
[Basic Asymmetric Key Foundry Client KMIP Profile](basic-asymmetric-key-foundry-client-kmip-profile.md) ·
[Asymmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile.md) ·
[Asymmetric Key Lifecycle Profiles](asymmetric-key-lifecycle-profiles.md)
