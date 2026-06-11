---
title: Key Encoding
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.13"
status: reviewed
related: ["key-block"]
keywords: ["key encoding", "AES", "Triple-DES", "AES-XTS", "byte order", "key material", "FIPS 197"]
---

# Key Encoding

## Overview

To ensure that two parties who receive the same key as a raw byte string use it identically, KMIP defines the exact byte ordering convention for AES, Triple-DES, and AES-XTS keys within a Key Value Byte String.

## Guidance

For AES, the first byte of the Key corresponds to index 0 in the FIPS 197 key expansion procedure; subsequent bytes follow in ascending index order. The correct interpretation can be verified against the 128-bit AES test vectors in FIPS 197 Appendix A.

For Triple-DES, the Key consists of three 64-bit (8-byte) sub-keys (Key1, Key2, Key3) concatenated in order, with each sub-key's most significant bit first. Two-key Triple-DES sets Key3 equal to Key1.

For AES-XTS, the two required AES sub-keys are registered as two separate KMIP objects (each a standard AES key), associated by a Link attribute (Next/Previous Link) and optionally a custom naming attribute. KMIP operations on the pair are batched together to maintain the logical association.

## Implementation Notes

The encoding specifications exist to eliminate implementation-defined ambiguity in byte ordering. Implementers integrating KMIP into hardware or software crypto libraries should cross-check against the NIST test vectors for each algorithm to confirm correct byte alignment before deploying. Misaligned encoding produces keys that are syntactically valid KMIP objects but cryptographically incompatible with other implementations.

## Related Concepts

See [Key Block](key-block.md) and [AES Key Encoding](../references/) for the referenced standards.
