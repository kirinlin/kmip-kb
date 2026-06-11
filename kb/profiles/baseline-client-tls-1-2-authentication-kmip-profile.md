---
title: Baseline Client TLS 1.2 Authentication KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.32"
status: reviewed
related: ["tls-1-2-authentication-suite", "basic-baseline-client-kmip-profile", "baseline-server-tls-1-2-authentication-kmip-profile", "base-profiles"]
keywords: ["baseline client", "TLS 1.2", "authentication suite", "conformance", "v1.1"]
---

# Baseline Client TLS 1.2 Authentication KMIP Profile

## Overview

The Baseline Client TLS 1.2 Authentication KMIP Profile is the TLS 1.2 variant of the [Basic Baseline Client KMIP Profile](basic-baseline-client-kmip-profile.md). It carries the standard baseline client capability — Get, Get Attributes, Locate, Query, Discover Versions — with the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) mandated for transport.

The companion server profile is the [Baseline Server TLS 1.2 Authentication KMIP Profile](baseline-server-tls-1-2-authentication-kmip-profile.md).

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Basic Baseline Client (Get/Get Attributes/Locate/Query/Discover Versions) |
| Authentication | TLS 1.2 Authentication Suite (TLS 1.2 mandatory, mutual cert auth, port 5696) |

## Implications for Implementers

- All capability requirements from the [Basic Baseline Client](basic-baseline-client-kmip-profile.md) apply unchanged; only the transport requirements differ.
- Higher-capability v1.1 TLS 1.2 client profiles (symmetric key, asymmetric key, certificate) all build on this foundation.

## Related Concepts

[Basic Baseline Client KMIP Profile](basic-baseline-client-kmip-profile.md) ·
[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Baseline Server TLS 1.2 Authentication KMIP Profile](baseline-server-tls-1-2-authentication-kmip-profile.md) ·
[Base Profiles](base-profiles.md)
