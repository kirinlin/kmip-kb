---
title: Activate
category: operation
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.19"
status: draft
related: ["create", "revoke", "destroy", "state", "activation-date"]
keywords: ["activate", "key state", "pre-active", "active", "activation date"]
---

# Activate

## Purpose

`Activate` brings a cryptographic object into service. It moves an object from
the Pre-Active [state](../attributes/state.md) to Active, marking the point at
which the object may be used for cryptographic work.

## Request Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | No | The object to activate; the ID Placeholder is used when omitted. |

## Response Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | Yes | The object's identifier. |

## Behavior & Server Requirements

The operation applies only to an object currently in the Pre-Active state;
applying it elsewhere is an error. On success the object's state becomes Active
and its [Activation Date](../attributes/activation-date.md) is set to the current
time. Template objects cannot be activated.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: the object is not in the Pre-Active state, an unknown object, or
insufficient permission.

## Related Operations

[Create](create.md) · [Revoke](revoke.md) · [Destroy](destroy.md)
