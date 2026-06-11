---
title: Asymmetric Key and Certificate Store Client TLS 1.2 Authentication KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.37"
status: draft
related: ["tls-1-2-authentication-suite", "basic-asymmetric-key-and-certificate-store-client-kmip-profile", "asymmetric-key-and-certificate-store-server-tls-1-2-authentication-kmip-profile", "asymmetric-key-foundry-and-certificate-client-tls-1-2-authentication-kmip-profile"]
keywords: ["asymmetric key", "certificate", "PKI", "TLS 1.2", "RSA", "authentication suite", "client profile"]
---

# Asymmetric Key and Certificate Store Client TLS 1.2 Authentication KMIP Profile

## Overview

The Asymmetric Key and Certificate Store Client TLS 1.2 Authentication KMIP Profile is the TLS 1.2 variant of the [Basic Asymmetric Key and Certificate Store Client KMIP Profile](basic-asymmetric-key-and-certificate-store-client-kmip-profile.md). It provides Register and Get on RSA Public Key, Private Key, and X.509 Certificate objects, with the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) mandated for transport.

The companion server profile is the [Asymmetric Key and Certificate Store Server TLS 1.2 Authentication KMIP Profile](asymmetric-key-and-certificate-store-server-tls-1-2-authentication-kmip-profile.md). For TLS 1.2 with key generation alongside certificate storage, see [Asymmetric Key Foundry and Certificate Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-and-certificate-client-tls-1-2-authentication-kmip-profile.md).

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Basic Asymmetric Key and Certificate Store Client (RSA key pairs + X.509 certificates, Register/Get/Locate) |
| Authentication | TLS 1.2 Authentication Suite |

## Implications for Implementers

- Capability requirements are unchanged from the [Basic Asymmetric Key and Certificate Store Client](basic-asymmetric-key-and-certificate-store-client-kmip-profile.md); only the transport requirements differ.
- This profile is appropriate for PKI integration clients that manage key-certificate pairs in regulated environments requiring TLS 1.2 mutual authentication.

## Related Concepts

[Basic Asymmetric Key and Certificate Store Client KMIP Profile](basic-asymmetric-key-and-certificate-store-client-kmip-profile.md) ·
[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Asymmetric Key and Certificate Store Server TLS 1.2 Authentication KMIP Profile](asymmetric-key-and-certificate-store-server-tls-1-2-authentication-kmip-profile.md) ·
[Asymmetric Key Foundry and Certificate Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-and-certificate-client-tls-1-2-authentication-kmip-profile.md)
