---
title: Contact Information
category: attribute
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.12"
v1_source_section: "3.37"
status: draft
related: ["description", "comment", "custom-attribute"]
keywords: ["contact information", "owner contact", "informational attribute"]
tag_hex: "420022"
xml_element: "ContactInformation"
---

# Contact Information

## Purpose

A who-to-call note attached to the object — an email address, a team name, a
ticket queue. Purely informational: servers store and return it but never
base policy decisions on it.

## Data Type & Structure

A single Text String with no prescribed format.

## Constraints

- Optional; single instance; freely modifiable and deletable by the client
  (and modifiable by the server).

## Applies To (Object Types)

All managed objects.

## Set / Modified By

Client or server; implicitly set by the object-creating operations
([Create](../operations/create.md),
[Create Key Pair](../operations/create-key-pair.md),
[Register](../operations/register.md),
[Derive Key](../operations/derive-key.md), certify and re-key families),
typically by inheritance from the predecessor or template.

## Related Attributes

[Description](description.md) · [Comment](comment.md) ·
[Custom Attribute](custom-attribute.md)
