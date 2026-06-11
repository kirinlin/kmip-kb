---
title: Opaque Managed Object Store Profiles
category: profile
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "prof-5.10"
status: draft
related: ["base-profiles", "tape-library-profiles"]
keywords: ["opaque object", "opaque data", "blob storage", "key management server", "Register"]
---

# Opaque Managed Object Store Profiles

## Overview

The Opaque Managed Object Store Profiles cover the use case of storing uninterpreted binary data — "opaque objects" — on a KMIP server. The server manages the object lifecycle and access control without interpreting the content. Typical uses include storing encrypted blobs, certificates in non-standard formats, or proprietary data structures that need centralized lifecycle management.

## Client

An Opaque Managed Object Store Client extends the [Baseline Client](base-profiles.md). No mandatory operations are added beyond the Baseline; the client may use Register to store objects and Get/Locate to retrieve them.

## Server

An Opaque Managed Object Store Server extends the [Baseline Server](base-profiles.md) and adds:
- **Object**: Opaque Object
- **Attribute**: `Object Type`
- **Operation**: Register
- **Enumeration**: `Opaque Data Type` (the classification of the opaque payload); `Object Type` with the value Opaque Object

## Mandatory and Optional Test Cases

`OMOS-M-1-21` exercises registering and retrieving an opaque object. `OMOS-O-1-21` (optional) covers additional attribute handling around opaque objects.

## Implications for Implementers

- Opaque objects enable a KMIP server to act as a general-purpose secure store, not just a key management service. This is useful for certificate bundles, PKCS#12 archives, or any binary artifact that must be access-controlled and audited alongside keys.
- The `Opaque Data Type` attribute classifies what kind of data the payload contains. Servers should support at least the KMIP-defined enum values for interoperability.
- Because the server never interprets the payload, lifecycle operations (Activate, Revoke, Destroy) still apply — clients must manage the opaque object's lifecycle explicitly.

## Related Concepts

[Base Profiles](base-profiles.md) ·
[Tape Library Profiles](tape-library-profiles.md)
