---
title: Synchronous and Asynchronous Operations
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-2.6"
status: draft
related: ["canceling-asynchronous-operations", "querying-outstanding-asynchronous-requests", "full-async"]
keywords: ["synchronous", "asynchronous", "pending", "polling", "correlation value"]
---

# Synchronous and Asynchronous Operations

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

KMIP supports two modes of operation: synchronous, in which the client waits for a complete response before proceeding; and asynchronous, in which the server immediately acknowledges with an Asynchronous Correlation Value while the client polls for the actual result. Servers must support synchronous operations; asynchronous support is optional.

## Guidance

In synchronous mode the client sends a request and blocks until the server returns the final result. In asynchronous mode the server returns an Asynchronous Correlation Value and a "pending" status; the client uses that correlation value in subsequent Poll requests to retrieve the result when it becomes available.

Asynchronous operations are valuable when a requested operation may take significantly longer than the client is willing to wait, or in resource-constrained environments (such as IoT devices) that cannot hold a connection open.

## Implementation Notes

Because asynchronous support is optional, clients must first verify via Query whether a server supports it before using asynchronous patterns. The Full Async mode in the request header instructs the server to respond asynchronously for all batch items, useful when even a single long-running item would otherwise block the connection. Cancelled asynchronous operations leave any partial server-side state unreported to the client.

## Related Concepts

See [Canceling Asynchronous Operations](canceling-asynchronous-operations.md), [Querying Outstanding Asynchronous Requests](querying-outstanding-asynchronous-requests.md), and [Full Async](full-async.md) for related operational patterns.
