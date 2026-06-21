---
title: Profile Name Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.41"
status: reviewed
related: ["profile-version", "query", "server-information"]
keywords: ["profile name", "conformance profile", "KMIP profile", "baseline server", "complete server", "storage array", "4200EC", "ProfileName"]
tag_hex: "4200EC"
xml_text: "ProfileName"
tag_type: "Enumeration"
---

# Profile Name Enumeration

## Overview

The Profile Name enumeration identifies the named KMIP conformance profiles defined in the separate KMIP Profiles document. Servers advertise which profiles they conform to in their [Query](../operations/query.md) responses via the [Profile Version](../structures/profile-version.md) structure, and clients can use this to select appropriate server capabilities without querying every individual feature. Profiles define a minimum compliant feature set that an implementation must support to claim conformance.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Complete Server Basic | `00000104` | `CompleteServerBasic` |  |
| Complete Server TLS v1.2 | `00000105` | `CompleteServerTLSV1_2` |  |
| Tape Library Client | `00000106` | `TapeLibraryClient` |  |
| Tape Library Server | `00000107` | `TapeLibraryServer` |  |
| Symmetric Key Lifecycle Client | `00000108` | `SymmetricKeyLifecycleClient` |  |
| Symmetric Key Lifecycle Server | `00000109` | `SymmetricKeyLifecycleServer` |  |
| Asymmetric Key Lifecycle Client | `0000010A` | `AsymmetricKeyLifecycleClient` |  |
| Asymmetric Key Lifecycle Server | `0000010B` | `AsymmetricKeyLifecycleServer` |  |
| Basic Cryptographic Client | `0000010C` | `BasicCryptographicClient` |  |
| Basic Cryptographic Server | `0000010D` | `BasicCryptographicServer` |  |
| Advanced Cryptographic Client | `0000010E` | `AdvancedCryptographicClient` |  |
| Advanced Cryptographic Server | `0000010F` | `AdvancedCryptographicServer` |  |
| RNG Cryptographic Client | `00000110` | `RNGCryptographicClient` |  |
| RNG Cryptographic Server | `00000111` | `RNGCryptographicServer` |  |
| Basic Symmetric Key Foundry Client | `00000112` | `BasicSymmetricKeyFoundryClient` |  |
| Intermediate Symmetric Key Foundry Client | `00000113` | `IntermediateSymmetricKeyFoundryClient` |  |
| Advanced Symmetric Key Foundry Client | `00000114` | `AdvancedSymmetricKeyFoundryClient` |  |
| Symmetric Key Foundry Server | `00000115` | `SymmetricKeyFoundryServer` |  |
| Opaque Managed Object Store Client | `00000116` | `OpaqueManagedObjectStoreClient` |  |
| Opaque Managed Object Store Server | `00000117` | `OpaqueManagedObjectStoreServer` |  |
| Storage Array with Self Encrypting Drive Client | `0000011C` | `StorageArrayWithSelfEncryptingDriveClient` |  |
| Storage Array with Self Encrypting Drive Server | `0000011D` | `StorageArrayWithSelfEncryptingDriveServer` |  |
| HTTPS Client | `0000011E` | `HTTPSClient` |  |
| HTTPS Server | `0000011F` | `HTTPSServer` |  |
| JSON Client | `00000120` | `JSONClient` |  |
| JSON Server | `00000121` | `JSONServer` |  |
| XML Client | `00000122` | `XMLClient` |  |
| XML Server | `00000123` | `XMLServer` |  |
| AES XTS Client | `00000124` | `AESXTSClient` |  |
| AES XTS Server | `00000125` | `AESXTSServer` |  |
| Quantum Safe Client | `00000126` | `QuantumSafeClient` |  |
| Quantum Safe Server | `00000127` | `QuantumSafeServer` |  |
| PKCS#11 Client | `00000128` | `PKCS_11Client` |  |
| PKCS#11 Server | `00000129` | `PKCS_11Server` |  |
| Baseline Client | `0000012A` | `BaselineClient` |  |
| Baseline Server | `0000012B` | `BaselineServer` |  |
| Complete Server | `0000012C` | `CompleteServer` |  |

Key profile name values across KMIP versions include:

**Server profiles**: Baseline Server Basic (BSB), Baseline Server Complete (BSC), Complete Server Basic (CSB), Complete Server Complete (CSC). These define tiers of server capability from a minimal viable implementation to the full feature set.

**Client profiles**: Baseline Client Basic (BCB), Complete Client Basic (CCB). Symmetric to the server tiers.

**Vertical profiles**: Storage Array with Self-Encrypting Drive Server/Client (SASC/SACL), Storage Array without Self-Encrypting Drive Server/Client, KMIP v1.x-specific profiles for tape, HSM, and enterprise key management appliance scenarios.

**Suite B and specialized profiles**: Suite B, Transport Layer Security, Cryptographic Message Syntax — for specific algorithm or transport requirements.

## Examples

A server that advertises **Complete Server Basic** supports the full set of KMIP operations at a basic authentication level. A storage array that includes SEDs advertises **SASC** to indicate it supports the specific attribute and operation set required for SED integration.

## Related

[Profile Version](../structures/profile-version.md) · [Query](../operations/query.md) · [Server Information](../structures/server-information.md)
