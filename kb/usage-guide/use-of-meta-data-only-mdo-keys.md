---
title: Use of Meta-Data Only (MDO) Keys
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.6"
status: reviewed
related: ["symmetric-key", "secret-data"]
keywords: ["MDO key", "meta-data only", "Key Value Present", "HSM", "key registration", "key value location"]
---

# Use of Meta-Data Only (MDO) Keys

## Overview

A Meta-Data Only (MDO) key is a managed key object whose Key Value is absent — only the metadata (attributes) about the key is stored on the KMIP server. MDO keys are used when a client wants to register key metadata without allowing the key material itself to leave the client's security boundary.

## Guidance

MDO keys apply to Symmetric Keys, Private Keys, Split Keys, and Secret Data objects. A typical use case is a key held inside an HSM: the key cannot leave the hardware, so the client registers metadata (algorithm, length, usage mask, lifecycle dates) without including the Key Value in the Register request. The server creates a Key Value Present attribute set to false to record that the key value is absent.

The optional Key Value Location attribute can record where the key material is physically stored, providing a reference for out-of-band retrieval.

The KMIP protocol does not support adding a Key Value to an existing MDO object after it is registered. If the client later needs to store the key value, it must register a new object.

## Implementation Notes

MDO keys cannot be the subject of Re-key, Re-key Key Pair, or Derive Key operations because the server has no key material to operate on. Attempts to perform these operations on an MDO key return an appropriate error. Clients implementing HSM-based key management should plan their lifecycle workflows to account for this limitation.

## Related Concepts

See [Symmetric Key](../objects/symmetric-key.md) and [Secret Data](../objects/secret-data.md) for the object types that support MDO registration.
