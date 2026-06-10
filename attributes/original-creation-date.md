---
title: Original Creation Date
category: attribute
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.38"
v1_source_section: "3.43"
status: draft
related: ["initial-date", "last-change-date", "random-number-generator"]
keywords: ["original creation date", "key age", "registration", "provenance"]
---

# Original Creation Date

## Purpose

When the key material was *really* born, regardless of when this server
first saw it. Added in 1.2 because [Initial Date](initial-date.md) measures
server custody, which misstates the age of keys generated elsewhere and
registered later — and key age drives crypto-period policy.

## Data Type & Structure

A Date-Time.

## Constraints

- For **server-generated** objects (Derive Key, Create, Create Key Pair,
  and the two re-key operations): mandatory, server-set, equal to Initial
  Date.
- For **registered** objects: optional; the client may supply it at
  [Register](../operations/register.md) or add it later via
  [Add Attribute](../operations/add-attribute.md) — the server cannot know
  it.
- Single instance; once set it is permanent: no update, no deletion, by
  either side.
- Deliberately *not* copied by re-key operations — the successor gets its
  own creation date.

## Applies To (Object Types)

All managed objects.

## Set / Modified By

Server (generated objects) or client (registered objects); implicitly set by
[Create](../operations/create.md),
[Create Key Pair](../operations/create-key-pair.md),
[Derive Key](../operations/derive-key.md),
[Re-key](../operations/re-key.md),
[Re-key Key Pair](../operations/re-key-key-pair.md).

## Related Attributes

[Initial Date](initial-date.md) · [Last Change Date](last-change-date.md) ·
[Random Number Generator](random-number-generator.md)
