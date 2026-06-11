---
title: Join Split Key
category: operation
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.27"
v1_source_section: "4.39"
status: draft
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

| Field | Required | Description |
|---|---|---|
| Object Type | Yes | The type of object to form from the splits. |
| Unique Identifier | Yes (may repeat) | The split objects to combine; at least the threshold number must be supplied. |
| Secret Data Type | No | When the result is secret data, which secret-data type the splits form. |
| Template-Attribute | No | Attributes for the reconstructed object. |

## Response Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | Yes | The identifier of the reconstructed object. |
| Template-Attribute | No | Attributes the server set implicitly. |

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
