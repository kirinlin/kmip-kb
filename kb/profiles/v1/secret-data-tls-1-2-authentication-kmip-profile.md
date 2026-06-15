---
title: Secret Data TLS 1.2 Authentication KMIP Profile
category: profile
spec_version: "1.0"
spec_versions: ["1.0"]
source_section: "prof-4.4"
status: reviewed
related: ["tls-1-2-authentication-suite", "basic-authentication-suite", "secret-data-kmip-profile", "secret-data-server-tls-1-2-authentication-kmip-profile", "secret-data-client-tls-1-2-authentication-kmip-profile"]
keywords: ["secret data", "TLS 1.2", "authentication suite", "password", "token", "opaque secret"]
---

# Secret Data TLS 1.2 Authentication KMIP Profile

## Overview

The Secret Data TLS 1.2 Authentication KMIP Profile is the stricter-transport variant of the [Secret Data KMIP Profile](secret-data-kmip-profile.md). It carries identical capability requirements — Register, Get, Locate, and Destroy on Secret Data objects — but mandates the [TLS 1.2 Authentication Suite](../authentication/tls-1-2-authentication-suite.md) for the channel rather than the Basic Authentication Suite. This profile is a KMIP v1.0 combined client-and-server definition. In KMIP v1.1 the same combination was represented as separate server ([Secret Data Server TLS 1.2 Authentication KMIP Profile](secret-data-server-tls-1-2-authentication-kmip-profile.md)) and client ([Secret Data Client TLS 1.2 Authentication KMIP Profile](secret-data-client-tls-1-2-authentication-kmip-profile.md)) profiles.

## Profile Composition

| Layer | Profile |
|---|---|
| Capability | Secret Data KMIP Profile (Register, Get, Locate, Destroy on Secret Data objects) |
| Authentication | TLS 1.2 Authentication Suite (TLS 1.2 mandatory, mutual certificate auth, port 5696) |

## Implications for Implementers

- Choose this profile over the [Basic variant](secret-data-kmip-profile.md) when your security policy mandates TLS 1.2 specifically, rather than allowing a wider TLS version range.
- The capability requirements are unchanged. Secret Data objects carry opaque values; no key-format handling is needed, but object-state lifecycle and attribute management still apply.
- For interoperability with KMIP v1.1 and later systems that declare separate client or server roles, target the v1.1 TLS 1.2 variants instead.

## Related Concepts

[Secret Data KMIP Profile](secret-data-kmip-profile.md) ·
[TLS 1.2 Authentication Suite](../authentication/tls-1-2-authentication-suite.md) ·
[Secret Data Server TLS 1.2 Authentication KMIP Profile](secret-data-server-tls-1-2-authentication-kmip-profile.md) ·
[Secret Data Client TLS 1.2 Authentication KMIP Profile](secret-data-client-tls-1-2-authentication-kmip-profile.md)
