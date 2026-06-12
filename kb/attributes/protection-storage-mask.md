---
title: Protection Storage Mask (Attribute)
category: attribute
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "4.44"
status: reviewed
related: ["protection-level", "protection-period", "sensitive", "extractable"]
keywords: ["protection storage mask", "storage constraints", "hsm storage", "software storage", "bit mask", "storage policy"]
---

# Protection Storage Mask (Attribute)

## Purpose

Protection Storage Mask is an attribute that records which storage environments are permissible for a key or secret object as a bit field. It constrains where the key material may reside — for instance, requiring HSM-on-premises storage while prohibiting cloud software storage. This is the object-level policy expression; the bit definitions themselves are defined by the Protection Storage Masks bit-mask structure in §12.2.

This attribute is distinct from the [Protection Storage Masks](../ttlv/protection-storage-masks.md) TTLV structure used in request/response messages to communicate server capabilities.

## Data Type & Structure

An Integer used as a bit field. Each bit position corresponds to a storage category: On Premises Hardware, On Premises Software, Off Premises Hardware, Off Premises Software, HSM On Premises, HSM Off Premises, and so on. Multiple bits may be set simultaneously to indicate that several storage types are all acceptable (OR semantics — any of the set types satisfies the constraint).

## Constraints

Single-instance. Optional. Evaluated by the server when determining where to store or whether to replicate an object. A server that cannot satisfy the mask for a given operation should return an error rather than silently violating the constraint. Updatable via [Set Attribute](../operations/set-attribute.md).

## Applies To (Object Types)

[Symmetric Key](../objects/symmetric-key.md), [Private Key](../objects/private-key.md), [Secret Data](../objects/secret-data.md), and related key-material objects.

## Set / Modified By

Client at creation/registration or via [Set Attribute](../operations/set-attribute.md). Servers may impose a minimum mask based on object type or policy.

## Related Attributes

[Protection Level](protection-level.md) · [Protection Period](protection-period.md) · [Sensitive](sensitive.md) · [Extractable](extractable.md)
