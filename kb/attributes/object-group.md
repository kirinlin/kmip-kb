---
title: Object Group
category: attribute
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.35"
v1_source_section: "3.33"
status: reviewed
related: ["name", "application-specific-information", "fresh"]
keywords: ["object group", "grouping", "group member", "locate", "default group"]
tag_hex: "420056"
xml_element: "ObjectGroup"
---

# Object Group

## Purpose

Tags an object as belonging to a named collection, so related objects (all
keys for one application, one tape pool, one tenant) can be managed and
[located](../operations/locate.md) together. Locate adds group-aware
semantics via its Object Group Member field (1.1+): a client can ask the
server for a *fresh* member of a group — one not previously served — or for
the group's default member, enabling simple server-side key pools.

## Data Type & Structure

A Text String holding the group name. The name `default` is reserved.

## Constraints

- Optional; multi-instance — an object may belong to several groups.
- Group semantics (who may create groups, what membership means) are server
  policy; the protocol only stores and matches the strings.

## Applies To (Object Types)

All managed objects.

## Set / Modified By

Client or server; modifiable and deletable by the client. Implicitly set by
the object-creating operations ([Create](../operations/create.md),
[Create Key Pair](../operations/create-key-pair.md),
[Register](../operations/register.md),
[Derive Key](../operations/derive-key.md), certify and re-key families),
e.g. when the new object inherits its predecessor's groups.

## Related Attributes

[Name](name.md) ·
[Application Specific Information](application-specific-information.md) ·
[Fresh](fresh.md)
