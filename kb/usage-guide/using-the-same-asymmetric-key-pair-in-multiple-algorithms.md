---
title: Using the Same Asymmetric Key Pair in Multiple Algorithms
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.7"
status: draft
related: ["private-key", "public-key"]
keywords: ["asymmetric key", "DSA", "ECDSA", "ECDH", "DH", "key format", "multiple algorithms", "key reuse"]
---

# Using the Same Asymmetric Key Pair in Multiple Algorithms

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

Certain asymmetric algorithm pairs — such as DSA and Diffie-Hellman, or ECDSA and ECDH — share the same mathematical key structure, meaning the same key pair could technically be used in both algorithms. KMIP chooses to maintain separate key format representations for each algorithm rather than allowing a single key to be registered under multiple algorithm identities.

## Guidance

The reason for separate representations is alignment with the reference standards (NIST FIPS 186-4, ANSI X9.42, etc.) that define each algorithm's key format independently, and with best practice guidance (NIST SP 800-57, SP 800-56A) that recommends against using a single key pair for more than one purpose.

Clients wishing to use what is mathematically the same key pair for two different algorithms should register two separate managed objects — one for each algorithm — even though the underlying key material may be identical.

## Implementation Notes

Registering the same key twice under different algorithm identities is permitted by the protocol. Each registered object has its own Unique Identifier, lifecycle state, and attributes. Clients are responsible for maintaining any out-of-band association between the two registrations if needed, since KMIP provides no built-in mechanism to link objects registered in this way.

## Related Concepts

See [Private Key](../objects/private-key.md) and [Public Key](../objects/public-key.md) for the asymmetric key object models.
