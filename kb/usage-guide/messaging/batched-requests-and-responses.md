---
title: Batched Requests and Responses
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-2.8"
status: reviewed
related: ["id-placeholder", "reducing-multiple-requests-through-the-use-of-batch", "maximum-message-size"]
keywords: ["batch", "batch error", "pipeline", "ID placeholder", "throughput", "undo"]
---

# Batched Requests and Responses

## Overview

KMIP includes a batching mechanism that allows a client to send multiple operation requests in a single message and receive their results in a single response. Batching improves throughput for workflows involving large numbers of objects.

## Guidance

Each item in a batch is a self-contained request/response pair. The Batch Error Continuation option controls how the server behaves when one item fails: it can stop processing, continue processing remaining items, or attempt to undo all previously completed items. Results from earlier batch items can be piped into later ones via the ID Placeholder (by omitting the Unique Identifier) or via an explicit reference by enumeration or index.

## Implementation Notes

Atomicity of batch operations is not guaranteed by the protocol. Servers may optionally support "undo" mode to roll back a batch if an error occurs, but clients cannot assume this is available. The optional "continue" mode is also server-dependent. Both can be discovered via the Query Capability Information function. The Maximum Response Size limit applies cumulatively across all items in a batch, so clients should account for this when constructing large batches.

## Related Concepts

See [ID Placeholder](../identification/id-placeholder.md) for cross-item reference details, [Reducing Multiple Requests Through the Use of Batch](reducing-multiple-requests-through-the-use-of-batch.md), and [Maximum Message Size](maximum-message-size.md).
