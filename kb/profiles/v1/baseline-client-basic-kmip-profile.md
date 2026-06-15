---
title: Baseline Client Basic KMIP Profile
category: profile
spec_version: "1.2"
spec_versions: ["1.2"]
source_section: "prof-4.3"
status: reviewed
related: ["basic-authentication-suite", "baseline-client-tls-v1-2-kmip-profile", "baseline-server-basic-kmip-profile", "basic-baseline-client-kmip-profile", "base-profiles"]
keywords: ["baseline client", "Basic Authentication Suite", "conformance", "v1.2", "client profile"]
---

# Baseline Client Basic KMIP Profile

## Overview

The Baseline Client Basic KMIP Profile is the KMIP v1.2 name for the standard baseline client conformance point using the [Basic Authentication Suite](../authentication/basic-authentication-suite.md). It is the renaming of the [Basic Baseline Client KMIP Profile](basic-baseline-client-kmip-profile.md) from v1.1, with the same word-order adjustment applied across all v1.2 profiles (capability tier first, authentication variant last). Capability requirements are substantively unchanged.

The companion server profile is the [Baseline Server Basic KMIP Profile](baseline-server-basic-kmip-profile.md). For the TLS 1.2 variant, see [Baseline Client TLS v1.2 KMIP Profile](baseline-client-tls-v1-2-kmip-profile.md). The v2.x successor is the Baseline Client tier within [Base Profiles](../base-encoding/base-profiles.md).

## Required Operations

The client must support Get, Get Attributes, Locate, Query, and Discover Versions, plus standard message-envelope handling. No key-creation operations are required at the baseline level.

## Implications for Implementers

- This profile is the minimum client conformance point for KMIP v1.2 deployments. All higher-capability v1.2 profiles build on this baseline.
- The naming change from v1.1 to v1.2 is cosmetic only; implementations claiming the v1.1 Basic Baseline Client profile satisfy this profile as well.

## Related Concepts

[Basic Authentication Suite](../authentication/basic-authentication-suite.md) ·
[Basic Baseline Client KMIP Profile](basic-baseline-client-kmip-profile.md) ·
[Baseline Client TLS v1.2 KMIP Profile](baseline-client-tls-v1-2-kmip-profile.md) ·
[Baseline Server Basic KMIP Profile](baseline-server-basic-kmip-profile.md) ·
[Base Profiles](../base-encoding/base-profiles.md)
