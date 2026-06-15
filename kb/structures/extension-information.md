---
title: Extension Information
category: structures
spec_version: "2.1"
spec_versions: ["1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "7.13"
v1_source_section: "2.1.9"
status: reviewed
related: ["ttlv-encoding", "message-extension"]
keywords: ["extension information", "vendor extension", "extension tag", "query extension list"]
tag_hex: "4200A4"
xml_element: "ExtensionInformation"
---

# Extension Information

## Overview

Metadata describing a vendor extension object — one whose TTLV tag lives in
the Extensions range (`540000`–`54FFFF`). Returned by
[Query](../operations/query.md) when a client asks for the extension list or
extension map, so implementations can discover what proprietary objects a
peer speaks. Added in 1.1.

## Encoding (Tag / Type / Length / Value)

Structure, tag `4200A4`:

| Field | Tag | XML Element | Type | Required |
|---|---|---|---|---|
| Extension Name | `4200A5` | `ExtensionName` | Text String | Yes |
| Extension Tag | `4200A6` | `ExtensionTag` | Integer | No |
| Extension Type | `4200A7` | `ExtensionType` | Integer | No |

## Fields & Structure

The name is the human-readable label for the extension object; the tag is
its numeric Item Tag; the type is its Item Type code (per the
[TTLV type table](../ttlv/ttlv-encoding.md)). Query's *Extension List* function
returns names only; *Extension Map* fills in tag and type as well — which is
why both fields are optional here.

## Examples

A server supporting a proprietary audit blob answers Query (Extension Map)
with Extension Information { Name = `"y-AcmeAuditRecord"`, Tag = 0x540007,
Type = 0x01 (Structure) }.

## Related

[TTLV Encoding](../ttlv/ttlv-encoding.md) ·
[Message Extension](../messages/message-extension.md) ·
[Query](../operations/query.md)
