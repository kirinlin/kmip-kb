---
title: Symmetric Key Foundry for FIPS 140 Profiles
category: profile
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "prof-5.7"
status: draft
related: ["base-profiles", "symmetric-key-lifecycle-profiles"]
keywords: ["FIPS 140", "key foundry", "symmetric key", "AES", "3DES", "compliance", "NIST"]
---

# Symmetric Key Foundry for FIPS 140 Profiles

## Overview

The Symmetric Key Foundry for FIPS 140 Profiles address the use case where a KMIP server acts as a central key generation service — a "foundry" — that produces symmetric keys for consumption by FIPS 140-validated cryptographic modules. The algorithm choices are constrained to those allowed under the NIST FIPS 140 validation program.

## Client Tiers

Three client tiers (Basic, Intermediate, Advanced) exist to accommodate implementations with different scopes. All three start from the [Baseline Client](base-profiles.md) and differ only in which test cases they must pass. The client obligations themselves are identical across tiers: conform to Baseline Client and optionally support additional spec clauses that do not conflict with the profile.

## Server

A Symmetric Key Foundry Server extends the [Baseline Server](base-profiles.md) and adds:
- **Object**: Symmetric Key
- **Attributes**: `Cryptographic Algorithm`, `Cryptographic Length`, `Object Type`, `Process Start Date`, `Protect Stop Date`
- **Operation**: Create
- **Algorithm support**: 3DES (168-bit) and AES (128, 192, 256-bit)
- **Key formats**: Raw and Transparent Symmetric Key

The FIPS 140 constraint means only FIPS-approved algorithms at FIPS-approved key lengths. Non-FIPS algorithms that might appear in the broader Symmetric Key Lifecycle profile are excluded.

## Mandatory Test Cases

- **Basic tier**: `SKFF-M-1-21` through `SKFF-M-4-21`
- **Intermediate tier**: `SKFF-M-5-21` through `SKFF-M-8-21`
- **Advanced tier**: `SKFF-M-9-21` through `SKFF-M-12-21`

Higher tiers include all lower-tier test cases.

## Implications for Implementers

- Use this profile when your deployment involves HSMs or software modules under FIPS 140 validation — the profile's algorithm restrictions map directly to what those modules accept.
- The three client tiers help interoperability plugfests categorize participants by capability without requiring all implementers to pass the full test suite.
- Key lengths of 128, 192, and 256 bits for AES are all explicitly required; do not omit 192-bit even if your primary use case is 256-bit only.

## Related Concepts

[Base Profiles](base-profiles.md) ·
[Symmetric Key Lifecycle Profiles](symmetric-key-lifecycle-profiles.md)
