---
title: Asymmetric Key and Certificate Store Server TLS 1.2 Authentication KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.17"
status: draft
related: ["tls-1-2-authentication-suite", "basic-asymmetric-key-and-certificate-store-server-kmip-profile", "asymmetric-key-and-certificate-store-client-tls-1-2-authentication-kmip-profile", "asymmetric-key-foundry-and-certificate-server-tls-1-2-authentication-kmip-profile"]
keywords: ["asymmetric key", "certificate", "PKI", "TLS 1.2", "RSA", "authentication suite", "server profile"]
---

# Asymmetric Key and Certificate Store Server TLS 1.2 Authentication KMIP Profile

## Overview

The Asymmetric Key and Certificate Store Server TLS 1.2 Authentication KMIP Profile is the TLS 1.2 variant of the [Basic Asymmetric Key and Certificate Store Server KMIP Profile](basic-asymmetric-key-and-certificate-store-server-kmip-profile.md). It combines RSA key pair storage with X.509 certificate management, using the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) for transport.

The companion client profile is the [Asymmetric Key and Certificate Store Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-and-certificate-store-client-tls-1-2-authentication-kmip-profile.md). For server-side key generation plus certificate storage with TLS 1.2, see [Asymmetric Key Foundry and Certificate Server TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-and-certificate-server-tls-1-2-authentication-kmip-profile.md).

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Basic Asymmetric Key and Certificate Store Server (RSA key pairs + X.509 certificates, Register/Get/Locate/Activate/Revoke/Destroy) |
| Authentication | TLS 1.2 Authentication Suite |

## Implications for Implementers

- All capability requirements from the [Basic Asymmetric Key and Certificate Store Server](basic-asymmetric-key-and-certificate-store-server-kmip-profile.md) apply unchanged; only the transport requirements differ.
- This profile suits PKI integration servers where both key pairs and certificates are managed centrally under a TLS 1.2 mutual-authentication policy.

## Related Concepts

[Basic Asymmetric Key and Certificate Store Server KMIP Profile](basic-asymmetric-key-and-certificate-store-server-kmip-profile.md) ·
[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Asymmetric Key and Certificate Store Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-and-certificate-store-client-tls-1-2-authentication-kmip-profile.md) ·
[Asymmetric Key Foundry and Certificate Server TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-and-certificate-server-tls-1-2-authentication-kmip-profile.md)
