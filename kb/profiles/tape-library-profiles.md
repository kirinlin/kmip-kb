---
title: Tape Library Profiles
category: profile
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "prof-5.12"
status: draft
related: ["base-profiles", "storage-array-with-self-encrypting-drives-profiles", "symmetric-key-lifecycle-profiles"]
keywords: ["tape library", "LTO", "KAD", "Application Specific Information", "Alternative Name", "barcode", "encryption key management"]
---

# Tape Library Profiles

## Overview

The Tape Library Profiles define how a tape library acting as a KMIP client interacts with a key management server to obtain AES-256 symmetric keys for LTO tape encryption. The profile addresses the tape-specific challenge of mapping between numeric KAD (Key Associated Data) bytes embedded in the tape format and the human-readable identifiers held by the KMIP server.

## KAD to KMIP Identifier Mapping

Tape hardware stores key identifiers in the authenticated and unauthenticated KAD fields of the tape format. The profile defines a deterministic conversion: each byte of the KAD is represented as exactly two uppercase hex characters, unauthenticated KAD first, then authenticated KAD concatenated. This hex string becomes the Application Data stored in the `Application Specific Information` attribute. Application Namespace identifiers follow the pattern `LIBRARY-{drive-generation}` — e.g., `LIBRARY-LTO`, `LIBRARY-LTO4`, `LIBRARY-LTO5`, `LIBRARY-LTO6` (v1.x); later versions added `LIBRARY-LTO7` and beyond. For backward compatibility with pre-standard deployments, servers may also accept `VENDOR-LIBRARY-LTO` namespaces (where the `VENDOR-` prefix is treated as opaque and the key is looked up as if the namespace were `LIBRARY-LTO`).

Key identifiers are created by the client (tape library), not the server. The client guarantees uniqueness within the Application Namespace.

## Barcode in Alternative Name

The tape's media barcode is stored as an `Alternative Name` attribute with type `Uninterpreted Text String`. It is used by server administrators to find the key associated with a specific tape cartridge, not by the client for normal encryption/decryption lookups (because barcodes are not guaranteed unique across namespaces). The client uses Application Specific Information for lookup.

## Client

A Tape Library Client extends the [Baseline Client](base-profiles.md), should implement `Application Specific Information` with client-generated Application Data, must support `Alternative Name` (from KMIP 1.2), and must store the barcode there at first use. Vendor Attributes that duplicate standard attributes are discouraged. For KMIP 1.0 and 1.1 (before `Alternative Name` existed), clients may instead store the barcode in a Custom Attribute named `x-Barcode` of type Text String.

## Server

A Tape Library Server extends the [Baseline Server](base-profiles.md) and adds:
- **Object**: Symmetric Key
- **Attributes**: `Alternative Name`, `Application Specific Information`, `Cryptographic Algorithm`, `Name`, `Vendor Attribute`
- **Operation**: Create
- **Algorithm**: AES-256 with Raw key format
- **Vendor attribute capacity**: minimum 30 vendor attributes per object, minimum 255-character values and names
- **Batch support**: Batch Count from 1 to 32, with Batch Order Option True

## Mandatory Test Cases

Test case identifiers encode the protocol version in their numeric suffix (`-10` = KMIP 1.0, `-11` = 1.1, `-12` = 1.2, `-21` = 2.1). Both clients and servers must pass all mandatory test cases for their declared version. For KMIP v2.1: `TL-M-1-21` — Query server capabilities; `TL-M-2-21` — Create an AES-256 key with Application Specific Information and Alternative Name barcode; `TL-M-3-21` — Locate the key via Application Specific Information, retrieve it, optionally update custom attributes, and destroy as cleanup.

## Permitted Test Case Variations

When validating against these test cases, the following values may legitimately differ between implementations without being deemed non-conformant: `UniqueIdentifier`, `UniqueBatchItemIdentifier`, `TimeStamp`, datetime attributes, and extensions reported in `Query` (`ExtensionList`, `ExtensionMap`, `ApplicationNamespaces`).

## Implications for Implementers

- The byte-by-byte KAD conversion is critical for interoperability: a mismatch in hex representation (lowercase vs uppercase, wrong concatenation order) will cause the Locate to fail.
- The 30-vendor-attribute capacity requirement exists because tape drive vendors pack rich metadata (serial numbers, drive bay IDs, write-protect flags) into vendor attributes. In the v1.x standalone document the minimum attribute value length is 256 characters and the minimum attribute name length is 64 characters; the v2.x profile (prof-5.12) specifies 255 characters for both.
- Application Specific Information uniquely identifies a key for read/write purposes; Alternative Name (barcode) is for human administration only — never use barcode for programmatic key lookup.
- The server must accept Custom Attributes of types Text String, Integer, and DateTime — not just Text String. Servers that restrict custom attribute types to strings will be non-conformant for tape library workflows that store numeric or timestamp metadata.
- For KMIP 1.0–1.2, the normative source was the standalone OASIS companion document (`kmip-tape-lib-profile/v1.0`). The profile was subsequently absorbed into KMIP-Prof, where it appears at `prof-5.12` in v2.x.

## Related Concepts

[Base Profiles](base-profiles.md) ·
[Storage Array with Self-Encrypting Drives Profiles](storage-array-with-self-encrypting-drives-profiles.md) ·
[Symmetric Key Lifecycle Profiles](symmetric-key-lifecycle-profiles.md)
