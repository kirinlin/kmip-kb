---
title: Basic Asymmetric Key and Certificate Store Server KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.7"
status: draft
related: ["basic-authentication-suite", "basic-asymmetric-key-store-server-kmip-profile", "basic-certificate-server-kmip-profile", "basic-asymmetric-key-and-certificate-store-client-kmip-profile", "asymmetric-key-and-certificate-store-server-tls-1-2-authentication-kmip-profile"]
keywords: ["asymmetric key", "certificate", "PKI", "RSA", "key store", "Basic Authentication Suite", "combined profile"]
---

# Basic Asymmetric Key and Certificate Store Server KMIP Profile

## Overview

The Basic Asymmetric Key and Certificate Store Server KMIP Profile combines asymmetric key storage with certificate management into a single server conformance point, using the [Basic Authentication Suite](basic-authentication-suite.md). It extends the [Basic Asymmetric Key Store Server](basic-asymmetric-key-store-server-kmip-profile.md) with Certificate object support, enabling a server to store, retrieve, and manage both key pairs and their associated certificates. This is the natural profile for a v1.1 PKI integration server where both sides of the key-certificate pairing need to be under KMIP management.

The companion client profile is the [Basic Asymmetric Key and Certificate Store Client KMIP Profile](basic-asymmetric-key-and-certificate-store-client-kmip-profile.md). For the TLS 1.2 variant, see [Asymmetric Key and Certificate Store Server TLS 1.2 Authentication KMIP Profile](asymmetric-key-and-certificate-store-server-tls-1-2-authentication-kmip-profile.md).

## Required Operations and Objects

The server must satisfy all requirements of the [Basic Asymmetric Key Store Server](basic-asymmetric-key-store-server-kmip-profile.md) and additionally support Register, Get, Locate, and Destroy on Certificate objects. X.509 is the mandatory certificate format.

## Implications for Implementers

- Storing both the private key and the corresponding certificate under the same KMIP server simplifies certificate lifecycle management: when a certificate is renewed, the associated private key can be located via attribute search without out-of-band record-keeping.
- Consider linking certificates to their private keys using the `Link` attribute (type `Certificate Link` on the key, `Private Key Link` on the certificate). Clients can then navigate between related objects in a single Locate step.
- If server-side key generation is required alongside certificate storage, use the [Basic Asymmetric Key Foundry and Certificate Server profile](basic-asymmetric-key-foundry-and-certificate-server-kmip-profile.md).

## Related Concepts

[Basic Authentication Suite](basic-authentication-suite.md) ·
[Basic Asymmetric Key Store Server KMIP Profile](basic-asymmetric-key-store-server-kmip-profile.md) ·
[Basic Certificate Server KMIP Profile](basic-certificate-server-kmip-profile.md) ·
[Basic Asymmetric Key and Certificate Store Client KMIP Profile](basic-asymmetric-key-and-certificate-store-client-kmip-profile.md) ·
[Asymmetric Key and Certificate Store Server TLS 1.2 Authentication KMIP Profile](asymmetric-key-and-certificate-store-server-tls-1-2-authentication-kmip-profile.md)
