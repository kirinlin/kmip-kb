---
title: Validation Information
category: ttlv
spec_version: "2.1"
spec_versions: ["1.3", "1.4", "2.0", "2.1"]
source_section: "7.41"
v1_source_section: "2.1.20"
status: draft
related: ["profile-information", "capability-information", "rng-parameters"]
keywords: ["validation information", "FIPS 140", "Common Criteria", "certification", "CMVP"]
tag_hex: "4200DF"
xml_element: "ValidationInformation"
---

# Validation Information

## Overview

A machine-readable certification claim: "this implementation holds formal
validation X at level Y from authority Z" — FIPS 140 from NIST CMVP, a
Common Criteria evaluation, etc. Returned by
[Query](../operations/query.md) (Query Validations) since 1.3, letting
compliance-sensitive clients verify they are talking to validated
cryptography before storing keys.

## Encoding (Tag / Type / Length / Value)

Structure, tag `4200DF`:

| Field | Tag | Type | Required |
|---|---|---|---|
| Validation Authority Type | `4200E0` | Enumeration | Yes — Unspecified, NIST CMVP, Common Criteria |
| Validation Authority Country | `4200E1` | Text String | No — two-letter ISO code |
| Validation Authority URI | `4200E2` | Text String | No |
| Validation Version Major | `4200E3` | Integer | Yes |
| Validation Version Minor | `4200E4` | Integer | No |
| Validation Type | `4200E5` | Enumeration | Yes — Hardware, Software, Firmware, Hybrid, Unspecified |
| Validation Level | `4200E6` | Integer | Yes — e.g. FIPS 140 level |
| Validation Certificate Identifier | `4200E7` | Text String | No |
| Validation Certificate URI | `4200E8` | Text String | No |
| Validation Vendor URI | `4200E9` | Text String | No |
| Validation Profile | `4200EA` | Text String | No; repeatable |

## Fields & Structure

Authority type + version major + type + level together uniquely identify a
validation from a given authority. When no certificate URI is available, the
vendor URI should point at information about the validation. A responder may
also legitimately return nothing — asserting validations is optional even
when asked.

## Examples

An HSM-backed server answers Query (Validations) with { NIST CMVP, country
US, Version Major 140, Validation Type = Hardware, Level = 3, Certificate
Identifier `"#3523"` }.

## Related

[Profile Information](profile-information.md) ·
[Capability Information](capability-information.md) ·
[RNG Parameters](rng-parameters.md)
