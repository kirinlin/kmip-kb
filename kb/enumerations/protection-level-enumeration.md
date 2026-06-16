---
title: Protection Level Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "11.42"
status: reviewed
related: ["protection-level", "protection-storage-mask", "sensitive"]
keywords: ["protection level", "software protection", "hardware module", "HSM", "FIPS 140", "key protection tier", "420145", "ProtectionLevel"]
tag_hex: "420145"
xml_text: "ProtectionLevel"
---

# Protection Level Enumeration

## Overview

The Protection Level enumeration classifies the minimum physical or logical security environment required to store and process a key or secret object. It is the type of the [Protection Level attribute](../attributes/protection-level.md), enabling servers and clients to express protection requirements in a standardized way. A server that cannot meet the stated level for an object should refuse the operation rather than silently storing the key in a less-secure environment.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| High | `00000001` | `High` |  |
| Low | `00000002` | `Low` |  |

- **Software**: The key material is stored and processed solely under operating-system-level software access controls, with no dedicated cryptographic hardware.
- **Hardware**: The key material is stored in or processed by dedicated cryptographic hardware that provides additional protection beyond OS controls — such as a hardware accelerator or TPM — but may not be a formally certified HSM.
- **FIPS 140-2 Level 1**: Meets the basic FIPS 140-2 validated module requirements (algorithmic correctness, documentation) but does not require physical security beyond standard components.
- **FIPS 140-2 Level 2**: Adds tamper-evidence requirements (e.g., epoxy coatings, pick-resistant locks) on top of Level 1.
- **FIPS 140-2 Level 3**: Adds tamper-resistance (attempts to destroy key material) and identity-based authentication.
- **FIPS 140-2 Level 4**: The highest level — adds environmental attack protection and continuous monitoring against physical penetration.

## Examples

A root CA private key requires **FIPS 140-2 Level 3** or higher. A short-lived session encryption key for a low-risk application might be acceptable at **Software**. Policy enforcement on the server can reject Create or Register requests that cannot meet the attribute's stated level.

## Related

[Protection Level attribute](../attributes/protection-level.md) · [Protection Storage Mask](../encoding/protection-storage-mask.md) · [Sensitive attribute](../attributes/sensitive.md)
