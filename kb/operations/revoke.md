---
title: Revoke
category: operation
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.44"
v1_source_section: "4.20"
status: reviewed
related: ["activate", "destroy", "state", "revocation-reason", "compromise-occurrence-date"]
keywords: ["revoke", "compromise", "deactivate", "revocation reason", "key state"]
xml_text: "Revoke"
---

# Revoke

## Purpose

`Revoke` takes a cryptographic or opaque object out of normal service, recording
why. Depending on the reason given, it either marks the object as compromised or
simply deactivates it.

## Request Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | No | The object to revoke; the ID Placeholder is used when omitted. |
| Revocation Reason | `420081` | `RevocationReason` | Yes | Why the object is being revoked (for example key compromise or cessation of operation). |
| Compromise Occurrence Date | `420021` | `CompromiseOccurrenceDate` | No | When the compromise happened; supplied only for a compromise reason and not otherwise. |

## Response Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes | The object's identifier. |

## Behavior & Server Requirements

The outcome depends on the [revocation reason](../attributes/revocation-reason.md):

- For a key-compromise or CA-compromise reason, the object enters the
  Compromised [state](../attributes/state.md), the compromise date is set to
  now, and the [Compromise Occurrence Date](../attributes/compromise-occurrence-date.md)
  is set from the request — or, if the client did not supply one, defaults to the
  object's initial date.
- For any other reason, the object enters the Deactivated state and its
  deactivation date is set to now.

Because revocation is a sensitive action, servers should restrict it to the
object's owner or an authorized security officer and enforce strong
authentication.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: a missing revocation reason, a compromise date supplied for a
non-compromise reason, an unknown object, or insufficient permission.

## Related Operations

[Activate](activate.md) · [Destroy](destroy.md)
