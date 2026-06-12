---
title: Destroy Action Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["2.0","2.1"]
source_section: "11.15"
status: reviewed
related: ["destroy", "shredding-algorithm-enumeration", "state-enumeration", "revoke"]
keywords: ["destroy action", "key destruction", "shred", "deletion", "metadata", "cryptographic erase", "destroy"]
---

# Destroy Action Enumeration

## Overview

The Destroy Action enumeration describes what actually happened to a managed object — and specifically to its key material and metadata — when a [Destroy](../../operations/destroy.md) operation was processed. Different security policies require different levels of assurance about what has been removed: simply deleting a database record is very different from overwriting key material with zeros or cryptographically erasing the storage medium. This enumeration allows servers to communicate and record the specific action taken, enabling auditors and policy engines to verify that destruction met the required assurance level.

## Encoding (Tag / Type / Length / Value)

Encoded as a 4-byte integer (TTLV type `05`, Enumeration). Returned in the Destroy response or stored in a Destroy Date / Destroy Action attribute on the object record after destruction.

## Fields & Structure

- **Unspecified**: The destruction method is not reported or is not meaningful for this object type. Used as a default when the server does not report granular action details.
- **Key Material Deleted**: The raw cryptographic key bytes were logically deleted from the server's storage (e.g., database row removed) but no secure overwrite was performed.
- **Key Material Shredded**: The raw key bytes were securely overwritten or cryptographically erased according to a defined shredding algorithm, providing assurance that the material cannot be recovered through storage forensics.
- **Metadata Deleted**: The object's metadata (attributes, access control entries, history) was logically deleted. May be used in combination with key material actions.
- **Metadata Shredded**: The metadata was securely overwritten, ensuring that even attribute values such as key labels and usage history cannot be recovered.
- **Deleted**: Both key material and metadata were logically deleted in a single atomic action.
- **Shredded**: Both key material and metadata were securely overwritten or cryptographically erased in a single atomic action. This is the highest assurance level for complete object destruction.

## Examples

A compliance requirement that mandates NIST 800-88 media sanitisation before decommissioning a key management appliance would require **Shredded** for all destroyed objects. A development environment where keys are discarded at session end may use **Deleted** for convenience without the overhead of secure overwrite.

## Related

- [Destroy operation](../../operations/destroy.md) — the operation that destroys a managed object
- [Shredding Algorithm Enumeration](shredding-algorithm-enumeration.md) — specifies the secure-erasure method used during shredding
- [State Enumeration](state-enumeration.md) — the object's lifecycle state transitions through Destroyed
