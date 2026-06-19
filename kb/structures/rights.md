---
title: Rights
category: structures
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "7.35"
status: reviewed
related: ["right", "constraint", "constraints", "set-constraints", "get-constraints"]
keywords: ["rights", "access rights", "principal permissions", "authorization policy", "KMIP access control", "operation list", "42014D"]
tag_hex: "42014D"
xml_text: "Rights"
---

# Rights

## Overview

Rights is a structure that groups a set of [Right](right.md) entries and associates them with a principal (an authenticated identity or group). Together with [Constraints](constraints.md), it forms the KMIP access control model introduced in v2.1: Constraints define what attribute-based rules apply to objects, while Rights define which operations a principal may perform on those objects.

A Rights structure appears in [Set Constraints](../operations/set-constraints.md) payloads (to grant permissions) and in [Get Constraints](../operations/get-constraints.md) responses (to report current permissions). The server uses Rights records to enforce authorization on a per-principal, per-operation basis.

## Encoding (Tag / Type / Length / Value)

Rights encodes as a Structure.

| Field | Tag | XML Text | Type | Required |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Text String | No |
| Right | `420232` | `Right` | Structure | One or more |

The optional Unique Identifier identifies the principal (a client ID or group identifier registered with the server) these rights are granted to. One or more Right children each permit a specific KMIP operation.

## Fields & Structure

**Unique Identifier** identifies the principal holding these rights. Its value is a reference to an identity registered with or known to the server — for example, a client certificate distinguished name, a credential identifier, or a group name. When absent, the Rights apply to the requesting party in the current session context.

**Right** children are [Right](right.md) structures, each naming one permitted operation via an Operation Enumeration. The collection of Rights in this structure constitutes the complete set of operations the identified principal is allowed to perform (on the objects governed by the enclosing Constraints structure, or on the server as a whole, depending on context).

Rights are additive: a principal with multiple Rights entries (or multiple Rights structures) is permitted to perform the union of all listed operations. There is no explicit deny mechanism in the base Rights model — operations not listed are simply not permitted.

## Examples

A Rights structure granting a backup service the ability to retrieve and list keys but not modify or destroy them:

```
Rights {
  Unique Identifier = "backup-service-client-id"
  Right { Operation = Get }
  Right { Operation = Get Attributes }
  Right { Operation = Locate }
}
```

A separate Rights structure for an administrator might include additional Right entries for Create, Activate, Revoke, and Destroy.

## Related

[Right](right.md) · [Constraint](constraint.md) · [Constraints](constraints.md) · [Set Constraints](../operations/set-constraints.md) · [Get Constraints](../operations/get-constraints.md)
