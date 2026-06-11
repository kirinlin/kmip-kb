---
title: Basic Secret Data Client KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.23"
status: draft
related: ["basic-authentication-suite", "basic-secret-data-server-kmip-profile", "secret-data-client-tls-1-2-authentication-kmip-profile", "secret-data-kmip-profile"]
keywords: ["secret data", "password", "token", "Basic Authentication Suite", "client profile"]
---

# Basic Secret Data Client KMIP Profile

## Overview

The Basic Secret Data Client KMIP Profile defines client requirements for managing Secret Data objects in KMIP v1.1, using the [Basic Authentication Suite](basic-authentication-suite.md). A client claiming this profile can store, retrieve, and manage opaque secret material — passwords, tokens, PINs, pre-shared keys — at a server that claims the [Basic Secret Data Server KMIP Profile](basic-secret-data-server-kmip-profile.md).

For the TLS 1.2 variant, see [Secret Data Client TLS 1.2 Authentication KMIP Profile](secret-data-client-tls-1-2-authentication-kmip-profile.md). The v1.0 combined predecessor is the [Secret Data KMIP Profile](secret-data-kmip-profile.md).

## Required Operations

The client must support Register and Get on Secret Data objects, enabling it to deposit pre-existing secrets and retrieve them on demand. Locate and Destroy are expected to be invoked as part of normal lifecycle management but are the server's responsibility to implement correctly.

## Implications for Implementers

- Treat Secret Data retrieval with the same access-control scrutiny as key retrieval. Passwords and tokens stored as Secret Data objects frequently carry credentials that grant lateral access to other systems.
- Register the secret with appropriate `Activation Date` and `Deactivation Date` attributes to support lifecycle-aware policies (for example, automatic deactivation of rotated credentials).
- For the TLS 1.2 transport requirement, target the [Secret Data Client TLS 1.2 Authentication KMIP Profile](secret-data-client-tls-1-2-authentication-kmip-profile.md).

## Related Concepts

[Basic Authentication Suite](basic-authentication-suite.md) ·
[Basic Secret Data Server KMIP Profile](basic-secret-data-server-kmip-profile.md) ·
[Secret Data Client TLS 1.2 Authentication KMIP Profile](secret-data-client-tls-1-2-authentication-kmip-profile.md) ·
[Secret Data KMIP Profile](secret-data-kmip-profile.md)
