---
title: AES XTS Profiles
category: profile
spec_version: "2.1"
spec_versions: ["1.4", "2.0", "2.1"]
source_section: "prof-5.13"
status: draft
related: ["base-profiles", "symmetric-key-lifecycle-profiles"]
keywords: ["AES XTS", "XTS-AES", "disk encryption", "key encrypting key", "KEK", "full-disk encryption", "NVMe"]
---

# AES XTS Profiles

## Overview

The AES XTS Profiles address the specific requirements of AES in XTS (XEX-based Tweaked CodeBook mode with ciphertext Stealing) mode, which is the dominant algorithm for full-disk and sector-level encryption in NVMe SSDs, self-encrypting drives, and storage controllers. XTS requires a different key-size convention than standard AES-CBC/GCM: a nominal 256-bit XTS key is actually two 128-bit AES keys (or a 512-bit XTS key is two 256-bit AES keys), and the profile makes this explicit.

## Client

An AES XTS Client extends the [Baseline Client](base-profiles.md) with no additional mandatory operations. The client decides whether to operate with or without a Key Encrypting Key (KEK) for the XTS key itself.

## Server

An AES XTS Server extends the [Baseline Server](base-profiles.md) and adds:
- **Object**: Symmetric Key
- **Attribute**: `Object Type`
- **Operation**: Create
- **Algorithm**: AES
- **Key formats**: Raw and Transparent Symmetric Key

## Mandatory Test Cases

`AX-M-1-21` — AES XTS key creation and use without a Key Encrypting Key. `AX-M-2-21` — AES XTS with a KEK, exercising the wrapped key path.

## Implications for Implementers

- XTS key lengths in KMIP follow the underlying AES key size of one component, not the combined key length. A 256-bit AES-XTS key is represented as `Cryptographic Length = 256` (one component), not 512.
- KEK-wrapped XTS keys are the recommended deployment pattern for servers that do not want to expose raw key material: the KEK lives on the server and the XTS key is returned only in wrapped form.
- AES XTS was §5.14 in KMIP-Prof v1.4 (before Suite B was removed and the section renumbered to §5.13 in v2.0). Code that hard-codes section numbers for routing should account for this.

## Related Concepts

[Base Profiles](base-profiles.md) ·
[Symmetric Key Lifecycle Profiles](symmetric-key-lifecycle-profiles.md)
