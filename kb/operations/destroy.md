---
title: Destroy
category: operation
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.15"
v1_source_section: "4.21"
status: reviewed
related: ["revoke", "archive", "state", "destroy-date"]
keywords: ["destroy", "delete key", "key destruction", "key material", "end of life"]
xml_text: "Destroy"
---

# Destroy

## Purpose

`Destroy` tells the server to dispose of an object's key material. It is the
end-of-life operation for a managed object's secret content.

## Request Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | No | The object to destroy; the ID Placeholder is used when omitted. |

## Response Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes | The object's identifier. |

## Behavior & Server Requirements

The server destroys the key material, but it may keep the object's metadata —
for instance to prove that a retired signing key is no longer usable. A
cryptographic object can only be destroyed from the Pre-Active or Deactivated
[state](../attributes/state.md). When the target is a Template object, the whole
object including its metadata is removed. As with [Revoke](revoke.md), servers
should restrict this operation to the owner or an authorized security officer
and enforce strong authentication.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: the object is in a state from which destruction is not allowed, an
unknown object, or insufficient permission.

## Related Operations

[Revoke](revoke.md) · [Archive](archive.md)
