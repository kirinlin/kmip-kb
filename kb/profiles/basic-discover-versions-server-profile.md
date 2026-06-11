---
title: Basic Discover Versions Server Profile
category: profile
spec_version: "1.1"
spec_versions: ["1.1"]
source_section: "prof-4.1"
status: draft
related: ["basic-authentication-suite", "basic-baseline-server-kmip-profile", "basic-discover-versions-client-kmip-profile", "discover-versions-tls-1-2-authentication-server-profile"]
keywords: ["Discover Versions", "version negotiation", "Basic Authentication Suite", "server profile"]
---

# Basic Discover Versions Server Profile

## Overview

The Basic Discover Versions Server Profile is the minimal KMIP v1.1 server conformance point. A server claiming this profile can respond to the Discover Versions operation and use the [Basic Authentication Suite](basic-authentication-suite.md) for transport security. It serves as the entry point for servers that may not yet support the full Baseline capability: a client can connect and determine which KMIP versions and supported operations the server offers before attempting any managed-object operations.

The companion client profile is the [Basic Discover Versions Client KMIP Profile](basic-discover-versions-client-kmip-profile.md). For the TLS 1.2 variant of this server profile, see [Discover Versions TLS 1.2 Authentication Server Profile](discover-versions-tls-1-2-authentication-server-profile.md).

## Required Operations

The server must support the Discover Versions operation, which returns the list of KMIP versions the server implements along with the operations and object types supported under each version. No other managed-object operations are required by this profile alone; higher-level profiles that layer on top add the object-management surface.

## Implications for Implementers

- Implement Discover Versions early in any server implementation — clients use it during session initialization to confirm compatibility before sending payload requests.
- A server claiming only this profile is not useful for actual key management. In practice, pair it with at least the [Basic Baseline Server](basic-baseline-server-kmip-profile.md) profile.
- The response to Discover Versions must accurately enumerate all operations the server supports for each advertised version. Advertising an operation that the server cannot actually perform will mislead clients and cause conformance test failures.

## Related Concepts

[Basic Authentication Suite](basic-authentication-suite.md) ·
[Basic Baseline Server KMIP Profile](basic-baseline-server-kmip-profile.md) ·
[Basic Discover Versions Client KMIP Profile](basic-discover-versions-client-kmip-profile.md) ·
[Discover Versions TLS 1.2 Authentication Server Profile](discover-versions-tls-1-2-authentication-server-profile.md)
