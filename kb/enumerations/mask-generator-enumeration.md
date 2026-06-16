---
title: Mask Generator Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.30"
status: reviewed
related: ["cryptographic-parameters", "padding-method-enumeration", "hashing-algorithm-enumeration"]
keywords: ["mask generator", "MGF", "MFG1", "OAEP", "PSS", "RSA", "mask generation function", "420101", "MaskGenerator"]
tag_hex: "420101"
xml_text: "MaskGenerator"
---

# Mask Generator Enumeration

## Overview

The Mask Generator enumeration identifies the mask generation function (MGF) used in RSA encryption and signature padding schemes that require one. RSA-OAEP (Optimal Asymmetric Encryption Padding) and RSA-PSS (Probabilistic Signature Scheme) both use a mask generation function to expand a seed value into a mask of arbitrary length. The choice of MGF and its underlying hash algorithm are part of the complete algorithm specification and must match between the sender and receiver. This enumeration names the MGF; the Hashing Algorithm field in the same Cryptographic Parameters structure specifies the hash function it uses internally.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| MFG1 | `00000001` | `MFG1` |  |

- **MFG1**: Mask Generation Function 1 as defined in PKCS#1 v2.x (RFC 8017) and IEEE P1363. MFG1 applies a hash function iteratively over a counter and seed to produce a mask of the required length. It is by far the most commonly deployed MGF: OAEP as used in TLS and S/MIME almost universally uses MFG1 with SHA-1, SHA-256, or SHA-384.

Additional MGF values may be defined for use with other padding schemes or international standards, though MFG1 covers the overwhelming majority of practical deployments.

## Examples

An RSA key pair used for email encryption (S/MIME or OpenPGP) configured with **OAEP** padding would specify **MFG1** as the mask generator and **SHA-256** as both the hash algorithm and the MGF hash, following the recommendations in RFC 8017 for RSA-OAEP.

## Related

- [Cryptographic Parameters](../attributes/cryptographic-parameters.md) — the structure that contains this field alongside Padding Method and Hashing Algorithm
- [Padding Method Enumeration](padding-method-enumeration.md) — selects OAEP or PSS, which require a mask generator
- [Hashing Algorithm Enumeration](hashing-algorithm-enumeration.md) — specifies the hash function used inside the MGF
