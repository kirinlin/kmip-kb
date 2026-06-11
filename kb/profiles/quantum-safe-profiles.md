---
title: Quantum Safe Profiles
category: profile
spec_version: "2.1"
spec_versions: ["2.0", "2.1"]
source_section: "prof-5.14"
status: draft
related: ["base-profiles", "cryptographic-profiles", "asymmetric-key-lifecycle-profiles", "basic-authentication-suite"]
keywords: ["quantum safe", "post-quantum", "McEliece", "SPHINCS", "TLS 1.3", "quantum resistant", "PQC", "Protection Level", "Protection Period"]
---

# Quantum Safe Profiles

## Overview

The Quantum Safe Profiles (§5.14–5.17 of [KMIP-Prof]) define a KMIP conformance tier for implementations that must protect key material against future quantum computer attacks. The profiles layer post-quantum cryptographic algorithm support onto the Baseline profiles and mandate TLS 1.3 as the transport channel (removing the TLS 1.2 fallback permitted by other profiles).

*Note: §5.15 (Quantum Safe Client), §5.16 (Quantum Safe Server), and §5.17 (Mandatory Test Cases) are sub-clauses of the §5.14 family. They appear at a different heading level in the source document but share the §5.14 section number sequence.*

## Quantum Safe Client (§5.15)

A Quantum Safe Client extends the [Baseline Client](base-profiles.md) and must support TLS v1.3. It may claim any other spec clauses that do not conflict with the profile.

## Quantum Safe Server (§5.16)

A Quantum Safe Server extends the [Baseline Server](base-profiles.md) and adds:
- **Objects**: Certificate, Private Key, Public Key, Symmetric Key
- **Attributes**: `Cryptographic Algorithm`, `Cryptographic Length`, `Protection Level`, `Protection Period`, `Quantum Safe`
- **Operations**: Create, Create Key Pair, Certify, Re-Certify, Register, Re-key, Re-key Key Pair, Decrypt, Encrypt, Sign, Signature Verify
- **Server-to-Client Operations**: Notify, Put
- **Algorithms**: AES, ChaCha20, ChaCha20Poly1305, McEliece-6960119, McEliece-8192128, SPHINCS-256
- **Hashing**: SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512
- **Key formats**: Raw, X.509
- **Recommended Curves**: P-384, P-521
- **Digital Signature Algorithms**: ECDSA with SHA-384 on P-384, Ed25519

TLS v1.3 is mandatory; the TLS 1.2 fallback permitted by the Basic Authentication Suite does not apply.

## New Attributes

`Protection Level` classifies the sensitivity of the protected information (influences algorithm and key-size selection). `Protection Period` specifies the required protection duration in years — used to choose algorithms with sufficient cryptographic security margins to outlast quantum advances during that window. `Quantum Safe` is a boolean flag marking the object as using quantum-resistant algorithms.

## Mandatory Test Cases

`QS-M-1-21` — Query server capabilities over TLS 1.3. `QS-M-2-21` — Create a key specifying Protection Period and Protection Level (the server selects an appropriate quantum-safe algorithm).

## Implications for Implementers

- The post-quantum algorithms in this profile (McEliece, SPHINCS) were under active standardization at the time of KMIP 2.1 publication. Check current NIST PQC standards for the latest recommended algorithms; KMIP-Prof versions after 2.1 may update the algorithm list.
- `Protection Period` drives algorithm agility: a key that must protect data for 30 years needs a quantum-safe algorithm today, while a key with a 1-year protection period may still use classical algorithms.
- TLS 1.3 is non-negotiable for this profile. If your deployment has clients that cannot support TLS 1.3, they cannot claim the Quantum Safe profile.

## Related Concepts

[Base Profiles](base-profiles.md) ·
[Cryptographic Profiles](cryptographic-profiles.md) ·
[Asymmetric Key Lifecycle Profiles](asymmetric-key-lifecycle-profiles.md) ·
[Basic Authentication Suite](basic-authentication-suite.md)
