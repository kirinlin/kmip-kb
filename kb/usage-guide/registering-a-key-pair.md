---
title: Registering a Key Pair
category: usage-guide
spec_version: "2.1"
spec_versions: ["2.0", "2.1"]
source_section: "ug-3.49"
status: draft
related: ["private-key", "public-key", "authentication"]
keywords: ["key pair", "Register", "Link attribute", "public key link", "private key link", "manual registration"]
---

# Registering a Key Pair

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

KMIP provides Create Key Pair for server-generated key pairs, which automatically creates Link attributes between the public and private key objects. For client-generated key pairs, the client must register the public and private keys separately and manually establish the Link attributes so the server recognises the relationship.

## Guidance

The recommended procedure for registering a key pair is:

1. **Register the public key**: set Cryptographic Algorithm, Cryptographic Length, and an appropriate Usage Mask reflecting public-key operations.
2. **Register the private key**: use the same Cryptographic Algorithm and Length; assign a distinct Usage Mask (public and private masks differ by design); optionally supply Cryptographic Parameters matching those of the public key.
3. **Set Link attributes**: add a Public Key Link on the private key pointing to the public key's Unique Identifier, and a Private Key Link on the public key pointing to the private key's Unique Identifier.

Once both Link attributes are in place, the server is expected to check mathematical consistency between the two objects and apply constraints equivalent to those for a server-generated pair.

## Implementation Notes

The server verification of key pair consistency is implementation-dependent: some servers perform full mathematical validation (e.g., confirming the private exponent matches the modulus), while others only check that a Link attribute was set. Clients should not rely on server validation as a substitute for their own key pair consistency check before registration.

## Related Concepts

See [Private Key](../objects/private-key.md), [Public Key](../objects/public-key.md), and [Authentication](authentication.md) for the underlying object types and authentication context.
