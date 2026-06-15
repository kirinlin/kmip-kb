---
title: Alternative Name
category: attribute
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.2"
v1_source_section: "3.40"
status: reviewed
related: ["name", "unique-identifier", "application-specific-information"]
keywords: ["alternative name", "alias", "locate", "URI", "DNS name", "email", "4200BF", "AlternativeName"]
tag_hex: "4200BF"
xml_text: "AlternativeName"
---

# Alternative Name

## Purpose

A second naming system, added in 1.2, for labels that — unlike
[Name](name.md) — do **not** have to be unique in the management domain.
Useful for indexing objects by attributes several objects might share
(a hostname, an email address, a serial scheme) or for migrating identifiers
from systems with looser naming rules.

## Data Type & Structure

A structure:

| Field | Tag | XML Element | Required | Type |
|---|---|---|---|---|
| Alternative Name Value | `4200C0` | `AlternativeNameValue` | Yes | Text String |
| Alternative Name Type | `4200C1` | `AlternativeNameType` | Yes | Enumeration — Uninterpreted Text String, URI, Object Serial Number, Email Address, DNS Name, X.500 Distinguished Name, or IP Address |

## Constraints

- Optional; multi-instance; intended to be human-readable.
- No uniqueness requirement — a [Locate](../operations/locate.md) by
  alternative name may match many objects.
- Server-side naming rules may apply, communicated out of band.

## Applies To (Object Types)

All managed objects.

## Set / Modified By

Client-set; client-modifiable and deletable. The server may write it only
when no value is present (e.g. filling in a generated alias).

## Related Attributes

[Name](name.md) · [Unique Identifier](unique-identifier.md) ·
[Application Specific Information](application-specific-information.md)
