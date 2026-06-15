---
title: Profile Version
category: ttlv
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "7.32"
status: reviewed
related: ["server-information", "query", "protocol-version"]
keywords: ["profile version", "profile name", "KMIP profile", "conformance profile", "server capabilities"]
---

# Profile Version

## Overview

Profile Version is a structure that identifies a KMIP conformance profile by name and version number. KMIP profiles define subsets of the protocol — combinations of operations, object types, and encodings — that are sufficient for particular use cases or certification tiers (Baseline, Complete, etc.). A server includes Profile Version structures in its [Query](../operations/query.md) response to declare which profiles it conforms to, allowing clients to determine which profile-defined features they can rely on.

## Encoding (Tag / Type / Length / Value)

Profile Version encodes as a Structure.

| Field | Tag | XML Element | Type | Required |
|---|---|---|---|---|
| Profile Name | `42010F` | `ProfileName` | Enumeration | Yes |
| Profile Version Major | `420110` | `ProfileVersionMajor` | Integer | Yes |
| Profile Version Minor | `420111` | `ProfileVersionMinor` | Integer | Yes |

All three fields are required. Profile Name identifies the profile; Profile Version Major and Minor together express the profile version as a two-component integer tuple.

## Fields & Structure

**Profile Name** is an Enumeration from the set of profile names defined in the KMIP Profiles document. Each named profile (Baseline Server, Complete Server, Storage Array with Self-Encrypting Drive, Tape Library, etc.) has a distinct enumeration value.

**Profile Version Major** and **Profile Version Minor** together identify the version of that profile the server implements. For example, a server conforming to the Baseline Server KMIP Profile version 2.1 would carry Major = 2, Minor = 1. Note that profile versions may advance independently of the core KMIP spec version.

Clients that need to verify whether a server supports a specific profile should check the Profile Version entries in the Query response against their requirements before sending profile-specific operations.

## Examples

A Query response from a server conforming to three profiles might include three Profile Version structures:

- Profile Name = Baseline Server, Major = 2, Minor = 1
- Profile Name = Complete Server, Major = 2, Minor = 1
- Profile Name = Storage Array with Self-Encrypting Drive, Major = 1, Minor = 0

A client that requires the Complete Server profile inspects this list to confirm it is present before relying on any Complete Server-specific features.

## Related

[Server Information](server-information.md) · [Query](../operations/query.md) · [Protocol Version](protocol-version.md)
