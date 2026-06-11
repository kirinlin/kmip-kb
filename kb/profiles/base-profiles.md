---
title: Base Profiles
category: profile
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "prof-5.1"
status: reviewed
related: ["complete-server-profile", "kmip-client-implementation-conformance", "kmip-server-implementation-conformance", "basic-authentication-suite", "query"]
keywords: ["baseline client", "baseline server", "conformance", "base profile", "KMIP-Prof"]
---

# Base Profiles

## Overview

The Base Profiles section of [KMIP-Prof] defines the two foundation conformance points — Baseline Client and Baseline Server — that every other KMIP profile builds on. A device or application meets one of these profiles before adding the capability-specific requirements of higher profiles such as the Symmetric Key Lifecycle or Cryptographic profiles.

## Baseline Client

A Baseline Client is the minimum useful KMIP client: it can query the server about its capabilities and retrieve already-managed objects. It must support the `Get`, `Get Attributes`, `Locate`, and `Query` operations; the core attributes `Unique Identifier`, `Object Type`, `State`, `Initial Date`, `Last Change Date`, `Activation Date`, `Deactivation Date`, and `Digest`; and the standard message envelope elements such as `Protocol Version`, `Batch Count`, `Result Status`, and `Operation`. Transport, Authentication, and TTLV message encoding are all mandatory.

The Baseline Client deliberately omits key-creation operations. Clients that only consume keys managed by a server can claim this profile without implementing Create or Register.

## Baseline Server

A Baseline Server is the minimum conformant key management server. It must support Create, Destroy, Register, Get, Get Attributes, Get Attribute List, Locate, Query, and Discover Versions, along with a comprehensive set of attributes and message structures. The server must also support the full Credential message element and handle Server-to-Client operations Notify, Put, Query, Discover Versions, and Set Endpoint Role.

The Baseline Server carries a significantly larger mandatory surface than the Baseline Client. This reflects that a server must accommodate clients with varying profiles — it cannot know which capabilities any given client will use.

## Mandatory Test Cases

The Baseline test suite (`BL-M-1-21` through `BL-M-13-21`) exercises the core Query/Get/Locate workflows and verifies correct handling of batch requests, error conditions, and attribute retrieval. All profiles that layer on top of Base Profiles must also pass these baseline test cases.

## Implications for Implementers

- Use `Query` at session startup to discover what the server actually supports; never assume capabilities from the profile label alone.
- A client that only claims Baseline Client need not implement Create or any crypto operations — but it must still handle unknown attributes in responses from servers at higher minor versions.
- Baseline Server is the entry point for new KMIP server implementations. Passing `BL-M-*` test cases first establishes a stable foundation before adding profile-specific operations.

## Related Concepts

[Complete Server Profile](complete-server-profile.md) ·
[KMIP Client Implementation Conformance](kmip-client-implementation-conformance.md) ·
[KMIP Server Implementation Conformance](kmip-server-implementation-conformance.md) ·
[Basic Authentication Suite](basic-authentication-suite.md) ·
[Query](../operations/query.md)
