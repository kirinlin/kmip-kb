---
title: Archive Date
category: attribute
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.5"
v1_source_section: "3.32"
status: reviewed
related: ["initial-date", "last-change-date", "state"]
keywords: ["archive date", "archival storage", "recover", "storage status", "420005", "ArchiveDate"]
tag_hex: "420005"
xml_text: "ArchiveDate"
tag_type: "Date-Time"
---

# Archive Date

## Purpose

Marks the object as being in archival (long-term, offline-ish) storage and
records when it was moved there. Its presence is also the protocol's signal
of archived status: [Locate](../operations/locate.md) can filter by storage
status, and operations on an archived object fail with the
`Object Archived` [result reason](../messages/result-reason.md) until a
[Recover](../operations/recover.md) brings it back.

## Data Type & Structure

A Date-Time.

## Constraints

- Present only while the object is archived; single instance.
- Not modifiable or deletable by clients; the server **deletes** it as part
  of every successful Recover — one of the few attributes designed to
  disappear.

## Applies To (Object Types)

All managed objects.

## Set / Modified By

Server only, implicitly during [Archive](../operations/archive.md); removed
during [Recover](../operations/recover.md). Archival is orthogonal to
[State](state.md) — an archived key keeps its lifecycle state.

## Related Attributes

[Initial Date](initial-date.md) · [Last Change Date](last-change-date.md) ·
[State](state.md)
