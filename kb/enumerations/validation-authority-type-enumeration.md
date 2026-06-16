---
title: Validation Authority Type Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.3","1.4","2.0","2.1"]
source_section: "11.61"
status: reviewed
related: ["cryptographic-parameters"]
keywords: ["validation authority", "CMVP", "Common Criteria", "NIST validation", "cryptographic module validation", "4200E0", "ValidationAuthorityType"]
tag_hex: "4200E0"
xml_text: "ValidationAuthorityType"
---

# Validation Authority Type Enumeration

## Overview

The Validation Authority Type enumeration identifies which standards body or programme validated the cryptographic implementation associated with a key or operation. It appears in Cryptographic Parameters and validation-related attributes, enabling clients and policy engines to enforce requirements for FIPS-validated or CC-evaluated implementations without inspection of implementation details.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Valid | `00000001` | `Valid` |  |
| Invalid | `00000002` | `Invalid` |  |
| Unknown | `00000003` | `Unknown` |  |

- **Unspecified**: No validation authority is identified. The implementation's validation status is unknown or not applicable.
- **NIST CMVP** (Cryptographic Module Validation Program): The module has been validated under the NIST FIPS 140 programme (CMVP), run jointly by NIST and CCCS. CMVP-validated modules carry a certificate number and validation level (1–4). Required by US federal information systems.
- **Common Criteria**: The product or module has been evaluated under the ISO/IEC 15408 (Common Criteria) evaluation assurance levels (EAL1–EAL7). Used widely in European and international procurement.

## Examples

A government procurement requirement mandates FIPS 140-2 Level 2 or higher: the client checks that the server reports **NIST CMVP** validation at Level 2 or higher before storing sensitive keys. A European financial institution may alternatively require **Common Criteria** EAL4+.

## Related

[Cryptographic Parameters](../attributes/cryptographic-parameters.md)
