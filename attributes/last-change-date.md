---
title: Last Change Date
category: attribute
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.29"
v1_source_section: "3.38"
status: draft
related: ["initial-date", "original-creation-date", "state"]
keywords: ["last change date", "modification time", "audit", "notify"]
---

# Last Change Date

## Purpose

The object's modification timestamp: updated by the server every time the
object or any of its attributes changes. Clients use it to detect staleness
of cached metadata, and [Notify](../operations/server-to-client/notify.md)
always includes it among the changed attributes it reports.

## Data Type & Structure

A Date-Time.

## Constraints

- Always present; single instance; maintained exclusively by the server —
  clients can neither set nor delete it.

## Applies To (Object Types)

All managed objects.

## Set / Modified By

Server only. Implicitly touched by essentially every mutating operation:
the create/register family, [Activate](../operations/activate.md),
[Revoke](../operations/revoke.md), [Destroy](../operations/destroy.md),
[Archive](../operations/archive.md) / [Recover](../operations/recover.md),
certify and re-key families,
[Add](../operations/add-attribute.md) /
[Modify](../operations/modify-attribute.md) /
[Delete Attribute](../operations/delete-attribute.md), and
[Get Usage Allocation](../operations/get-usage-allocation.md).

## Related Attributes

[Initial Date](initial-date.md) ·
[Original Creation Date](original-creation-date.md) · [State](state.md)
