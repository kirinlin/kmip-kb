---
title: Basic Discover Versions Client KMIP Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.21"
status: draft
related: ["basic-authentication-suite", "basic-discover-versions-server-profile", "discover-versions-client-tls-1-2-authentication-kmip-profile"]
keywords: ["Discover Versions", "version negotiation", "Basic Authentication Suite", "client profile"]
---

# Basic Discover Versions Client KMIP Profile

## Overview

The Basic Discover Versions Client KMIP Profile defines the minimum client capability for performing version negotiation with a KMIP v1.1 server, using the [Basic Authentication Suite](basic-authentication-suite.md). A client claiming this profile can invoke the Discover Versions operation and use the response to determine which KMIP versions and operations the server supports.

The companion server profile is the [Basic Discover Versions Server Profile](basic-discover-versions-server-profile.md). For the TLS 1.2 variant, see [Discover Versions Client TLS 1.2 Authentication KMIP Profile](discover-versions-client-tls-1-2-authentication-kmip-profile.md).

## Required Operations

The client must be able to send a Discover Versions request and parse the response listing the server's supported protocol versions and operations. No managed-object operations are required by this profile alone.

## Implications for Implementers

- Clients should call Discover Versions at session startup to confirm KMIP version compatibility before sending any managed-object requests. This avoids protocol-version mismatches at runtime.
- This profile is rarely claimed in isolation; in practice, pair it with the applicable managed-object client profile. A client that only claims Discover Versions Client has no other KMIP capability.

## Related Concepts

[Basic Authentication Suite](basic-authentication-suite.md) ·
[Basic Discover Versions Server Profile](basic-discover-versions-server-profile.md) ·
[Discover Versions Client TLS 1.2 Authentication KMIP Profile](discover-versions-client-tls-1-2-authentication-kmip-profile.md)
