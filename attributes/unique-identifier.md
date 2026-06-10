---
title: Unique Identifier
category: attribute
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "3.1"
status: draft
related: ["name", "object-type", "alternative-name", "link"]
keywords: ["unique identifier", "UID", "object identity", "ID placeholder"]
---

# Unique Identifier

## Purpose

Every managed object's primary key. The server mints this value when an
object enters its custody and every subsequent operation refers to the object
by it — [Get](../operations/get.md), [Locate](../operations/locate.md)
results, [Link](link.md) targets, and the ID Placeholder used to chain batch
items all traffic in Unique Identifiers.

## Data Type & Structure

A single Text String. The spec leaves the format to the server: UUIDs are
common, but any string unique within that server's identifier space is legal.
Global uniqueness is recommended (not required) so objects can move between
key-management domains without collisions.

## Constraints

- Always present, from creation/registration until the object is destroyed.
- Single instance; read-only for both client and server once assigned —
  never modified, never deletable by the client.

## Applies To (Object Types)

All managed objects.

## Set / Modified By

Set by the server, implicitly, during any operation that creates an object:
[Create](../operations/create.md),
[Create Key Pair](../operations/create-key-pair.md),
[Register](../operations/register.md),
[Derive Key](../operations/derive-key.md),
[Certify](../operations/certify.md) /
[Re-certify](../operations/re-certify.md),
[Re-key](../operations/re-key.md) /
[Re-key Key Pair](../operations/re-key-key-pair.md). Clients can never choose
or change it; human-friendly handles belong in [Name](name.md).

## Related Attributes

[Name](name.md) · [Alternative Name](alternative-name.md) ·
[Object Type](object-type.md) · [Link](link.md)
