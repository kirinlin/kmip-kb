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
| Complete Server Basic | `00000104` | `CompleteServerBasic` | Legacy v1.4 named profile combining Complete Server feature coverage with the Basic Authentication Suite. |
| Complete Server TLS v1.2 | `00000105` | `CompleteServerTLSV1_2` | Legacy v1.4 named profile combining Complete Server feature coverage with the TLS v1.2 Authentication Suite. |
| Tape Library Client | `00000106` | `TapeLibraryClient` | Tape library device acting as a KMIP client; stores per-tape key identifiers using Application Specific Information and Alternative Name attributes. |
| Tape Library Server | `00000107` | `TapeLibraryServer` | KMIP server supporting tape library clients; manages symmetric keys and the Alternative Name, Application Specific Information, and Vendor Attribute metadata they require. |
| Symmetric Key Lifecycle Client | `00000108` | `SymmetricKeyLifecycleClient` | Client that requests symmetric key lifecycle operations (create, activate, revoke, destroy) from a KMIP server. |
| Symmetric Key Lifecycle Server | `00000109` | `SymmetricKeyLifecycleServer` | Server performing symmetric key lifecycle management, supporting Create and the AES/3DES algorithms with Raw and Transparent Symmetric Key formats. |
| Asymmetric Key Lifecycle Client | `0000010A` | `AsymmetricKeyLifecycleClient` | Client that requests asymmetric (public/private) key lifecycle operations from a KMIP server. |
| Asymmetric Key Lifecycle Server | `0000010B` | `AsymmetricKeyLifecycleServer` | Server performing asymmetric key lifecycle management, supporting RSA key pairs in PKCS#1, PKCS#8, and Transparent RSA formats. |
| Basic Cryptographic Client | `0000010C` | `BasicCryptographicClient` | Client that requests Encrypt and/or Decrypt operations from a KMIP server. |
| Basic Cryptographic Server | `0000010D` | `BasicCryptographicServer` | Server that performs Encrypt and Decrypt operations on behalf of clients. |
| Advanced Cryptographic Client | `0000010E` | `AdvancedCryptographicClient` | Client that requests encryption, decryption, hashing, MAC, signing, verification, and/or RNG operations from a KMIP server. |
| Advanced Cryptographic Server | `0000010F` | `AdvancedCryptographicServer` | Server that performs the full cryptographic service set: Encrypt, Decrypt, Hash, MAC, MAC Verify, Sign, Signature Verify, RNG Retrieve, and RNG Seed. |
| RNG Cryptographic Client | `00000110` | `RNGCryptographicClient` | Client that requests RNG Retrieve and/or RNG Seed operations from a KMIP server. |
| RNG Cryptographic Server | `00000111` | `RNGCryptographicServer` | Server that performs RNG Retrieve and RNG Seed operations on behalf of clients. |
| Basic Symmetric Key Foundry Client | `00000112` | `BasicSymmetricKeyFoundryClient` | Client at the basic tier of the FIPS 140-restricted Symmetric Key Foundry profile set. |
| Intermediate Symmetric Key Foundry Client | `00000113` | `IntermediateSymmetricKeyFoundryClient` | Client at the intermediate tier of the FIPS 140-restricted Symmetric Key Foundry profile set. |
| Advanced Symmetric Key Foundry Client | `00000114` | `AdvancedSymmetricKeyFoundryClient` | Client at the advanced tier of the FIPS 140-restricted Symmetric Key Foundry profile set. |
| Symmetric Key Foundry Server | `00000115` | `SymmetricKeyFoundryServer` | Server performing FIPS 140-restricted symmetric key lifecycle operations, supporting AES (128/192/256-bit) and 3DES keys. |
| Opaque Managed Object Store Client | `00000116` | `OpaqueManagedObjectStoreClient` | Client that stores and retrieves opaque (vendor-defined) managed objects on a KMIP server. |
| Opaque Managed Object Store Server | `00000117` | `OpaqueManagedObjectStoreServer` | Server that stores opaque managed objects, supporting the Register operation and the Opaque Data Type enumeration. |
| Storage Array with Self Encrypting Drive Client | `0000011C` | `StorageArrayWithSelfEncryptingDriveClient` | Storage array containing self-encrypting drives (SEDs), acting as a KMIP client to retrieve and manage drive encryption keys. |
| Storage Array with Self Encrypting Drive Server | `0000011D` | `StorageArrayWithSelfEncryptingDriveServer` | KMIP server that manages keys for storage arrays with self-encrypting drives. |
| HTTPS Client | `0000011E` | `HTTPSClient` | Client that transports KMIP messages over HTTPS (HTTP/1.0 or HTTP/1.1 over TLS per RFC 2818) using POST to /kmip. |
| HTTPS Server | `0000011F` | `HTTPSServer` | Server that accepts KMIP messages carried over HTTPS, returning HTTP 200 with the KMIP response body. |
| JSON Client | `00000120` | `JSONClient` | Client that uses JSON message encoding in place of TTLV for KMIP request/response messages. |
| JSON Server | `00000121` | `JSONServer` | Server that accepts KMIP messages encoded in JSON rather than TTLV. |
| XML Client | `00000122` | `XMLClient` | Client that uses XML message encoding in place of TTLV for KMIP request/response messages. |
| XML Server | `00000123` | `XMLServer` | Server that accepts KMIP messages encoded in XML rather than TTLV. |
| AES XTS Client | `00000124` | `AESXTSClient` | Client that requests AES XTS symmetric key generation and management from a KMIP server for disk/storage encryption use cases. |
| AES XTS Server | `00000125` | `AESXTSServer` | Server that generates and manages AES XTS symmetric keys, supporting the Create operation with Raw and Transparent Symmetric Key formats. |
| Quantum Safe Client | `00000126` | `QuantumSafeClient` | Client that requires TLS v1.3 transport and supports quantum-safe key management operations. |
| Quantum Safe Server | `00000127` | `QuantumSafeServer` | Server that requires TLS v1.3 and manages quantum-safe keys and certificates, supporting the Protection Level and Quantum Safe attributes. |
| PKCS#11 Client | `00000128` | `PKCS_11Client` | Client that tunnels PKCS#11 function calls through the KMIP PKCS#11 operation using the defined binary encoding. |
| PKCS#11 Server | `00000129` | `PKCS_11Server` | Server that executes PKCS#11 function calls received via the KMIP PKCS#11 operation and returns results using the defined encoding. |
| Baseline Client | `0000012A` | `BaselineClient` | Client providing minimum KMIP conformance: Query, Get, Get Attributes, and Locate operations with TTLV transport and authentication. |
| Baseline Server | `0000012B` | `BaselineServer` | Server providing minimum KMIP conformance: full attribute and operation set, Query response with server/profile information, and TTLV transport. |
| Complete Server | `0000012C` | `CompleteServer` | Server implementing the entire KMIP specification — every object type, attribute, operation, message structure, and enumeration. |

Key profile name values across KMIP versions include:

**Server profiles**: Baseline Server Basic (BSB), Baseline Server Complete (BSC), Complete Server Basic (CSB), Complete Server Complete (CSC). These define tiers of server capability from a minimal viable implementation to the full feature set.

**Client profiles**: Baseline Client Basic (BCB). Symmetric to the server tiers.

**Vertical profiles**: Storage Array with Self-Encrypting Drive Server/Client (SASC/SACL), Storage Array without Self-Encrypting Drive Server/Client, KMIP v1.x-specific profiles for tape, HSM, and enterprise key management appliance scenarios.

**Suite B and specialized profiles**: Suite B, Transport Layer Security, Cryptographic Message Syntax — for specific algorithm or transport requirements.

## Examples

A server that advertises **Complete Server Basic** supports the full set of KMIP operations at a basic authentication level. A storage array that includes SEDs advertises **SASC** to indicate it supports the specific attribute and operation set required for SED integration.

## Related

[Profile Version](../structures/profile-version.md) · [Query](../operations/query.md) · [Server Information](../structures/server-information.md)
