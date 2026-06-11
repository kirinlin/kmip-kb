---
title: HTTPS Authentication Suite
category: profile
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "prof-3.2"
status: draft
related: ["basic-authentication-suite", "https-profiles", "kmip-server-implementation-conformance"]
keywords: ["HTTPS", "HTTP over TLS", "authentication", "transport", "RFC2818"]
---

# HTTPS Authentication Suite

## Overview

The HTTPS Authentication Suite is a transport-level variant of the [Basic Authentication Suite](basic-authentication-suite.md) that wraps KMIP messages in HTTP over TLS rather than raw TLS. It inherits the full cipher-suite, mutual-authentication, and TLS version requirements from the Basic suite and adds HTTP-layer rules for content type and caching.

## Relationship to the Basic Suite

The HTTPS suite delegates its protocol version, cipher suite, and client-authenticity requirements entirely to the corresponding Basic Authentication clauses. The only additions are the HTTP layer: method (POST), content type (`application/octet-stream` for TTLV, `text/xml` for XML, `application/json` for JSON), and mandatory `Cache-Control: no-cache`. Servers return HTTP 200 whenever a KMIP response is available.

## Port and URI

KMIP servers that support both TTLV-over-TLS and HTTPS on the same instance should use port 5696 for both, with `/kmip` as the recommended URI path. Servers may choose a different port or URI for HTTPS if the deployment requires it; clients must support user-configurable target URIs and port numbers.

## Implications for Implementers

- Servers that support server-to-client operations must also behave as an HTTPS client (initiating connections back to the KMIP client).
- Clients that support responding to server-to-client operations must behave as an HTTPS server.
- Use the same PKI trust anchor and mutual-auth setup as the Basic suite — the difference is only the framing layer.
- When `Content-Length` is omitted or incorrect, parsing of batched responses becomes unreliable; always compute and send it.

## Related Concepts

[Basic Authentication Suite](basic-authentication-suite.md) ·
[HTTPS Profiles](https-profiles.md) ·
[KMIP Server Implementation Conformance](kmip-server-implementation-conformance.md)
