---
title: Basic Secret Data Server KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.3"
status: reviewed
related: ["basic-authentication-suite", "basic-baseline-server-kmip-profile", "basic-secret-data-client-kmip-profile", "secret-data-server-tls-1-2-authentication-kmip-profile", "secret-data-kmip-profile"]
keywords: ["secret data", "password", "token", "Basic Authentication Suite", "Register", "server profile"]
---

# Basic Secret Data Server KMIP Profile

## Overview

The Basic Secret Data Server KMIP Profile defines server requirements for managing Secret Data objects in KMIP v1.1 deployments using the [Basic Authentication Suite](basic-authentication-suite.md). It extends the [Basic Baseline Server](basic-baseline-server-kmip-profile.md) with explicit Secret Data object support. Secret Data objects hold opaque secret material — passwords, API tokens, PINs, pre-shared keys, or any credential that is not a structured cryptographic key.

The companion client profile is the [Basic Secret Data Client KMIP Profile](basic-secret-data-client-kmip-profile.md). For the TLS 1.2 variant, see [Secret Data Server TLS 1.2 Authentication KMIP Profile](secret-data-server-tls-1-2-authentication-kmip-profile.md). The v1.0 combined client-and-server predecessor is the [Secret Data KMIP Profile](secret-data-kmip-profile.md).

## Required Operations and Objects

The server must support Register, Get, Locate, and Destroy on Secret Data objects, in addition to the baseline operations. No Create is required for Secret Data, as these objects represent pre-existing secret material rather than server-generated values.

Core attributes that apply to Secret Data: `Unique Identifier`, `Object Type`, `Name`, `State`, `Initial Date`, `Last Change Date`, `Activation Date`, `Deactivation Date`.

## Implications for Implementers

- Apply access control to Get operations on Secret Data at least as strictly as for symmetric keys — these objects frequently carry credentials that grant access to other systems.
- Secret Data objects do not have key-format or algorithm attributes; validate only the standard managed-object attributes and the `Secret Data Type` attribute during Register.
- If your deployment requires TLS 1.2 mutual authentication, target the [TLS 1.2 variant](secret-data-server-tls-1-2-authentication-kmip-profile.md) instead.

## Related Concepts

[Basic Authentication Suite](basic-authentication-suite.md) ·
[Basic Baseline Server KMIP Profile](basic-baseline-server-kmip-profile.md) ·
[Basic Secret Data Client KMIP Profile](basic-secret-data-client-kmip-profile.md) ·
[Secret Data Server TLS 1.2 Authentication KMIP Profile](secret-data-server-tls-1-2-authentication-kmip-profile.md) ·
[Secret Data KMIP Profile](secret-data-kmip-profile.md)
