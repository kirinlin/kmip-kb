---
title: NIST Key Type
category: attribute
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "4.34"
status: reviewed
related: ["cryptographic-algorithm", "cryptographic-usage-mask", "symmetric-key", "protection-level"]
keywords: ["nist key type", "sp 800-57", "key classification", "signing key", "wrapping key", "data encryption key", "key agreement", "authentication key"]
---

# NIST Key Type

## Purpose

NIST Key Type classifies a cryptographic key according to the functional categories defined in NIST SP 800-57 Part 1. Where Cryptographic Usage Mask captures the bit-level permitted operations, NIST Key Type provides the higher-level role classification — whether the key is a data-encryption key, a key-encrypting key (wrapping), a signing key, a key-agreement key, an authentication key, and so on. This classification supports policy enforcement and audit without requiring the server to inspect usage mask bits.

## Data Type & Structure

An Enumeration drawn from the NIST Key Type enumeration. Values correspond to the key-type categories in SP 800-57: for example, symmetric data-encryption keys, symmetric key-wrapping keys, asymmetric private/public signing keys, asymmetric key-agreement keys, symmetric authentication keys, and similar. The specific enumeration values follow the KMIP v2.1 specification's mapping of the SP 800-57 taxonomy.

## Constraints

Single-instance. Optional. Clients may set it at creation or registration time and may update it via [Set Attribute](../operations/set-attribute.md) or [Adjust Attribute](../operations/adjust-attribute.md) while the object is in a mutable state. Its value should be consistent with [Cryptographic Usage Mask](cryptographic-usage-mask.md) — servers may validate this consistency according to policy.

## Applies To (Object Types)

[Symmetric Key](../objects/symmetric-key.md), [Public Key](../objects/public-key.md), [Private Key](../objects/private-key.md), [Secret Data](../objects/secret-data.md).

## Set / Modified By

Client at creation or registration; also updatable post-creation via [Set Attribute](../operations/set-attribute.md).

## Related Attributes

[Cryptographic Algorithm](cryptographic-algorithm.md) · [Cryptographic Usage Mask](cryptographic-usage-mask.md) · [Protection Level](protection-level.md)
