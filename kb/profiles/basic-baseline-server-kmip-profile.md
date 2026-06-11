---
title: Basic Baseline Server KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.2"
status: draft
related: ["basic-authentication-suite", "tls-1-2-authentication-suite", "basic-baseline-client-kmip-profile", "baseline-server-tls-1-2-authentication-kmip-profile", "base-profiles"]
keywords: ["baseline server", "Basic Authentication Suite", "conformance", "key management", "v1.1"]
---

# Basic Baseline Server KMIP Profile

## Overview

The Basic Baseline Server KMIP Profile defines the standard server conformance point for KMIP v1.1 deployments using the [Basic Authentication Suite](basic-authentication-suite.md). It is the v1.1 equivalent of the Baseline Server described in [Base Profiles](base-profiles.md) for v2.x, carrying the same core mandatory operations but scoped to the v1.1 protocol surface and paired with the Basic (non-TLS-1.2-specific) authentication option.

The companion client profile is the [Basic Baseline Client KMIP Profile](basic-baseline-client-kmip-profile.md). For the TLS 1.2 variant, see [Baseline Server TLS 1.2 Authentication KMIP Profile](baseline-server-tls-1-2-authentication-kmip-profile.md).

## Required Operations and Objects

The server must support Create, Register, Get, Get Attributes, Get Attribute List, Locate, Destroy, Query, Discover Versions, and the full set of message structures (batch requests, error responses). Object types Symmetric Key, Public Key, Private Key, Certificate, and Secret Data are all within scope. The mandatory attribute set includes `Unique Identifier`, `Object Type`, `State`, `Cryptographic Algorithm`, `Cryptographic Length`, `Cryptographic Usage Mask`, `Initial Date`, `Last Change Date`, `Activation Date`, and `Deactivation Date`.

## Implications for Implementers

- The Basic Baseline Server is the minimum useful server for a broad-purpose KMIP deployment. All higher-capability v1.1 profiles (Secret Data, Symmetric Key, Asymmetric Key) layer on this foundation.
- Use Discover Versions at the start of every session so clients can adapt to the exact server version without hard-coding version assumptions.
- If your deployment policy requires TLS 1.2 mutual authentication, target [Baseline Server TLS 1.2 Authentication KMIP Profile](baseline-server-tls-1-2-authentication-kmip-profile.md) instead.

## Related Concepts

[Basic Authentication Suite](basic-authentication-suite.md) ·
[Basic Baseline Client KMIP Profile](basic-baseline-client-kmip-profile.md) ·
[Baseline Server TLS 1.2 Authentication KMIP Profile](baseline-server-tls-1-2-authentication-kmip-profile.md) ·
[Base Profiles](base-profiles.md)
