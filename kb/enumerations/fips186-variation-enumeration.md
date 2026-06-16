---
title: FIPS 186 Variation Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.20"
status: reviewed
related: ["cryptographic-parameters", "cryptographic-algorithm-enumeration", "create-key-pair"]
keywords: ["FIPS 186", "DSA", "key generation", "prime generation", "GPB", "provable primes", "probable primes"]
---

# FIPS 186 Variation Enumeration

## Overview

The FIPS 186 Variation enumeration specifies which variation of the FIPS 186 standard should be used when generating DSA domain parameters or key pairs. FIPS 186 (Digital Signature Standard) has been revised through multiple editions, and each edition allows several methods for generating the prime numbers and domain parameters that define a DSA or elliptic-curve key. Selecting the correct variation ensures that the generated key material satisfies the mathematical guarantees required by a specific edition of the standard. This enumeration appears in the Cryptographic Parameters structure used during key generation.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Unspecified | `00000001` | `Unspecified` |  |
| GP x-Original | `00000002` | `GPXOriginal` |  |
| GP x-Change Notice | `00000003` | `GPXChangeNotice` |  |
| x-Original | `00000004` | `XOriginal` |  |
| x-Change Notice | `00000005` | `XChangeNotice` |  |
| k-Original | `00000006` | `KOriginal` |  |
| k-Change Notice | `00000007` | `KChangeNotice` |  |

- **Unspecified**: No specific variation is requested; the server selects an appropriate method according to its policy and the FIPS 186 edition it implements.
- **GPB** (Generation of Probable Primes by testing candidates): Domain parameters are generated using a probabilistic primality test (e.g., Miller-Rabin). This is the most common and efficient method in practice. The security relies on the probability of a composite passing repeated tests being negligibly small.
- **Probable Random Primes**: A categorisation of prime-generation methods based on random sampling and probabilistic testing, aligned with specific annexes of FIPS 186.
- **Provable Random Primes**: Domain parameters are generated using a constructive (provably prime) method such as Shawe-Taylor or Maurer's algorithm. Slower than probabilistic methods but provides a mathematical proof of primality, satisfying higher-assurance requirements.
- **Probable Primes with Conditions** / **Provable Primes with Conditions**: Variants that impose additional constraints on the prime structure (e.g., safe-prime requirements or specific bit patterns) for enhanced security against certain number-theoretic attacks.

## Examples

A FIPS 140-3-certified HSM generating DSA keys for a government agency might be required to use **Provable Random Primes** to satisfy the highest-assurance requirements. A commercial enterprise generating DSA domain parameters for an internal signing service would typically use **GPB** or **Probable Random Primes** for acceptable performance.

## Related

- [Cryptographic Parameters](../attributes/cryptographic-parameters.md) — the structure that contains this enumeration
- [Cryptographic Algorithm Enumeration](cryptographic-algorithm-enumeration.md) — DSA is the algorithm this variation applies to
- [Create Key Pair operation](../operations/create-key-pair.md) — key generation operation for asymmetric key pairs
