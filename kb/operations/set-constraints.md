---
title: Set Constraints
category: operation
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "6.1.52"
status: reviewed
related: ["get-constraints", "set-defaults", "query", "constraint", "constraints", "unique-identifier", "object-type"]
keywords: ["set constraints", "constraints", "access control", "operation permission", "policy", "object policy", "type-level policy"]
---

# Set Constraints

## Purpose

`Set Constraints` stores or replaces the [Constraints](../ttlv/constraints.md) governing which operations are permitted on a specific managed object or on a class of objects of a given type. Constraints encode fine-grained operation permissions beyond what the standard access-control model provides — for example, specifying that a particular key may only be used for encryption by clients presenting a specific certificate, or that the `Destroy` operation requires a quorum of administrators.

`Set Constraints` is the write counterpart to [`Get Constraints`](get-constraints.md) and was introduced in v2.1 alongside the full Constraints and Defaults system.

## Request Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | No | The identifier of the specific managed object whose constraints should be set. When omitted, the server uses the ID Placeholder. |
| Object Type | `420057` | `ObjectType` | No | When supplied without a Unique Identifier, sets the type-level default constraints for objects of that type, applying to all future objects of that type that do not have explicit per-object constraints. |
| Constraints | `420168` | `Constraints` | Yes | The [Constraints](../ttlv/constraints.md) structure defining the new permission policy. If constraints already exist on the target, this call replaces them entirely — it is not a merge operation. |

## Response Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | No | Present when the request targeted a specific object; echoes back the identifier. |

## Behavior & Server Requirements

When a Unique Identifier is supplied, the server replaces the constraints on that specific object. When only an Object Type is supplied, the server replaces the type-level defaults. Supplying both a Unique Identifier and an Object Type is an error or implementation-defined behavior — callers should supply exactly one of the two.

Because `Set Constraints` performs a full replacement rather than a merge, callers that want to add or remove a single constraint entry must first call [`Get Constraints`](get-constraints.md), modify the retrieved structure, and then submit the updated whole via `Set Constraints`.

Changes take effect immediately and apply to all subsequent operations. Operations already in flight at the time of the change are not affected.

The server must enforce its own authorization rules on this operation: not all clients should be permitted to change constraints. Typically only administrative clients or the object owner have this capability.

Servers that support the Constraints system must advertise this in their [`Query`](query.md) response. Servers that do not support it return Operation Not Supported.

## Errors

Uses centralized error handling per the [error handling](../concepts/error-handling.md) conventions. Common failure causes include:

- The Constraints structure is malformed or contains invalid operation identifiers.
- The calling client lacks administrative permission to set constraints on the specified object or type.
- The Unique Identifier refers to an object that does not exist.
- The server does not support the Constraints system — returns Operation Not Supported.
- Both Unique Identifier and Object Type are supplied when the server requires exactly one.

## Examples

An administrator restricts a high-value signing key so that only the `Sign` and `Get Attributes` operations are permitted, and only by clients with a specific role:

```
Operation: Set Constraints
  Unique Identifier: "signing-key-prod-01"
  Constraints:
    Constraint:
      Operation: Sign
      Attribute: ...
    Constraint:
      Operation: Get Attributes
```

All other operations (Get, Export, Destroy, etc.) on `"signing-key-prod-01"` will subsequently return an authorization error unless the server's base access control already prohibits them.

Setting a type-level default that prevents any client from exporting newly created private keys:

```
Operation: Set Constraints
  Object Type: Private Key
  Constraints:
    Constraint:
      Operation: Export
      Forbidden: True
```

## Related Operations

[Get Constraints](get-constraints.md) · [Set Defaults](set-defaults.md) · [Query](query.md)
