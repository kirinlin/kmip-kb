---
title: Split Key
category: object
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "2.8"
v1_source_section: "2.2.5"
status: reviewed
related: ["create-split-key", "join-split-key", "symmetric-key", "private-key", "register", "get", "key-block"]
keywords: ["split key", "secret sharing", "key splitting", "threshold", "XOR", "420089", "SplitKey"]
tag_hex: "420089"
xml_text: "SplitKey"
---

# Split Key

## Purpose

A Split Key is a managed cryptographic object representing one share of a secret
that has been broken into several parts for added security. The underlying
secret — usually a symmetric or private key — is divided so that the shares can
be distributed among multiple holders, and a quorum of them is needed to
reconstruct it. KMIP produces shares with
[Create Split Key](../operations/create-split-key.md) and reassembles the secret
with [Join Split Key](../operations/join-split-key.md).

## Structure

Each Split Key object holds one share plus the parameters describing the
splitting scheme.

| Field | Tag | XML Text | Required | Meaning |
|---|---|---|---|---|
| Split Key Parts | `42008B` | `SplitKeyParts` | Yes | Total number of shares the secret was divided into. |
| Key Part Identifier | `420044` | `KeyPartIdentifier` | Yes | Which share this object holds (from 1 up to Split Key Parts). |
| Split Key Threshold | `42008C` | `SplitKeyThreshold` | Yes | Minimum number of shares needed to reconstruct the secret. |
| Split Key Method | `42008A` | `SplitKeyMethod` | Yes | The sharing algorithm used (see below). |
| Prime Field Size | `420062` | `PrimeFieldSize` | Conditional | Required only when the method is polynomial sharing over a prime field. |
| Key Block | `420040` | `KeyBlock` | Yes | The [Key Block](../structures/key-block.md) carrying this share's material. |

## Key Attributes

Beyond the structural fields, a split key carries the usual managed-object
attributes — [Unique Identifier](../attributes/unique-identifier.md),
[Object Type](../attributes/object-type.md), and [State](../attributes/state.md)
— and the cryptographic descriptors of the secret it shares. KMIP defines three
splitting methods: a simple XOR scheme, where every share is combined to recover
the secret, and two polynomial secret-sharing schemes (over a prime field or over
a binary field) where any threshold-sized subset of shares suffices. The precise
field arithmetic is defined in the spec and the referenced literature; this entry
only summarizes the intent.

## Lifecycle & State

Each share is an independent managed object following the standard
[State](../attributes/state.md) lifecycle, but the shares are managed as a group
that together represents one logical secret. Shares are distributed after
creation and brought back together only when the secret must be reconstructed.

## Related Objects

[Symmetric Key](symmetric-key.md) · [Private Key](private-key.md) · [Secret Data](secret-data.md)
