---
title: Symmetric Key Foundry for FIPS 140 Profiles
category: profile
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "prof-5.7"
status: reviewed
related: ["base-profiles", "symmetric-key-lifecycle-profiles"]
keywords: ["FIPS 140", "key foundry", "symmetric key", "AES", "3DES", "compliance", "NIST"]
---

# Symmetric Key Foundry for FIPS 140 Profiles

## Overview

The Symmetric Key Foundry for FIPS 140 Profiles address the use case where a KMIP server acts as a central key generation service — a "foundry" — that produces symmetric keys for consumption by FIPS 140-validated cryptographic modules. The algorithm choices are constrained to those allowed under the NIST FIPS 140 validation program.

## Client Tiers

Three client tiers (Basic, Intermediate, Advanced) exist to accommodate implementations with different scopes. All three start from the [Baseline Client](base-profiles.md); the client-side obligations are identical across tiers (conform to Baseline Client, optionally extend without conflicting). The tiers are differentiated entirely by which test cases a client must pass — and a client at any given tier only needs to pass **at least one** mandatory test case from that tier's set, not all of them and not the lower tiers' sets.

## Server

A Symmetric Key Foundry Server extends the [Baseline Server](base-profiles.md) and adds:
- **Object**: Symmetric Key
- **Attributes**: `Cryptographic Algorithm`, `Cryptographic Length`, `Object Type`, `Process Start Date`, `Process Stop Date`
- **Operation**: Create
- **Algorithm support**: 3DES (168-bit) and AES (128, 192, 256-bit)
- **Key formats**: Raw and Transparent Symmetric Key

The FIPS 140 constraint means only FIPS-approved algorithms at FIPS-approved key lengths. Non-FIPS algorithms that might appear in the broader Symmetric Key Lifecycle profile are excluded.

## Mandatory Test Cases

Test case identifiers encode the tier and protocol version: `SKFF-M-N-10` (KMIP 1.0), `-11` (1.1), `-12` (1.2), `-21` (2.1). For KMIP v2.1:

- **Basic tier**: `SKFF-M-1-21` through `SKFF-M-4-21`
- **Intermediate tier**: `SKFF-M-5-21` through `SKFF-M-8-21`
- **Advanced tier**: `SKFF-M-9-21` through `SKFF-M-12-21`

Conformance requirements differ sharply by role: a **client** must pass at least one test from its declared tier only. A **server** must pass all mandatory test cases across all three tiers — Basic, Intermediate, and Advanced — making the server the comprehensive baseline that supports every client category.

## Permitted Test Case Variations

When validating against these test cases, the following values may legitimately differ between implementations without being deemed non-conformant: `UniqueIdentifier`, `UniqueBatchItemIdentifier`, `TimeStamp`, key material for server-generated objects, and datetime attributes (`ActivationDate`, `InitialDate`, `LastChangeDate`, etc.) when not fixed in the request.

## Implications for Implementers

- Use this profile when your deployment involves HSMs or software modules under FIPS 140 validation — the profile's algorithm restrictions map directly to what those modules accept.
- The three client tiers help interoperability plugfests categorize participants by capability without requiring all implementers to pass the full test suite. A Basic client need only demonstrate one key-creation scenario; an Advanced client demonstrates more complex flows.
- Key lengths of 128, 192, and 256 bits for AES are all explicitly required on the server; do not omit 192-bit even if your primary use case is 256-bit only.
- For KMIP 1.0–1.2, the normative source was the standalone OASIS companion document (`kmip-sym-foundry-profile/v1.0`). The profile was subsequently absorbed into KMIP-Prof, where it appears at `prof-5.7` in v2.x.

## Related Concepts

[Base Profiles](base-profiles.md) ·
[Symmetric Key Lifecycle Profiles](symmetric-key-lifecycle-profiles.md)
