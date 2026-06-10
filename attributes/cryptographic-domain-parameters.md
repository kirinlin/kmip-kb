---
title: Cryptographic Domain Parameters
category: attribute
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.14"
v1_source_section: "3.7"
status: draft
related: ["cryptographic-parameters", "cryptographic-length", "cryptographic-algorithm"]
keywords: ["domain parameters", "Qlength", "recommended curve", "DSA", "DH", "elliptic curve"]
---

# Cryptographic Domain Parameters

## Purpose

Tells the server which mathematical domain to generate an asymmetric key pair
in. Discrete-log algorithms (DSA, DH) need the subgroup size; elliptic-curve
algorithms need a named curve. Supplied by the client in
[Create Key Pair](../operations/create-key-pair.md) requests.

## Data Type & Structure

A structure with two optional fields:

| Field | Type | Used for |
|---|---|---|
| Qlength | Integer | Bit length of the subgroup order Q (DSA/DH). The length of the prime P comes from [Cryptographic Length](cryptographic-length.md). |
| Recommended Curve | Enumeration | Named curve for EC algorithms — NIST P/K/B curves, SECG, ANSI X9.62, and (1.2+) Brainpool curves. |

## Constraints

- Optional; single instance; once set, neither side modifies or deletes it.
- Only meaningful at generation time — it directs key creation rather than
  describing ongoing use (that is
  [Cryptographic Parameters](cryptographic-parameters.md)' job).

## Applies To (Object Types)

Asymmetric keys (and formerly templates).

## Set / Modified By

Client-set in the Create Key Pair (or Register) request; carried over
implicitly by [Re-key](../operations/re-key.md) and
[Re-key Key Pair](../operations/re-key-key-pair.md) so the replacement pair
lives in the same domain.

## Related Attributes

[Cryptographic Parameters](cryptographic-parameters.md) ·
[Cryptographic Length](cryptographic-length.md) ·
[Cryptographic Algorithm](cryptographic-algorithm.md)
