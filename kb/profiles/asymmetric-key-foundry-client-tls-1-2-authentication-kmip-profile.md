---
title: Asymmetric Key Foundry Client TLS 1.2 Authentication KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.38"
status: reviewed
related: ["tls-1-2-authentication-suite", "basic-asymmetric-key-foundry-client-kmip-profile", "asymmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile", "asymmetric-key-foundry-and-certificate-client-tls-1-2-authentication-kmip-profile"]
keywords: ["asymmetric key", "Create Key Pair", "RSA", "TLS 1.2", "key generation", "authentication suite", "client profile"]
---

# Asymmetric Key Foundry Client TLS 1.2 Authentication KMIP Profile

## Overview

The Asymmetric Key Foundry Client TLS 1.2 Authentication KMIP Profile is the TLS 1.2 variant of the [Basic Asymmetric Key Foundry Client KMIP Profile](basic-asymmetric-key-foundry-client-kmip-profile.md). It provides Create Key Pair and Get on RSA key pairs (server-side generation), with the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) mandated for transport.

The companion server profile is the [Asymmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile.md). To also manage certificates with TLS 1.2, see [Asymmetric Key Foundry and Certificate Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-and-certificate-client-tls-1-2-authentication-kmip-profile.md).

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Basic Asymmetric Key Foundry Client (Create Key Pair/Get on RSA key pairs) |
| Authentication | TLS 1.2 Authentication Suite |

## Implications for Implementers

- Capability requirements are unchanged from the [Basic Asymmetric Key Foundry Client](basic-asymmetric-key-foundry-client-kmip-profile.md); only the transport requirements differ.
- Requesting server-side RSA key generation over a TLS 1.2 mutually authenticated channel ensures that the resulting key identifiers are only transmitted to verified, authorized clients.

## Related Concepts

[Basic Asymmetric Key Foundry Client KMIP Profile](basic-asymmetric-key-foundry-client-kmip-profile.md) ·
[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Asymmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile.md) ·
[Asymmetric Key Foundry and Certificate Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-and-certificate-client-tls-1-2-authentication-kmip-profile.md)
