---
title: Public Key
category: object
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "2.2.3"
status: draft
related: ["private-key", "create-key-pair", "certify", "register", "get", "certificate", "key-block", "cryptographic-algorithm", "cryptographic-usage-mask"]
keywords: ["public key", "asymmetric key", "RSA", "EC", "key pair"]
---

# Public Key

## Purpose

A Public Key is a managed cryptographic object holding the public half of an
asymmetric key pair. It is the key alone — not a certificate — used for
operations such as verifying signatures or encrypting to the matching private
key. Public keys are usually produced by
[Create Key Pair](../operations/create-key-pair.md) or supplied with
[Register](../operations/register.md).

## Structure

| Field | Required | Meaning |
|---|---|---|
| Key Block | Yes | The [Key Block](../ttlv/key-block.md) carrying the public key's format, algorithm, length, and material. |

## Key Attributes

Its defining attributes are
[Cryptographic Algorithm](../attributes/cryptographic-algorithm.md),
[Cryptographic Length](../attributes/cryptographic-length.md), and a
[Cryptographic Usage Mask](../attributes/cryptographic-usage-mask.md) set for
public-key operations (for example verify or encrypt). The server assigns a
[Unique Identifier](../attributes/unique-identifier.md) and maintains a
[Link](../attributes/link.md) of type Private Key pointing at the partner
[Private Key](private-key.md), plus its [State](../attributes/state.md).

## Lifecycle & State

A public key follows the managed-object lifecycle through its
[State](../attributes/state.md). It is generated together with its private
partner and cross-linked to it; it may further be linked to a
[Certificate](certificate.md) issued over it via
[Certify](../operations/certify.md). [Revoke](../operations/revoke.md) and
[Destroy](../operations/destroy.md) end its life.

## Related Objects

[Private Key](private-key.md) · [Certificate](certificate.md)
