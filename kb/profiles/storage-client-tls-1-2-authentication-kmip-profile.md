---
title: Storage Client TLS 1.2 Authentication KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.42"
status: draft
related: ["tls-1-2-authentication-suite", "storage-client-kmip-profile", "opaque-managed-object-store-profiles"]
keywords: ["storage client", "Opaque Managed Object", "TLS 1.2", "authentication suite", "client profile"]
---

# Storage Client TLS 1.2 Authentication KMIP Profile

## Overview

The Storage Client TLS 1.2 Authentication KMIP Profile is the TLS 1.2 variant of the [Storage Client KMIP Profile](storage-client-kmip-profile.md). It provides Register, Get, Locate, and Destroy on Opaque Managed Object types, with the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) mandated for transport.

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Storage Client (Register/Get/Locate/Destroy on Opaque Managed Objects) |
| Authentication | TLS 1.2 Authentication Suite |

## Implications for Implementers

- Capability requirements are unchanged from the [Storage Client KMIP Profile](storage-client-kmip-profile.md); only the transport requirements differ.
- Use this profile when organizational policy requires TLS 1.2 mutual authentication for storing arbitrary binary data artifacts under KMIP management.

## Related Concepts

[Storage Client KMIP Profile](storage-client-kmip-profile.md) ·
[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Opaque Managed Object Store Profiles](opaque-managed-object-store-profiles.md)
