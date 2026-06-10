---
title: Key Value Location
category: attribute
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.27"
v1_source_section: "3.42"
status: draft
related: ["key-value-present", "application-specific-information"]
keywords: ["key value location", "external key material", "URI", "metadata-only registration"]
---

# Key Value Location

## Purpose

The companion to [Key Value Present](key-value-present.md): when a client
registers an object whose material lives elsewhere, this attribute says
*where* — a URI or an uninterpreted locator string pointing at the real
storage (an HSM slot, an external vault, a tape).

## Data Type & Structure

A structure:

| Field | Type | Required |
|---|---|---|
| Key Value Location Value | Text String | Yes — the locator itself |
| Key Value Location Type | Enumeration | Yes — `URI` or `Uninterpreted Text String` |

## Constraints

- Optional; multi-instance (material can be reachable several ways).
- Client-owned: the server records it but does not resolve or validate the
  locator; it is never set implicitly.
- Only meaningful for the same object types whose key block may omit
  material.

## Applies To (Object Types)

Symmetric keys, private keys, split keys, and secret data. Not certificates,
public keys, opaque objects, or templates.

## Set / Modified By

Client only — at [Register](../operations/register.md) time or later via
[Add Attribute](../operations/add-attribute.md); client-modifiable and
deletable.

## Related Attributes

[Key Value Present](key-value-present.md) ·
[Application Specific Information](application-specific-information.md)
