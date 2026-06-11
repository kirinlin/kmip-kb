---
title: Quantum Safe Server
category: profile
spec_version: "2.1"
spec_versions: ["2.0", "2.1"]
source_section: "prof-5.16"
status: reviewed
related: ["quantum-safe-profiles", "quantum-safe-client", "mandatory-quantum-safe-test-cases-kmip-v2-0", "base-profiles", "cryptographic-profiles", "asymmetric-key-lifecycle-profiles"]
keywords: ["quantum safe", "post-quantum", "McEliece", "SPHINCS", "TLS 1.3", "Protection Level", "Protection Period", "Quantum Safe attribute", "PQC", "server profile"]
---

# Quantum Safe Server

## Overview

The Quantum Safe Server profile (§5.16 of [KMIP-Prof]) defines the server-side conformance requirements for quantum-safe key management. It extends the [Baseline Server](base-profiles.md) with a specific set of algorithms, new attributes, operations, and key formats designed to protect key material against future quantum computer attacks. TLS 1.3 is mandatory; TLS 1.2 fallback is not permitted.

For the broader context of the quantum-safe profile family, see [Quantum Safe Profiles](quantum-safe-profiles.md).

## Required Objects and Operations

The server must support the following object types: Certificate, Private Key, Public Key, and Symmetric Key.

Operations required beyond the Baseline Server: Create, Create Key Pair, Certify, Re-Certify, Register, Re-key, Re-key Key Pair, Decrypt, Encrypt, Sign, Signature Verify. Server-to-client operations Notify and Put are also required.

## Required Algorithms and Key Formats

**Symmetric**: AES, ChaCha20, ChaCha20Poly1305.

**Post-quantum asymmetric**: McEliece-6960119, McEliece-8192128 (key encapsulation), SPHINCS-256 (hash-based signatures). These were the algorithms specified at the time of KMIP 2.0/2.1 publication; subsequent KMIP-Prof revisions and NIST PQC finalization may update or extend this list.

**Hashing**: SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512.

**Recommended curves**: P-384, P-521 (for transitional hybrid uses alongside post-quantum algorithms).

**Digital signature algorithms**: ECDSA with SHA-384 on P-384, Ed25519.

**Key formats**: Raw (symmetric keys), X.509 (certificates and public keys).

## New Attributes

The Quantum Safe Server introduces three new managed-object attributes:

**Protection Level** — a classification value indicating the sensitivity of the data the key protects (e.g., Public, Sensitive, Highly Sensitive). The server uses this to floor the algorithm choice: higher-sensitivity data requires algorithms with larger security margins.

**Protection Period** — the required protection duration in years. Combined with Protection Level, this governs algorithm selection: a key protecting data for 30 years needs a quantum-safe algorithm that maintains its security margin over that window. A key with a 2-year protection period might still be acceptable with a classical algorithm.

**Quantum Safe** — a boolean attribute set to True on objects whose algorithms are quantum-resistant. Clients and policy engines can use this flag to enforce "all new keys must be quantum-safe" policies without needing to understand the algorithm list directly.

## Algorithm Selection

When a client invokes Create with `Protection Period` and `Protection Level`, the server selects an algorithm that satisfies both constraints. The server is not required to expose its selection logic, but must choose from the approved algorithm list. If a client specifies an explicit algorithm that does not meet the protection parameters, the server may reject the request.

## Mandatory Test Cases

See [Mandatory Quantum Safe Test Cases KMIP v2.0](mandatory-quantum-safe-test-cases-kmip-v2-0.md) for the normative test identifiers and scenarios.

## Implications for Implementers

- Post-quantum algorithm support (McEliece, SPHINCS) requires a cryptographic library that implements these algorithms. At the time KMIP 2.0/2.1 was published these were not yet universally available in mainstream TLS and cryptographic libraries; verify library support before claiming this profile.
- The TLS 1.3 requirement for the server itself means the server's certificate must be compatible with TLS 1.3 cipher suites.
- Protection Period is the most operationally significant new attribute: build tooling that tracks this value per key and flags approaching expiry so keys can be re-keyed before their protection period lapses.
- The algorithm list may expand in future KMIP-Prof versions as NIST PQC standardization matures. Design your algorithm registry to be extensible.

## Related Concepts

[Quantum Safe Profiles](quantum-safe-profiles.md) ·
[Quantum Safe Client](quantum-safe-client.md) ·
[Mandatory Quantum Safe Test Cases KMIP v2.0](mandatory-quantum-safe-test-cases-kmip-v2-0.md) ·
[Base Profiles](base-profiles.md) ·
[Cryptographic Profiles](cryptographic-profiles.md)
