---
title: Profiles
category: index
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "14"
v1_source_section: "12"
status: draft
related: ["kmip-server-implementation-conformance", "kmip-client-implementation-conformance"]
keywords: ["profiles", "conformance", "baseline", "interoperability"]
---

# Profiles

How conformance works in KMIP: the spec's §14 (v1.x §12) defers to the
separate OASIS profiles document ([KMIP-Prof]), which defines named server and
client profiles — baseline messaging plus use-case bundles (symmetric key
lifecycle, asymmetric keys, cryptographic services, tape libraries, ...) with
test cases.

## Implementation Conformance

- [KMIP Server Implementation Conformance](kmip-server-implementation-conformance.md)
  — what it means for a server to conform (v2.1 §14.2).
- [KMIP Client Implementation Conformance](kmip-client-implementation-conformance.md)
  — the client-side counterpart (v2.1 §14.1).

Runtime discovery of what a peer actually implements goes through
[Query](../operations/query.md) and, from 1.3,
[Profile Information](../ttlv/profile-information.md).

## Authentication Suites ([KMIP-Prof] §3)

- [Basic Authentication Suite](basic-authentication-suite.md)
  — TLS mutual auth, cipher suites, port 5696.
- [HTTPS Authentication Suite](https-authentication-suite.md)
  — HTTP over TLS variant of the Basic suite.

## Base and Encoding Profiles ([KMIP-Prof] §5.1–5.5)

- [Base Profiles](base-profiles.md)
  — Baseline Client and Baseline Server; the foundation every other profile builds on.
- [Complete Server Profile](complete-server-profile.md)
  — a server implementing the entire KMIP specification.
- [HTTPS Profiles](https-profiles.md)
  — KMIP over HTTP/TLS framing.
- [XML Profiles](xml-profiles.md)
  — CamelCase XML encoding as an alternative to TTLV binary.
- [JSON Profiles](json-profiles.md)
  — JSON object encoding as an alternative to TTLV binary.

## Key Management Profiles ([KMIP-Prof] §5.6–5.14)

- [Symmetric Key Lifecycle Profiles](symmetric-key-lifecycle-profiles.md)
  — Create and manage AES/3DES symmetric keys.
- [Symmetric Key Foundry for FIPS 140 Profiles](symmetric-key-foundry-for-fips-140-profiles.md)
  — FIPS-approved algorithm key generation; Basic, Intermediate, and Advanced client tiers.
- [Asymmetric Key Lifecycle Profiles](asymmetric-key-lifecycle-profiles.md)
  — RSA public/private key pair management.
- [Cryptographic Profiles](cryptographic-profiles.md)
  — Server-side Encrypt/Decrypt, Sign/Verify, MAC, and RNG operations.
- [Opaque Managed Object Store Profiles](opaque-managed-object-store-profiles.md)
  — Centralized storage of uninterpreted binary data (opaque objects).
- [Storage Array with Self-Encrypting Drives Profiles](storage-array-with-self-encrypting-drives-profiles.md)
  — Storage array SED authentication key management.
- [Tape Library Profiles](tape-library-profiles.md)
  — LTO tape encryption key management with KAD-based identifiers.
- [AES XTS Profiles](aes-xts-profiles.md)
  — AES XTS sector-encryption key management (NVMe, FDE); with and without KEK wrapping.
- [Quantum Safe Profiles](quantum-safe-profiles.md)
  — Post-quantum algorithms (McEliece, SPHINCS); TLS 1.3 mandatory.
- [PKCS#11 Profiles](pkcs-11-profiles.md)
  — KMIP as a PKCS#11 Cryptoki transport.
