---
title: Protection Level
category: attribute
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "4.42"
status: reviewed
related: ["protection-storage-mask", "protection-period", "sensitive", "extractable", "cryptographic-usage-mask"]
keywords: ["protection level", "hsm", "hardware security", "software protection", "storage protection", "key protection tier"]
---

# Protection Level

## Purpose

Protection Level expresses the minimum security strength of the physical or logical environment in which a key or secret must be stored and processed. It bridges the gap between an object's cryptographic properties and the operational security requirements that govern where it may live — for example, mandating hardware-security-module residency for root CA keys while permitting software storage for ephemeral session keys.

## Data Type & Structure

An Enumeration. Defined values progress from least to most protective: Software (protected by OS-level controls), Hardware (dedicated cryptographic hardware short of a certified HSM), HSM (a validated hardware security module), and potentially vendor-defined tiers. The exact enumeration is extensible.

## Constraints

Single-instance. Optional. May be set at creation or registration and later updated via [Set Attribute](../operations/set-attribute.md) subject to server policy. A server that enforces protection levels may refuse to store or export a key in a manner inconsistent with the stated level. Lowering the protection level of an existing key may be restricted or prohibited by policy.

## Applies To (Object Types)

[Symmetric Key](../objects/symmetric-key.md), [Private Key](../objects/private-key.md), [Secret Data](../objects/secret-data.md), and other key-material objects.

## Set / Modified By

Client at creation/registration; updateable via [Set Attribute](../operations/set-attribute.md). Servers may enforce a minimum level based on algorithm, length, or usage policy.

## Related Attributes

[Protection Storage Mask](protection-storage-mask.md) · [Protection Period](protection-period.md) · [Sensitive](sensitive.md) · [Extractable](extractable.md)
