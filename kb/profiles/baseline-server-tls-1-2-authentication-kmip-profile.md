---
title: Baseline Server TLS 1.2 Authentication KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.12"
status: draft
related: ["tls-1-2-authentication-suite", "basic-baseline-server-kmip-profile", "baseline-client-tls-1-2-authentication-kmip-profile", "base-profiles"]
keywords: ["baseline server", "TLS 1.2", "authentication suite", "conformance", "v1.1"]
---

# Baseline Server TLS 1.2 Authentication KMIP Profile

## Overview

The Baseline Server TLS 1.2 Authentication KMIP Profile is the TLS 1.2 variant of the [Basic Baseline Server KMIP Profile](basic-baseline-server-kmip-profile.md). It carries the full baseline server capability — Create, Register, Get, Get Attributes, Get Attribute List, Locate, Destroy, Query, Discover Versions — while mandating the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) for transport security.

The companion client profile is the [Baseline Client TLS 1.2 Authentication KMIP Profile](baseline-client-tls-1-2-authentication-kmip-profile.md).

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Basic Baseline Server (full v1.1 baseline operation set) |
| Authentication | TLS 1.2 Authentication Suite (TLS 1.2 mandatory, mutual cert auth, port 5696) |

## Implications for Implementers

- Use this profile when your organizational security policy requires TLS 1.2 specifically (as opposed to allowing any TLS version supported by the Basic Authentication Suite).
- All capability requirements from the [Basic Baseline Server](basic-baseline-server-kmip-profile.md) apply unchanged. Only the transport layer requirements differ.
- Higher-capability v1.1 TLS 1.2 server profiles (symmetric key, asymmetric key, certificate) all build on this foundation.

## Related Concepts

[Basic Baseline Server KMIP Profile](basic-baseline-server-kmip-profile.md) ·
[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Baseline Client TLS 1.2 Authentication KMIP Profile](baseline-client-tls-1-2-authentication-kmip-profile.md) ·
[Base Profiles](base-profiles.md)
