---
title: Cancel
category: operation
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.5"
v1_source_section: "4.27"
status: reviewed
related: ["poll", "asynchronous-correlation-value"]
keywords: ["cancel", "asynchronous", "correlation value", "abort operation"]
---

# Cancel

## Purpose

`Cancel` requests that the server stop an outstanding asynchronous operation. It
is used together with the asynchronous-operation mechanism, where a long-running
request returns a correlation value the client can later cancel or
[poll](poll.md).

## Request Fields

| Field | Required | Description |
|---|---|---|
| Asynchronous Correlation Value | Yes | Identifies the pending operation to cancel. |

## Response Fields

| Field | Required | Description |
|---|---|---|
| Asynchronous Correlation Value | Yes | Echoes the value from the request. |
| Cancellation Result | Yes | The outcome of the cancellation attempt. |

## Behavior & Server Requirements

The Cancellation Result reports what happened: the operation was canceled; it
could not be canceled; it had already finished successfully before the cancel
took effect; it had already finished with a failure; or the correlation value
did not match any recent pending or completed operation. The response to a
`Cancel` is always synchronous.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). The status
of the cancellation itself is conveyed in the Cancellation Result rather than as
an error.

## Related Operations

[Poll](poll.md)
