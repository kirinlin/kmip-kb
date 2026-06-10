---
title: Notify
category: operation
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4"]
source_section: "5.1"
status: draft
related: ["put", "query", "modify-attribute", "get-attributes", "last-change-date"]
keywords: ["notify", "server-to-client", "push notification", "attribute change", "event"]
---

# Notify

## Purpose

`Notify` lets a server tell a client that attributes of a managed object have
changed — for example that a key was revoked or its dates were modified.
Unlike everything in section 4 of the spec, the server initiates this
exchange: it can only happen over a channel the server is able to open toward
the client, arranged through configuration outside the protocol.

## Request Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | Yes | Which object the notification is about. |
| Attribute | Yes (repeatable) | Each attribute that changed, with its new value. [Last Change Date](../../attributes/last-change-date.md) is always among them. A deleted attribute is conveyed by an [Attribute structure](../../ttlv/attribute.md) with no Attribute Value. |

## Response Fields

The client replies with an empty-payload response message — just the standard
header and batch item carrying the result status. No payload fields are
defined.

## Behavior & Server Requirements

The message reuses the normal [request message
format](../../ttlv/message-structure.md), minus the fields that only make
sense for client requests: Asynchronous Indicator, Maximum Response Size,
Batch Order Option, and Batch Error Continuation Option must not appear. The
server learns where and how to reach the client through out-of-band
configuration; the spec does not define registration, delivery channels, or
retry behavior. A client that receives a Notify acknowledges it with an empty
response unless both sides already agreed (out of band) that the client
cannot respond.

## Errors

Uses the centralized [error handling](../../concepts/error-handling.md).
Because the roles are reversed, it is the client that returns a failure
status if it cannot parse or accept the notification.

## Examples

A server revokes a key at an administrator's request. For each client
configured to hear about that key, the server opens its notification channel
and sends Notify with the key's Unique Identifier and the changed attributes:
[State](../../attributes/state.md) = Deactivated,
[Deactivation Date](../../attributes/deactivation-date.md), and the new Last
Change Date. Each client acknowledges and refreshes its cached copy.

## Related Operations

[Put](put.md) · [Query (server-to-client)](query.md) ·
[Get Attributes](../get-attributes.md)
