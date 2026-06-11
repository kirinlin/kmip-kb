---
title: Secret Data KMIP Profile
category: profile
spec_version: "1.0"
spec_versions: ["1.0"]
source_section: "prof-4.1"
status: reviewed
related: ["basic-authentication-suite", "tls-1-2-authentication-suite", "basic-secret-data-server-kmip-profile", "basic-secret-data-client-kmip-profile"]
keywords: ["secret data", "password", "passphrase", "token", "opaque secret", "Register", "key management"]
---

# Secret Data KMIP Profile

## Overview

The Secret Data KMIP Profile is the original KMIP v1.0 profile for managing Secret Data objects — opaque secret material such as passwords, passphrases, PINs, API tokens, and pre-shared keys that do not fit into a structured cryptographic key type. It is a combined client-and-server profile (KMIP v1.0 did not yet separate client and server conformance roles); in KMIP v1.1 the same capability was reorganized into separate [Basic Secret Data Server](basic-secret-data-server-kmip-profile.md) and [Basic Secret Data Client](basic-secret-data-client-kmip-profile.md) profiles.

## Authentication

This profile uses the [Basic Authentication Suite](basic-authentication-suite.md). For the TLS 1.2 variant of the same capability, see [Secret Data TLS 1.2 Authentication KMIP Profile](secret-data-tls-1-2-authentication-kmip-profile.md).

## Required Operations and Objects

The profile covers the Register, Get, Locate, and Destroy operations applied to Secret Data objects. Register allows a client to store pre-existing secret material at the server; Get retrieves it; Locate finds objects by attribute; Destroy removes them. The Secret Data object carries the opaque secret value along with standard managed-object attributes.

Create is not mandated — Secret Data objects are typically pre-existing (a password, a token) rather than server-generated. Servers claiming this profile must handle all four operations; clients must support at least Register and Get.

## Implications for Implementers

- Secret Data is the right object type for anything that is a secret but not a key: passwords stored for HSM access, API credentials, authentication tokens, or out-of-band pre-shared secrets.
- Because the value is opaque, key-format handling is not required; however, the server must still enforce all standard object-state transitions and attribute management.
- Access control over Secret Data is particularly sensitive — these objects frequently carry credentials that could grant access to other systems. Apply policy restrictions to Get operations at least as strictly as for symmetric keys.
- If your deployment requires TLS 1.2 mutual authentication, use the [Secret Data TLS 1.2 Authentication KMIP Profile](secret-data-tls-1-2-authentication-kmip-profile.md) instead.

## Related Concepts

[Basic Authentication Suite](basic-authentication-suite.md) ·
[Secret Data TLS 1.2 Authentication KMIP Profile](secret-data-tls-1-2-authentication-kmip-profile.md) ·
[Basic Secret Data Server KMIP Profile](basic-secret-data-server-kmip-profile.md) ·
[Basic Secret Data Client KMIP Profile](basic-secret-data-client-kmip-profile.md)
