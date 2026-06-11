---
title: ReEncrypt
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.4", "2.0", "2.1"]
source_section: "ug-4.10"
status: draft
related: ["cryptographic-services", "batched-requests-and-responses"]
keywords: ["ReEncrypt", "re-encryption", "ephemeral", "plaintext protection", "Decrypt Encrypt batch", "Data Enumeration"]
---

# ReEncrypt

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

ReEncrypt is the process of changing the key used to protect data without exposing the plaintext to the client. KMIP v1.4 introduced this capability using the combination of the Ephemeral tag and the Data Enumeration, enabling a Decrypt followed by an Encrypt in a single batch where the intermediate plaintext is never returned to the client.

## Guidance

The Ephemeral tag in a Request Batch Item instructs the server not to return the plaintext output of a cryptographic operation to the client. Pairing this with the Data Enumeration — which lets one batch item reference the output of a prior item — a client can issue:

1. Decrypt (with Ephemeral=true): the server decrypts the ciphertext but does not return the plaintext.
2. Encrypt (referencing the output of step 1 via Data Enumeration): the server encrypts the plaintext from step 1 with a new key.

The result is a new ciphertext encrypted under a different key, without the plaintext ever appearing in the network communication.

## Implementation Notes

This pattern is useful for key rotation scenarios where large amounts of stored data must be re-encrypted under a new key. By keeping the plaintext server-side and expressing the re-encryption as a single batch, the client avoids network bandwidth for the plaintext data and reduces the window of exposure. The server must execute the batch atomically enough that no partial state is observable between the decrypt and encrypt steps.

## Related Concepts

See [Cryptographic Services](cryptographic-services.md) and [Batched Requests and Responses](batched-requests-and-responses.md).
