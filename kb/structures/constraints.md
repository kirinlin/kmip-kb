---
title: Constraints
category: structures
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "7.7"
status: reviewed
related: ["constraint", "rights", "right", "set-constraints", "get-constraints", "unique-identifier"]
keywords: ["constraints", "access control policy", "constraint list", "policy", "KMIP constraints", "object policy", "420168"]
tag_hex: "420168"
xml_text: "Constraints"
tag_type: "Structure"
---

# Constraints

## Overview

Constraints is the top-level access control and policy container introduced in KMIP v2.1. It holds a list of [Constraint](constraint.md) entries that collectively form the access policy for a managed object or a set of objects. The Constraints structure is submitted to the server via [Set Constraints](../operations/set-constraints.md) and returned by [Get Constraints](../operations/get-constraints.md).

The KMIP v2.1 access control model has two layers:

1. **Constraints** — attribute-based rules that govern which operations are valid given the state of an object's attributes.
2. **Rights** — principal-based permissions that control which identities are allowed to invoke which operations at all.

A request must satisfy both layers to succeed: the principal must have a [Right](right.md) for the operation, and the object must satisfy the relevant Constraints for that operation.

## Encoding (Tag / Type / Length / Value)

Constraints encodes as a Structure.

| Field | Tag | XML Text | Type | Required |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Text String | No |
| Constraint | `420208` | `Constraint` | Structure | Zero or more |

The optional Unique Identifier identifies the object whose policy this Constraints structure governs. When absent in a Set Constraints request, the constraints apply to the object identified in the request's target. Zero or more Constraint children carry the individual rules.

## Fields & Structure

**Unique Identifier** binds the Constraints to a specific managed object. Including it in a Set Constraints payload targets that specific object. In a Get Constraints response it tells the caller which object's policy is being returned.

**Constraint** children are [Constraint](constraint.md) structures. Each entry carries its own scoping (object type, attribute references, operation) and together they define the complete policy. The server evaluates all applicable Constraint entries when deciding whether an operation is permitted.

An empty Constraints structure (no Constraint children) clears all policy rules for the identified object, effectively making it ungoverned by the constraint model — the server falls back to whatever default policy applies.

Policy changes made via Set Constraints take effect for subsequent operations; in-flight operations are not interrupted.

## Examples

A Constraints structure for a sensitive signing key might contain two Constraint entries:

1. Object Type = Private Key, Attribute Reference = `"State"`, Operation = Get — requiring that the key be Active before it can be retrieved.
2. Object Type = Private Key, Attribute Reference = `"Cryptographic Usage Mask"`, Operation = any — ensuring the usage mask attribute always carries the Sign bit.

When a client attempts a Get on the private key, the server evaluates Constraint 1 and verifies that State = Active before returning the key material. Any attempt to modify the usage mask via Set Attribute is evaluated against Constraint 2.

## Related

[Constraint](constraint.md) · [Rights](rights.md) · [Right](right.md) · [Set Constraints](../operations/set-constraints.md) · [Get Constraints](../operations/get-constraints.md) · [Unique Identifier](../attributes/unique-identifier.md)
