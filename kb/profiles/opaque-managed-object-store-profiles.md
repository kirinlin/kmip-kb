---
title: Opaque Managed Object Store Profiles
category: profile
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "prof-5.10"
status: reviewed
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

Test case identifiers encode the protocol version in their numeric suffix (`-10` = KMIP 1.0, `-11` = 1.1, `-12` = 1.2, `-21` = 2.1). For KMIP v2.1, `OMOS-M-1-21` exercises registering and retrieving an opaque object. `OMOS-O-1-21` (optional) covers additional attribute handling around opaque objects. The same sequences appear under `-10`/`-11`/`-12` labels in the v1.x-era standalone companion document.

## Permitted Test Case Variations

When validating against these test cases, the following values may legitimately differ between implementations without being deemed non-conformant: `UniqueIdentifier`, `UniqueBatchItemIdentifier`, `TimeStamp`, and datetime attributes (`ActivationDate`, `InitialDate`, `LastChangeDate`, etc.) when not fixed in the request. Extensions reported in `Query` (`ExtensionList`, `ExtensionMap`, `ApplicationNamespaces`) are similarly unconstrained.

## Implications for Implementers

- Opaque objects enable a KMIP server to act as a general-purpose secure store, not just a key management service. This is useful for certificate bundles, PKCS#12 archives, or any binary artifact that must be access-controlled and audited alongside keys.
- The `Opaque Data Type` attribute classifies what kind of data the payload contains. Servers should support at least the KMIP-defined enum values for interoperability.
- Because the server never interprets the payload, lifecycle operations (Activate, Revoke, Destroy) still apply — clients must manage the opaque object's lifecycle explicitly.
- For KMIP 1.0–1.2, the normative source was the standalone OASIS companion document (`kmip-opaque-obj-profile/v1.0`). The profile was subsequently absorbed into KMIP-Prof, where it appears at `prof-5.10` in v2.x.

## Related Concepts

[Base Profiles](base-profiles.md) ·
[Tape Library Profiles](tape-library-profiles.md)
