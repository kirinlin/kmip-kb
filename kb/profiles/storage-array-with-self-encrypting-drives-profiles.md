---
title: Storage Array with Self-Encrypting Drives Profiles
category: profile
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "prof-5.11"
status: draft
related: ["base-profiles", "symmetric-key-lifecycle-profiles", "tape-library-profiles"]
keywords: ["SED", "self-encrypting drive", "storage array", "authentication key", "Secret Data", "vendor attribute"]
---

# Storage Array with Self-Encrypting Drives Profiles

## Overview

The Storage Array with Self-Encrypting Drives (SA-SED) Profiles address the specific interoperability needs of storage arrays that embed self-encrypting drives. The storage array acts as the KMIP client, registering and retrieving authentication keys that unlock individual drives. The profile prescribes how these keys are typed, named, and attributed so that heterogeneous storage arrays and key management servers can interoperate.

## Client

An SA-SED Client extends the [Baseline Client](base-profiles.md) with one additional constraint: it should not use Vendor Attributes to duplicate information already expressible in standard KMIP attributes. This keeps the server's attribute schema clean and avoids interoperability breakage when a different client queries the same objects.

## Server

An SA-SED Server extends the [Baseline Server](base-profiles.md) and adds:
- **Object**: Secret Data
- **Attributes**: Vendor Attribute (Text String type)
- **Operation**: Register
- **Object Type enumeration**: Secret Data; Name Type: Uninterpreted Text String; Secret Data Type: Password
- **Vendor attribute capacity**: minimum 20 vendor attributes per object, minimum 128 characters per attribute name and value, minimum 128 characters for Name attribute values

The explicit capacity requirements address the reality that storage array vendors embed drive-serial numbers, bay identifiers, and other hardware metadata in vendor attributes. The profile ensures the server can store all of this without arbitrary truncation.

## Mandatory Test Cases

`SASED-M-1-21` performs a Query to discover server capabilities. `SASED-M-2-21` registers an authentication key with Object Group membership to simulate a new or replacement drive authentication key. `SASED-M-3-21` locates and retrieves the registered key, then destroys it as cleanup.

## Implications for Implementers

- Use `Object Group` to associate authentication keys with the storage array unit or drive group they protect. The SA-SED profile requires servers to support Object Group-based grouping, either through open attribute policies or pre-configured groups.
- `Secret Data` with type `Password` is the correct object type for authentication keys — not Symmetric Key. This distinction matters for lifecycle operations and for servers that apply different policies to different object types.
- The 128-character minimum for Vendor Attribute names and values is a hard requirement, not a recommendation. Servers that truncate silently will cause data loss.

## Related Concepts

[Base Profiles](base-profiles.md) ·
[Symmetric Key Lifecycle Profiles](symmetric-key-lifecycle-profiles.md) ·
[Tape Library Profiles](tape-library-profiles.md)
