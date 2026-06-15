---
title: Right
category: structures
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "7.34"
status: reviewed
related: ["rights", "constraint", "constraints", "set-constraints", "get-constraints"]
keywords: ["right", "access right", "operation permission", "KMIP operation", "authorization", "access control"]
tag_hex: "420150"
xml_element: "Right"
---

# Right

## Overview

A Right is the atomic unit of access control in the KMIP Constraints model. It encodes permission to perform a specific KMIP operation — Create, Get, Destroy, and so on — potentially subject to conditions. Multiple Right entries are collected into a [Rights](rights.md) structure that expresses the access policy for a particular principal.

The Right structure separates operation identity (which operation is permitted) from the conditions under which that permission applies, allowing fine-grained policies to be expressed cleanly.

## Encoding (Tag / Type / Length / Value)

Right encodes as a Structure.

| Field | Tag | XML Element | Type | Required |
|---|---|---|---|---|
| Operation | `42005C` | `Operation` | Enumeration | Yes |

Additional condition fields may accompany the Operation in extended implementations; the base form requires only the operation enumeration.

## Fields & Structure

**Operation** is an Enumeration value identifying the KMIP operation this right permits. It maps directly to the KMIP operation enumeration values: Create, Create Key Pair, Register, Locate, Get, Get Attributes, Add Attribute, Set Attribute, Delete Attribute, Activate, Revoke, Destroy, Query, Discover Versions, MAC, Derive Key, Re-Key, and so on.

A Right with a given Operation value grants the holder of the enclosing [Rights](rights.md) permission to invoke that operation. Absence of a Right for a particular operation means that operation is not permitted under the associated policy — the server should refuse requests that lack a matching Right.

The Right structure in the base spec is straightforward (operation only), but server extensions or profile-specific additions may add condition attributes — for example, time-of-day constraints, requester identity constraints, or attribute-value preconditions — as additional fields within the Right structure.

## Examples

A Rights structure for a read-only service account might contain three Right entries: Operation = Get, Operation = Get Attributes, and Operation = Locate. The service account can retrieve keys and their metadata but cannot create, modify, or destroy them.

A privileged auditor account might have a single Right with Operation = Query, granting access to server information without the ability to touch managed objects.

## Related

[Rights](rights.md) · [Constraint](constraint.md) · [Constraints](constraints.md) · [Set Constraints](../operations/set-constraints.md) · [Get Constraints](../operations/get-constraints.md)
