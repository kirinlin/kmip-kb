---
title: Baseline Server TLS v1.2 KMIP Profile
category: profile
spec_version: "1.2"
spec_versions: ["1.2"]
source_section: "prof-4.2"
status: draft
related: ["tls-1-2-authentication-suite", "baseline-server-basic-kmip-profile", "baseline-client-tls-v1-2-kmip-profile", "baseline-server-tls-1-2-authentication-kmip-profile", "base-profiles"]
keywords: ["baseline server", "TLS 1.2", "authentication suite", "conformance", "v1.2", "server profile"]
---

# Baseline Server TLS v1.2 KMIP Profile

## Overview

The Baseline Server TLS v1.2 KMIP Profile is the KMIP v1.2 name for the baseline server conformance point with TLS 1.2 transport, using the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md). It is the renaming of the [Baseline Server TLS 1.2 Authentication KMIP Profile](baseline-server-tls-1-2-authentication-kmip-profile.md) from v1.1. The profile name was simplified in v1.2 to "Baseline Server TLS v1.2" rather than "Baseline Server TLS 1.2 Authentication"; the capability requirements are substantively unchanged.

The companion client profile is the [Baseline Client TLS v1.2 KMIP Profile](baseline-client-tls-v1-2-kmip-profile.md). For the Basic Authentication variant, see [Baseline Server Basic KMIP Profile](baseline-server-basic-kmip-profile.md).

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Baseline Server (v1.2 equivalent of Baseline Server Basic) |
| Authentication | TLS 1.2 Authentication Suite |

## Implications for Implementers

- KMIP v1.2 only changed the profile name, not the capability or transport requirements. Implementations that passed the v1.1 Baseline Server TLS 1.2 Authentication test suite will typically satisfy this profile.
- For v2.x successors, the Basic Authentication Suite in v2.x mandates TLS 1.3; there is no separate TLS 1.2 variant in v2.x.

## Related Concepts

[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Baseline Server Basic KMIP Profile](baseline-server-basic-kmip-profile.md) ·
[Baseline Client TLS v1.2 KMIP Profile](baseline-client-tls-v1-2-kmip-profile.md) ·
[Baseline Server TLS 1.2 Authentication KMIP Profile](baseline-server-tls-1-2-authentication-kmip-profile.md) ·
[Base Profiles](base-profiles.md)
