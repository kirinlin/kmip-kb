---
title: Operation Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.36"
status: reviewed
related: ["right", "rights", "constraint", "constraints", "message-structure"]
keywords: ["operation", "operation code", "KMIP operations", "rights", "access control", "batch item", "42005C"]
tag_hex: "42005C"
xml_text: "Operation"
tag_type: "Enumeration"
---

# Operation Enumeration

## Overview

The Operation enumeration assigns a numeric code to every KMIP operation, making it possible to reference operations by value in structures that talk about operations rather than perform them — most importantly in [Rights](../structures/rights.md) access control entries, in [Constraints](../structures/constraints.md), in Cancel requests, and in Query responses. It is the machine-readable complement to the human-readable operation names used throughout the specification.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Create | `00000001` | `Create` |  |
| Create Key Pair | `00000002` | `CreateKeyPair` |  |
| Register | `00000003` | `Register` |  |
| Re-key | `00000004` | `ReKey` |  |
| Derive Key | `00000005` | `DeriveKey` |  |
| Certify | `00000006` | `Certify` |  |
| Re-certify | `00000007` | `ReCertify` |  |
| Locate | `00000008` | `Locate` |  |
| Check | `00000009` | `Check` |  |
| Get | `0000000A` | `Get` |  |
| Get Attributes | `0000000B` | `GetAttributes` |  |
| Get Attribute List | `0000000C` | `GetAttributeList` |  |
| Add Attribute | `0000000D` | `AddAttribute` |  |
| Modify Attribute | `0000000E` | `ModifyAttribute` |  |
| Delete Attribute | `0000000F` | `DeleteAttribute` |  |
| Obtain Lease | `00000010` | `ObtainLease` |  |
| Get Usage Allocation | `00000011` | `GetUsageAllocation` |  |
| Activate | `00000012` | `Activate` |  |
| Revoke | `00000013` | `Revoke` |  |
| Destroy | `00000014` | `Destroy` |  |
| Archive | `00000015` | `Archive` |  |
| Recover | `00000016` | `Recover` |  |
| Validate | `00000017` | `Validate` |  |
| Query | `00000018` | `Query` |  |
| Cancel | `00000019` | `Cancel` |  |
| Poll | `0000001A` | `Poll` |  |
| Notify | `0000001B` | `Notify` |  |
| Put | `0000001C` | `Put` |  |
| Re-key Key Pair | `0000001D` | `ReKeyKeyPair` |  |
| Discover Versions | `0000001E` | `DiscoverVersions` |  |
| Encrypt | `0000001F` | `Encrypt` |  |
| Decrypt | `00000020` | `Decrypt` |  |
| Sign | `00000021` | `Sign` |  |
| Signature Verify | `00000022` | `SignatureVerify` |  |
| MAC | `00000023` | `MAC` |  |
| MAC Verify | `00000024` | `MACVerify` |  |
| RNG Retrieve | `00000025` | `RNGRetrieve` |  |
| RNG Seed | `00000026` | `RNGSeed` |  |
| Hash | `00000027` | `Hash` |  |
| Create Split Key | `00000028` | `CreateSplitKey` |  |
| Join Split Key | `00000029` | `JoinSplitKey` |  |
| Import | `0000002A` | `Import` |  |
| Export | `0000002B` | `Export` |  |
| Log | `0000002C` | `Log` |  |
| Login | `0000002D` | `Login` |  |
| Logout | `0000002E` | `Logout` |  |
| Delegated Login | `0000002F` | `DelegatedLogin` |  |
| Adjust Attribute | `00000030` | `AdjustAttribute` |  |
| Set Attribute | `00000031` | `SetAttribute` |  |
| Set Endpoint Role | `00000032` | `SetEndpointRole` |  |
| PKCS#11 | `00000033` | `PKCS_11` |  |
| Interop | `00000034` | `Interop` |  |
| Re-Provision | `00000035` | `ReProvision` |  |
| Set Defaults | `00000036` | `SetDefaults` |  |
| Set Constraints | `00000037` | `SetConstraints` |  |
| Get Constraints | `00000038` | `GetConstraints` |  |
| Query Asynchronous Requests | `00000039` | `QueryAsynchronousRequests` |  |
| Process | `0000003A` | `Process` |  |
| Ping | `0000003B` | `Ping` |  |

Key operations and their enumeration presence across versions:

**Core CRUD and lifecycle** (v1.0+): Create, Create Key Pair, Register, Get, Get Attributes, Get Attribute List, Add Attribute, Modify Attribute, Delete Attribute, Obtain Lease, Get Usage Allocation, Activate, Revoke, Destroy, Archive, Recover, Query.

**Cryptographic operations** (v1.0+): MAC, MAC Verify; (v1.2+): Encrypt, Decrypt, Sign, Signature Verify, Hash, RNG Retrieve, RNG Seed.

**Advanced key management** (v1.0+): Locate, Re-key, Derive Key, Re-certify, Certify, Re-key Key Pair, Join Split Key, Create Split Key.

**Protocol management** (v1.0+): Discover Versions, Cancel, Poll, Notify, Put.

**Import/Export** (v2.0+): Import, Export.

**v2.1 additions**: Adjust Attribute, Set Attribute, Set Defaults, Set Constraints, Get Constraints, Set Endpoint Role, Ping, Log, Login, Logout, Delegated Login, Interop, PKCS#11, Process, Query Asynchronous Requests, Re-Provision.

## Examples

A [Right](../structures/right.md) entry granting a service account permission to perform Get and Activate on a symmetric key lists **Get** and **Activate** as Operation values. A Cancel request targeting a pending async operation names the operation being cancelled using this enumeration.

## Related

[Right](../structures/right.md) · [Rights](../structures/rights.md) · [Constraint](../structures/constraint.md) · [Message Structure](../messages/message-structure.md)
