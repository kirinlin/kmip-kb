---
title: Basic Symmetric Key Store and Server TLS 1.2 Authentication KMIP Profile
category: profile
spec_version: "1.0"
spec_versions: ["1.0"]
source_section: "prof-4.5"
status: reviewed
related: ["tls-1-2-authentication-suite", "basic-symmetric-key-store-and-server-kmip-profile", "symmetric-key-store-and-server-tls-1-2-authentication-kmip-profile"]
keywords: ["symmetric key", "key store", "TLS 1.2", "AES", "Register", "authentication suite"]
---

# Basic Symmetric Key Store and Server TLS 1.2 Authentication KMIP Profile

## Overview

The Basic Symmetric Key Store and Server TLS 1.2 Authentication KMIP Profile is the TLS 1.2 variant of the [Basic Symmetric Key Store and Server KMIP Profile](basic-symmetric-key-store-and-server-kmip-profile.md). The capability layer is identical — Register, Get, Locate, Activate, Revoke, and Destroy on AES Symmetric Key objects — but the channel layer uses the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) instead of the Basic Authentication Suite. It is a KMIP v1.0 combined client-and-server profile.

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Basic Symmetric Key Store and Server (Register/Get/Locate/Activate/Revoke/Destroy, AES Symmetric Key) |
| Authentication | TLS 1.2 Authentication Suite (TLS 1.2 mandatory, mutual cert auth, port 5696) |

## Implications for Implementers

- Use this profile when your security policy requires TLS 1.2 specifically for symmetric key storage operations in a v1.0-era deployment.
- For KMIP v1.1 and later, the equivalent TLS 1.2 capability is represented in the [Symmetric Key Store and Server TLS 1.2 Authentication KMIP Profile](symmetric-key-store-and-server-tls-1-2-authentication-kmip-profile.md) with separate server and client roles.
- Capability requirements are unchanged from the non-TLS variant; the only difference is the mandatory TLS 1.2 channel and cipher suite constraints.

## Related Concepts

[Basic Symmetric Key Store and Server KMIP Profile](basic-symmetric-key-store-and-server-kmip-profile.md) ·
[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Symmetric Key Store and Server TLS 1.2 Authentication KMIP Profile](symmetric-key-store-and-server-tls-1-2-authentication-kmip-profile.md)
