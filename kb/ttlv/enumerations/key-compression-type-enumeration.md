---
title: Key Compression Type Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.24"
status: reviewed
related: ["key-block", "recommended-curve-enumeration", "cryptographic-algorithm-enumeration", "create-key-pair"]
keywords: ["key compression", "EC public key", "point compression", "uncompressed", "X9.62", "elliptic curve", "key format"]
tag_hex: "420041"
xml_element: "KeyCompressionType"
---

# Key Compression Type Enumeration

## Overview

The Key Compression Type enumeration specifies how an elliptic curve public key point is represented in the key material. An EC public key is a point on the curve, mathematically described by both an X and a Y coordinate. The X9.62 standard (and SEC 1) defines several wire-format representations that trade off between compactness and universality: the uncompressed form includes both coordinates, while compressed forms include only the X coordinate plus a parity bit that allows the Y coordinate to be recovered. Hybrid forms include both coordinates redundantly for compatibility with systems that may not support point decompression. Selecting the correct form is important for interoperability with the target cryptographic library or HSM.

## Encoding (Tag / Type / Length / Value)

Encoded as a 4-byte integer (TTLV type `05`, Enumeration). Appears in the Key Block structure for EC public keys, alongside the key format type and the recommended curve.

## Fields & Structure

- **EC Public Key Type Uncompressed**: The public key point is encoded as a full `04 || X || Y` byte string where both the X and Y coordinates are included at full length. This is the most universally supported format — virtually every EC library accepts uncompressed points.
- **EC Public Key Type X9.62 Compressed Prime**: Compressed encoding for curves over prime fields (e.g., NIST P-256, P-384). The Y coordinate is omitted and replaced by a prefix byte (`02` or `03`) indicating the parity of Y. Halves the public key size but requires the receiver to support point decompression.
- **EC Public Key Type X9.62 Compressed Char2**: Compressed encoding for curves over characteristic-2 binary fields (e.g., NIST B-163, K-163). Similar to compressed prime but uses different prefix bytes and a different recovery formula suited to the binary field arithmetic.
- **EC Public Key Type X9.62 Hybrid**: Encodes both the compressed prefix byte and the full `X || Y` coordinates, providing a self-consistent encoding that simultaneously allows quick compressed-form parsing and direct extraction of Y.

## Examples

A TLS 1.3 key exchange using ECDH over P-256 typically transmits **EC Public Key Type Uncompressed** points, as all TLS implementations support this form. A constrained IoT device may request **EC Public Key Type X9.62 Compressed Prime** keys to minimise storage and transmission overhead for P-256 public keys.

## Related

- [Key Block structure](../../structures/key-block.md) — the container that holds the key material and this compression type field
- [Recommended Curve Enumeration](recommended-curve-enumeration.md) — specifies which elliptic curve the key is on
- [Cryptographic Algorithm Enumeration](cryptographic-algorithm-enumeration.md) — identifies the algorithm (ECDH, ECDSA, etc.) for this key
