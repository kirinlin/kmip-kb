---
title: Batch Order Option
category: messages
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "9.8"
v1_source_section: "6.12"
status: reviewed
related: ["batch-count", "batch-error-continuation-option", "batch-item"]
keywords: ["batch order option", "in-order execution", "batching", "ID placeholder"]
tag_hex: "420010"
xml_element: "BatchOrderOption"
---

# Batch Order Option

## Overview

A request-header Boolean for multi-item batches: True forces the server to
execute the items in the order they appear; False (the default when absent)
lets it run them in any order it likes.

## Encoding (Tag / Type / Length / Value)

Tag `420010`, Boolean, request header; only meaningful when
[Batch Count](batch-count.md) > 1.

## Fields & Structure

Ordered execution matters whenever items depend on each other — most
commonly via the ID Placeholder, the implicit variable that carries the
Unique Identifier from one item ("Create") into the next ("Activate",
"Get"). Support is optional: a server that does not implement ordering must
reject an entire request that asks for True rather than silently reordering
it.

## Examples

Create → Activate → Get in one request, Batch Order Option = True, with the
Activate and Get omitting their Unique Identifier so the placeholder from
Create flows through.

## Related

[Batch Count](batch-count.md) ·
[Batch Error Continuation Option](batch-error-continuation-option.md) ·
[Batch Item](batch-item.md)
