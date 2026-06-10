---
title: Poll
category: operation
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.28"
status: draft
related: ["cancel", "recover", "asynchronous-correlation-value"]
keywords: ["poll", "asynchronous", "correlation value", "operation status", "pending"]
---

# Poll

## Purpose

`Poll` checks on the status of an outstanding asynchronous operation. After a
request is accepted for asynchronous processing, the client uses `Poll` with the
returned correlation value to find out whether it has finished and, if so, to
collect its result.

## Request Fields

| Field | Required | Description |
|---|---|---|
| Asynchronous Correlation Value | Yes | Identifies the pending operation to poll. |

## Response Fields

The response takes one of two forms depending on whether the operation has
finished (see Behavior).

## Behavior & Server Requirements

If the operation is still running, the server replies with an empty payload and
a Pending result status. If it has finished, the server replies with the normal
payload for that operation — exactly what the client would have received had the
operation run synchronously. The response to a `Poll` is itself always
synchronous. Operations like [Recover](recover.md) commonly rely on `Poll`
because retrieving an object from the archive may take time.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: a correlation value that matches no pending operation.

## Related Operations

[Cancel](cancel.md) · [Recover](recover.md)
