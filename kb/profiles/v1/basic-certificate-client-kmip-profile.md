---
title: Basic Certificate Client KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.29"
status: reviewed
related: ["basic-authentication-suite", "basic-certificate-server-kmip-profile", "certificate-client-tls-1-2-authentication-kmip-profile", "basic-asymmetric-key-and-certificate-store-client-kmip-profile"]
keywords: ["certificate", "X.509", "PKI", "Register", "Basic Authentication Suite", "client profile"]
---

# Basic Certificate Client KMIP Profile

## Overview

The Basic Certificate Client KMIP Profile defines client requirements for storing and retrieving X.509 certificates at a KMIP v1.1 server, using the [Basic Authentication Suite](../authentication/basic-authentication-suite.md). A client claiming this profile can register CA-issued certificates and retrieve them on demand, without needing to manage the associated private keys through KMIP. The companion server profile is the [Basic Certificate Server KMIP Profile](basic-certificate-server-kmip-profile.md).

For the TLS 1.2 variant, see [Certificate Client TLS 1.2 Authentication KMIP Profile](certificate-client-tls-1-2-authentication-kmip-profile.md).

## Required Operations

The client must support Register and Get on Certificate objects. Locate is expected for attribute-based certificate lookups. X.509 is the required certificate format.

## Implications for Implementers

- This profile suits clients that manage only the certificate layer — for example, a TLS terminator that stores and retrieves server certificates via KMIP but manages private keys through a separate mechanism (HSM direct integration, PKCS#11, etc.).
- When registering certificates, populate `Subject Distinguished Name`, `Issuer Distinguished Name`, `Serial Number`, and validity-period attributes to enable efficient Locate queries.
- To manage both the certificate and its associated key pair together, use the [Basic Asymmetric Key and Certificate Store Client](basic-asymmetric-key-and-certificate-store-client-kmip-profile.md).

## Related Concepts

[Basic Authentication Suite](../authentication/basic-authentication-suite.md) ·
[Basic Certificate Server KMIP Profile](basic-certificate-server-kmip-profile.md) ·
[Certificate Client TLS 1.2 Authentication KMIP Profile](certificate-client-tls-1-2-authentication-kmip-profile.md) ·
[Basic Asymmetric Key and Certificate Store Client KMIP Profile](basic-asymmetric-key-and-certificate-store-client-kmip-profile.md)
