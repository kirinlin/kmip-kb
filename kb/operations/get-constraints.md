---
title: Get Constraints
category: operation
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "6.1.22"
status: reviewed
related: ["set-constraints", "set-defaults", "query", "constraint", "constraints", "unique-identifier", "object-type"]
keywords: ["get constraints", "operation constraints", "access control", "permission", "object constraints", "policy retrieval"]
---

# Get Constraints

## Purpose

`Get Constraints` retrieves the [Constraints](../structures/constraints.md) structure that governs which operations a client may perform on a specific managed object or on a class of objects sharing the same type. Constraints encode operation-level permission rules — for example, restricting which clients may invoke [`Destroy`](destroy.md), or limiting the cryptographic operations permitted against a particular key. Retrieving current constraints is the first step in any workflow that audits or modifies access policy.

`Get Constraints` is the read counterpart to [`Set Constraints`](set-constraints.md) and was introduced in v2.1 alongside the full Constraints and Defaults system.

## Request Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | No | The identifier of the specific managed object whose constraints should be returned. When omitted, the server uses the ID Placeholder. |
| Object Type | `420057` | `ObjectType` | No | When supplied without a Unique Identifier, requests the server-wide default constraints for that object type rather than constraints on a specific object instance. |

## Response Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | No | Present when the request targeted a specific object; echoes back the identifier. |
| Constraints | `420168` | `Constraints` | Yes | The [Constraints](../structures/constraints.md) structure describing the operation permissions in effect for the identified object or object type. |

## Behavior & Server Requirements

When a Unique Identifier is supplied, the server returns the constraints attached to that object. When only an Object Type is supplied, the server returns the type-level default constraints (those that would apply to a newly created object of that type before any object-specific constraints are set). When neither is supplied, server behavior is implementation-defined — some servers return a global default, others return an error.

Constraints are stored separately from object attributes and are not returned by [`Get Attributes`](get-attributes.md). A caller must use `Get Constraints` to inspect access policy.

The server may enforce visibility controls on this operation itself: a client without administrative privilege might be permitted to read constraints on objects it owns but not on objects owned by others.

If the identified object exists but has no explicit constraints set, the server returns an empty or minimal Constraints structure rather than an error. A missing Constraints object typically means that server-wide defaults or the object's type defaults apply.

## Errors

Uses centralized error handling per the [error handling](../concepts/error-handling.md) conventions. Common failure causes include:

- The Unique Identifier refers to an object that does not exist.
- The caller lacks permission to read constraints on the specified object.
- Neither Unique Identifier nor Object Type is supplied and the server requires at least one.
- The server does not support the Constraints system — returns Operation Not Supported.

## Examples

An administrator auditing access policy on a high-value signing key retrieves its current constraints:

```
Operation: Get Constraints
  Unique Identifier: "signing-key-prod-01"
```

The server responds with the Constraints structure, which might list that only clients presenting a specific certificate are allowed to invoke [`Get`](get.md) or [`Export`](export.md), while [`MAC`](mac.md) and [`Sign`](mac.md) are unrestricted.

A tool generating an access-policy report for all symmetric keys in a key management system might first retrieve type-level defaults with `Object Type: Symmetric Key`, then compare individual key constraints against that baseline.

## Related Operations

[Set Constraints](set-constraints.md) · [Set Defaults](set-defaults.md) · [Query](query.md) · [Get Attributes](get-attributes.md)
