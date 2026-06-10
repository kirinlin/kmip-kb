---
title: Unique Batch Item ID
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "9.21"
v1_source_section: "6.4"
status: draft
related: ["batch-item", "batch-count", "batch-order-option"]
keywords: ["unique batch item ID", "correlation", "batching", "request response matching"]
---

# Unique Batch Item ID

## Overview

The per-item correlation token inside batched messages: when a request packs
several [batch items](batch-item.md), each carries an ID, and the server
copies the ID onto the corresponding response item so the client can match
answers to questions regardless of processing order.

## Encoding (Tag / Type / Length / Value)

Tag `420093`, Byte String, client-chosen content (a counter, a UUID —
anything unique within the message).

## Fields & Structure

Optional in single-item messages, required whenever
[Batch Count](batch-count.md) exceeds 1. The response item's ID must equal
the request item's. This is correlation *within* one message — not across
messages (that is the
[Asynchronous Correlation Value](asynchronous-correlation-value.md)'s job)
and not for logging (the 1.4
[client](client-correlation-value.md)/[server](server-correlation-value.md)
correlation values).

## Examples

A request batching Create + Activate + Get carries IDs `01`, `02`, `03`;
the response's three items echo them, so the client knows which Result
Status belongs to the Activate even though all three report on one new key.

## Related

[Batch Item](batch-item.md) · [Batch Count](batch-count.md) ·
[Batch Order Option](batch-order-option.md)
