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
| [Create](../operations/create.md) | `00000001` | `Create` |  |
| [Create Key Pair](../operations/create-key-pair.md) | `00000002` | `CreateKeyPair` |  |
| [Register](../operations/register.md) | `00000003` | `Register` |  |
| [Re-key](../operations/re-key.md) | `00000004` | `ReKey` |  |
| [Derive Key](../operations/derive-key.md) | `00000005` | `DeriveKey` |  |
| [Certify](../operations/certify.md) | `00000006` | `Certify` |  |
| [Re-certify](../operations/re-certify.md) | `00000007` | `ReCertify` |  |
| [Locate](../operations/locate.md) | `00000008` | `Locate` |  |
| [Check](../operations/check.md) | `00000009` | `Check` |  |
| [Get](../operations/get.md) | `0000000A` | `Get` |  |
| [Get Attributes](../operations/get-attributes.md) | `0000000B` | `GetAttributes` |  |
| [Get Attribute List](../operations/get-attribute-list.md) | `0000000C` | `GetAttributeList` |  |
| [Add Attribute](../operations/add-attribute.md) | `0000000D` | `AddAttribute` |  |
| [Modify Attribute](../operations/modify-attribute.md) | `0000000E` | `ModifyAttribute` |  |
| [Delete Attribute](../operations/delete-attribute.md) | `0000000F` | `DeleteAttribute` |  |
| [Obtain Lease](../operations/obtain-lease.md) | `00000010` | `ObtainLease` |  |
| [Get Usage Allocation](../operations/get-usage-allocation.md) | `00000011` | `GetUsageAllocation` |  |
| [Activate](../operations/activate.md) | `00000012` | `Activate` |  |
| [Revoke](../operations/revoke.md) | `00000013` | `Revoke` |  |
| [Destroy](../operations/destroy.md) | `00000014` | `Destroy` |  |
| [Archive](../operations/archive.md) | `00000015` | `Archive` |  |
| [Recover](../operations/recover.md) | `00000016` | `Recover` |  |
| [Validate](../operations/validate.md) | `00000017` | `Validate` |  |
| [Query](../operations/query.md) | `00000018` | `Query` |  |
| [Cancel](../operations/cancel.md) | `00000019` | `Cancel` |  |
| [Poll](../operations/poll.md) | `0000001A` | `Poll` |  |
| [Notify](../operations/server-to-client/notify.md) | `0000001B` | `Notify` |  |
| [Put](../operations/server-to-client/put.md) | `0000001C` | `Put` |  |
| [Re-key Key Pair](../operations/re-key-key-pair.md) | `0000001D` | `ReKeyKeyPair` |  |
| [Discover Versions](../operations/discover-versions.md) | `0000001E` | `DiscoverVersions` |  |
| [Encrypt](../operations/encrypt.md) | `0000001F` | `Encrypt` |  |
| [Decrypt](../operations/decrypt.md) | `00000020` | `Decrypt` |  |
| [Sign](../operations/sign.md) | `00000021` | `Sign` |  |
| [Signature Verify](../operations/signature-verify.md) | `00000022` | `SignatureVerify` |  |
| [MAC](../operations/mac.md) | `00000023` | `MAC` |  |
| [MAC Verify](../operations/mac-verify.md) | `00000024` | `MACVerify` |  |
| [RNG Retrieve](../operations/rng-retrieve.md) | `00000025` | `RNGRetrieve` |  |
| [RNG Seed](../operations/rng-seed.md) | `00000026` | `RNGSeed` |  |
| [Hash](../operations/hash.md) | `00000027` | `Hash` |  |
| [Create Split Key](../operations/create-split-key.md) | `00000028` | `CreateSplitKey` |  |
| [Join Split Key](../operations/join-split-key.md) | `00000029` | `JoinSplitKey` |  |
| [Import](../operations/import.md) | `0000002A` | `Import` |  |
| [Export](../operations/export.md) | `0000002B` | `Export` |  |
| [Log](../operations/log.md) | `0000002C` | `Log` |  |
| [Login](../operations/login.md) | `0000002D` | `Login` |  |
| [Logout](../operations/logout.md) | `0000002E` | `Logout` |  |
| [Delegated Login](../operations/delegated-login.md) | `0000002F` | `DelegatedLogin` |  |
| [Adjust Attribute](../operations/adjust-attribute.md) | `00000030` | `AdjustAttribute` |  |
| [Set Attribute](../operations/set-attribute.md) | `00000031` | `SetAttribute` |  |
| [Set Endpoint Role](../operations/set-endpoint-role.md) | `00000032` | `SetEndpointRole` |  |
| [PKCS#11](../operations/pkcs-11.md) | `00000033` | `PKCS_11` |  |
| [Interop](../operations/interop.md) | `00000034` | `Interop` |  |
| [Re-Provision](../operations/re-provision.md) | `00000035` | `ReProvision` |  |
| [Set Defaults](../operations/set-defaults.md) | `00000036` | `SetDefaults` |  |
| [Set Constraints](../operations/set-constraints.md) | `00000037` | `SetConstraints` |  |
| [Get Constraints](../operations/get-constraints.md) | `00000038` | `GetConstraints` |  |
| [Query Asynchronous Requests](../operations/query-asynchronous-requests.md) | `00000039` | `QueryAsynchronousRequests` |  |
| [Process](../operations/process.md) | `0000003A` | `Process` |  |
| [Ping](../operations/ping.md) | `0000003B` | `Ping` |  |

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
