---
title: Basic Symmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile
category: profile
spec_version: "1.0"
spec_versions: ["1.0"]
source_section: "prof-4.6"
status: draft
related: ["tls-1-2-authentication-suite", "basic-symmetric-key-foundry-and-server-kmip-profile", "symmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile"]
keywords: ["symmetric key", "key foundry", "key generation", "TLS 1.2", "Create", "AES", "authentication suite"]
---

# Basic Symmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile

## Overview

The Basic Symmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile is the TLS 1.2 variant of the [Basic Symmetric Key Foundry and Server KMIP Profile](basic-symmetric-key-foundry-and-server-kmip-profile.md). The capability layer is unchanged — Register, Create, Get, Locate, Activate, Revoke, and Destroy on AES Symmetric Key objects, including server-side key generation — but the channel uses the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md). It is a KMIP v1.0 combined client-and-server profile.

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Basic Symmetric Key Foundry and Server (Create/Register/Get/Locate/Activate/Revoke/Destroy, AES Symmetric Key) |
| Authentication | TLS 1.2 Authentication Suite (TLS 1.2 mandatory, mutual cert auth, port 5696) |

## Implications for Implementers

- Use this profile for KMIP v1.0 deployments where the server generates symmetric keys and the channel must be explicitly TLS 1.2.
- For KMIP v1.1 and later, the equivalent TLS 1.2 foundry capability is split across [Symmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile](symmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile.md) (server) and a corresponding client profile.
- Capability and key-material requirements are identical to the non-TLS variant; only the channel constraints differ.

## Related Concepts

[Basic Symmetric Key Foundry and Server KMIP Profile](basic-symmetric-key-foundry-and-server-kmip-profile.md) ·
[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Symmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile](symmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile.md)
