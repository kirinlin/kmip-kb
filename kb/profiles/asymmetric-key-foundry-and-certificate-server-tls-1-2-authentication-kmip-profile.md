---
title: Asymmetric Key Foundry and Certificate Server TLS 1.2 Authentication KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.20"
status: reviewed
related: ["tls-1-2-authentication-suite", "basic-asymmetric-key-foundry-and-certificate-server-kmip-profile", "asymmetric-key-foundry-and-certificate-client-tls-1-2-authentication-kmip-profile", "asymmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile", "certificate-server-tls-1-2-authentication-kmip-profile"]
keywords: ["asymmetric key", "certificate", "Create Key Pair", "PKI", "TLS 1.2", "authentication suite", "server profile"]
---

# Asymmetric Key Foundry and Certificate Server TLS 1.2 Authentication KMIP Profile

## Overview

The Asymmetric Key Foundry and Certificate Server TLS 1.2 Authentication KMIP Profile is the TLS 1.2 variant of the [Basic Asymmetric Key Foundry and Certificate Server KMIP Profile](basic-asymmetric-key-foundry-and-certificate-server-kmip-profile.md). It is the most comprehensive asymmetric-key server capability in KMIP v1.1 with TLS 1.2: Create Key Pair for server-side RSA key generation plus Register/Get/Locate/Destroy on both key pairs and X.509 certificates, all over the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md).

The companion client profile is the [Asymmetric Key Foundry and Certificate Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-and-certificate-client-tls-1-2-authentication-kmip-profile.md).

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Basic Asymmetric Key Foundry and Certificate Server (Create Key Pair + full lifecycle on RSA key pairs and X.509 certificates) |
| Authentication | TLS 1.2 Authentication Suite |

## Implications for Implementers

- All capability requirements from the [Basic Asymmetric Key Foundry and Certificate Server](basic-asymmetric-key-foundry-and-certificate-server-kmip-profile.md) apply unchanged.
- This profile supports the full generate-then-certify PKI workflow under TLS 1.2 mutual authentication, making it appropriate for regulated environments that require both PKI lifecycle management and explicit TLS 1.2 transport compliance.

## Related Concepts

[Basic Asymmetric Key Foundry and Certificate Server KMIP Profile](basic-asymmetric-key-foundry-and-certificate-server-kmip-profile.md) ·
[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Asymmetric Key Foundry and Certificate Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-and-certificate-client-tls-1-2-authentication-kmip-profile.md) ·
[Asymmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile.md)
