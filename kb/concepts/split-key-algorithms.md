---
title: Split Key Algorithms
category: concept
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "13.1"
status: reviewed
related: ["split-key", "cryptographic-algorithm", "cryptographic-parameters", "transparent-key-structures"]
keywords: ["split key", "secret sharing", "shamir", "polynomial secret sharing", "xor split", "threshold", "key ceremony", "k-of-n"]
---

# Split Key Algorithms

## Overview

KMIP supports storing and managing split-key objects — key material that has been divided into multiple shares using a secret-sharing scheme, such that no individual share is usable on its own. The [Split Key](../objects/split-key.md) object type carries one share; the full secret is reconstructed only when a threshold number of shares are combined. KMIP §13.1 defines the algorithm options and their parameters so that interoperating implementations agree on how shares are generated and recombined.

## Details

### XOR Split

The simplest approach divides a key bit string into two shares using the exclusive-OR operation. Share 1 is generated as a random string the same length as the key; Share 2 is the XOR of Share 1 and the original key. Reconstruction requires both shares. This is a strict 2-of-2 scheme with no threshold flexibility: losing either share is irrecoverable. XOR splits are computationally trivial and add no key-length expansion.

### Polynomial Secret Sharing (Shamir's Secret Sharing)

Shamir's scheme embeds the secret as the constant term of a polynomial of degree k−1 over a finite field, where k is the reconstruction threshold. N evaluation points (shares) are distributed; any k of them suffice to reconstruct the polynomial via Lagrange interpolation and thus recover the secret, while any k−1 or fewer shares reveal nothing about the secret. The Split Key object carries the threshold value k, the share index, and the total share count N. This is the standard choice for n-of-m key ceremonies in HSM environments and key escrow.

KMIP specifies two finite-field variants: polynomial sharing over GF(2^8) and over a prime field. The GF(2^8) variant operates on bytes with XOR-based arithmetic; the prime-field variant uses modular integer arithmetic. Both provide the same k-of-n threshold property and information-theoretic security.

### Blakley Geometric Secret Sharing

KMIP also references the Blakley geometric approach. Blakley's scheme represents the secret as a point in a multidimensional space and distributes hyperplane equations as shares. k hyperplanes are necessary and sufficient to determine their intersection point, which encodes the secret. The two schemes are information-theoretically equivalent in security, differing in mathematical substrate and share-size characteristics.

## Implications for Implementers

Each Split Key object records the algorithm (XOR, Polynomial GF(2^8), Polynomial Prime Field, or Blakley/GF(2^16)), the share number, the total count of shares, and — for threshold schemes — the reconstruction threshold. When registering or creating split-key shares, clients must supply consistent metadata across all share objects so that the server can validate completeness without holding all shares simultaneously.

Reconstruction itself is a client-side operation; KMIP does not define a server operation that assembles shares. Servers store and manage shares as independent objects linked by the Unique Identifier of the key they protect, without ever holding the reconstituted secret unless the client submits it.

The choice of algorithm is fixed at split time; switching schemes requires destroying all shares and re-splitting the key.

## Related Concepts

[Split Key](../objects/split-key.md) · [Cryptographic Parameters](../attributes/cryptographic-parameters.md) · [Transparent Key Structures](../ttlv/transparent-key-structures.md)
