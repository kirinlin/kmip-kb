---
title: TLS 1.2 Authentication Suite
category: profile
spec_version: "1.2"
spec_versions: ["1.0", "1.1", "1.2"]
source_section: "prof-3.2"
status: reviewed
related: ["basic-authentication-suite", "https-authentication-suite"]
keywords: ["TLS 1.2", "authentication suite", "cipher suite", "mutual authentication", "port 5696", "transport security"]
---

# TLS 1.2 Authentication Suite

## Overview

The TLS 1.2 Authentication Suite (§3.2 of early KMIP-Prof releases) defines the stricter of the two transport security options available to KMIP v1.0–v1.2 implementations. Profiles that claim this suite mandate TLS 1.2 specifically, along with an explicit set of permitted cipher suites, mutual certificate-based authentication, and the standard KMIP port. It was superseded in KMIP 2.0 when the [Basic Authentication Suite](basic-authentication-suite.md) was updated to mandate TLS 1.3 and the separate TLS 1.2 option was retired.

## Protocol Requirements

TLS 1.2 is the minimum permitted protocol version; earlier TLS versions and all SSL variants are prohibited. Permitted cipher suites include selections from the `TLS_RSA_WITH_AES_*`, `TLS_ECDHE_RSA_WITH_AES_*`, and `TLS_ECDHE_ECDSA_WITH_AES_*` families with SHA-256 or SHA-384 MACs. No cipher suite outside the defined list is permitted for conformant peers.

## Authentication Requirements

Servers must require mutual TLS authentication. Client identity is established through the TLS handshake certificate. When a client also presents a KMIP `Authentication` object, that credential supplements (and may override) the TLS-level identity for authorization decisions. Unauthenticated or anonymous TLS connections are not permitted.

## Port

Conformant deployments use TCP port 5696, the IANA-assigned KMIP port. Non-standard ports require explicit out-of-band agreement between client and server.

## Relationship to the Basic Authentication Suite

In KMIP v1.0–v1.2, profiles came in two authentication-suite variants: those using the [Basic Authentication Suite](basic-authentication-suite.md) (which placed fewer restrictions on the TLS version) and those using the TLS 1.2 Authentication Suite (this profile). A profile name ending in "TLS 1.2 Authentication" signals the stricter variant. In v2.0 and later, the distinction was eliminated: the single Basic Authentication Suite was updated to require TLS 1.3, and all per-profile authentication variants were removed.

## Implications for Implementers

- Any client or server that only needs to interoperate with v1.x peers should implement this suite; if forward compatibility with v2.x systems matters, plan a migration path to TLS 1.3.
- Mutual TLS requires both sides to have certificates from a shared trust anchor. Establish the PKI chain before running KMIP conformance tests — authentication failures at the TLS layer will produce non-conformance results that have nothing to do with the KMIP payload.
- The cipher suite list in the profile specification is normative; do not add suites beyond it even if your TLS library offers them, since strict peers may reject connections advertising non-listed suites.

## Related Concepts

[Basic Authentication Suite](basic-authentication-suite.md) ·
[HTTPS Authentication Suite](https-authentication-suite.md)
