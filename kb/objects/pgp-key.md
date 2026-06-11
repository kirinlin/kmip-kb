---
title: PGP Key
category: object
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "2.4"
v1_source_section: "2.2.9"
status: draft
related: ["register", "get", "public-key", "private-key", "opaque-object", "key-block"]
keywords: ["PGP key", "OpenPGP", "RFC 4880", "ASCII armor", "key block"]
---

# PGP Key

## Purpose

A PGP Key is a managed cryptographic object holding a text-based PGP key, added
to KMIP in version 1.2. Its material is the ASCII-armored export of an OpenPGP
key (per RFC 4880), which may contain a public key block alone or both a public
and a private key block. It lets KMIP manage PGP key material alongside other
managed objects.

## Structure

| Field | Required | Meaning |
|---|---|---|
| PGP Key Version | Yes | The PGP key format version — version 3 or version 4 keys may be stored. |
| Key Block | Yes | The [Key Block](../ttlv/key-block.md) carrying the ASCII-armored PGP export. |

## Key Attributes

Implementations are expected to treat the Key Block as an opaque blob; the
server need not parse the PGP structure. PGP-aware clients take responsibility
for decomposing it into constituent [Public Keys](public-key.md),
[Private Keys](private-key.md), and so on. The object still carries the common
managed-object attributes — [Unique Identifier](../attributes/unique-identifier.md),
[Object Type](../attributes/object-type.md), [State](../attributes/state.md).

## Lifecycle & State

A PGP Key follows the standard managed-object [State](../attributes/state.md)
lifecycle. Because it was introduced in 1.2, it is unavailable in earlier
versions.

## Related Objects

[Public Key](public-key.md) · [Private Key](private-key.md) · [Certificate](certificate.md) · [Opaque Object](opaque-object.md)
