---
title: Join Split Key
category: operation
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.27"
v1_source_section: "4.39"
status: reviewed
related: ["create-split-key", "split-key", "secret-data"]
keywords: ["join split key", "reconstruct key", "secret sharing", "combine splits"]
---

# Join Split Key

## Purpose

`Join Split Key` reconstructs a single key from a set of
[split key](../objects/split-key.md) parts, registering the result as a new
managed object. It is the inverse of [Create Split Key](create-split-key.md) and
was added in KMIP 1.2.

## Request Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Object Type | `420057` | `ObjectType` | Yes | The type of object to form from the splits. |
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes (may repeat) | The split objects to combine; at least the threshold number must be supplied. |
| Secret Data Type | `420086` | `SecretDataType` | No | When the result is secret data, which secret-data type the splits form. |
| Template-Attribute | `420091` | `TemplateAttribute` | No | Attributes for the reconstructed object. In KMIP 2.0+ this wrapper is replaced by the flat [Attributes](../structures/template-attribute-structures.md) structure. |

## Response Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes | The identifier of the reconstructed object. |
| Template-Attribute | `420091` | `TemplateAttribute` | No | Attributes the server set implicitly. |

## Behavior & Server Requirements

The client must supply at least as many splits as the threshold recorded in the
split keys; fewer cannot reconstruct the key. The server combines them into the
requested object type, registers it, and sets the ID Placeholder to its
identifier.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: too few splits to meet the threshold, mismatched or invalid splits, or
insufficient permission.

## Related Operations

[Create Split Key](create-split-key.md)
