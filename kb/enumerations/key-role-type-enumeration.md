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
| BDK | `00000001` | `BDK` | (Base Derivation Key): The root key from which session keys, device-specific keys, or PIN encryption keys are derived in triple-DES payment key hierarchies (e.g., DUKPT). |
| CVK | `00000002` | `CVK` | (Card Verification Key): Used to compute and verify the Card Verification Value printed on payment cards. |
| DEK | `00000003` | `DEK` | (Data Encryption Key): Encrypts cardholder data, transaction records, or other application data. |
| MKAC | `00000004` | `MKAC` | (Application Master Key — Application Cryptogram): EMV issuer master key from which the chip derives session keys for generating Application Cryptograms — the transaction signatures the issuer verifies to authorise a payment. |
| MKSMC | `00000005` | `MKSMC` | (Application Master Key — Secure Messaging Confidentiality): EMV issuer master key from which session keys for encrypting issuer-to-card secure messaging command data are derived. |
| MKSMI | `00000006` | `MKSMI` | (Application Master Key — Secure Messaging Integrity): EMV issuer master key from which session keys for authenticating issuer-to-card secure messaging commands are derived. |
| MKDAC | `00000007` | `MKDAC` | (Application Master Key — Data Authentication Code): EMV issuer master key from which session keys for computing the static Data Authentication Code on card records are derived. |
| MKDN | `00000008` | `MKDN` | (Application Master Key — Dynamic Number): EMV issuer master key from which session keys for generating unpredictable Dynamic Numbers used in dynamic data authentication are derived. |
| MKCP | `00000009` | `MKCP` | (Application Master Key — Card Personalisation): EMV issuer master key from which session keys used to secure card data loading during chip personalisation are derived. |
| MKOTH | `0000000A` | `MKOTH` | (Application Master Key — Other): EMV issuer master key for proprietary or vendor-specific session key derivation not covered by the dedicated MKAC–MKCP roles. |
| KEK | `0000000B` | `KEK` | (Key Encryption Key): Wraps or encrypts other keys for secure transport. KEKs are central to key hierarchy management. |
| MAC16609 | `0000000C` | `MAC16609` | MAC key conforming to ISO 16609 (triple-DES retail MAC), used for authenticating ATM and POS financial messages in payment networks. |
| MAC97971 | `0000000D` | `MAC97971` | MAC key used with ISO 9797-1 Algorithm 1 (single-DES CBC-MAC without output transformation). |
| MAC97972 | `0000000E` | `MAC97972` | MAC key used with ISO 9797-1 Algorithm 2 (CBC-MAC with XOR of last block before final cipher). |
| MAC97973 | `0000000F` | `MAC97973` | MAC key used with ISO 9797-1 Algorithm 3 (Retail MAC — triple-DES variant widely used in payment messaging). |
| MAC97974 | `00000010` | `MAC97974` | MAC key used with ISO 9797-1 Algorithm 4 (CBC-MAC with double-length key and additional final block operation). |
| MAC97975 | `00000011` | `MAC97975` | MAC key used with ISO 9797-1 Algorithm 5 (CMAC-based construction offering stronger security guarantees). |
| ZPK | `00000012` | `ZPK` | (Zone PIN Key): Encrypts PIN blocks for transport between ATM/POS terminals and payment processing networks within a defined zone. |
| PVKIBM | `00000013` | `PVKIBM` | (PIN Verification Key — IBM): Used with IBM's PIN offset algorithm to verify PINs against a stored offset without keeping the PIN in cleartext. |
| PVKPVV | `00000014` | `PVKPVV` | (PIN Verification Key — PVV): Used with Visa's PIN Verification Value algorithm to verify PINs through a computed verification value stored on the card or in a host database. |
| PVKOTH | `00000015` | `PVKOTH` | (PIN Verification Key — Other): PIN verification key for proprietary or non-IBM/non-Visa PIN verification schemes. |
| DUKPT | `00000016` | `DUKPT` | (Derived Unique Key Per Transaction): A transaction-level session key derived from a Base Derivation Key under the ANSI X9.24-1 DUKPT scheme; each transaction uses a distinct, non-reusable key. |
| IV | `00000017` | `IV` | (Initialisation Vector): A key or key-like value used as the initialisation vector for a block cipher mode of operation, managed as a key object within the KMIP hierarchy. |
| TRKBK | `00000018` | `TRKBK` | (Track Block): Encrypts magnetic stripe track data captured at payment terminals before transmission to the acquirer host. |

## Examples

A payment HSM managing a DUKPT terminal hierarchy stores the Base Derivation Key as a split key with role **BDK**, distributed across two trusted users with each holding one share. When merging the shares to re-inject the key into a new terminal, KMIP Join Split Key reconstructs the BDK from its parts.

## Related

- [Split Key object](../objects/split-key.md) — the managed object type that carries split key material and role information
- [Create Split Key operation](../operations/create-split-key.md) — creates split key shares
- [Join Split Key operation](../operations/join-split-key.md) — reassembles the key from shares
