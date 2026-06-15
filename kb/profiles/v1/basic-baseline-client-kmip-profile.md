---
title: Basic Baseline Client KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.22"
status: reviewed
related: ["basic-authentication-suite", "basic-baseline-server-kmip-profile", "baseline-client-tls-1-2-authentication-kmip-profile", "base-profiles"]
keywords: ["baseline client", "Basic Authentication Suite", "conformance", "v1.1", "client profile"]
---

# Basic Baseline Client KMIP Profile

## Overview

The Basic Baseline Client KMIP Profile defines the standard client conformance point for KMIP v1.1 deployments using the [Basic Authentication Suite](../authentication/basic-authentication-suite.md). It is the v1.1 equivalent of the Baseline Client described in [Base Profiles](../base-encoding/base-profiles.md) for v2.x, carrying the same core mandatory client-side operations paired with the Basic authentication option.

The companion server profile is the [Basic Baseline Server KMIP Profile](basic-baseline-server-kmip-profile.md). For the TLS 1.2 variant, see [Baseline Client TLS 1.2 Authentication KMIP Profile](baseline-client-tls-1-2-authentication-kmip-profile.md).

## Required Operations

The client must support Get, Get Attributes, Locate, and Query, plus Discover Versions for version negotiation. It must handle standard message envelope elements and core attribute types. Create and other object-creation operations are not required at the baseline level — a client that only retrieves and inspects objects can claim this profile without implementing key-creation flows.

## Implications for Implementers

- The Baseline Client is the minimum useful KMIP client. All higher-capability v1.1 client profiles build on this foundation.
- Call Query and Discover Versions at session startup to confirm the server's capability surface before sending managed-object requests.
- If your deployment requires TLS 1.2 mutual authentication, target [Baseline Client TLS 1.2 Authentication KMIP Profile](baseline-client-tls-1-2-authentication-kmip-profile.md).

## Related Concepts

[Basic Authentication Suite](../authentication/basic-authentication-suite.md) ·
[Basic Baseline Server KMIP Profile](basic-baseline-server-kmip-profile.md) ·
[Baseline Client TLS 1.2 Authentication KMIP Profile](baseline-client-tls-1-2-authentication-kmip-profile.md) ·
[Base Profiles](../base-encoding/base-profiles.md)
