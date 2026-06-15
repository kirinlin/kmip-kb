---
title: Querying Outstanding Asynchronous Requests
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.35"
status: reviewed
related: ["synchronous-and-asynchronous-operations", "canceling-asynchronous-operations"]
keywords: ["QueryAsynchronousRequests", "outstanding requests", "async status", "correlation value", "operation type"]
---

# Querying Outstanding Asynchronous Requests

## Overview

The QueryAsynchronousRequests operation allows a client to retrieve the status of all pending asynchronous requests that have not yet been returned via Poll or Cancel. This addresses a gap that becomes significant as asynchronous usage grows: clients may lose track of which operations are still in flight.

## Guidance

A client can query all outstanding requests at once or filter by operation type, by specific Asynchronous Correlation Values, or by both. This is a dedicated operation (not a parameter of the general Query operation) to keep the async management path clean and queryable independently of the main Query function.

## Implementation Notes

QueryAsynchronousRequests is useful for client recovery scenarios: after a crash or reconnection, the client can call this operation to discover which previously submitted operations are still pending and resume polling for them. The server's definition of "outstanding" is operations for which the result has not yet been delivered to the client via Poll or Cancel.

## Related Concepts

See [Synchronous and Asynchronous Operations](synchronous-and-asynchronous-operations.md) and [Canceling Asynchronous Operations](canceling-asynchronous-operations.md).
