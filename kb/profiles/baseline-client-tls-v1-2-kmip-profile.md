---
title: Baseline Client TLS v1.2 KMIP Profile
category: profile
spec_version: "1.2"
spec_versions: ["1.2"]
source_section: "prof-4.4"
status: reviewed
related: ["tls-1-2-authentication-suite", "baseline-client-basic-kmip-profile", "baseline-server-tls-v1-2-kmip-profile", "baseline-client-tls-1-2-authentication-kmip-profile", "base-profiles"]
keywords: ["baseline client", "TLS 1.2", "authentication suite", "conformance", "v1.2", "client profile"]
---

# Baseline Client TLS v1.2 KMIP Profile

## Overview

The Baseline Client TLS v1.2 KMIP Profile is the KMIP v1.2 name for the baseline client conformance point with TLS 1.2 transport, using the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md). It is the renaming of the [Baseline Client TLS 1.2 Authentication KMIP Profile](baseline-client-tls-1-2-authentication-kmip-profile.md) from v1.1. Capability requirements are unchanged.

The companion server profile is the [Baseline Server TLS v1.2 KMIP Profile](baseline-server-tls-v1-2-kmip-profile.md). For the Basic Authentication variant, see [Baseline Client Basic KMIP Profile](baseline-client-basic-kmip-profile.md).

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Baseline Client (Get/Get Attributes/Locate/Query/Discover Versions) |
| Authentication | TLS 1.2 Authentication Suite |

## Implications for Implementers

- This is the minimum client conformance point for v1.2 deployments that mandate TLS 1.2 mutual authentication. The naming change from v1.1 is cosmetic only.
- For v2.x, TLS 1.3 is the minimum under the Basic Authentication Suite; there is no separate TLS v1.2 client profile in v2.x.

## Related Concepts

[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Baseline Client Basic KMIP Profile](baseline-client-basic-kmip-profile.md) ·
[Baseline Server TLS v1.2 KMIP Profile](baseline-server-tls-v1-2-kmip-profile.md) ·
[Baseline Client TLS 1.2 Authentication KMIP Profile](baseline-client-tls-1-2-authentication-kmip-profile.md) ·
[Base Profiles](base-profiles.md)
