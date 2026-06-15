---
title: Derivation Parameters
category: structures
spec_version: "2.1"
spec_versions: ["2.0", "2.1"]
source_section: "7.12"
status: reviewed
related: ["derive-key", "key-block", "cryptographic-algorithm"]
keywords: ["derivation parameters", "key derivation", "PBKDF2", "HKDF", "SP800-108", "derivation method", "salt", "iteration count", "KDF"]
tag_hex: "420032"
xml_element: "DerivationParameters"
---

# Derivation Parameters

## Overview

Derivation Parameters is the structure that bundles all the inputs a key derivation function (KDF) needs to produce a derived key. It appears in the request payload of the [Derive Key](../operations/derive-key.md) operation and carries the method selector along with all method-specific configuration — hashing algorithm, iteration count, salt or label data, and the optional initialization vector.

KMIP supports several standard derivation approaches. The Derivation Method enumeration in this structure selects among them, and the remaining fields supply the method's required inputs.

## Encoding (Tag / Type / Length / Value)

Derivation Parameters encodes as a Structure.

| Field | Tag | XML Element | Type | Required |
|---|---|---|---|---|
| Derivation Method | `420269` | `DerivationMethod` | Enumeration | Yes |
| Derivation Data | `4200C8` | `DerivationData` | Byte String | No |
| Hash Algorithm | `420038` |  | Enumeration | No |
| Salt Value | `42009D` |  | Byte String | No |
| Iteration Count | `4200CA` | `IterationCount` | Integer | No |
| Cryptographic Parameters | `420028` | `CryptographicParameters` | Structure | No |
| Initialization Vector | `42003D` | `InitializationVector` | Byte String | No |
| Unique Identifier | `420094` | `UniqueIdentifier` | Text String | No |

Fields beyond Derivation Method are conditionally required depending on the chosen method; a server returns an error if required inputs for the selected method are absent.

## Fields & Structure

**Derivation Method** selects the algorithm family. Common values include:

- *PBKDF2* — password-based key derivation per RFC 8018; requires Hash Algorithm and Iteration Count, optionally Salt Value.
- *HKDF* — HMAC-based extract-and-expand per RFC 5869; requires Hash Algorithm and optionally Salt Value and Derivation Data as the info input.
- *SP800-108 Counter* / *SP800-108 Feedback* / *SP800-108 Double Pipeline* — the NIST-defined PRF-based KDFs; require a [Cryptographic Parameters](../attributes/cryptographic-parameters.md) structure specifying the underlying PRF and optionally Initialization Vector.
- *ECDH* — Elliptic-Curve Diffie-Hellman agreement; the Unique Identifier field identifies the peer key on the server.

**Derivation Data** is the contextual input whose role varies by method — it functions as the "info" string in HKDF or the label/context in SP800-108 derivations.

**Hash Algorithm** names the underlying hash function (SHA-256, SHA-384, SHA-512, etc.) used internally by the KDF.

**Salt Value** carries the salt for PBKDF2 or the "salt" input for HKDF's extract step. When absent in HKDF, a zero-length salt is implied.

**Iteration Count** is the PBKDF2 work factor — the number of times the underlying PRF is applied. Values below a cryptographically meaningful threshold (often several hundred thousand) should be treated as a configuration warning.

**Initialization Vector** provides the feedback register seed for SP800-108 Feedback mode.

**Unique Identifier** references a key already managed by the server that participates in the derivation (for example, the peer public key in an ECDH exchange).

## Examples

A client wants to derive an AES-256 key from a password using PBKDF2-SHA256 with 600,000 iterations. The Derivation Parameters structure carries Derivation Method = PBKDF2, Hash Algorithm = SHA-256, Iteration Count = 600000, and Salt Value = a 16-byte random salt. The enclosing Derive Key request also specifies the target Cryptographic Algorithm = AES and Cryptographic Length = 256 for the output key.

## Related

[Derive Key](../operations/derive-key.md) · [Cryptographic Parameters](../attributes/cryptographic-parameters.md) · [Key Block](key-block.md) · [Cryptographic Algorithm](../attributes/cryptographic-algorithm.md)
