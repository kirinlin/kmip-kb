---
title: Batch Count
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "9.5"
v1_source_section: "6.14"
status: draft
related: ["batch-item", "batch-order-option", "unique-batch-item-id"]
keywords: ["batch count", "message header", "number of operations"]
tag_hex: "42000D"
xml_element: "BatchCount"
---

# Batch Count

## Overview

The required header field stating how many [batch items](batch-item.md)
follow — the parser's contract for the rest of the message. A
single-operation message simply has Batch Count = 1.

## Encoding (Tag / Type / Length / Value)

Tag `42000D`, Integer, last field of both request and response headers.

## Fields & Structure

The response's count matches the number of items the server reports on —
which under the `Stop` [continuation policy](batch-error-continuation-option.md)
can be fewer than the request's count, since items after the failure are
never answered. Counts above 1 unlock (and require) the batching machinery:
[Unique Batch Item IDs](unique-batch-item-id.md), and optionally ordering
and error-continuation choices.

## Examples

Request header ends `Batch Count = 3`; the body then contains exactly three
Batch Item structures.

## Related

[Batch Item](batch-item.md) ·
[Unique Batch Item ID](unique-batch-item-id.md) ·
[Message Structure](message-structure.md)
