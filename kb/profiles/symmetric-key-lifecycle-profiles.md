---
title: Symmetric Key Lifecycle Profiles
category: profile
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "prof-5.6"
status: draft
related: ["base-profiles", "symmetric-key-foundry-for-fips-140-profiles", "asymmetric-key-lifecycle-profiles", "cryptographic-profiles"]
keywords: ["symmetric key", "key lifecycle", "Create", "AES", "3DES", "key management"]
---

# Symmetric Key Lifecycle Profiles

## Overview

The Symmetric Key Lifecycle Profiles define what a KMIP server must support to manage the full lifecycle of symmetric keys — creation, activation, use, deactivation, and destruction — on behalf of KMIP clients. This profile family has existed since the earliest KMIP version and reflects the core use case of enterprise key management for data-at-rest encryption.

## Client

A Symmetric Key Lifecycle Client extends the [Baseline Client](base-profiles.md) with the ability to request symmetric key operations from the server. No additional operations are mandatory on the client side beyond the Baseline — the client may invoke any operation the server supports and may choose which of the lifecycle steps to drive.

## Server

A Symmetric Key Lifecycle Server extends the [Baseline Server](base-profiles.md) and adds:
- **Object**: Symmetric Key
- **Attributes**: `Cryptographic Algorithm`, `Object Type`, `Process Start Date`, `Protect Stop Date`
- **Operation**: Create
- **Algorithm support**: AES (required) and 3DES
- **Key formats**: Raw and Transparent Symmetric Key

## Mandatory Test Cases

Test case identifiers encode the protocol version in their numeric suffix (`-10` = KMIP 1.0, `-11` = 1.1, `-12` = 1.2, `-21` = 2.1). For KMIP v2.1, `SKLC-M-1-21`, `SKLC-M-2-21`, and `SKLC-M-3-21` exercise the create-activate-get-revoke-destroy lifecycle for AES symmetric keys. `SKLC-O-1-21` (optional) exercises additional attribute handling.

Unlike profiles where clients need only pass a subset of test cases, the Symmetric Key Lifecycle profile requires **both clients and servers** to pass all mandatory test cases for their declared KMIP version.

## Permitted Test Case Variations

When validating against these test cases, the following values may legitimately differ between implementations without being deemed non-conformant: `UniqueIdentifier`, `UniqueBatchItemIdentifier`, `TimeStamp`, key material for server-generated objects, and datetime attributes (`ActivationDate`, `InitialDate`, `LastChangeDate`, etc.) when not fixed in the request. Cryptographic output in `Data`/`SignatureData`/`MACData` may also vary when inherently non-deterministic.

## Implications for Implementers

- The Symmetric Key Lifecycle Profile is the entry point for data-at-rest key management. Start here when building a KMIP server for disk encryption, database encryption, or file-level encryption use cases.
- `Process Start Date` and `Protect Stop Date` govern the operational window: Process Start is when the key may begin protecting new data; Protect Stop is when it must stop doing so (but may still be used to decrypt previously protected data). These are distinct from `Activation Date` and `Deactivation Date`, which bound the overall cryptographic validity window.
- 3DES support is for legacy interoperability; prefer AES for new deployments.
- For KMIP 1.0–1.2, the normative source was the standalone OASIS companion document (`kmip-sym-key-profile/v1.0`). The profile was subsequently absorbed into KMIP-Prof, where it appears at `prof-5.6` in v2.x.

## Related Concepts

[Base Profiles](base-profiles.md) ·
[Symmetric Key Foundry for FIPS 140 Profiles](symmetric-key-foundry-for-fips-140-profiles.md) ·
[Asymmetric Key Lifecycle Profiles](asymmetric-key-lifecycle-profiles.md) ·
[Cryptographic Profiles](cryptographic-profiles.md)
