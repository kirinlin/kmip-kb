---
title: Tag Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.56"
status: reviewed
related: ["ttlv-encoding", "item-data-types", "message-structure"]
keywords: ["tag", "TTLV tag", "42XXXX", "tag enumeration", "field identifier", "tag namespace"]
tag_hex: "420138"
xml_element: "Tag"
---

# Tag Enumeration

## Overview

The Tag enumeration is the master registry of TTLV tag values — the 3-byte `42xxxx` identifiers that name every field, structure, and enumeration in a KMIP message. Every field in every KMIP request or response is prefixed with a 3-byte tag drawn from this enumeration, giving KMIP's encoding a self-describing character: a parser needs only the tag registry to identify any field it encounters, without a separate per-message schema.

Tags are grouped by range:
- `0x420000`–`0x42FFFF`: Standard KMIP tags defined in this enumeration.
- `0x540000`–`0x54FFFF`: Extension tags. The range `0x540000`–`0x547FFF` is available for private-use extensions; `0x548000`–`0x54FFFF` is reserved for KMIP specification use.

## Encoding (Tag / Type / Length / Value)

Tags appear as the first 3 bytes of every TTLV item: `[Tag 3B][Type 1B][Length 4B][Value nB][Padding]`. The type byte following the tag identifies the data type (Structure, Integer, Enumeration, etc.). Tags themselves are not encoded as TTLV values; they are the framing identifiers.

## Fields & Structure

The Tag Enumeration is large — KMIP v2.1 defines over 400 standard tags — covering every field name used in the specification. Examples include:

- `420001` — Activation Date
- `420028` — Cryptographic Algorithm
- `42002A` — Cryptographic Length
- `42002C` — Cryptographic Usage Mask
- `420040` — Key Block
- `420042` — Key Format Type
- `420057` — Object Type
- `42005C` — Operation
- `420094` — Unique Identifier
- `4200BE` — Name
- `4200C3` — State

Vendor extension tags in the `54xxxx` range do not appear in this enumeration; they are defined by the extending party.

## Examples

A TTLV decoder encountering `42 00 28 05 00 00 00 04 00 00 00 03 00 00 00 00` parses tag `420028` (Cryptographic Algorithm), type `05` (Enumeration), length `4`, value `3` (AES), with 4 bytes of padding.

## Related

[TTLV Encoding](../ttlv-encoding.md) · [Item Data Types](../../references/item-data-types.md) · [Message Structure](../../messages/message-structure.md)
