---
title: Operation Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.36"
status: reviewed
related: ["right", "rights", "constraint", "constraints", "message-structure"]
keywords: ["operation", "operation code", "KMIP operations", "rights", "access control", "batch item"]
---

# Operation Enumeration

## Overview

The Operation enumeration assigns a numeric code to every KMIP operation, making it possible to reference operations by value in structures that talk about operations rather than perform them — most importantly in [Rights](../rights.md) access control entries, in [Constraints](../constraints.md), in Cancel requests, and in Query responses. It is the machine-readable complement to the human-readable operation names used throughout the specification.

## Encoding (Tag / Type / Length / Value)

Encoded as a 4-byte integer (TTLV type `05`, Enumeration), tag `42005C`.

## Fields & Structure

Key operations and their enumeration presence across versions:

**Core CRUD and lifecycle** (v1.0+): Create, Create Key Pair, Register, Get, Get Attributes, Get Attribute List, Add Attribute, Modify Attribute, Delete Attribute, Obtain Lease, Get Usage Allocation, Activate, Revoke, Destroy, Archive, Recover, Query.

**Cryptographic operations** (v1.0+): MAC, MAC Verify; (v1.2+): Encrypt, Decrypt, Sign, Signature Verify, Hash, RNG Retrieve, RNG Seed.

**Advanced key management** (v1.0+): Locate, Re-key, Derive Key, Re-certify, Certify, Re-key Key Pair, Join Split Key, Create Split Key.

**Protocol management** (v1.0+): Discover Versions, Cancel, Poll, Notify, Put.

**Import/Export** (v2.0+): Import, Export.

**v2.1 additions**: Adjust Attribute, Set Attribute, Set Defaults, Set Constraints, Get Constraints, Set Endpoint Role, Ping, Log, Login, Logout, Delegated Login, Interop, PKCS#11, Process, Query Asynchronous Requests, Re-Provision.

## Examples

A [Right](../right.md) entry granting a service account permission to perform Get and Activate on a symmetric key lists **Get** and **Activate** as Operation values. A Cancel request targeting a pending async operation names the operation being cancelled using this enumeration.

## Related

[Right](../right.md) · [Rights](../rights.md) · [Constraint](../constraint.md) · [Message Structure](../message-structure.md)
