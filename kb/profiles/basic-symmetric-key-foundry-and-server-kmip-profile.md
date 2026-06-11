---
title: Basic Symmetric Key Foundry and Server KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.0", "1.1"]
source_section: "prof-4.3"
status: reviewed
related: ["basic-authentication-suite", "tls-1-2-authentication-suite", "symmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile", "basic-symmetric-key-store-and-server-kmip-profile", "basic-symmetric-key-foundry-client-kmip-profile"]
keywords: ["symmetric key", "key foundry", "key generation", "Create", "AES", "Basic Authentication Suite"]
---

# Basic Symmetric Key Foundry and Server KMIP Profile

## Overview

The Basic Symmetric Key Foundry and Server KMIP Profile extends the [Store variant](basic-symmetric-key-store-and-server-kmip-profile.md) with server-side key generation. The "Foundry" designation means the server can forge (create) symmetric keys on demand rather than only accepting client-provided material. This profile uses the [Basic Authentication Suite](basic-authentication-suite.md); for the TLS 1.2 variant see [Symmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile](symmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile.md).

The profile originated in KMIP-Prof v1.0 as a combined client-and-server definition. KMIP-Prof v1.1 retained it and added a dedicated [Basic Symmetric Key Foundry Client](basic-symmetric-key-foundry-client-kmip-profile.md) profile for clients that declare only their side.

## Required Operations and Objects

**Server** — everything required by the [Basic Symmetric Key Store and Server profile](basic-symmetric-key-store-and-server-kmip-profile.md) plus the Create operation. AES is mandatory; the server selects cryptographic parameters when the client does not specify them.

**Client** — may invoke Create to request key generation in addition to the Register/Get operations available under the Store profile.

Key attributes and object-state lifecycle requirements mirror those of the Store profile.

## Implications for Implementers

- The Foundry profile is the right choice when the server is the trusted source of entropy for key generation — for example, an HSM-backed KMIP server where clients should never handle raw key material.
- Ensure the Create operation generates keys using an approved DRBG and that the `Cryptographic Algorithm` and `Cryptographic Length` attributes are set correctly when the client omits them. AES-256 is the recommended default.
- Servers must handle both Register (client-provided material) and Create (server-generated) — the profile does not restrict clients to only one path.
- Pair with the [Foundry Client profile](basic-symmetric-key-foundry-client-kmip-profile.md) for deployments where you want a clear client-side conformance claim.

## Related Concepts

[Basic Authentication Suite](basic-authentication-suite.md) ·
[Basic Symmetric Key Store and Server KMIP Profile](basic-symmetric-key-store-and-server-kmip-profile.md) ·
[Basic Symmetric Key Foundry Client KMIP Profile](basic-symmetric-key-foundry-client-kmip-profile.md) ·
[Symmetric Key Foundry and Server TLS 1.2 Authentication KMIP Profile](symmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile.md)
