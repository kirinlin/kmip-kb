---
title: Set Attribute
category: operation
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "6.1.51"
status: reviewed
related: ["adjust-attribute", "add-attribute", "modify-attribute", "delete-attribute", "get-attributes", "unique-identifier", "attribute"]
keywords: ["set attribute", "attribute update", "single attribute", "overwrite", "attribute management", "v2.1 attribute operations"]
---

# Set Attribute

## Purpose

`Set Attribute` creates or replaces a single attribute on a managed object. If the named attribute does not yet exist on the object, the server adds it. If it already exists and is a single-valued attribute, the server replaces the current value with the supplied one. For multi-valued attributes, the attribute must be identified by an index or name so the server knows which instance to replace.

`Set Attribute` was introduced in v2.1 as a simpler alternative to the pre-v2.1 pattern of calling [`Add Attribute`](add-attribute.md) to create or [`Modify Attribute`](modify-attribute.md) to update, which required the caller to first determine whether the attribute existed. `Set Attribute` is unconditional: create-or-replace in one call.

For applying a numeric or date delta to an existing attribute, use [`Adjust Attribute`](adjust-attribute.md) instead.

## Request Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | No | Identifies the object to update. Defaults to the server's ID Placeholder when omitted. |
| Attribute | `420008` | `Attribute` | Yes | The [Attribute](../structures/attribute.md) structure carrying the attribute name and the new value to set. The attribute name is the canonical KMIP attribute name (e.g., `Activation Date`, `Name`, `Cryptographic Usage Mask`). |

## Response Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes | Confirms the identifier of the updated object. |

## Behavior & Server Requirements

The server resolves the object, applies the supplied attribute value, and records the change with a new `Last Change Date` timestamp. If the attribute has server-enforced constraints (for example, `Cryptographic Algorithm` cannot be changed after the object leaves the Pre-Active state), the server validates those constraints before applying the change and returns an error if they are violated.

For multi-instance attributes (such as `Name`, which can appear multiple times on the same object), the request must include sufficient information to identify the target instance. When no instance identifier is supplied and the attribute is multi-valued, server behavior is implementation-defined — some servers replace all instances, others return an error requiring an explicit identifier. Callers should always supply an instance identifier when working with multi-valued attributes.

`Set Attribute` on an attribute that does not exist creates it, making `Add Attribute` redundant for single-valued attributes in v2.1 implementations. Servers that support `Set Attribute` must accept it in place of `Add Attribute` for any attribute that `Add Attribute` would accept.

## Errors

Uses centralized error handling per the [error handling](../concepts/error-handling.md) conventions. Common failure causes include:

- The attribute value is invalid for the attribute type (wrong data type, out of range, or violates enumeration constraints).
- The object's current state does not permit modification of the named attribute.
- The caller lacks permission to modify the attribute.
- The Unique Identifier refers to an object that does not exist.
- Multi-valued attribute without instance identifier when the server requires one.

## Examples

Setting an activation date on a newly created key that was created without one:

```
Operation: Set Attribute
  Unique Identifier: "sym-key-batch-99"
  Attribute:
    Attribute Name: Activation Date
    Attribute Value: 2026-07-01T00:00:00Z
```

Updating the name of an existing key:

```
Operation: Set Attribute
  Unique Identifier: "sym-key-batch-99"
  Attribute:
    Attribute Name: Name
    Attribute Value:
      Name Value: "prod-encryption-key-Q3-2026"
      Name Type: Uninterpreted Text String
```

Both operations return the Unique Identifier `"sym-key-batch-99"` in the response.

## Related Operations

[Adjust Attribute](adjust-attribute.md) · [Add Attribute](add-attribute.md) · [Modify Attribute](modify-attribute.md) · [Delete Attribute](delete-attribute.md) · [Get Attributes](get-attributes.md)
