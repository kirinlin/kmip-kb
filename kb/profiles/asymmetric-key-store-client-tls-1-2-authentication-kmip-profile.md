---
title: Asymmetric Key Store Client TLS 1.2 Authentication KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.36"
status: draft
related: ["tls-1-2-authentication-suite", "basic-asymmetric-key-store-client-kmip-profile", "asymmetric-key-store-server-tls-1-2-authentication-kmip-profile", "asymmetric-key-foundry-client-tls-1-2-authentication-kmip-profile"]
keywords: ["asymmetric key", "RSA", "key store", "TLS 1.2", "Register", "authentication suite", "client profile"]
---

# Asymmetric Key Store Client TLS 1.2 Authentication KMIP Profile

## Overview

The Asymmetric Key Store Client TLS 1.2 Authentication KMIP Profile is the TLS 1.2 variant of the [Basic Asymmetric Key Store Client KMIP Profile](basic-asymmetric-key-store-client-kmip-profile.md). It provides Register and Get on RSA Public Key and Private Key objects, with the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) mandated for transport.

The companion server profile is the [Asymmetric Key Store Server TLS 1.2 Authentication KMIP Profile](asymmetric-key-store-server-tls-1-2-authentication-kmip-profile.md). For TLS 1.2 key generation, see [Asymmetric Key Foundry Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-client-tls-1-2-authentication-kmip-profile.md).

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Basic Asymmetric Key Store Client (Register/Get on RSA Public Key and Private Key objects) |
| Authentication | TLS 1.2 Authentication Suite |

## Implications for Implementers

- Capability requirements are unchanged from the [Basic Asymmetric Key Store Client](basic-asymmetric-key-store-client-kmip-profile.md); only the transport requirements differ.
- Private key material is especially sensitive; the TLS 1.2 mutual-authentication requirement ensures that RSA private keys are only deposited or retrieved over a verified, encrypted channel.

## Related Concepts

[Basic Asymmetric Key Store Client KMIP Profile](basic-asymmetric-key-store-client-kmip-profile.md) ·
[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Asymmetric Key Store Server TLS 1.2 Authentication KMIP Profile](asymmetric-key-store-server-tls-1-2-authentication-kmip-profile.md) ·
[Asymmetric Key Foundry Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-client-tls-1-2-authentication-kmip-profile.md)
