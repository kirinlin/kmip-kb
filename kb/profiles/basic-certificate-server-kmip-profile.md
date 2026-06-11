---
title: Basic Certificate Server KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.9"
status: draft
related: ["basic-authentication-suite", "basic-certificate-client-kmip-profile", "basic-asymmetric-key-and-certificate-store-server-kmip-profile", "certificate-server-tls-1-2-authentication-kmip-profile"]
keywords: ["certificate", "X.509", "PKI", "Basic Authentication Suite", "Register", "server profile"]
---

# Basic Certificate Server KMIP Profile

## Overview

The Basic Certificate Server KMIP Profile defines the minimal server capability for managing X.509 Certificate objects in KMIP v1.1, using the [Basic Authentication Suite](basic-authentication-suite.md). It covers certificate storage and retrieval without requiring the server to also manage the asymmetric keys associated with those certificates. This profile is appropriate for a certificate repository use case — where an external CA issues certificates and KMIP provides the distribution and lifecycle-management layer.

The companion client profile is the [Basic Certificate Client KMIP Profile](basic-certificate-client-kmip-profile.md). For the TLS 1.2 variant, see [Certificate Server TLS 1.2 Authentication KMIP Profile](certificate-server-tls-1-2-authentication-kmip-profile.md). To add asymmetric key management alongside certificate storage, see [Basic Asymmetric Key and Certificate Store Server](basic-asymmetric-key-and-certificate-store-server-kmip-profile.md).

## Required Operations and Objects

The server must support Register, Get, Get Attributes, Locate, and Destroy on Certificate objects. X.509 is the required certificate format. Object-state lifecycle (Pre-Active → Active → Deactivated → Destroyed) applies to certificates, with `Initial Date`, `Activation Date`, and `Deactivation Date` attributes tracked.

## Implications for Implementers

- A certificate-only server is useful in scenarios where the key management and certificate management concerns are separated across different systems — for example, HSM-backed key storage with KMIP providing the certificate distribution layer.
- Index certificates by `Subject Distinguished Name`, `Issuer Distinguished Name`, and `Serial Number` attributes to support efficient Locate queries from clients looking for specific certificates.
- If certificates must be linked to their corresponding private keys, extend to the [Asymmetric Key and Certificate Store Server](basic-asymmetric-key-and-certificate-store-server-kmip-profile.md).

## Related Concepts

[Basic Authentication Suite](basic-authentication-suite.md) ·
[Basic Certificate Client KMIP Profile](basic-certificate-client-kmip-profile.md) ·
[Basic Asymmetric Key and Certificate Store Server KMIP Profile](basic-asymmetric-key-and-certificate-store-server-kmip-profile.md) ·
[Certificate Server TLS 1.2 Authentication KMIP Profile](certificate-server-tls-1-2-authentication-kmip-profile.md)
