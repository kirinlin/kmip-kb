---
title: Basic Authentication Suite
category: profile
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "prof-3.1"
status: reviewed
related: ["https-authentication-suite", "kmip-server-implementation-conformance", "kmip-client-implementation-conformance"]
keywords: ["TLS", "authentication", "cipher suite", "mutual authentication", "port 5696", "transport security"]
---

# Basic Authentication Suite

## Overview

The Basic Authentication Suite defines the channel-security requirements that apply to most KMIP profiles. It pins the TLS version, cipher suites, mutual-authentication obligations, and the standard TCP port. Any profile that claims to use the Basic Authentication Suite inherits these requirements without restating them.

## Protocol Requirements

TLS 1.3 is mandatory for conformant servers and strongly recommended for clients. TLS 1.2 is permitted as a fallback but should be treated as transitional. SSL in any version and TLS 1.0/1.1 are explicitly prohibited.

Servers must support both mandatory TLS 1.3 cipher suites: `TLS13-AES-256-GCM-SHA384` and `TLS13-CHACHA20-POLY1305-SHA256`. Clients must support at least one. For TLS 1.2, a specified subset of `TLS_RSA_*`, `TLS_ECDH*`, and `TLS_PSK_*` cipher suites is allowed; nothing outside that list is permitted for either side.

## Client Authenticity and Identity

Servers must require TLS mutual authentication for all operational requests. When a client does not include an `Authentication` object in its request, the server derives client identity from the TLS certificate. When a client does include an `Authentication` object, that credential takes precedence over the channel identity. Automated provisioning workflows are the sole exception where mutual TLS may be deferred.

## Port

Conformant servers listen on TCP port 5696, the IANA-assigned KMIP port. Any non-standard port requires explicit out-of-band configuration on the client.

## Implications for Implementers

- Negotiate TLS 1.3 first; fall back to 1.2 only when the peer cannot support 1.3 and only after consulting your security policy.
- Provision server and client certificates from a shared PKI trust anchor so that mutual authentication succeeds at connection setup, before any KMIP message is exchanged.
- Hard-code port 5696 as the default but expose it as a configurable parameter — some deployments run multiple KMIP instances on distinct ports.
- Do not offer cipher suites outside the specified list even as optional; some implementations enforce the prohibition by rejecting connections that advertise non-listed suites.

## Related Concepts

[HTTPS Authentication Suite](https-authentication-suite.md) ·
[KMIP Server Implementation Conformance](kmip-server-implementation-conformance.md) ·
[KMIP Client Implementation Conformance](kmip-client-implementation-conformance.md)
