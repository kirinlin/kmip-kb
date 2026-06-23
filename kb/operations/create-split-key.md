---
title: Create Split Key
category: operation
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.10"
v1_source_section: "4.38"
status: reviewed
related: ["join-split-key", "create", "split-key"]
keywords: ["create split key", "split key", "key splitting", "secret sharing", "threshold"]
xml_text: "CreateSplitKey"
---

# Create Split Key

## Purpose

`Create Split Key` generates a [split key](../objects/split-key.md) — a key
broken into several parts (splits) under a secret-sharing scheme — and registers
each part as its own managed object. It was added in KMIP 1.2.

## Request Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Object Type | `420057` | `ObjectType` | Yes | The type of object to create. |
| Unique Identifier | `420094` | `UniqueIdentifier` | No | An existing key to split, when the client wants the server to split a known key. |
| Split Key Parts | `42008B` | `SplitKeyParts` | Yes | How many parts to produce in all. |
| Split Key Threshold | `42008C` | `SplitKeyThreshold` | Yes | How many parts must be combined to rebuild the key. |
| Split Key Method | `42008A` | `SplitKeyMethod` | Yes | The secret-sharing method used to split the key. |
| Prime Field Size | `420062` | `PrimeFieldSize` | No | The prime field size, for methods that need one. |
| Template-Attribute | `420091` | `TemplateAttribute` | Yes | Attributes for the new objects. In KMIP 2.0+ this wrapper is replaced by the flat [Attributes](../structures/template-attribute-structures.md) structure. |

## Response Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes (may repeat) | The identifiers of all the split objects created. |
| Template-Attribute | `420091` | `TemplateAttribute` | No | Attributes the server set implicitly. |

## Behavior & Server Requirements

The client can either let the server generate fresh key material to split or name
an existing key to be split; when an existing key is named and its attributes
differ from those supplied in the request, the key's own attributes win. The
server creates every split as a separate object and sets the ID Placeholder to
the split whose part identifier is 1. Reconstruction later requires at least
*threshold* parts via [Join Split Key](join-split-key.md).

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: an unsupported split method, an inconsistent parts/threshold
combination, or insufficient permission.

## Related Operations

[Join Split Key](join-split-key.md) · [Create](create.md)
