---
title: Comment
category: attribute
spec_version: "2.1"
spec_versions: ["1.4", "2.0", "2.1"]
source_section: "4.9"
v1_source_section: "3.47"
status: draft
related: ["description", "contact-information", "custom-attribute"]
keywords: ["comment", "notes", "informational attribute"]
---

# Comment

## Purpose

Free-text working notes on an object — "rotated early after incident
INC-1234", "pending decommission". Added in 1.4 as the informal sibling of
[Description](description.md): Description says what the object *is*,
Comment captures remarks about it. Neither influences policy.

## Data Type & Structure

A single Text String. (The spec's encoding table for this attribute
mislabels the row as "Description" — a known editorial slip; the attribute
name is Comment.)

## Constraints

- Optional; single instance; client-modifiable and deletable, server-
  modifiable.

## Applies To (Object Types)

All managed objects.

## Set / Modified By

Client or server, at creation/registration or later via
[Add](../operations/add-attribute.md) /
[Modify Attribute](../operations/modify-attribute.md).

## Related Attributes

[Description](description.md) ·
[Contact Information](contact-information.md) ·
[Custom Attribute](custom-attribute.md)
