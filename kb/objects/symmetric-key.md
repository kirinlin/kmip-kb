---
title: Symmetric Key
category: object
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "2.9"
v1_source_section: "2.2.2"
status: reviewed
related: ["create", "register", "get", "derive-key", "encrypt", "decrypt", "key-block", "cryptographic-algorithm", "cryptographic-length", "cryptographic-usage-mask"]
keywords: ["symmetric key", "AES", "secret key", "managed cryptographic object", "key block", "42008F", "SymmetricKey"]
tag_hex: "42008F"
xml_text: "SymmetricKey"
---

# Symmetric Key

## Purpose

A Symmetric Key is a managed cryptographic object that holds a single secret key
used for symmetric algorithms such as AES or 3DES, where the same key both
encrypts and decrypts (or computes and verifies a MAC). It is the simplest and
most common managed cryptographic object in KMIP, and the natural result of a
[Create](../operations/create.md) request.

## Structure

A Symmetric Key carries its key material in a single [Key Block](../structures/key-block.md),
which wraps the format, algorithm, length, and the actual bytes (optionally in
wrapped form).

| Field | Tag | XML Text | Required | Meaning |
|---|---|---|---|---|
| Key Block | `420040` | `KeyBlock` | Yes | The container holding the key's format, cryptographic algorithm and length, and the key material itself. |

## Key Attributes

The defining attributes of a symmetric key are its
[Cryptographic Algorithm](../attributes/cryptographic-algorithm.md),
[Cryptographic Length](../attributes/cryptographic-length.md) (e.g. 128 or 256
bits for AES), and [Cryptographic Usage Mask](../attributes/cryptographic-usage-mask.md),
which states what the key may be used for (encrypt, decrypt, wrap, MAC, and so
on). Like every managed object it also carries a server-assigned
[Unique Identifier](../attributes/unique-identifier.md),
[Object Type](../attributes/object-type.md), and
[State](../attributes/state.md).

## Lifecycle & State

A symmetric key moves through the standard KMIP key lifecycle tracked by its
[State](../attributes/state.md) attribute: it begins Pre-Active when created or
registered, becomes Active once activated, and eventually reaches Deactivated,
Compromised, or Destroyed. [Activate](../operations/create.md) makes it usable,
[Revoke](../operations/revoke.md) and [Destroy](../operations/destroy.md) end
its useful life, and [Archive](../operations/archive.md) moves it to offline
storage.

## Related Objects

[Secret Data](secret-data.md) · [Split Key](split-key.md) · [Private Key](private-key.md)
