---
title: Full Async
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.34"
status: draft
related: ["synchronous-and-asynchronous-operations", "canceling-asynchronous-operations"]
keywords: ["Full Async", "mandatory async", "Asynchronous Correlation Value", "IoT", "batch", "pending status"]
---

# Full Async

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

Setting the "Mandatory Asynchronous" option in the Request Header instructs the server to respond to all batch items with Asynchronous Correlation Values (i.e., treat every item as if it were an asynchronous request). This is useful in environments — particularly IoT — where a client cannot hold a connection open long enough to wait for the server to process a long-running batch item.

## Guidance

Full Async allows a client to submit a complete batch of operations and immediately disconnect, then reconnect later to poll for each correlation value separately. This decouples the submission latency from the processing latency, which is important for resource-constrained devices or high-latency networks.

## Implementation Notes

Not all servers support asynchronous operations (it is optional in the protocol). Before using Full Async, clients should confirm via Query that the server supports asynchronous operation. When a server does not support asynchronous operations, the "Mandatory Asynchronous" option will cause the request to fail.

## Related Concepts

See [Synchronous and Asynchronous Operations](synchronous-and-asynchronous-operations.md) for the fundamental async model.
