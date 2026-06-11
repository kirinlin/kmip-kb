---
title: Asymmetric Key Foundry and Certificate Client TLS 1.2 Authentication KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.40"
status: reviewed
related: ["tls-1-2-authentication-suite", "basic-asymmetric-key-foundry-and-certificate-client-kmip-profile", "asymmetric-key-foundry-and-certificate-server-tls-1-2-authentication-kmip-profile", "asymmetric-key-foundry-client-tls-1-2-authentication-kmip-profile", "certificate-client-tls-1-2-authentication-kmip-profile"]
keywords: ["asymmetric key", "certificate", "Create Key Pair", "PKI", "TLS 1.2", "authentication suite", "client profile"]
---

# Asymmetric Key Foundry and Certificate Client TLS 1.2 Authentication KMIP Profile

## Overview

The Asymmetric Key Foundry and Certificate Client TLS 1.2 Authentication KMIP Profile is the TLS 1.2 variant of the [Basic Asymmetric Key Foundry and Certificate Client KMIP Profile](basic-asymmetric-key-foundry-and-certificate-client-kmip-profile.md). It enables the full PKI enrollment workflow — Create Key Pair plus Register on Certificate — over the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md).

The companion server profile is the [Asymmetric Key Foundry and Certificate Server TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-and-certificate-server-tls-1-2-authentication-kmip-profile.md).

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Basic Asymmetric Key Foundry and Certificate Client (Create Key Pair + Register/Get on X.509 certificates) |
| Authentication | TLS 1.2 Authentication Suite |

## Implications for Implementers

- Capability requirements are unchanged from the [Basic Asymmetric Key Foundry and Certificate Client](basic-asymmetric-key-foundry-and-certificate-client-kmip-profile.md); only the transport requirements differ.
- This profile supports the generate-then-certify PKI enrollment workflow in environments that mandate TLS 1.2 mutual authentication for all KMIP interactions.

## Related Concepts

[Basic Asymmetric Key Foundry and Certificate Client KMIP Profile](basic-asymmetric-key-foundry-and-certificate-client-kmip-profile.md) ·
[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Asymmetric Key Foundry and Certificate Server TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-and-certificate-server-tls-1-2-authentication-kmip-profile.md) ·
[Asymmetric Key Foundry Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-client-tls-1-2-authentication-kmip-profile.md)
