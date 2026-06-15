---
title: Archive
category: operation
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.4"
v1_source_section: "4.22"
status: reviewed
related: ["recover", "destroy", "archive-date"]
keywords: ["archive", "offline storage", "object archival", "lifecycle"]
---

# Archive

## Purpose

`Archive` signals that, from the client's perspective, an object may be moved to
archival storage. It is a hint rather than a command — the server decides if,
when, where, and at what hierarchy level the object is actually archived.

## Request Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | No | The object to archive; the ID Placeholder is used when omitted. |

## Response Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes | The object's identifier. |

## Behavior & Server Requirements

The actual archival — its timing, location, and storage tier — is governed by
server policy and not specified by the client. The request only conveys the
client's consent that the object may be archived. Servers should restrict the
operation to the owner or an authorized security officer and enforce strong
authentication. An archived object is brought back online with
[Recover](recover.md).

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: an unknown object, or insufficient permission.

## Related Operations

[Recover](recover.md) · [Destroy](destroy.md)
