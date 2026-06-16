---
title: Validation Type Enumeration
category: encoding
spec_version: "2.1"
spec_versions: ["1.3","1.4","2.0","2.1"]
source_section: "11.62"
status: reviewed
related: ["cryptographic-parameters", "validation-authority-type-enumeration"]
keywords: ["validation type", "software validation", "hardware validation", "firmware validation", "hybrid validation", "cryptographic validation", "4200E5", "ValidationType"]
tag_hex: "4200E5"
xml_text: "ValidationType"
---

# Validation Type Enumeration

## Overview

The Validation Type enumeration classifies the implementation layer that was subject to cryptographic validation. While [Validation Authority Type](validation-authority-type-enumeration.md) names the body that performed the validation, Validation Type identifies what was validated — whether the cryptographic algorithms run in pure software, in dedicated hardware, in firmware, or a combination. This allows policy engines to distinguish between a software-only FIPS module (acceptable for some uses) and a hardware module (required for higher-assurance uses).

## Fields & Structure

| Value | Hex | XML Text | Description |
|---|---|---|---|
| Encrypt | `0x00000001` | `Encrypt` |  |
| MAC/sign | `0x00000002` | `MACSign` |  |
| Encrypt then MAC/sign | `0x00000003` | `EncryptThenMACSign` |  |
| MAC/sign then encrypt | `0x00000004` | `MACSignThenEncrypt` |  |
| TR-31 | `0x00000005` | `TR_31` |  |

- **Unspecified**: The validation type is unknown or not applicable.
- **Software**: The cryptographic implementation that was validated runs entirely in software, with no hardware cryptographic accelerator or tamper-resistant element involved. A software FIPS module on a general-purpose CPU falls into this category.
- **Hardware**: The validated implementation resides in dedicated cryptographic hardware — typically an HSM, cryptographic accelerator, or SED controller that implements the algorithms in silicon.
- **Firmware**: The implementation runs as firmware within a hardware device (e.g., embedded in a smart card microcontroller or a TPM) that is neither pure software nor a full hardware implementation.
- **Hybrid**: The validated implementation spans both software and hardware components — for example, an FIPS-validated library that offloads some operations to a hardware accelerator where available and falls back to software otherwise.

## Examples

A laptop TPM that holds a private key reports Validation Type = **Firmware** and Validation Authority Type = **NIST CMVP**. An HSM-based key management appliance reports **Hardware** and CMVP.

## Related

[Validation Authority Type Enumeration](validation-authority-type-enumeration.md) · [Cryptographic Parameters](../../attributes/cryptographic-parameters.md)
