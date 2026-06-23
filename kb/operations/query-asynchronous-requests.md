---
title: Query Asynchronous Requests
category: operation
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "6.1.41"
status: reviewed
related: ["query", "cancel", "poll", "asynchronous-request", "asynchronous-correlation-values"]
keywords: ["query asynchronous requests", "async", "asynchronous", "pending operations", "correlation value", "async status", "long-running operation"]
xml_text: "QueryAsynchronousRequests"
---

# Query Asynchronous Requests

## Purpose

`Query Asynchronous Requests` checks the status of one or more operations that were submitted asynchronously and have not yet completed. When a client submits an operation with the Asynchronous Indicator set, the server acknowledges immediately and returns an Asynchronous Correlation Value rather than waiting for the operation to finish. The client later calls `Query Asynchronous Requests` to learn whether those operations have completed, and if so, to retrieve their results.

This operation is the primary polling mechanism in the KMIP asynchronous execution model. It complements the older [`Poll`](poll.md) operation and provides direct status access for multiple pending operations in a single round-trip.

## Request Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Asynchronous Correlation Value | `420006` | `AsynchronousCorrelationValue` | Yes (one or more) | One or more [Asynchronous Correlation Values](../structures/asynchronous-correlation-values.md) identifying the pending operations whose status the client wants. Each value was issued by the server when the corresponding asynchronous request was accepted. |

## Response Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Asynchronous Request | `420173` | `AsynchronousRequest` | Yes (one per queried value) | One [Asynchronous Request](../structures/asynchronous-request.md) entry for each correlation value in the request. Each entry carries the correlation value, the current status of the operation (pending, processing, complete, failed), and — when the operation has completed — the full result that the operation would have returned synchronously. |

## Behavior & Server Requirements

The server looks up each submitted Asynchronous Correlation Value in its table of pending operations. For each one it finds, it includes an Asynchronous Request entry in the response with the current processing state.

If an operation is still pending or in progress, the entry indicates the ongoing state. The client should wait and retry. Servers may provide progress information (e.g., an estimated completion percentage) but are not required to.

Once an operation completes, its result is held by the server until the client retrieves it via `Query Asynchronous Requests`. After the client has successfully retrieved the result, the server may remove the correlation value from its active table. Subsequent queries for the same value may return an error indicating the result has already been collected or has expired.

If a correlation value is not recognized — because it was never issued, was already retrieved, or has expired — the server returns an appropriate error for that entry. Other entries in the same request are still processed normally.

For large batches of asynchronous operations, a client may submit several correlation values in a single `Query Asynchronous Requests` call rather than polling for each individually.

## Errors

Uses centralized error handling per the [error handling](../concepts/error-handling.md) conventions. Common failure causes include:

- A supplied Asynchronous Correlation Value is not recognized — it was never issued by this server, the result was already collected, or the entry expired.
- The calling client is not the same client that submitted the original asynchronous operation (authorization mismatch).
- The server does not support asynchronous operations — returns Operation Not Supported.

## Examples

A client submits a computationally expensive [`Re-Key`](re-key.md) operation asynchronously and receives correlation value `"async-re-key-9912"`. Ten seconds later it polls for the result:

```
Operation: Query Asynchronous Requests
  Asynchronous Correlation Value: "async-re-key-9912"
```

While the re-key is still in progress, the server responds:

```
Asynchronous Request:
  Asynchronous Correlation Value: "async-re-key-9912"
  Operation State: Executing
```

When the re-key has finished, a subsequent poll yields:

```
Asynchronous Request:
  Asynchronous Correlation Value: "async-re-key-9912"
  Operation State: Completed
  Response Payload:
    Unique Identifier: "new-key-7734"
```

A client tracking multiple concurrent key-creation operations can query all of them in one call by including multiple Asynchronous Correlation Values in the request.

## Related Operations

[Poll](poll.md) · [Cancel](cancel.md) · [Query](query.md)
