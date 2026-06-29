---
title: Split Key Method Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.54"
status: reviewed
related: ["split-key", "split-key-algorithms", "cryptographic-parameters"]
keywords: ["split key method", "secret sharing", "XOR", "Shamir", "polynomial sharing", "Blakley", "GF", "key splitting", "42008A", "SplitKeyMethod"]
tag_hex: "42008A"
xml_text: "SplitKeyMethod"
tag_type: "Enumeration"
---

# Split Key Method Enumeration

## Overview

The Split Key Method enumeration identifies the mathematical technique used to divide a cryptographic key into shares and later reconstruct it. It is stored in the [Split Key](../objects/split-key.md) object alongside the share index and threshold, giving any holder of multiple shares the parameters needed to reconstruct the original secret. See [Split Key Algorithms](../concepts/split-key-algorithms.md) for a conceptual overview.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| XOR | `00000001` | `XOR` | A trivial 2-of-2 split. One share is random; the second share is the XOR of the random share and the original key. Both shares are required for reconstruction; there is no threshold flexibility. |
| Polynomial Sharing GF (216) | `00000002` | `PolynomialSharingGF216` | Shamir's Secret Sharing over GF(2^16), the Galois field with 65,536 elements. Polynomial evaluation uses 16-bit word arithmetic in a finite field, enabling k-of-n threshold sharing. Larger than GF(2^8) per share word, offering a wider element space at the cost of more complex field arithmetic. |
| Polynomial Sharing Prime Field | `00000003` | `PolynomialSharingPrimeField` | Shamir's Secret Sharing over a prime field (modular integer arithmetic). The same k-of-n threshold property, operating over integers modulo a large prime. Often easier to implement in arbitrary-precision arithmetic environments. |
| Polynomial Sharing GF (28) | `00000004` | `PolynomialSharingGF28` | Shamir's Secret Sharing over GF(2^8), the Galois field with 256 elements. Polynomial evaluation uses byte-level finite field arithmetic (mod an irreducible polynomial over GF(2)), making it highly efficient for byte-oriented secrets. Each share byte is independently computed, and any k shares suffice to reconstruct the original key. The most widely implemented variant. |

## Examples

A bank key ceremony that requires 3-of-5 custodians to reconstruct a root key uses **Polynomial Sharing Prime Field** or **Polynomial Sharing GF(2^8)**, with Split Key Threshold = 3 and Split Key Parts = 5. A two-officer dual-control environment may use the simpler **XOR** method.

## Related

[Split Key](../objects/split-key.md) · [Split Key Algorithms](../concepts/split-key-algorithms.md) · [Cryptographic Parameters](../attributes/cryptographic-parameters.md)
