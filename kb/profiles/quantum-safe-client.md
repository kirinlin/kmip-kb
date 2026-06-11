---
title: Quantum Safe Client
category: profile
spec_version: "2.1"
spec_versions: ["2.0", "2.1"]
source_section: "prof-5.15"
status: reviewed
related: ["quantum-safe-profiles", "quantum-safe-server", "mandatory-quantum-safe-test-cases-kmip-v2-0", "base-profiles", "basic-authentication-suite"]
keywords: ["quantum safe", "post-quantum", "TLS 1.3", "Protection Level", "Protection Period", "PQC", "client profile"]
---

# Quantum Safe Client

## Overview

The Quantum Safe Client profile (§5.15 of [KMIP-Prof]) defines the minimum conformance requirements for a KMIP client that interoperates with a [Quantum Safe Server](quantum-safe-server.md). It extends the [Baseline Client](base-profiles.md) with a single mandatory transport constraint: TLS 1.3. A client that cannot support TLS 1.3 cannot claim this profile.

For the broader context of the quantum-safe profile family — including the motivation, the new attributes, and the server-side requirements — see [Quantum Safe Profiles](quantum-safe-profiles.md).

## Required Capability

A Quantum Safe Client:
- Extends the Baseline Client capability (Get, Get Attributes, Locate, Query, Discover Versions).
- Must negotiate TLS 1.3 for every KMIP connection. The TLS 1.2 fallback permitted by the Basic Authentication Suite does not apply.
- May invoke any additional operation that the server supports and that does not conflict with the profile.

No additional mandatory operations beyond the baseline are imposed on the client side. A client may choose to invoke Create with `Protection Period` and `Protection Level` attributes — in which case the server selects an appropriate quantum-safe algorithm — or it may invoke Create Key Pair, Encrypt, Sign, or any other operation the server supports.

## Working with Protection Period and Protection Level

When a client invokes Create on a server that supports the Quantum Safe profile, it may include the `Protection Period` attribute (years of required protection) and the `Protection Level` attribute (sensitivity classification of the protected data) in the request. The server uses these values to select an algorithm with sufficient security margin. A client that does not specify these attributes will receive a key using server default algorithm selection.

The `Quantum Safe` boolean attribute on a retrieved object indicates whether the object uses a quantum-resistant algorithm. Clients should check this attribute if they need to enforce a policy that all new keys are quantum-safe.

## Implications for Implementers

- The TLS 1.3 requirement is the only non-negotiable addition over the Baseline Client. If your TLS library does not support TLS 1.3, you cannot claim this profile regardless of which KMIP operations you implement.
- Clients do not need to understand the post-quantum algorithms themselves; the server performs all algorithm selection. The client's responsibility is to request appropriate protection parameters and to store and forward the `Quantum Safe` flag correctly.
- When computing `Protection Period`, consider both the expected encryption key lifetime and the anticipated timeline for a cryptographically relevant quantum computer becoming available.

## Related Concepts

[Quantum Safe Profiles](quantum-safe-profiles.md) ·
[Quantum Safe Server](quantum-safe-server.md) ·
[Mandatory Quantum Safe Test Cases KMIP v2.0](mandatory-quantum-safe-test-cases-kmip-v2-0.md) ·
[Base Profiles](base-profiles.md)
