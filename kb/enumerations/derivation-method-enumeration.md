---
title: Derivation Method Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.4","2.0","2.1"]
source_section: "11.14"
status: reviewed
related: ["derive-key", "derivation-parameters", "hashing-algorithm-enumeration", "cryptographic-algorithm-enumeration"]
keywords: ["key derivation", "KDF", "PBKDF2", "HKDF", "HMAC", "NIST 800-108", "AWS", "derive key", "derivation method", "420031", "DerivationMethod"]
tag_hex: "420031"
xml_text: "DerivationMethod"
tag_type: "Enumeration"
---

# Derivation Method Enumeration

## Overview

The Derivation Method enumeration names the key derivation function (KDF) or key derivation algorithm applied when creating a new key from a base key material or secret. It appears in the [Derivation Parameters](../structures/derivation-parameters.md) structure of a [Derive Key](../operations/derive-key.md) request. The choice of derivation method determines which additional parameters are required — for example, PBKDF2 requires an iteration count and salt, while NIST 800-108 counter mode requires a label and context string. Correct selection is critical because different KDFs have different security properties and are appropriate for different use cases.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| PBKDF2 | `00000001` | `PBKDF2` |  |
| HASH | `00000002` | `HASH` |  |
| HMAC | `00000003` | `HMAC` |  |
| ENCRYPT | `00000004` | `ENCRYPT` |  |
| NIST800-108-C | `00000005` | `NIST800_108_C` |  |
| NIST800-108-F | `00000006` | `NIST800_108_F` |  |
| NIST800-108-DPI | `00000007` | `NIST800_108_DPI` |  |
| Asymmetric Key | `00000008` | `AsymmetricKey` |  |
| AWS Signature Version 4 | `00000009` | `AWSSignatureVersion4` |  |
| HKDF | `0000000A` | `HKDF` |  |

- **PBKDF2** (Password-Based Key Derivation Function 2, RFC 8018): Derives a key from a password and salt using an iterated HMAC or hash. The iteration count controls computational cost to resist offline brute-force attacks. The standard choice for deriving encryption keys from passwords.
- **Hash**: Derives key material by hashing the input directly (without HMAC). A simple but less flexible option; the hash algorithm is specified in the accompanying Hashing Algorithm field.
- **HMAC**: Applies an HMAC over the input key material and optional context data. Provides keyed derivation using a specified hash algorithm.
- **ENCRYPT**: Derives key material by encrypting the input using a specified block cipher, as in the key-based key derivation approaches used in some legacy protocols.
- **NIST800-108-C** (Counter Mode KDF): NIST SP 800-108 KDF in counter mode. Uses a PRF keyed by the base key, a counter, and optional label and context data to produce derived key material. Widely used in Windows/Active Directory environments.
- **NIST800-108-F** (Feedback Mode KDF): NIST SP 800-108 KDF in feedback mode. Each output block feeds back into the PRF along with a counter, providing additional chaining.
- **NIST800-108-DPI** (Double Pipeline Iteration KDF): NIST SP 800-108 KDF using a two-stage pipeline for additional independence between derived outputs.
- **AWS Signature Version 4**: Amazon Web Services signing key derivation as specified in the AWS SigV4 algorithm, enabling KMIP-managed keys to produce AWS request signing keys.
- **HKDF** (HMAC-based Key Derivation Function, RFC 5869): A two-phase extract-then-expand KDF built on HMAC. The extract phase condenses input keying material into a pseudorandom key; the expand phase stretches it to the desired length. HKDF is widely used in TLS 1.3 and modern protocol designs.

## Examples

A cloud application storing tenant secrets in KMIP might derive per-tenant encryption keys using **HKDF** from a master key, with each tenant's ID as the context info. An enterprise Active Directory–integrated application might use **NIST800-108-C** to derive service-specific keys matching the patterns expected by Windows CNG.

## Related

- [Derivation Parameters structure](../structures/derivation-parameters.md) — the structure that carries the derivation method and its parameters
- [Derive Key operation](../operations/derive-key.md) — the operation that performs key derivation
- [Hashing Algorithm Enumeration](hashing-algorithm-enumeration.md) — selects the underlying hash for HMAC- and hash-based methods
