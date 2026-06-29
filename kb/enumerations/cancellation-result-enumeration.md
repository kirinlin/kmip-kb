---
title: Cancellation Result Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.7"
status: reviewed
related: ["cancel", "asynchronous-indicator-enumeration", "processing-stage-enumeration", "query-asynchronous-requests"]
keywords: ["cancellation", "cancel", "async", "asynchronous operation", "stop", "abort", "420012", "CancellationResult"]
tag_hex: "420012"
xml_text: "CancellationResult"
tag_type: "Enumeration"
---

# Cancellation Result Enumeration

## Overview

The Cancellation Result enumeration conveys the server's response to a [Cancel](../operations/cancel.md) request. When a client has submitted an operation asynchronously and subsequently decides it no longer needs the result, it sends a Cancel request with the operation's correlation value. The Cancellation Result tells the client whether the server was able to honour the request, what state the operation was in, or why cancellation was not possible. This feedback is important for clients that need to decide whether to wait for a result or treat the operation as abandoned.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Canceled | `00000001` | `Canceled` | The server successfully stopped the in-progress operation before it completed; no result will be produced for this correlation value. |
| Unable to Cancel | `00000002` | `UnableToCancel` | The operation has already completed by the time the Cancel request arrived. The result is available via Query Asynchronous Requests; the Cancel had no effect. |
| Completed | `00000003` | `Completed` | The asynchronous operation finished successfully before the Cancel request arrived; the operation cannot be undone but its result is available via Query Asynchronous Requests. |
| Failed | `00000004` | `Failed` | The asynchronous operation terminated with an error before the Cancel request was processed; a failure result is recorded and retrievable via Query Asynchronous Requests. |
| Unavailable | `00000005` | `Unavailable` | The server has no record of an asynchronous operation matching the supplied correlation value, or the operation's tracking entry has already expired or been purged. |

## Examples

A client that submitted a large key derivation job asynchronously but then received updated key material from another source sends a Cancel. If the derivation was still queued, the server returns **Cancelled** and the client can move on. If the derivation had already finished, the server returns **Unable to Cancel** and the client retrieves the completed result from the asynchronous queue.

## Related

- [Cancel operation](../operations/cancel.md) — the operation that returns this enumeration
- [Processing Stage Enumeration](processing-stage-enumeration.md) — describes the stage of an asynchronous operation
- [Query Asynchronous Requests operation](../operations/query-asynchronous-requests.md) — retrieves results of completed async operations
- [Asynchronous Indicator Enumeration](asynchronous-indicator-enumeration.md) — controls whether operations run asynchronously
