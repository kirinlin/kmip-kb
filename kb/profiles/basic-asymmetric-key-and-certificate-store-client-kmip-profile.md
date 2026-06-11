---
title: Basic Asymmetric Key and Certificate Store Client KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.27"
status: reviewed
related: ["basic-authentication-suite", "basic-asymmetric-key-and-certificate-store-server-kmip-profile", "asymmetric-key-and-certificate-store-client-tls-1-2-authentication-kmip-profile", "basic-asymmetric-key-store-client-kmip-profile", "basic-certificate-client-kmip-profile"]
keywords: ["asymmetric key", "certificate", "PKI", "RSA", "Basic Authentication Suite", "client profile"]
---

# Basic Asymmetric Key and Certificate Store Client KMIP Profile

## Overview

The Basic Asymmetric Key and Certificate Store Client KMIP Profile defines client requirements for storing and retrieving both asymmetric key pairs and X.509 certificates at a KMIP v1.1 server, using the [Basic Authentication Suite](basic-authentication-suite.md). It combines the capabilities of the [Basic Asymmetric Key Store Client](basic-asymmetric-key-store-client-kmip-profile.md) and the [Basic Certificate Client](basic-certificate-client-kmip-profile.md) profiles. The companion server profile is the [Basic Asymmetric Key and Certificate Store Server KMIP Profile](basic-asymmetric-key-and-certificate-store-server-kmip-profile.md).

For the TLS 1.2 variant, see [Asymmetric Key and Certificate Store Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-and-certificate-store-client-tls-1-2-authentication-kmip-profile.md).

## Required Operations

The client must support Register and Get on Public Key, Private Key, and Certificate objects, plus Locate for searching by attribute. RSA is the mandatory asymmetric algorithm; X.509 is the required certificate format.

## Implications for Implementers

- This profile is the right choice for clients that manage full PKI entities — importing key pairs from an HSM or CA alongside the certificates that bind those keys to identities.
- Use `Link` attributes when registering certificates to reference the associated Private Key and Public Key objects. Future Locate calls can then navigate from a certificate to its key pair.
- For TLS 1.2 mutual authentication, target [Asymmetric Key and Certificate Store Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-and-certificate-store-client-tls-1-2-authentication-kmip-profile.md).

## Related Concepts

[Basic Authentication Suite](basic-authentication-suite.md) ·
[Basic Asymmetric Key and Certificate Store Server KMIP Profile](basic-asymmetric-key-and-certificate-store-server-kmip-profile.md) ·
[Basic Asymmetric Key Store Client KMIP Profile](basic-asymmetric-key-store-client-kmip-profile.md) ·
[Basic Certificate Client KMIP Profile](basic-certificate-client-kmip-profile.md) ·
[Asymmetric Key and Certificate Store Client TLS 1.2 Authentication KMIP Profile](asymmetric-key-and-certificate-store-client-tls-1-2-authentication-kmip-profile.md)
