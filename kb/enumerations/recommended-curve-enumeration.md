---
title: Recommended Curve Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.45"
status: reviewed
related: ["cryptographic-parameters", "cryptographic-algorithm-enumeration", "create-key-pair"]
keywords: ["elliptic curve", "EC curve", "P-256", "P-384", "P-521", "Curve25519", "secp256k1", "brainpool", "recommended curve", "420075", "RecommendedCurve"]
tag_hex: "420075"
xml_text: "RecommendedCurve"
tag_type: "Enumeration"
---

# Recommended Curve Enumeration

## Overview

The Recommended Curve enumeration identifies the named elliptic curve used when the Cryptographic Algorithm is one of the EC-family values (EC, ECDSA, ECDH, Ed25519, Ed448, etc.). Because the algorithm value alone does not determine the group parameters, the curve name is supplied separately in [Cryptographic Parameters](../attributes/cryptographic-parameters.md). The enumeration covers NIST prime curves, Koblitz curves, binary curves, Brainpool curves, and the modern Bernstein curves.

## Fields & Structure

| Name | Value | XML Text |
|---|---|---|
| P-192 | `00000001` | `P_192` |
| K-163 | `00000002` | `K_163` |
| B-163 | `00000003` | `B_163` |
| P-224 | `00000004` | `P_224` |
| K-233 | `00000005` | `K_233` |
| B-233 | `00000006` | `B_233` |
| P-256 | `00000007` | `P_256` |
| K-283 | `00000008` | `K_283` |
| B-283 | `00000009` | `B_283` |
| P-384 | `0000000A` | `P_384` |
| K-409 | `0000000B` | `K_409` |
| B-409 | `0000000C` | `B_409` |
| P-521 | `0000000D` | `P_521` |
| K-571 | `0000000E` | `K_571` |
| B-571 | `0000000F` | `B_571` |
| SECP112R1 | `00000010` | `SECP112R1` |
| SECP112R2 | `00000011` | `SECP112R2` |
| SECP128R1 | `00000012` | `SECP128R1` |
| SECP128R2 | `00000013` | `SECP128R2` |
| SECP160K1 | `00000014` | `SECP160K1` |
| SECP160R1 | `00000015` | `SECP160R1` |
| SECP160R2 | `00000016` | `SECP160R2` |
| SECP192K1 | `00000017` | `SECP192K1` |
| SECP224K1 | `00000018` | `SECP224K1` |
| SECP256K1 | `00000019` | `SECP256K1` |
| SECT113R1 | `0000001A` | `SECT113R1` |
| SECT113R2 | `0000001B` | `SECT113R2` |
| SECT131R1 | `0000001C` | `SECT131R1` |
| SECT131R2 | `0000001D` | `SECT131R2` |
| SECT163R1 | `0000001E` | `SECT163R1` |
| SECT193R1 | `0000001F` | `SECT193R1` |
| SECT193R2 | `00000020` | `SECT193R2` |
| SECT239K1 | `00000021` | `SECT239K1` |
| ANSIX9P192V2 | `00000022` | `ANSIX9P192V2` |
| ANSIX9P192V3 | `00000023` | `ANSIX9P192V3` |
| ANSIX9P239V1 | `00000024` | `ANSIX9P239V1` |
| ANSIX9P239V2 | `00000025` | `ANSIX9P239V2` |
| ANSIX9P239V3 | `00000026` | `ANSIX9P239V3` |
| ANSIX9C2PNB163V1 | `00000027` | `ANSIX9C2PNB163V1` |
| ANSIX9C2PNB163V2 | `00000028` | `ANSIX9C2PNB163V2` |
| ANSIX9C2PNB163V3 | `00000029` | `ANSIX9C2PNB163V3` |
| ANSIX9C2PNB176V1 | `0000002A` | `ANSIX9C2PNB176V1` |
| ANSIX9C2TNB191V1 | `0000002B` | `ANSIX9C2TNB191V1` |
| ANSIX9C2TNB191V2 | `0000002C` | `ANSIX9C2TNB191V2` |
| ANSIX9C2TNB191V3 | `0000002D` | `ANSIX9C2TNB191V3` |
| ANSIX9C2PNB208W1 | `0000002E` | `ANSIX9C2PNB208W1` |
| ANSIX9C2TNB239V1 | `0000002F` | `ANSIX9C2TNB239V1` |
| ANSIX9C2TNB239V2 | `00000030` | `ANSIX9C2TNB239V2` |
| ANSIX9C2TNB239V3 | `00000031` | `ANSIX9C2TNB239V3` |
| ANSIX9C2PNB272W1 | `00000032` | `ANSIX9C2PNB272W1` |
| ANSIX9C2PNB304W1 | `00000033` | `ANSIX9C2PNB304W1` |
| ANSIX9C2TNB359V1 | `00000034` | `ANSIX9C2TNB359V1` |
| ANSIX9C2PNB368W1 | `00000035` | `ANSIX9C2PNB368W1` |
| ANSIX9C2TNB431R1 | `00000036` | `ANSIX9C2TNB431R1` |
| BRAINPOOLP160R1 | `00000037` | `BRAINPOOLP160R1` |
| BRAINPOOLP160T1 | `00000038` | `BRAINPOOLP160T1` |
| BRAINPOOLP192R1 | `00000039` | `BRAINPOOLP192R1` |
| BRAINPOOLP192T1 | `0000003A` | `BRAINPOOLP192T1` |
| BRAINPOOLP224R1 | `0000003B` | `BRAINPOOLP224R1` |
| BRAINPOOLP224T1 | `0000003C` | `BRAINPOOLP224T1` |
| BRAINPOOLP256R1 | `0000003D` | `BRAINPOOLP256R1` |
| BRAINPOOLP256T1 | `0000003E` | `BRAINPOOLP256T1` |
| BRAINPOOLP320R1 | `0000003F` | `BRAINPOOLP320R1` |
| BRAINPOOLP320T1 | `00000040` | `BRAINPOOLP320T1` |
| BRAINPOOLP384R1 | `00000041` | `BRAINPOOLP384R1` |
| BRAINPOOLP384T1 | `00000042` | `BRAINPOOLP384T1` |
| BRAINPOOLP512R1 | `00000043` | `BRAINPOOLP512R1` |
| BRAINPOOLP512T1 | `00000044` | `BRAINPOOLP512T1` |
| CURVE25519 | `00000045` | `CURVE25519` |
| CURVE448 | `00000046` | `CURVE448` |

**NIST prime curves** (most widely deployed): P-192, P-224, P-256, P-384, P-521. P-256 and P-384 are the default choices in TLS 1.3 and most PKI systems.

**NIST Koblitz curves**: K-163, K-233, K-283, K-409, K-571. These binary-field curves were popular in constrained environments but have declined in favour of prime curves.

**NIST binary curves**: B-163, B-233, B-283, B-409, B-571.

**Additional SECG prime curves**: secp112r1/r2, secp128r1/r2, secp160k1/r1/r2, secp192k1, secp224k1, secp256k1 (used in Bitcoin).

**Brainpool curves**: brainpoolP160r1/t1 through brainpoolP512r1/t1 — prime curves standardised by the Brainpool consortium with deterministic generation to avoid potential backdoors from opaque seed values.

**Modern Bernstein curves**: curve25519 (for ECDH key agreement, underpinning X25519) and curve448 (for X448). These are not typically used with ECDSA; Ed25519 and Ed448 in the algorithm enumeration cover the corresponding signing variants.

## Examples

A Create Key Pair request for an ECDSA signing key using NIST P-256 carries Cryptographic Algorithm = **ECDSA** and Recommended Curve = **P-256** in its Cryptographic Parameters. An ECDH key agreement key for use with X25519 uses Algorithm = **ECDH** and Curve = **curve25519**.

## Related

[Cryptographic Parameters](../attributes/cryptographic-parameters.md) · [Cryptographic Algorithm Enumeration](cryptographic-algorithm-enumeration.md) · [Create Key Pair](../operations/create-key-pair.md)
