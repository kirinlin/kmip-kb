---
title: Recommended Curve Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.45"
status: reviewed
related: ["cryptographic-parameters", "cryptographic-algorithm-enumeration", "create-key-pair"]
keywords: ["elliptic curve", "EC curve", "P-256", "P-384", "P-521", "Curve25519", "secp256k1", "brainpool", "recommended curve"]
---

# Recommended Curve Enumeration

## Overview

The Recommended Curve enumeration identifies the named elliptic curve used when the Cryptographic Algorithm is one of the EC-family values (EC, ECDSA, ECDH, Ed25519, Ed448, etc.). Because the algorithm value alone does not determine the group parameters, the curve name is supplied separately in [Cryptographic Parameters](../../attributes/cryptographic-parameters.md). The enumeration covers NIST prime curves, Koblitz curves, binary curves, Brainpool curves, and the modern Bernstein curves.

## Encoding (Tag / Type / Length / Value)

Encoded as a 4-byte integer (TTLV type `05`, Enumeration), tag `420380`.

## Fields & Structure

**NIST prime curves** (most widely deployed): P-192, P-224, P-256, P-384, P-521. P-256 and P-384 are the default choices in TLS 1.3 and most PKI systems.

**NIST Koblitz curves**: K-163, K-233, K-283, K-409, K-571. These binary-field curves were popular in constrained environments but have declined in favour of prime curves.

**NIST binary curves**: B-163, B-233, B-283, B-409, B-571.

**Additional SECG prime curves**: secp112r1/r2, secp128r1/r2, secp160k1/r1/r2, secp192k1, secp224k1, secp256k1 (used in Bitcoin).

**Brainpool curves**: brainpoolP160r1/t1 through brainpoolP512r1/t1 — prime curves standardised by the Brainpool consortium with deterministic generation to avoid potential backdoors from opaque seed values.

**Modern Bernstein curves**: curve25519 (for ECDH key agreement, underpinning X25519) and curve448 (for X448). These are not typically used with ECDSA; Ed25519 and Ed448 in the algorithm enumeration cover the corresponding signing variants.

## Examples

A Create Key Pair request for an ECDSA signing key using NIST P-256 carries Cryptographic Algorithm = **ECDSA** and Recommended Curve = **P-256** in its Cryptographic Parameters. An ECDH key agreement key for use with X25519 uses Algorithm = **ECDH** and Curve = **curve25519**.

## Related

[Cryptographic Parameters](../../attributes/cryptographic-parameters.md) · [Cryptographic Algorithm Enumeration](cryptographic-algorithm-enumeration.md) · [Create Key Pair](../../operations/create-key-pair.md)
