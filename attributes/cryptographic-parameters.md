---
title: Cryptographic Parameters
category: attribute
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4"]
source_section: "3.6"
status: draft
related: ["cryptographic-algorithm", "cryptographic-domain-parameters", "cryptographic-usage-mask"]
keywords: ["cryptographic parameters", "block cipher mode", "padding", "IV", "key role", "OAEP", "PSS"]
---

# Cryptographic Parameters

## Purpose

A bundle of *how-to-use-this-key* settings: cipher mode, padding, hash, IV
construction, and signature scheme details. Operations like
[Encrypt](../operations/encrypt.md) and [Sign](../operations/sign.md) either
take these parameters in the request or fall back to an instance stored on
the object. For certificates it describes the embedded public key. Key
wrapping uses it too, via the key-information structures in
[Key Wrapping Data](../ttlv/key-wrapping-data.md).

## Data Type & Structure

A structure in which every field is optional:

| Field group | Fields |
|---|---|
| Cipher basics | Block Cipher Mode, Padding Method, Hashing Algorithm, Cryptographic Algorithm |
| Signatures | Digital Signature Algorithm (alternative: algorithm + hash combination) |
| Financial / TR-31 | Key Role Type (BDK, DEK, KEK, MAC algorithms, PIN keys, ...) |
| IV handling | Random IV, IV Length (required for variable-IV modes like CTR/GCM), Tag Length (GCM/CCM), Fixed Field Length, Invocation Field Length, Counter Length, Initial Counter Value |
| RSA padding details (1.4) | Salt Length, Mask Generator, Mask Generator Hashing Algorithm, P Source, Trailer Field — defaults match PKCS#1 (MGF1, SHA-1, empty P, standard PSS trailer) |

## Constraints

- Optional; **multi-instance** — an object can store several parameter sets
  (e.g. one for CBC, one for GCM), distinguished by Attribute Index.
- When a [Key Wrapping Specification](../ttlv/key-wrapping-specification.md)
  names parameters, they must match one stored instance; with none specified,
  the server uses the instance with the lowest index.
- For digital signatures, specify either the Digital Signature Algorithm
  field or the algorithm+hash pair — not a conflicting mixture.

## Applies To (Object Types)

Keys, certificates, and (formerly) templates.

## Set / Modified By

Client-set and client-modifiable/deletable; the server does not rewrite it on
its own. Copied implicitly to replacement objects by
[Re-key](../operations/re-key.md),
[Re-key Key Pair](../operations/re-key-key-pair.md), and
[Re-certify](../operations/re-certify.md).

## Related Attributes

[Cryptographic Algorithm](cryptographic-algorithm.md) ·
[Cryptographic Domain Parameters](cryptographic-domain-parameters.md) ·
[Cryptographic Usage Mask](cryptographic-usage-mask.md)
