---
title: Transparent Key Structures
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "3.4"
v1_source_section: "2.1.7"
status: draft
related: ["key-block", "key-value", "cryptographic-domain-parameters"]
keywords: ["transparent key", "key material structure", "RSA components", "DSA", "EC private key", "CRT"]
---

# Transparent Key Structures

## Overview

Algorithm-aware encodings of key material: instead of an opaque DER blob,
the Key Material inside the [Key Value](key-value.md) becomes a TTLV
structure whose fields are the actual mathematical components (modulus,
exponents, curve, point). Selected by the [Key Block](key-block.md)'s Key Format Type field
(`Transparent Symmetric Key`, `Transparent RSA Private Key`, ...).

## Encoding (Tag / Type / Length / Value)

Key Material (`420043`) encoded as a Structure. Component fields are Big
Integers except where noted, using dedicated tags: P `42005E`, Q `420071`,
G `420037`, X `42009F`, Y `4200A0`, J `42003E`, Modulus `420052`, Private
Exponent `420063`, Public Exponent `42006C`, Prime Exponent P/Q
`420060`/`420061`, CRT Coefficient `420027`, D `42002E`, Q String `420072`
(Byte String), Recommended Curve `420075` (Enumeration), Key `42003F`
(Byte String).

## Fields & Structure

Per format type:

- **Transparent Symmetric Key** — just Key (the raw bytes, as a structure
  field).
- **Transparent DSA Private/Public** — P, Q, G plus X (private) or Y
  (public); all required.
- **Transparent RSA Private** — Modulus required, then enough private
  components to determine the key: the Private Exponent, *or* the primes
  P and Q, *or* the CRT pair Prime Exponent P + Prime Exponent Q (with
  optional Public Exponent and CRT Coefficient alongside).
- **Transparent RSA Public** — Modulus + Public Exponent.
- **Transparent DH Private/Public** — P, G required, Q and the cofactor J
  optional, plus X or Y.
- **Transparent EC Private/Public** (1.3+) — Recommended Curve plus D
  (private scalar) or Q String (public point). The older per-scheme
  ECDSA/ECDH/ECMQV variants carry identical fields and are deprecated since
  1.3 in favor of the generic EC pair.

Field semantics map one-to-one onto PKCS#1, FIPS 186, X9.42/SP 800-56A, and
X9.62 parameter names.

## Examples

An RSA-2048 private key in CRT form: Key Material structure with Modulus,
Public Exponent, P, Q, Prime Exponent P, Prime Exponent Q, and CRT
Coefficient — directly consumable without an ASN.1 parser.

## Related

[Key Block](key-block.md) · [Key Value](key-value.md) ·
[Cryptographic Domain Parameters](../attributes/cryptographic-domain-parameters.md)
