---
title: Discover Versions Client TLS 1.2 Authentication KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.31"
status: draft
related: ["tls-1-2-authentication-suite", "basic-discover-versions-client-kmip-profile", "discover-versions-tls-1-2-authentication-server-profile"]
keywords: ["Discover Versions", "TLS 1.2", "version negotiation", "client profile"]
---

# Discover Versions Client TLS 1.2 Authentication KMIP Profile

## Overview

The Discover Versions Client TLS 1.2 Authentication KMIP Profile is the TLS 1.2 variant of the [Basic Discover Versions Client KMIP Profile](basic-discover-versions-client-kmip-profile.md). The capability is identical — invoking Discover Versions for session-startup version negotiation — but the channel uses the [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md).

The companion server profile is the [Discover Versions TLS 1.2 Authentication Server Profile](discover-versions-tls-1-2-authentication-server-profile.md).

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Discover Versions client (version negotiation) |
| Authentication | TLS 1.2 Authentication Suite |

## Implications for Implementers

- Use this profile when TLS 1.2 mutual authentication is required at the channel level for all KMIP connections, including version-negotiation exchanges.
- Capability requirements are unchanged from the Basic variant; only the transport requirements differ.

## Related Concepts

[Basic Discover Versions Client KMIP Profile](basic-discover-versions-client-kmip-profile.md) ·
[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) ·
[Discover Versions TLS 1.2 Authentication Server Profile](discover-versions-tls-1-2-authentication-server-profile.md)
