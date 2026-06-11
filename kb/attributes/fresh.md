---
title: Fresh
category: attribute
spec_version: "2.1"
spec_versions: ["1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.24"
v1_source_section: "3.34"
status: draft
related: ["object-group", "initial-date", "key-value-present"]
keywords: ["fresh", "unused key", "key pool", "group member fresh"]
tag_hex: "4200A8"
xml_element: "Fresh"
---

# Fresh

## Purpose

A served/not-yet-served flag: True means no client has ever retrieved this
object's material. Added in 1.1 to support pre-generated key pools — a client
asking [Locate](../operations/locate.md) for a "Group Member Fresh" object
gets a key guaranteed untouched by any other consumer.

## Data Type & Structure

A Boolean. True on creation; flipped to False by the server the first time
the object is served to a client (e.g. via [Get](../operations/get.md)).

## Constraints

- Optional; single instance.
- One-way and server-owned after creation: clients can supply an initial
  value when registering but can never modify or delete it, and the server
  only ever moves it True → False.

## Applies To (Object Types)

All cryptographic objects.

## Set / Modified By

Initially set by server (or client at registration); implicitly set by every
object-creating operation ([Create](../operations/create.md),
[Create Key Pair](../operations/create-key-pair.md),
[Register](../operations/register.md),
[Derive Key](../operations/derive-key.md), certify/re-key families); updated
by the server on first delivery.

## Related Attributes

[Object Group](object-group.md) · [Initial Date](initial-date.md) ·
[Key Value Present](key-value-present.md)
