---
title: Basic Asymmetric Key Foundry and Certificate Server KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.10"
status: draft
related: ["basic-authentication-suite", "basic-asymmetric-key-foundry-and-server-kmip-profile", "basic-certificate-server-kmip-profile", "basic-asymmetric-key-foundry-and-certificate-client-kmip-profile", "asymmetric-key-foundry-and-certificate-server-tls-1-2-authentication-kmip-profile"]
keywords: ["asymmetric key", "certificate", "PKI", "Create Key Pair", "RSA", "Basic Authentication Suite", "full PKI server"]
---

# Basic Asymmetric Key Foundry and Certificate Server KMIP Profile

## Overview

The Basic Asymmetric Key Foundry and Certificate Server KMIP Profile is the most comprehensive asymmetric-key server capability in KMIP v1.1 using the [Basic Authentication Suite](basic-authentication-suite.md). It combines server-side key-pair generation (the "Foundry" capability of [Basic Asymmetric Key Foundry and Server](basic-asymmetric-key-foundry-and-server-kmip-profile.md)) with X.509 certificate storage (from [Basic Certificate Server](basic-certificate-server-kmip-profile.md)) into a single profile. A server claiming this profile can generate key pairs and then store the CA-issued certificates for those keys, covering the full enrollment workflow under KMIP management.

The companion client profile is the [Basic Asymmetric Key Foundry and Certificate Client KMIP Profile](basic-asymmetric-key-foundry-and-certificate-client-kmip-profile.md). For the TLS 1.2 variant, see [Asymmetric Key Foundry and Certificate Server TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-and-certificate-server-tls-1-2-authentication-kmip-profile.md).

## Required Operations and Objects

All requirements of both [Basic Asymmetric Key Foundry and Server](basic-asymmetric-key-foundry-and-server-kmip-profile.md) and [Basic Certificate Server](basic-certificate-server-kmip-profile.md) apply: Create Key Pair, Register, Get, Get Attributes, Locate, Activate, Revoke, and Destroy on Public Key, Private Key, and Certificate objects.

## Implications for Implementers

- This profile enables the "generate-then-certify" workflow: a client invokes Create Key Pair, retrieves the public key, submits it to a CA for signing, and then registers the resulting certificate back under the same KMIP server using Register on Certificate. Both the key pair and the certificate end up under unified lifecycle management.
- Use `Link` attributes to bind the private key, public key, and certificate together. Future clients can then navigate from any one object to the others using Locate.
- This is the recommended profile for enterprise PKI integrations where KMIP serves as the secure key repository behind a certificate authority.

## Related Concepts

[Basic Authentication Suite](basic-authentication-suite.md) ·
[Basic Asymmetric Key Foundry and Server KMIP Profile](basic-asymmetric-key-foundry-and-server-kmip-profile.md) ·
[Basic Certificate Server KMIP Profile](basic-certificate-server-kmip-profile.md) ·
[Basic Asymmetric Key Foundry and Certificate Client KMIP Profile](basic-asymmetric-key-foundry-and-certificate-client-kmip-profile.md) ·
[Asymmetric Key Foundry and Certificate Server TLS 1.2 Authentication KMIP Profile](asymmetric-key-foundry-and-certificate-server-tls-1-2-authentication-kmip-profile.md)
