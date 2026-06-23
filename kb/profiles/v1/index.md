---
title: v1.x Named Profiles
category: index
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4"]
source_section: "prof-4"
status: reviewed
related: ["baseline-server-basic-kmip-profile", "complete-server-basic-kmip-profile", "secret-data-kmip-profile"]
keywords: ["profiles", "v1.x", "named profiles", "conformance", "baseline", "TLS 1.2 authentication", "foundry", "store"]
---

# v1.x Named Profiles

The 52 individually named conformance profiles from the v1.x Profiles document
([KMIP-Prof] §4 in v1.0–v1.2, §5 in v1.3–v1.4). Each pairs a capability set
(baseline, symmetric/asymmetric key, certificate, secret data, etc.) with a
role (client or server) and an authentication variant — **Basic** or
**TLS 1.2 Authentication**. v2.0 replaced this enumeration of named profiles
with the composable profile model documented at the
[profiles index](../index.md).

## Baseline

- [Baseline Client Basic](baseline-client-basic-kmip-profile.md) ·
  [Baseline Server Basic](baseline-server-basic-kmip-profile.md)
- [Baseline Client TLS v1.2](baseline-client-tls-v1-2-kmip-profile.md) ·
  [Baseline Server TLS v1.2](baseline-server-tls-v1-2-kmip-profile.md)
- [Baseline Client TLS 1.2 Authentication](baseline-client-tls-1-2-authentication-kmip-profile.md) ·
  [Baseline Server TLS 1.2 Authentication](baseline-server-tls-1-2-authentication-kmip-profile.md)
- [Basic Baseline Client](basic-baseline-client-kmip-profile.md) ·
  [Basic Baseline Server](basic-baseline-server-kmip-profile.md)

## Complete server

- [Complete Server Basic](complete-server-basic-kmip-profile.md) ·
  [Complete Server TLS v1.2](complete-server-tls-v1-2-kmip-profile.md)

## Symmetric key

- [Basic Symmetric Key Store Client](basic-symmetric-key-store-client-kmip-profile.md) ·
  [Basic Symmetric Key Store and Server](basic-symmetric-key-store-and-server-kmip-profile.md) ·
  [Basic Symmetric Key Store and Server TLS 1.2 Authentication](basic-symmetric-key-store-and-server-tls-1-2-authentication-kmip-profile.md)
- [Symmetric Key Store Client TLS 1.2 Authentication](symmetric-key-store-client-tls-1-2-authentication-kmip-profile.md) ·
  [Symmetric Key Store and Server TLS 1.2 Authentication](symmetric-key-store-and-server-tls-1-2-authentication-kmip-profile.md)
- [Basic Symmetric Key Foundry Client](basic-symmetric-key-foundry-client-kmip-profile.md) ·
  [Basic Symmetric Key Foundry and Server](basic-symmetric-key-foundry-and-server-kmip-profile.md) ·
  [Basic Symmetric Key Foundry and Server TLS 1.2 Authentication](basic-symmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile.md)
- [Symmetric Key Foundry Client TLS 1.2 Authentication](symmetric-key-foundry-client-tls-1-2-authentication-kmip-profile.md) ·
  [Symmetric Key Foundry and Server TLS 1.2 Authentication](symmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile.md)

## Asymmetric key

- [Basic Asymmetric Key Store Client](basic-asymmetric-key-store-client-kmip-profile.md) ·
  [Basic Asymmetric Key Store Server](basic-asymmetric-key-store-server-kmip-profile.md)
- [Asymmetric Key Store Client TLS 1.2 Authentication](asymmetric-key-store-client-tls-1-2-authentication-kmip-profile.md) ·
  [Asymmetric Key Store Server TLS 1.2 Authentication](asymmetric-key-store-server-tls-1-2-authentication-kmip-profile.md)
- [Basic Asymmetric Key Foundry Client](basic-asymmetric-key-foundry-client-kmip-profile.md) ·
  [Basic Asymmetric Key Foundry and Server](basic-asymmetric-key-foundry-and-server-kmip-profile.md)
- [Asymmetric Key Foundry Client TLS 1.2 Authentication](asymmetric-key-foundry-client-tls-1-2-authentication-kmip-profile.md) ·
  [Asymmetric Key Foundry and Server TLS 1.2 Authentication](asymmetric-key-foundry-and-server-tls-1-2-authentication-kmip-profile.md)
- [Basic Asymmetric Key and Certificate Store Client](basic-asymmetric-key-and-certificate-store-client-kmip-profile.md) ·
  [Basic Asymmetric Key and Certificate Store Server](basic-asymmetric-key-and-certificate-store-server-kmip-profile.md)
- [Asymmetric Key and Certificate Store Client TLS 1.2 Authentication](asymmetric-key-and-certificate-store-client-tls-1-2-authentication-kmip-profile.md) ·
  [Asymmetric Key and Certificate Store Server TLS 1.2 Authentication](asymmetric-key-and-certificate-store-server-tls-1-2-authentication-kmip-profile.md)
- [Basic Asymmetric Key Foundry and Certificate Client](basic-asymmetric-key-foundry-and-certificate-client-kmip-profile.md) ·
  [Basic Asymmetric Key Foundry and Certificate Server](basic-asymmetric-key-foundry-and-certificate-server-kmip-profile.md)
- [Asymmetric Key Foundry and Certificate Client TLS 1.2 Authentication](asymmetric-key-foundry-and-certificate-client-tls-1-2-authentication-kmip-profile.md) ·
  [Asymmetric Key Foundry and Certificate Server TLS 1.2 Authentication](asymmetric-key-foundry-and-certificate-server-tls-1-2-authentication-kmip-profile.md)

## Certificate

- [Basic Certificate Client](basic-certificate-client-kmip-profile.md) ·
  [Basic Certificate Server](basic-certificate-server-kmip-profile.md)
- [Certificate Client TLS 1.2 Authentication](certificate-client-tls-1-2-authentication-kmip-profile.md) ·
  [Certificate Server TLS 1.2 Authentication](certificate-server-tls-1-2-authentication-kmip-profile.md)

## Secret data

- [Basic Secret Data Client](basic-secret-data-client-kmip-profile.md) ·
  [Basic Secret Data Server](basic-secret-data-server-kmip-profile.md)
- [Secret Data](secret-data-kmip-profile.md) ·
  [Secret Data TLS 1.2 Authentication](secret-data-tls-1-2-authentication-kmip-profile.md)
- [Secret Data Client TLS 1.2 Authentication](secret-data-client-tls-1-2-authentication-kmip-profile.md) ·
  [Secret Data Server TLS 1.2 Authentication](secret-data-server-tls-1-2-authentication-kmip-profile.md)

## Discover versions

- [Basic Discover Versions Client](basic-discover-versions-client-kmip-profile.md) ·
  [Basic Discover Versions Server](basic-discover-versions-server-profile.md)
- [Discover Versions Client TLS 1.2 Authentication](discover-versions-client-tls-1-2-authentication-kmip-profile.md) ·
  [Discover Versions TLS 1.2 Authentication Server](discover-versions-tls-1-2-authentication-server-profile.md)

## Storage

- [Storage Client](storage-client-kmip-profile.md) ·
  [Storage Client TLS 1.2 Authentication](storage-client-tls-1-2-authentication-kmip-profile.md)
