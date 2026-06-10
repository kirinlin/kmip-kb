---
title: Description
category: attribute
spec_version: "1.4"
spec_versions: ["1.4", "2.0", "2.1"]
source_section: "3.46"
status: draft
related: ["comment", "contact-information", "custom-attribute"]
keywords: ["description", "informational attribute", "metadata"]
---

# Description

## Purpose

A free-text label describing what the object is for — "TDE master key for
prod-db-7", say. Added in 1.4 to give this common need a standard home
instead of every vendor inventing an `x-description`
[custom attribute](custom-attribute.md). Informational only; never policy
input.

## Data Type & Structure

A single Text String.

## Constraints

- Optional; single instance; modifiable and deletable by the client,
  modifiable by the server.
- Distinguish from [Comment](comment.md) (working notes) and
  [Name](name.md) (a unique, locatable handle) — Description carries no
  uniqueness or lookup semantics, though servers may allow Locate matches
  on it.

## Applies To (Object Types)

All managed objects.

## Set / Modified By

Client or server, at creation/registration or any time afterwards via
[Add](../operations/add-attribute.md) /
[Modify Attribute](../operations/modify-attribute.md).

## Related Attributes

[Comment](comment.md) · [Contact Information](contact-information.md) ·
[Custom Attribute](custom-attribute.md)
