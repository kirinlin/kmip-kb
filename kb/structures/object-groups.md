---
title: Object Groups
category: structures
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "7.23"
status: reviewed
related: ["objects", "query", "locate", "server-information"]
keywords: ["object groups", "group names", "object group", "group membership", "locate filter", "420166", "ObjectGroups"]
tag_hex: "420166"
xml_text: "ObjectGroups"
---

# Object Groups

## Overview

Object Groups is a structure that carries a list of Object Group name strings — the groups that objects on the server belong to (or that the server supports). KMIP allows managed objects to be assigned to named groups for organizational and access-control purposes. The Object Groups structure surfaces those group names in two main contexts: in Query responses (where it lists the group names the server recognizes) and as a filter or annotation in [Locate](../operations/locate.md) requests (where a client can restrict a search to objects belonging to specific groups).

## Encoding (Tag / Type / Length / Value)

Object Groups encodes as a Structure containing one or more Object Group Text String entries.

| Field | Tag | XML Element | Type | Required |
|---|---|---|---|---|
| Object Group | `42004D` | `ObjectGroup` | Text String | One or more |

Each Text String is the name of one group. The order of entries is not semantically significant.

## Fields & Structure

Each Object Group Text String is a server-defined or policy-defined name identifying a collection of managed objects. Groups may represent organizational units, application namespaces, key lifecycle stages, or any other administrative classification meaningful to the deployment.

Objects are assigned to groups via the Object Group attribute. The Object Groups structure in a Query response lists all groups that exist (or are recognized) on the server. In a Locate request, specifying an Object Group value restricts the search to objects that carry that group membership attribute.

Group names are case-sensitive text strings. KMIP imposes no naming constraints beyond being a valid text string; conventions are deployment-specific.

## Examples

A Query response from a server that organizes keys by application might include an Object Groups structure with entries: `"finance-app"`, `"hr-app"`, `"backup-service"`. A client performing a Locate to find all keys belonging to the finance application would include an Attribute filter with Object Group = `"finance-app"` in its request rather than using the Object Groups structure directly.

## Related

[Objects](objects.md) · [Query](../operations/query.md) · [Locate](../operations/locate.md) · [Server Information](server-information.md)
