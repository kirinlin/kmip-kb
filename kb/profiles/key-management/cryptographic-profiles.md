---
title: Cryptographic Profiles
category: profile
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "prof-5.9"
status: reviewed
related: ["base-profiles", "symmetric-key-lifecycle-profiles", "asymmetric-key-lifecycle-profiles", "quantum-safe-profiles"]
keywords: ["cryptographic services", "Encrypt", "Decrypt", "Sign", "MAC", "RNG", "hash", "server-side crypto"]
---

# Cryptographic Profiles

## Overview

The Cryptographic Profiles define three tiers of server-side cryptographic operation support: Basic (encryption/decryption only), Advanced (the full signature, MAC, and hash set), and RNG (random number generation). These profiles address the use case where a KMIP client delegates cryptographic work to the key management server rather than retrieving keys and performing operations locally.

## Profile Tiers

**Basic Cryptographic Client/Server** — the client must support Encrypt or Decrypt (at least one). The server must support both Encrypt and Decrypt. This covers the common use case of requesting the server to encrypt data under a managed key without exposing the key material.

**Advanced Cryptographic Client/Server** — extends Basic with Sign, Signature Verify, MAC, MAC Verify, Hash, RNG Retrieve, and RNG Seed. The client must support at least one of the full set; the server must support all of them.

**RNG Cryptographic Client/Server** — a narrower profile specifically for random number generation, requiring RNG Retrieve and RNG Seed on both client and server.

## Mandatory Test Cases

Test case identifiers follow the pattern `CS-<tier>-M/O-<n>-<ver>` where `<tier>` is `BC` (Basic), `AC` (Advanced), or `RNG`, and the numeric suffix encodes the protocol version (`-12` = KMIP 1.2, `-21` = KMIP 2.1, etc.).

- **Basic**: `CS-BC-M-1-21` through `CS-BC-M-14-21` plus GCM variants (`CS-BC-M-GCM-*`) and ChaCha20 variants (`CS-BC-M-CHACHA20-*`, `CS-BC-M-CHACHA20POLY1305-*`)
- **Advanced**: `CS-AC-M-1-21` through `CS-AC-M-8-21` plus OAEP variants (`CS-AC-M-OAEP-1-21` through `CS-AC-M-OAEP-10-21`)
- **RNG mandatory**: `CS-RNG-M-1-21`
- **RNG optional**: `CS-RNG-O-1-21` through `CS-RNG-O-4-21`

Conformance requirements are asymmetric by role: a **client** must pass at least one mandatory test case for its chosen tier (matching that it only needs to implement one operation); a **server** must pass all mandatory test cases for a tier (matching that servers must support the full operation set).

## Permitted Test Case Variations

When validating against these test cases, the following values may legitimately differ between implementations without being deemed non-conformant: `UniqueIdentifier`, `PrivateKeyUniqueIdentifier`, `PublicKeyUniqueIdentifier`, `UniqueBatchItemIdentifier`, `TimeStamp`, key material and `IVCounterNonce` for server-generated or inherently variable operations, and cryptographic output in `Data`/`SignatureData`/`MACData`. Datetime attributes (`ActivationDate`, `InitialDate`, `DeactivationDate`, etc.) may vary when not fixed in the request.

## Implications for Implementers

- Server-side crypto (delegating operations rather than key retrieval) is architecturally more secure than key-out-of-HSM models because key material never leaves the server.
- The Basic profile mandates AES-CBC and AES-GCM test cases; ChaCha20/ChaCha20Poly1305 tests were added in v2.1 to reflect modern cipher preferences.
- OAEP test cases in the Advanced profile require RSA key support alongside symmetric key support.
- An RNG-only client is a legitimate use case for applications that need secure entropy from a hardware-backed server without needing other key operations.
- For KMIP 1.2, the normative source for these three tiers was the standalone OASIS companion document (`kmip-cs-profile/v1.0`), which covered KMIP 1.2 only. The content was subsequently absorbed into KMIP-Prof, where it appears at `prof-5.9` in v2.x with additional algorithm coverage (Hash, ChaCha20, OAEP variants).

## Related Concepts

[Base Profiles](../base-encoding/base-profiles.md) ·
[Symmetric Key Lifecycle Profiles](symmetric-key-lifecycle-profiles.md) ·
[Asymmetric Key Lifecycle Profiles](asymmetric-key-lifecycle-profiles.md) ·
[Quantum Safe Profiles](quantum-safe-profiles.md)
