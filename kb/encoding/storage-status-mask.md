---
title: Storage Status Mask
category: encoding
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "12.3"
status: reviewed
related: ["locate", "protection-storage-mask", "state"]
keywords: ["storage status mask", "bit mask", "online storage", "archival storage", "destroyed storage", "locate filter", "storage status", "42008E", "StorageStatusMask"]
tag_hex: "42008E"
xml_text: "StorageStatusMask"
---

# Storage Status Mask

## Overview

The Storage Status Mask is a 32-bit integer bit field defined in §12.3 of the KMIP specification. Its bits classify the current storage state of managed objects — whether the object is in on-line storage (immediately accessible), archival storage (retrievable but not immediately available), or a destroyed state where material has been removed but a record remains. The mask is used as a filter in [Locate](../operations/locate.md) requests and may be returned in Get Attributes responses to describe an object's current storage status.

## Encoding (Tag / Type / Length / Value)

The Storage Status Mask value encodes as a 32-bit Integer (tag `42008E`). It is a scalar field whose bits are interpreted individually.

| Tag | XML Text | Type | Width |
|---|---|---|---|
| `42008E` | StorageStatusMask | Integer | 32 bits |

## Fields & Structure

The defined bit positions and their storage status categories:

| Bit | Status | XML Text |
|---|---|---|
| 0 (0x00000001) | On-Line Storage | `OnLineStorage` |
| 1 (0x00000002) | Archival Storage | `ArchivalStorage` |
| 2 (0x00000004) | Destroyed Storage | `DestroyedStorage` |

Bits 3 and above are reserved for standard use; extension values use even-numbered bit positions only. Multiple bits may be set when an object exists in more than one storage state simultaneously (for example, an object whose original is in on-line storage while an archival copy also exists).

When used as a Locate filter, a non-zero Storage Status Mask restricts the search to objects whose storage state matches at least one of the set bits. Setting the mask to `00000001` (On-Line Storage) returns only objects currently in active storage, excluding archived or destroyed records. Setting it to `00000007` (all bits) returns all objects regardless of storage state.

A server may apply a default storage status filter of On-Line Storage to Locate queries that do not specify a mask, returning only active objects by default.

## Examples

A normal application looking for active keys passes Storage Status Mask = `00000001` (On-Line Storage) in a Locate request. This excludes archived and destroyed records, which is the most common filter.

A compliance audit that must enumerate all objects — including destroyed ones — to verify destruction records passes `00000007` (On-Line Storage | Archival Storage | Destroyed Storage), selecting across all defined states.

An archival retrieval workflow that wants only objects in cold storage passes `00000002` (Archival Storage) to avoid pulling back active on-line keys.

## Related

[Locate](../operations/locate.md) · [Protection Storage Mask](protection-storage-mask.md) · [State](../attributes/state.md)
