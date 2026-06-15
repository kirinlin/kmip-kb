---
title: Storage Client KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.41"
status: reviewed
related: ["basic-authentication-suite", "storage-client-tls-1-2-authentication-kmip-profile", "opaque-managed-object-store-profiles", "basic-baseline-client-kmip-profile"]
keywords: ["storage client", "Opaque Managed Object", "opaque data", "Register", "Basic Authentication Suite", "client profile"]
---

# Storage Client KMIP Profile

## Overview

The Storage Client KMIP Profile defines client requirements for storing and retrieving opaque, uninterpreted data blobs at a KMIP v1.1 server, using the [Basic Authentication Suite](../authentication/basic-authentication-suite.md). Clients claiming this profile work with Opaque Managed Object types — arbitrary binary data that has no cryptographic structure as far as KMIP is concerned. This distinguishes the Storage Client from the [Basic Secret Data Client](basic-secret-data-client-kmip-profile.md), which specifically handles structured secret material (passwords, tokens) under the Secret Data object type.

For the TLS 1.2 variant, see [Storage Client TLS 1.2 Authentication KMIP Profile](storage-client-tls-1-2-authentication-kmip-profile.md). The corresponding server-side capability is described in [Opaque Managed Object Store Profiles](../key-management/opaque-managed-object-store-profiles.md).

## Required Operations

The client must support Register and Get on Opaque Managed Object instances. Locate allows searching by attribute; Destroy removes objects. The Opaque Data Type attribute specifies how the stored bytes should be interpreted by whatever application retrieves them.

## Implications for Implementers

- The Storage Client profile is appropriate when the data being managed does not fit the KMIP key or certificate object model — for example, encrypted archives, firmware images, configuration blobs, or vendor-specific binary artifacts that need lifecycle management and access control but not cryptographic attribute handling.
- Because KMIP does not parse the stored content, validation and integrity checking of the data value are the responsibility of the application layer.
- If the stored data is a credential (password, API key, pre-shared key), use the [Basic Secret Data Client](basic-secret-data-client-kmip-profile.md) instead, which provides more appropriate attribute semantics.

## Related Concepts

[Basic Authentication Suite](../authentication/basic-authentication-suite.md) ·
[Storage Client TLS 1.2 Authentication KMIP Profile](storage-client-tls-1-2-authentication-kmip-profile.md) ·
[Opaque Managed Object Store Profiles](../key-management/opaque-managed-object-store-profiles.md) ·
[Basic Baseline Client KMIP Profile](basic-baseline-client-kmip-profile.md)
