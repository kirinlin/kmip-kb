---
title: Basic Symmetric Key Store Client KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.24"
status: reviewed
related: ["basic-authentication-suite", "basic-symmetric-key-store-and-server-kmip-profile", "symmetric-key-store-client-tls-1-2-authentication-kmip-profile"]
keywords: ["symmetric key", "key store", "AES", "Register", "Basic Authentication Suite", "client profile"]
---

# Basic Symmetric Key Store Client KMIP Profile

## Overview

The Basic Symmetric Key Store Client KMIP Profile defines client requirements for depositing and retrieving symmetric keys at a KMIP v1.1 server, using the [Basic Authentication Suite](basic-authentication-suite.md). A client claiming this profile provides key material via Register and retrieves it via Get. The server side is the [Basic Symmetric Key Store and Server KMIP Profile](basic-symmetric-key-store-and-server-kmip-profile.md).

For the TLS 1.2 variant, see [Symmetric Key Store Client TLS 1.2 Authentication KMIP Profile](symmetric-key-store-client-tls-1-2-authentication-kmip-profile.md).

## Required Operations

The client must support Register on Symmetric Key objects to deposit externally generated key material, and Get to retrieve keys on demand. AES is the mandatory key algorithm. Locate and lifecycle operations (Activate, Revoke, Destroy) may be invoked as needed.

## Implications for Implementers

- This is the right client profile for applications that generate AES keys locally (or via an HSM) and need a central server for distribution and lifecycle management.
- Set `Cryptographic Algorithm`, `Cryptographic Length`, and `Cryptographic Usage Mask` on every Register request; a server may reject or rekey objects with incomplete attributes.
- If your client must also request server-generated keys (Create), it needs the corresponding Foundry client profile ([Basic Symmetric Key Foundry Client](basic-symmetric-key-foundry-client-kmip-profile.md)).

## Related Concepts

[Basic Authentication Suite](basic-authentication-suite.md) ·
[Basic Symmetric Key Store and Server KMIP Profile](basic-symmetric-key-store-and-server-kmip-profile.md) ·
[Basic Symmetric Key Foundry Client KMIP Profile](basic-symmetric-key-foundry-client-kmip-profile.md) ·
[Symmetric Key Store Client TLS 1.2 Authentication KMIP Profile](symmetric-key-store-client-tls-1-2-authentication-kmip-profile.md)
