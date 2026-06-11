---
title: Complete Server TLS v1.2 KMIP Profile
category: profile
spec_version: "1.2"
spec_versions: ["1.2"]
source_section: "prof-4.6"
status: draft
related: ["tls-1-2-authentication-suite", "complete-server-basic-kmip-profile", "complete-server-profile", "baseline-server-tls-v1-2-kmip-profile"]
keywords: ["complete server", "TLS 1.2", "authentication suite", "full compliance", "conformance", "v1.2"]
---

# Complete Server TLS v1.2 KMIP Profile

## Overview

The Complete Server TLS v1.2 KMIP Profile is the highest server conformance tier for KMIP v1.2 deployments using the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md). A server claiming this profile implements the entire KMIP v1.2 specification with TLS 1.2 mutual authentication mandated for all connections. It is the TLS 1.2 variant of the [Complete Server Basic KMIP Profile](complete-server-basic-kmip-profile.md).

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Complete Server (all KMIP v1.2 operations, object types, and attributes) |
| Authentication | TLS 1.2 Authentication Suite |

## When to Claim This Profile

This profile is appropriate for full-compliance KMIP v1.2 server implementations in regulated environments where TLS 1.2 mutual authentication is a hard requirement. It combines the broadest possible capability surface with the stricter transport security option.

## Implications for Implementers

- All capability requirements from [Complete Server Basic](complete-server-basic-kmip-profile.md) apply unchanged; only the transport requirements differ.
- This is the profile to target for regulated environments (financial services, healthcare, government) that need both full KMIP compliance and explicit TLS 1.2 transport certification.
- The v2.x successor, [Complete Server Profile](complete-server-profile.md), uses the updated Basic Authentication Suite which mandates TLS 1.3.

## Related Concepts

[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Complete Server Basic KMIP Profile](complete-server-basic-kmip-profile.md) ·
[Complete Server Profile](complete-server-profile.md) ·
[Baseline Server TLS v1.2 KMIP Profile](baseline-server-tls-v1-2-kmip-profile.md)
