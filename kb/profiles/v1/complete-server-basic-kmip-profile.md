---
title: Complete Server Basic KMIP Profile
category: profile
spec_version: "1.2"
spec_versions: ["1.2"]
source_section: "prof-4.5"
status: reviewed
related: ["basic-authentication-suite", "complete-server-tls-v1-2-kmip-profile", "complete-server-profile", "baseline-server-basic-kmip-profile"]
keywords: ["complete server", "Basic Authentication Suite", "full compliance", "conformance", "v1.2"]
---

# Complete Server Basic KMIP Profile

## Overview

The Complete Server Basic KMIP Profile defines the highest server conformance tier for KMIP v1.2 deployments using the [Basic Authentication Suite](../authentication/basic-authentication-suite.md). A server claiming this profile implements the entire KMIP v1.2 specification — every object type, attribute, operation, and message structure — paired with the Basic authentication option. It is the v1.2 predecessor of the [Complete Server Profile](../base-encoding/complete-server-profile.md) in v2.x.

For the TLS 1.2 variant of the same capability, see [Complete Server TLS v1.2 KMIP Profile](complete-server-tls-v1-2-kmip-profile.md).

## Requirements

A Complete Server must satisfy all mandatory requirements of the KMIP v1.2 specification: the full set of operations (including Create, Create Key Pair, Register, Re-key, Locate, Get, Get Attributes, Activate, Revoke, Destroy, Query, Discover Versions, Get Usage Allocation, Obtain Lease, and all server-to-client operations), all object types (Symmetric Key, Asymmetric Key, Certificate, Secret Data, Opaque Managed Object), and all attribute and message structures.

## When to Claim This Profile

The Complete Server profile is most relevant for:
- Reference implementations used in interoperability plugfests.
- Test harnesses that need to respond to any well-formed KMIP v1.2 request.
- Key management services that must serve heterogeneous fleets of clients claiming different v1.x profiles.

## Implications for Implementers

- Claiming this profile is a strong statement: it asserts full KMIP v1.2 spec coverage. Ensure that all operations including rarely-exercised ones (Get Usage Allocation, Obtain Lease, Archive, Recover) are implemented.
- For environments that also require TLS 1.2 mutual authentication, use [Complete Server TLS v1.2 KMIP Profile](complete-server-tls-v1-2-kmip-profile.md).
- The v2.x successor, [Complete Server Profile](../base-encoding/complete-server-profile.md), dropped the authentication-suite distinction.

## Related Concepts

[Basic Authentication Suite](../authentication/basic-authentication-suite.md) ·
[Complete Server TLS v1.2 KMIP Profile](complete-server-tls-v1-2-kmip-profile.md) ·
[Complete Server Profile](../base-encoding/complete-server-profile.md) ·
[Baseline Server Basic KMIP Profile](baseline-server-basic-kmip-profile.md)
