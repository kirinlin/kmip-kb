---
title: Discover Versions TLS 1.2 Authentication Server Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.11"
status: draft
related: ["tls-1-2-authentication-suite", "basic-discover-versions-server-profile", "discover-versions-client-tls-1-2-authentication-kmip-profile"]
keywords: ["Discover Versions", "TLS 1.2", "version negotiation", "server profile"]
---

# Discover Versions TLS 1.2 Authentication Server Profile

## Overview

The Discover Versions TLS 1.2 Authentication Server Profile is the TLS 1.2 variant of the [Basic Discover Versions Server Profile](basic-discover-versions-server-profile.md). The capability is identical — the server supports the Discover Versions operation — but the channel uses the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) rather than the Basic Authentication Suite.

The companion client profile is the [Discover Versions Client TLS 1.2 Authentication KMIP Profile](discover-versions-client-tls-1-2-authentication-kmip-profile.md).

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Discover Versions server (version negotiation) |
| Authentication | TLS 1.2 Authentication Suite |

## Implications for Implementers

- Use this profile in KMIP v1.1 deployments where your security policy mandates TLS 1.2 mutual authentication at the transport layer.
- The Discover Versions capability and response format are unchanged from the Basic variant; only the transport requirements differ.

## Related Concepts

[Basic Discover Versions Server Profile](basic-discover-versions-server-profile.md) ·
[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Discover Versions Client TLS 1.2 Authentication KMIP Profile](discover-versions-client-tls-1-2-authentication-kmip-profile.md)
