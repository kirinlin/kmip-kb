---
title: Profiles
category: index
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "14"
v1_source_section: "12"
status: reviewed
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
[Profile Information](../structures/profile-information.md).

## Authentication Suites ([KMIP-Prof] §3)

- [Basic Authentication Suite](authentication/basic-authentication-suite.md)
  — TLS mutual auth, cipher suites, port 5696.
- [HTTPS Authentication Suite](authentication/https-authentication-suite.md)
  — HTTP over TLS variant of the Basic suite.
- [TLS 1.2 Authentication Suite](authentication/tls-1-2-authentication-suite.md)
  — TLS 1.2 mutual auth variant.
- [Suite B minLOS 128 Authentication Suite](authentication/suite-b-minlos-128-authentication-suite.md)
  — NSA Suite B 128-bit minimum level of security.
- [Suite B minLOS 192 Authentication Suite](authentication/suite-b-minlos-192-authentication-suite.md)
  — NSA Suite B 192-bit minimum level of security.

## Base and Encoding Profiles ([KMIP-Prof] §5.1–5.5)

- [Base Profiles](base-encoding/base-profiles.md)
  — Baseline Client and Baseline Server; the foundation every other profile builds on.
- [Complete Server Profile](base-encoding/complete-server-profile.md)
  — a server implementing the entire KMIP specification.
- [HTTPS Profiles](base-encoding/https-profiles.md)
  — KMIP over HTTP/TLS framing.
- [XML Profiles](base-encoding/xml-profiles.md)
  — CamelCase XML encoding as an alternative to TTLV binary.
- [JSON Profiles](base-encoding/json-profiles.md)
  — JSON object encoding as an alternative to TTLV binary.

## Key Management Profiles ([KMIP-Prof] §5.6+)

- [Symmetric Key Lifecycle Profiles](key-management/symmetric-key-lifecycle-profiles.md)
  — Create and manage AES/3DES symmetric keys.
- [Symmetric Key Foundry for FIPS 140 Profiles](key-management/symmetric-key-foundry-for-fips-140-profiles.md)
  — FIPS-approved algorithm key generation; Basic, Intermediate, and Advanced client tiers.
- [Asymmetric Key Lifecycle Profiles](key-management/asymmetric-key-lifecycle-profiles.md)
  — RSA public/private key pair management.
- [Cryptographic Profiles](key-management/cryptographic-profiles.md)
  — Server-side Encrypt/Decrypt, Sign/Verify, MAC, and RNG operations.
- [Opaque Managed Object Store Profiles](key-management/opaque-managed-object-store-profiles.md)
  — Centralized storage of uninterpreted binary data (opaque objects).
- [Storage Array with Self-Encrypting Drives Profiles](key-management/storage-array-with-self-encrypting-drives-profiles.md)
  — Storage array SED authentication key management.
- [Tape Library Profiles](key-management/tape-library-profiles.md)
  — LTO tape encryption key management with KAD-based identifiers.
- [AES XTS Profiles](key-management/aes-xts-profiles.md)
  — AES XTS sector-encryption key management (NVMe, FDE); with and without KEK wrapping.
- [Suite B Profiles](key-management/suite-b-profiles.md)
  — NSA Suite B cryptographic profile bundle.
- [Quantum Safe Profiles](key-management/quantum-safe-profiles.md)
  — Post-quantum algorithms (McEliece, SPHINCS); TLS 1.3 mandatory.
- [Quantum Safe Client](key-management/quantum-safe-client.md)
  — Quantum-safe client profile specification.
- [Quantum Safe Server](key-management/quantum-safe-server.md)
  — Quantum-safe server profile specification.
- [Mandatory Quantum Safe Test Cases KMIP v2.0](key-management/mandatory-quantum-safe-test-cases-kmip-v2-0.md)
  — Mandatory test cases for quantum-safe conformance.
- [PKCS#11 Profiles](key-management/pkcs-11-profiles.md)
  — KMIP as a PKCS#11 Cryptoki transport.

## v1.x Named Profiles ([KMIP-Prof] §4/§5, v1.0–v1.4)

The [v1/](v1/index.md) subdirectory contains 52 individually named conformance
profiles from the v1.x Profiles document ([KMIP-Prof] §4 in v1.0–v1.2, §5 in
v1.3–v1.4). These cover baseline, symmetric key, asymmetric key, certificate,
secret data, discover-versions, and storage-client profiles in both the Basic
and TLS 1.2 authentication variants. See the
[v1.x Named Profiles index](v1/index.md) for the full list.
