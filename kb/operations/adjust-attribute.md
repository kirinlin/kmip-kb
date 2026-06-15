---
title: Adjust Attribute
category: operation
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "6.1.3"
status: reviewed
related: ["set-attribute", "add-attribute", "modify-attribute", "delete-attribute", "get-attributes", "unique-identifier", "attribute"]
keywords: ["adjust attribute", "delta", "increment", "decrement", "attribute update", "numeric attribute", "date attribute", "usage counter", "rotation offset"]
---

# Adjust Attribute

## Purpose

`Adjust Attribute` modifies the current value of an existing attribute by applying a delta rather than overwriting it with a new absolute value. Instead of reading the current value, computing a new one client-side, and writing it back, the client describes the adjustment and lets the server perform the arithmetic atomically. This is particularly useful for counters, generation numbers, and rotation offsets where race conditions would otherwise require separate read-then-write sequences.

`Adjust Attribute` was introduced in v2.1 alongside [`Set Attribute`](set-attribute.md). Together they replace the pre-v2.1 pattern of `Add Attribute` + `Modify Attribute` + `Delete Attribute` for managing individual attributes.

## Request Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | No | Identifies the managed object to update. Defaults to the server's ID Placeholder when omitted. |
| Attribute Name | `42000A` | `AttributeName` | Yes | The name of the attribute whose value is being adjusted. Must refer to a numeric or date-time attribute that supports delta operations. |
| Adjustment Type | `420158` | `AdjustmentType` | Yes | Enumeration indicating how to combine the current value with the adjustment value: `Add`, `Subtract`, or `Multiply` for numeric attributes; `Replace` for date-time attributes where an absolute rewrite is performed. |
| Attribute | `420008` | `Attribute` | Yes | Carries the adjustment value — the operand applied to the current attribute value according to the Adjustment Type. The structure mirrors the standard [Attribute](../structures/attribute.md) structure but holds the delta, not a final value. |

## Response Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes | Confirms which object was updated. |
| Attribute | `420008` | `Attribute` | Yes | Returns the updated [Attribute](../structures/attribute.md), containing the attribute name and the resulting value after the adjustment was applied. |

## Behavior & Server Requirements

The server locates the attribute named in the request on the identified object and applies the adjustment atomically. If the attribute does not exist on the object, the operation fails — `Adjust Attribute` modifies existing attributes only; it does not create them. Use [`Set Attribute`](set-attribute.md) to set an attribute's value unconditionally, or [`Add Attribute`](add-attribute.md) for multi-instance attributes that need a new instance added.

The Adjustment Type `Replace` is provided for date-time attributes where "add a delta" is ambiguous; it performs a plain replacement and is functionally equivalent to [`Set Attribute`](set-attribute.md) for those cases.

The server must enforce any access controls, object state restrictions, and attribute-specific rules that apply to modifications of the named attribute. For example, adjusting `Activation Date` on an Active object may be prohibited depending on server policy.

If the object is identified by the ID Placeholder mechanism, the server applies the same adjustment to each object currently referenced by the placeholder. Each adjusted object contributes one entry to a batch response if the operation is part of a batch request.

## Errors

Uses centralized error handling per the [error handling](../concepts/error-handling.md) conventions. Common failure causes include:

- The named attribute does not exist on the object — the server returns an invalid field error.
- The Adjustment Type is incompatible with the attribute's data type (e.g., `Multiply` on a date-time field).
- The resulting adjusted value would fall outside the permitted range for that attribute.
- The client lacks permission to modify the attribute, or the object's current state disallows the change.
- The Unique Identifier refers to an object that does not exist.

## Examples

A client managing a symmetric key that tracks how many times it has been used for encryption can increment a usage counter without needing to read the current count first:

```
Operation: Adjust Attribute
  Unique Identifier: "key-7a3f"
  Attribute Name: "Usage Count"
  Adjustment Type: Add
  Attribute:
    Attribute Name: "Usage Count"
    Attribute Value: 1
```

The server applies the addition and responds with the new counter value, e.g.:

```
Operation: Adjust Attribute (Response)
  Unique Identifier: "key-7a3f"
  Attribute:
    Attribute Name: "Usage Count"
    Attribute Value: 42
```

A rotation management workflow might multiply a `Rotate Interval` attribute to double the rotation frequency without knowing the current value in advance:

```
Adjustment Type: Multiply
Attribute Value: 2
```

## Related Operations

[Set Attribute](set-attribute.md) · [Add Attribute](add-attribute.md) · [Modify Attribute](modify-attribute.md) · [Delete Attribute](delete-attribute.md) · [Get Attributes](get-attributes.md)
