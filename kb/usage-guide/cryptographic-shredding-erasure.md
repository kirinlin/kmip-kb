---
title: Cryptographic Shredding (Erasure)
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.3", "1.4", "2.0", "2.1"]
source_section: "ug-4.8"
status: reviewed
related: ["key-shredding", "using-notify-and-put-operations"]
keywords: ["cryptographic shredding", "crypto erasure", "Destroy", "Notify", "key deletion", "data unrecoverable"]
---

# Cryptographic Shredding (Erasure)

## Overview

Cryptographic shredding — also called cryptographic erasure — is the practice of destroying a cryptographic key to render data encrypted with that key permanently unrecoverable. KMIP supports this via the Destroy operation (client-to-server) and optionally via the Notify operation (server-to-client).

## Guidance

**Simple shredding**: If the key material is stored only on the KMIP server (not at the encryption point), the client issues a Destroy request. How the server physically destroys the key and whether it retains metadata is vendor-defined.

**Coordinated shredding**: If the key material also exists at the encryption point (cached at the client or co-located with the encrypting hardware), the server can use the Notify operation with the Destroy Date attribute to inform the client that the server's copy has been deleted. The client (or its proxy at the encryption point) may then destroy its local copy.

KMIP does not require either the server or the client to support Notify, nor does it require a client to act on a Notify. The coordinated shredding example is illustrative of how it could be used, not a protocol mandate.

## Implementation Notes

Cryptographic shredding is effective only if all copies of the key are destroyed. In environments with multiple key replicas, key caches, or key escrow copies, the client must ensure that all copies are accounted for and destroyed. A Destroy request to the KMIP server addresses only the server's copy.

## Related Concepts

See [Key Shredding](key-shredding.md) for physical key destruction methods, and [Using Notify and Put Operations](using-notify-and-put-operations.md) for the push notification mechanism.
