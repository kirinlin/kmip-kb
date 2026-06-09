---
title: Secret Data
category: object
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4"]
source_section: "2.2.7"
status: draft
related: ["derive-key", "register", "get", "symmetric-key", "key-block", "cryptographic-usage-mask"]
keywords: ["secret data", "password", "shared secret", "seed", "derivation"]
---

# Secret Data

## Purpose

A Secret Data object is a managed cryptographic object holding a shared secret
value that is neither a key nor a certificate — for example a password,
passphrase, or seed. It lets KMIP manage such secrets with the same lifecycle,
access control, and protection as keys, and they often serve as input to
[Derive Key](../operations/derive-key.md).

## Structure

| Field | Required | Meaning |
|---|---|---|
| Secret Data Type | Yes | Classifies the secret (for example a password or a seed). |
| Key Block | Yes | The [Key Block](../ttlv/key-block.md) carrying the secret value, which may itself be wrapped. |

## Key Attributes

A Secret Data object carries the common managed-object attributes —
[Unique Identifier](../attributes/unique-identifier.md),
[Object Type](../attributes/object-type.md), [State](../attributes/state.md) —
and a [Cryptographic Usage Mask](../attributes/cryptographic-usage-mask.md)
describing how the secret may be used (commonly as derivation input). Unlike a
[Symmetric Key](symmetric-key.md) it need not carry a cryptographic algorithm,
since it is not tied to a specific cipher.

## Lifecycle & State

Secret Data follows the standard managed-object [State](../attributes/state.md)
lifecycle. It is registered or derived, used (often to derive other keys), and
eventually [revoked](../operations/revoke.md) and
[destroyed](../operations/destroy.md).

## Related Objects

[Symmetric Key](symmetric-key.md) · [Split Key](split-key.md) · [Opaque Object](opaque-object.md)
