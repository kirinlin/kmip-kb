---
title: Complete Server Profile
category: profile
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "prof-5.2"
status: reviewed
related: ["base-profiles", "kmip-server-implementation-conformance"]
keywords: ["complete server", "full compliance", "conformance", "interoperability"]
---

# Complete Server Profile

## Overview

The Complete Server Profile is the highest conformance tier for a KMIP server. A server claiming this profile implements the entire KMIP specification: every object type, attribute, operation, message element, and encoding. It is effectively an "all of the above" profile rather than a use-case-specific bundle.

## Requirements

A Complete Server must satisfy [KMIP Server Implementation Conformance](kmip-server-implementation-conformance.md), then add support for every Objects section, Object Data Structures, Object Attributes, Attribute Data Structures, Operations, Operations Data Structures, Messages, Message Data Structures, Message Protocols, Enumerations, and Bit Masks defined in [KMIP-SPEC]. Vendor extensions that do not contradict any KMIP requirements are permitted.

## When to Claim This Profile

Most production deployments target a specific subset of the protocol. The Complete Server Profile is most relevant for:
- Reference implementations used in OASIS interoperability plugfests.
- Test harnesses that need to respond correctly to any well-formed request.
- Key management services that must serve heterogeneous fleets of clients claiming different profiles.

In practice, a server that passes the mandatory test cases for every individual use-case profile (Symmetric Key Lifecycle, Asymmetric Key Lifecycle, Cryptographic, and so on) will be close to — but not identical to — a Complete Server, because some spec surface is exercised only by explicit test cases at the Complete Server level.

## Implications for Implementers

- Validate against every section of KMIP-SPEC, not just the sections your primary use case touches. Features like `Usage Limits`, `Archive`/`Recover`, and split-key operations have small but non-trivial surface areas.
- The Complete Server profile does not require passing test cases from every sub-profile — only the baseline `BL-M-*` cases are normatively cited. However, every practical deployment should run the full profile test matrix before claiming completeness.
- Consider the Complete Server Profile as a documentation commitment, not just an implementation goal. Clients expecting complete coverage will exercise edge cases that narrower profiles never exercise.

## Related Concepts

[Base Profiles](base-profiles.md) ·
[KMIP Server Implementation Conformance](kmip-server-implementation-conformance.md)
