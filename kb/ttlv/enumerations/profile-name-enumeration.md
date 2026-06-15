---
title: Profile Name Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.41"
status: reviewed
related: ["profile-version", "query", "server-information"]
keywords: ["profile name", "conformance profile", "KMIP profile", "baseline server", "complete server", "storage array"]
tag_hex: "4200EC"
xml_element: "ProfileName"
---

# Profile Name Enumeration

## Overview

The Profile Name enumeration identifies the named KMIP conformance profiles defined in the separate KMIP Profiles document. Servers advertise which profiles they conform to in their [Query](../../operations/query.md) responses via the [Profile Version](../../structures/profile-version.md) structure, and clients can use this to select appropriate server capabilities without querying every individual feature. Profiles define a minimum compliant feature set that an implementation must support to claim conformance.

## Encoding (Tag / Type / Length / Value)

Encoded as a 4-byte integer (TTLV type `05`, Enumeration).

## Fields & Structure

Key profile name values across KMIP versions include:

**Server profiles**: Baseline Server Basic (BSB), Baseline Server Complete (BSC), Complete Server Basic (CSB), Complete Server Complete (CSC). These define tiers of server capability from a minimal viable implementation to the full feature set.

**Client profiles**: Baseline Client Basic (BCB), Complete Client Basic (CCB). Symmetric to the server tiers.

**Vertical profiles**: Storage Array with Self-Encrypting Drive Server/Client (SASC/SACL), Storage Array without Self-Encrypting Drive Server/Client, KMIP v1.x-specific profiles for tape, HSM, and enterprise key management appliance scenarios.

**Suite B and specialized profiles**: Suite B, Transport Layer Security, Cryptographic Message Syntax — for specific algorithm or transport requirements.

## Examples

A server that advertises **Complete Server Basic** supports the full set of KMIP operations at a basic authentication level. A storage array that includes SEDs advertises **SASC** to indicate it supports the specific attribute and operation set required for SED integration.

## Related

[Profile Version](../../structures/profile-version.md) · [Query](../../operations/query.md) · [Server Information](../../structures/server-information.md)
