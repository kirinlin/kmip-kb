---
title: Batch Error Continuation Option
category: messages
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "9.6"
v1_source_section: "6.13"
status: reviewed
related: ["batch-order-option", "batch-count", "result-status", "capability-information"]
keywords: ["batch error continuation", "undo", "stop", "continue", "rollback"]
tag_hex: "42000E"
xml_element: "BatchErrorContinuationOption"
---

# Batch Error Continuation Option

## Overview

What the server should do with the rest of a multi-item batch after one item
fails. Three policies:

| Value | On failure |
|---|---|
| Continue (1) | Report the failure, keep processing the remaining items. |
| Stop (2, default) | Stop there; earlier completed items stand, later items are never run. |
| Undo (3) | Roll back the items already completed, reporting them as Operation Undone. |

## Encoding (Tag / Type / Length / Value)

Tag `42000E`, Enumeration, request header; only allowed when
[Batch Count](batch-count.md) > 1.

## Fields & Structure

Stop is assumed when the field is absent. Supporting anything beyond Stop is
optional — a server without the feature must reject a request specifying
Continue or Undo outright. From 1.4, servers advertise Undo/Continue support
via [Capability Information](../structures/capability-information.md) (Batch Undo /
Batch Continue Capability), so clients can check before depending on
transactional batches.

## Examples

Provisioning ten keys atomically: Batch Error Continuation Option = Undo; a
quota failure on key 7 rolls back keys 1–6, whose response items report
Operation Undone.

## Related

[Batch Order Option](batch-order-option.md) ·
[Result Status](result-status.md) ·
[Error Handling](../concepts/error-handling.md)
