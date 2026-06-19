---
title: Import
category: operation
spec_version: "2.1"
spec_versions: ["1.4", "2.0", "2.1"]
source_section: "6.1.25"
v1_source_section: "4.41"
status: reviewed
related: ["export", "register", "get"]
keywords: ["import", "object import", "migration", "replace existing", "key wrapping"]
---

# Import

## Purpose

`Import` brings a managed object into the server with all of its attributes set
exactly as supplied — the migration counterpart to [Export](export.md). Unlike
[Register](register.md), it preserves the object's existing identity and
attribute values rather than letting the server assign its own. `Import` is new
in KMIP 1.4.

## Request Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes | The identifier the imported object should have. |
| Replace Existing | `420124` | `ReplaceExisting` | No | A boolean; when true, an existing object with the same identifier is replaced, otherwise a clash makes the operation fail. |
| Key Wrap Type | `4200F8` | `KeyWrapType` | No | Whether the object arrives wrapped; if "not wrapped" the server unwraps it before storing (and errors if the wrapping key is unavailable), otherwise it stores it as given. |
| Attribute | `420008` | `Attribute` | Yes (repeated) | Every attribute the object should have. |
| Managed Object |  |  | Yes | The object value, supplied as in [Register](register.md). |

## Response Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes | The identifier of the imported object. |

## Behavior & Server Requirements

The normal attribute rules about which values are server-set or implicitly set
are **not** applied: every attribute is stored exactly as supplied. The server
copies the identifier into the ID Placeholder. Whether an identifier clash is an
error or a replacement is governed by the Replace Existing flag. As with
[Export](export.md), servers should restrict the operation to the owner or an
authorized security officer and enforce strong authentication.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: an identifier clash when replacement was not requested, an unavailable
wrapping key, or insufficient permission.

## Related Operations

[Export](export.md) · [Register](register.md)
