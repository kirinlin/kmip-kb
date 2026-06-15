---
title: Export
category: operation
spec_version: "2.1"
spec_versions: ["1.4", "2.0", "2.1"]
source_section: "6.1.18"
v1_source_section: "4.40"
status: reviewed
related: ["import", "get", "register", "key-wrapping-specification"]
keywords: ["export", "object export", "migration", "key wrapping", "attributes"]
---

# Export

## Purpose

`Export` retrieves a managed object together with all of its attributes,
intended for moving an object out of one server (typically toward
[Import](import.md) into another). It extends [Get](get.md) by also returning the
object's full attribute set. `Export` is new in KMIP 1.4.

## Request Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | No | The object to export; the ID Placeholder is used when omitted. |
| Key Format Type | `420042` | `KeyFormatType` | No | The format in which to return the key. |
| Key Wrap Type | `4200F8` | `KeyWrapType` | No | The wrap form applied to the exported key bytes. |
| Key Compression Type | `420041` | `KeyCompressionType` | No | How elliptic-curve public keys should be compressed. |
| Key Wrapping Specification | `420047` | `KeyWrappingSpecification` | No | The keys and parameters for wrapping the returned object. |

The format, wrap, compression, and wrapping fields carry the same meaning as in
[Get](get.md).

## Response Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Object Type | `420057` | `ObjectType` | Yes | The type of the returned object. |
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes | The object's identifier. |
| Attribute | `420008` | `Attribute` | Yes (repeated) | Every attribute of the object. |
| Managed Object |  |  | Yes | The object value, returned as in [Get](get.md). |

## Behavior & Server Requirements

The server returns the object and the complete set of its attributes, copying the
identifier into the ID Placeholder. If the object has already been destroyed, the
key material is left out of the response. Because exporting an object exposes it
for migration, servers should restrict the operation to the owner or an
authorized security officer and enforce strong authentication.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: an unknown object, a format the server cannot produce, or insufficient
permission.

## Related Operations

[Import](import.md) · [Get](get.md) · [Register](register.md)
