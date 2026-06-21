---
title: Key Role Type Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.26"
status: reviewed
related: ["split-key", "create-split-key", "join-split-key"]
keywords: ["key role", "split key", "BDK", "KEK", "PIN", "payment", "DEK", "CVK", "base derivation key", "420083", "KeyRoleType"]
tag_hex: "420083"
xml_text: "KeyRoleType"
tag_type: "Enumeration"
---

# Key Role Type Enumeration

## Overview

The Key Role Type enumeration identifies the functional role of a cryptographic key within a split-key scheme and specifically within payment card industry key hierarchies. When a master key is split across multiple shares using a secret-sharing scheme, each share inherits the role of the original key. The role type allows key management systems to enforce policy based on what the key is used for — for example, restricting which operations are permitted on a Base Derivation Key versus a PIN Encryption Key. This enumeration is most prevalent in payment and financial system integrations. It appears in [Split Key](../objects/split-key.md) objects.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| BDK | `00000001` | `BDK` |  |
| CVK | `00000002` | `CVK` |  |
| DEK | `00000003` | `DEK` |  |
| MKAC | `00000004` | `MKAC` |  |
| MKSMC | `00000005` | `MKSMC` |  |
| MKSMI | `00000006` | `MKSMI` |  |
| MKDAC | `00000007` | `MKDAC` |  |
| MKDN | `00000008` | `MKDN` |  |
| MKCP | `00000009` | `MKCP` |  |
| MKOTH | `0000000A` | `MKOTH` |  |
| KEK | `0000000B` | `KEK` |  |
| MAC16609 | `0000000C` | `MAC16609` |  |
| MAC97971 | `0000000D` | `MAC97971` |  |
| MAC97972 | `0000000E` | `MAC97972` |  |
| MAC97973 | `0000000F` | `MAC97973` |  |
| MAC97974 | `00000010` | `MAC97974` |  |
| MAC97975 | `00000011` | `MAC97975` |  |
| ZPK | `00000012` | `ZPK` |  |
| PVKIBM | `00000013` | `PVKIBM` |  |
| PVKPVV | `00000014` | `PVKPVV` |  |
| PVKOTH | `00000015` | `PVKOTH` |  |
| DUKPT | `00000016` | `DUKPT` |  |
| IV | `00000017` | `IV` |  |
| TRKBK | `00000018` | `TRKBK` |  |

**Derivation and master keys:**
- **BDK** (Base Derivation Key): The root key from which session keys, device-specific keys, or PIN encryption keys are derived in triple-DES payment key hierarchies (e.g., DUKPT).
- **CVK** (Card Verification Key): Used to compute and verify the Card Verification Value printed on payment cards.
- **DEK** (Data Encryption Key): Encrypts cardholder data, transaction records, or other application data.
- **MKAC** / **MKSMC** / **MKSMI** / **MKDAC** / **MKDN** / **MKCP** / **MKOTH**: A family of EMV application master key types used to derive session keys for application cryptograms (AC), secure messaging confidentiality (SMC), secure messaging integrity (SMI), data authentication code (DAC), dynamic number (DN), card personalisation (CP), and other uses.

**Key encryption keys:**
- **KEK** (Key Encryption Key): Wraps or encrypts other keys for secure transport. KEKs are central to key hierarchy management.

**MAC keys:**
- **MAC16609** / **MAC97971-3** / **MAC97971-4** / **MAC97971-6**: Payment-specific MAC keys aligned with ISO 16609 and ISO 9797-1 MAC algorithms used in ATM and POS terminal message authentication.

**PIN and encryption keys:**
- **PIN** (PIN Encryption Key, also PEK): Encrypts or protects a cardholder's Personal Identification Number during transmission between a PIN entry device and the processing host.
- **PGK** (PIN Generation Key): Generates or encrypts PINs during card personalisation.
- **PEK** (Private Encryption Key): A general-purpose key used in HSM-based encryption workflows, distinct from PIN encryption.

## Examples

A payment HSM managing a DUKPT terminal hierarchy stores the Base Derivation Key as a split key with role **BDK**, distributed across two trusted users with each holding one share. When merging the shares to re-inject the key into a new terminal, KMIP Join Split Key reconstructs the BDK from its parts.

## Related

- [Split Key object](../objects/split-key.md) — the managed object type that carries split key material and role information
- [Create Split Key operation](../operations/create-split-key.md) — creates split key shares
- [Join Split Key operation](../operations/join-split-key.md) — reassembles the key from shares
