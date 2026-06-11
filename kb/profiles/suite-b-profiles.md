---
title: Suite B Profiles
category: profile
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4"]
source_section: "prof-5.13"
status: reviewed
related: ["suite-b-minlos-128-authentication-suite", "suite-b-minlos-192-authentication-suite", "base-profiles", "asymmetric-key-lifecycle-profiles"]
keywords: ["Suite B", "NSA", "ECDSA", "ECDH", "AES-GCM", "minLOS_128", "minLOS_192", "classified", "ECC"]
---

# Suite B Profiles

## Overview

The Suite B Profiles apply KMIP to environments governed by the NSA's Suite B cryptographic standards, which mandate elliptic-curve algorithms for classified U.S. government communications. Two tiers exist: minLOS_128 (minimum 128-bit level of security, suitable for SECRET-level material) and minLOS_192 (minimum 192-bit level of security, required for TOP SECRET material). Both tiers are represented in two companion articles covering authentication suites and in this profile article covering the key management operations.

Suite B was deprecated by NSA in 2017 in favour of the CNSA (Commercial National Security Algorithm) suite, which shifts to larger RSA and DH parameters alongside ECC. As a result, the Suite B profiles do not appear in KMIP-Prof v2.0 or later.

## Algorithm Columns

Suite B defines two non-signature primitive sets:

| Primitive | Column 1 (128-bit floor) | Column 2 (192-bit floor) |
|---|---|---|
| Key agreement | ECDH over P-256 | ECDH over P-384 |
| Symmetric encryption | AES-128 | AES-256 |
| Hashing (PRF/MAC) | SHA-256 | SHA-384 |

At minLOS_128 a session must commit to a single column — all algorithms from Column 1 or all from Column 2, never a mix. At minLOS_192, only Column 2 is permitted.

Digital signatures use ECDSA. At minLOS_128 either ECDSA-256 (P-256 + SHA-256) or ECDSA-384 (P-384 + SHA-384) may be used, and the two peers may authenticate with different sizes. At minLOS_192 both parties must use ECDSA-384.

## Client (Both Tiers)

A Suite B Client extends the [Baseline Client](base-profiles.md). The key constraint is that clients must restrict all enumerated type values to Suite B-permitted values — non-Suite-B algorithms must not be used even if the server advertises them.

## Server — minLOS_128

A minLOS_128 Server extends the [Baseline Server](base-profiles.md) and adds:

- **Objects**: Certificate, Symmetric Key, Public Key, Private Key
- **Operations**: Create, Create Key Pair, Register, Re-key, Re-key Key Pair
- **Mandatory algorithms/curves**: AES, ECDSA, ECDH, HMAC-SHA-256; P-256 (SECP256R1); SHA-256; ECDSA with SHA-256 on P-256
- **Mandatory key formats**: Raw, ECPrivateKey, X.509, Transparent ECDSA/ECDH Private/Public Key
- **Mandatory key lengths**: 128-bit with AES; 256-bit with SHA, ECDH, or ECDSA
- **Optional (Column 2 support)**: P-384, HMAC-SHA-384, SHA-384, ECDSA with SHA-384 on P-384; 256-bit AES and 384-bit EC lengths

## Server — minLOS_192

A minLOS_192 Server extends the [Baseline Server](base-profiles.md) with the same object and operation set as minLOS_128, but the algorithm set is locked to Column 2 with no optional Column 1 fallback:

- **Mandatory algorithms/curves**: AES, ECDSA, ECDH, HMAC-SHA-384; P-384 (SECP384R1); SHA-384; ECDSA with SHA-384 on P-384
- **Mandatory key lengths**: 384-bit with SHA, ECDH, or ECDSA (AES-256 is implied by Column 2)
- No optional weaker parameters — everything must be at the 384-bit ECC level

## Mandatory Test Cases

Test case identifiers encode the tier and protocol version: `SUITEB_128-M-N-10` (minLOS_128, KMIP 1.0) and `SUITEB_192-M-N-10` (minLOS_192, KMIP 1.0), with `-11`/`-12` variants for KMIP 1.1 and 1.2. The sole mandatory test case for each tier and version is a Query verifying that the server advertises the required operations and objects under the mandated TLS cipher suite.

## Permitted Test Case Variations

Query responses may legitimately differ in which operations and object types they enumerate, as may `UniqueIdentifier`, `UniqueBatchItemIdentifier`, `TimeStamp`, and datetime attributes. Extensions reported in `Query` (`ExtensionList`, `ExtensionMap`, `ApplicationNamespaces`) are unconstrained.

## Implications for Implementers

- The Suite B profiles mandate TLS 1.2 with ECDSA mutual authentication. ECDSA certificate chains must comply with the RFC 5759 Suite B Certificate Profile — standard RSA-signed certificates are not acceptable even as intermediates.
- The column constraint (Column 1 or Column 2, never mixed within a session) applies to key agreement and symmetric encryption, not just signature. Implementations that allow negotiation must ensure the selected column is applied consistently.
- Re-key and Re-key Key Pair are mandatory server operations — Suite B environments require formal key replacement procedures rather than ad-hoc re-creation.
- For KMIP 1.0–1.2, the normative source was the standalone OASIS companion document (`kmip-suite-b-profile/v1.0`). The profile was absorbed into KMIP-Prof §5.13 for v1.3 and v1.4, then dropped in v2.0 following NSA's 2017 deprecation of Suite B.

## Related Concepts

[Suite B minLOS_128 Authentication Suite](suite-b-minlos-128-authentication-suite.md) ·
[Suite B minLOS_192 Authentication Suite](suite-b-minlos-192-authentication-suite.md) ·
[Base Profiles](base-profiles.md) ·
[Asymmetric Key Lifecycle Profiles](asymmetric-key-lifecycle-profiles.md)
