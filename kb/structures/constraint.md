---
title: Constraint
category: structures
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "7.6"
status: reviewed
related: ["constraints", "rights", "right", "attribute-reference", "set-constraints", "get-constraints", "object-type"]
keywords: ["constraint", "access constraint", "attribute constraint", "policy rule", "object type constraint", "operation constraint", "420169"]
tag_hex: "420169"
xml_text: "Constraint"
---

# Constraint

## Overview

A Constraint is the atomic unit of the KMIP attribute-based access control and policy model introduced in v2.1. It encodes a single rule: for a particular object type, when a specific operation is performed, the specified attributes must satisfy the rule's conditions. A collection of Constraint entries assembled into a [Constraints](constraints.md) structure forms the complete policy attached to an object or group of objects.

While [Rights](rights.md) describe which operations a principal may invoke, Constraints describe the attribute preconditions and invariants that govern those operations regardless of who is performing them.

## Encoding (Tag / Type / Length / Value)

Constraint encodes as a Structure.

| Field | Tag | XML Text | Type | Required |
|---|---|---|---|---|
| Object Type | `420057` | `ObjectType` | Enumeration | No |
| Attribute Reference | `420204` | `AttributeReference` | Structure | Zero or more |
| Operation | `42005C` | `Operation` | Enumeration | No |

All fields are optional, allowing Constraints to be scoped broadly (applying to all object types) or narrowly (applying to one specific operation on one specific object type).

## Fields & Structure

**Object Type** scopes the constraint to a specific kind of managed object — Symmetric Key, Certificate, etc. When absent the constraint applies to objects of any type.

**Attribute Reference** entries identify the attributes this constraint governs. Each [Attribute Reference](attribute-reference.md) names an attribute (and optionally an index) without carrying a value — the constraint rule itself (what the attribute must equal or satisfy) is expressed in the enclosing or associated policy mechanism, not within the Constraint structure itself. Multiple references may appear when the rule involves more than one attribute.

**Operation** scopes the constraint to a specific KMIP operation — Get, Destroy, Activate, etc. When absent the constraint applies regardless of which operation triggers evaluation.

A Constraint with all three fields populated expresses the most specific rule: "When performing Operation X on object of Type Y, the following attributes must satisfy their conditions." A Constraint with only Attribute Reference populated is a general invariant: "Regardless of operation or object type, these attributes are in scope."

## Examples

A Constraint enforcing that only objects with Cryptographic Algorithm = AES may be destroyed via an automated process might carry:
- Object Type = Symmetric Key
- Attribute Reference: `"Cryptographic Algorithm"`
- Operation = Destroy

The containing Constraints structure provides the full rule (must equal AES), while this Constraint entry scopes it to symmetric keys being destroyed.

A simpler read-only constraint that applies to all gets of any object type might omit Object Type and Operation, carrying only an Attribute Reference to `"State"` — with the associated rule requiring State = Active before a Get is permitted.

## Related

[Constraints](constraints.md) · [Rights](rights.md) · [Attribute Reference](attribute-reference.md) · [Set Constraints](../operations/set-constraints.md) · [Get Constraints](../operations/get-constraints.md)
