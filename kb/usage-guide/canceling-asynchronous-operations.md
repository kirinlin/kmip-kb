---
title: Canceling Asynchronous Operations
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.33"
status: draft
related: ["synchronous-and-asynchronous-operations", "querying-outstanding-asynchronous-requests"]
keywords: ["async cancel", "Cancel", "asynchronous", "partial completion", "operation status", "server state"]
---

# Canceling Asynchronous Operations

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

When a client cancels an asynchronous operation, the server returns no information about any partial work that may have been completed. Responsibility for identifying and remediating any partially completed side effects lies entirely with the server; the client receives only a success or failure for the cancellation itself.

## Guidance

After a successful cancellation, the server is responsible for tidying up any intermediate state produced by the partially executed operation. The client cannot rely on the partial state being rolled back, committed, or in any particular condition after cancellation.

The server also determines independently how long to retain the status of completed asynchronous operations. Once the client has polled a final status (any status other than "pending"), subsequent polls for the same operation may return either the same status or an "unavailable" response — clients must handle both.

## Implementation Notes

Clients implementing async workflows should not assume that cancellation is immediate or atomic. If partial state matters (e.g., a Create that may have partially registered a key), clients should follow up with a Get or Locate to determine actual server state before assuming the cancellation was clean.

## Related Concepts

See [Synchronous and Asynchronous Operations](synchronous-and-asynchronous-operations.md) and [Querying Outstanding Asynchronous Requests](querying-outstanding-asynchronous-requests.md).
