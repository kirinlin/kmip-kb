---
title: Cryptographic Services
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.37"
status: reviewed
related: ["key-block"]
keywords: ["cryptographic services", "encrypt", "decrypt", "sign", "verify", "MAC", "hash", "RNG", "streaming"]
---

# Cryptographic Services

## Overview

In addition to key management, KMIP supports delegating cryptographic work to the server via dedicated operations covering symmetric encryption and decryption, asymmetric signing and verification, MAC computation and checking, entropy generation, and hashing. These operations allow clients to delegate cryptographic work to the server, strengthening integration between key management and cryptographic execution.

## Guidance

Cryptographic services are analogous to KMIP's certificate management support: the protocol provides a base set of operations that allow the server to act as a cryptographic proxy or as a cryptographic device itself. Clients that benefit most are those where performing cryptographic operations inside the key management boundary improves security — for example, by keeping plaintext from ever appearing on the network.

For operations involving plaintext data, both client and server should ensure the TLS channel provides protection commensurate with the sensitivity of the data being processed. KMIP does not enforce any minimum channel protection level for cryptographic service calls.

The RNG Seed and RNG Retrieve operations allow clients to contribute entropy to and retrieve random data from the server's random number generator. Servers should apply their own policy regarding trust in client-supplied entropy.

## Implementation Notes

Multi-part (streaming) cryptographic operations are supported via additional parameters that identify the stage (initialise, update, finalise). The server issues a Correlation Value on the first call; subsequent calls reference this value to continue the stream. Streaming capability can be queried via Query Capability Information.

## Related Concepts

See [Key Block](key-block.md) for the key material structure used with cryptographic service operations.
