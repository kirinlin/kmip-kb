---
title: Capability Information
category: ttlv
spec_version: "2.1"
spec_versions: ["1.3", "1.4", "2.0", "2.1"]
source_section: "7.5"
v1_source_section: "2.1.21"
status: reviewed
related: ["profile-information", "validation-information", "correlation-value"]
keywords: ["capability information", "streaming capability", "asynchronous capability", "destroy action", "unwrap mode"]
tag_hex: "4200F7"
xml_element: "CapabilityInformation"
---

# Capability Information

## Overview

Feature flags for a KMIP implementation, returned by
[Query](../operations/query.md) (Query Capabilities) since 1.3. Where
[Profile Information](profile-information.md) names conformance bundles,
this structure answers specific operational questions: can you stream? do
you answer asynchronously? what does Destroy actually do to the bytes?

## Encoding (Tag / Type / Length / Value)

Structure, tag `4200F7`; every field optional:

| Field | Tag | XML Element | Type |
|---|---|---|---|
| Streaming Capability | `4200EF` | `StreamingCapability` | Boolean |
| Asynchronous Capability | `4200F0` | `AsynchronousCapability` | Boolean |
| Attestation Capability | `4200F1` | `AttestationCapability` | Boolean |
| Batch Undo Capability | `4200F9` | `BatchUndoCapability` | Boolean (1.4) |
| Batch Continue Capability | `4200FA` | `BatchContinueCapability` | Boolean (1.4) |
| Unwrap Mode | `4200F2` | `UnwrapMode` | Enumeration — Processed, Not Processed, Unspecified |
| Destroy Action | `4200F3` | `DestroyAction` | Enumeration — Key Material Deleted/Shredded, Meta Data Deleted/Shredded, Deleted, Shredded, Unspecified |
| Shredding Algorithm | `4200F4` | `ShreddingAlgorithm` | Enumeration — Cryptographic, Unsupported, Unspecified |
| RNG Mode | `4200F5` | `RNGMode` | Enumeration — Shared / Non-Shared Instantiation, Unspecified |

## Fields & Structure

The booleans gate protocol features: streaming
([Correlation Value](correlation-value.md) flows), asynchronous responses
([Poll](../operations/poll.md)/[Cancel](../operations/cancel.md)),
attestation, and the 1.4 batch-error options Undo and Continue. The
enumerations describe semantics: Unwrap Mode says whether a wrapped key
registered with the server is stored as-received or unwrapped first; Destroy
Action and Shredding Algorithm say how thorough
[Destroy](../operations/destroy.md) is; RNG Mode says whether the
[RNG](rng-parameters.md) instance is shared across clients.

## Examples

A client checks Capability Information before relying on `Undo` batch
semantics: { Asynchronous Capability = True, Batch Undo Capability = True,
Destroy Action = Key Material Shredded } means batched provisioning can be
rolled back and destroyed keys are unrecoverable.

## Related

[Profile Information](profile-information.md) ·
[Validation Information](validation-information.md) ·
[Batch Error Continuation Option](batch-error-continuation-option.md)
