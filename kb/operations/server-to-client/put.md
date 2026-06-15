---
title: Put
category: operation
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.2.3"
v1_source_section: "5.2"
status: reviewed
related: ["notify", "query", "get", "re-key", "obtain-lease", "lease-time"]
keywords: ["put", "server-to-client", "push", "key distribution", "replace", "put function"]
---

# Put

## Purpose

`Put` is the server-initiated counterpart of [Get](../get.md): the server
pushes a managed object to a client without being asked. Typical use is
proactive key distribution — delivering a replacement before the current
certificate or key expires — to clients that cannot or do not poll.

## Request Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes | Identifier of the object being delivered. |
| Put Function | `420070` | `PutFunction` | Yes | `New` (an object the client has not seen) or `Replace` (supersedes an object the client already holds). |
| Replaced Unique Identifier | `420076` | `ReplacedUniqueIdentifier` | When Put Function is Replace | Which client-held object is being superseded. |
| Managed Object |  |  | Yes | The object itself — symmetric key, certificate, public or private key, secret data, split key, template, or opaque object. |
| Attribute | `420008` | `Attribute` | No (repeatable) | Attributes the server sends along, e.g. usage guidance or a [Lease Time](../../attributes/lease-time.md) granting a lease. |

## Response Fields

The client returns an empty-payload response message acknowledging receipt;
no payload fields are defined.

## Behavior & Server Requirements

Like [Notify](notify.md), Put uses the standard [request
format](../../messages/message-structure.md) without Asynchronous Indicator,
Maximum Response Size, Batch Order Option, or Batch Error Continuation
Option, and rides a server-initiated channel arranged out of band. If the
client receives `Replace` naming an object it does not hold, it treats the
message as `New`. When the pushed key is wrapped, the wrapping arrangement
(which KEK, which parameters) must have been agreed beforehand — there is no
in-band [Key Wrapping Specification](../../structures/key-wrapping-specification.md)
exchange in this flow.

## Errors

Uses the centralized [error handling](../../concepts/error-handling.md); the
client reports the failure if it cannot store or parse the pushed object.

## Examples

A storage array's encryption certificate nears expiry. The server creates the
successor, then sends Put with Put Function = Replace, the new certificate,
the expiring certificate's identifier in Replaced Unique Identifier, and an
Activation Date attribute. The array acknowledges, installs the new
certificate, and retires the old one.

## Related Operations

[Notify](notify.md) · [Get](../get.md) · [Re-key](../re-key.md) ·
[Obtain Lease](../obtain-lease.md)
