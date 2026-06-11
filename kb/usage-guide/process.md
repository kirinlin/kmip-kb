---
title: Process
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.36"
status: draft
related: ["synchronous-and-asynchronous-operations", "full-async"]
keywords: ["Process operation", "async escalation", "immediate response", "Asynchronous Correlation Value", "priority"]
---

# Process

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

The Process operation converts a previously submitted asynchronous operation from "do it eventually" to "do it now." It takes one or more Asynchronous Correlation Values and instructs the server to guarantee that subsequent Poll calls for those correlation values will no longer come back with a pending status.

## Guidance

Process is useful when circumstances change after an async operation was submitted: for example, a key pair creation that was submitted asynchronously becomes urgently needed because a compromise was reported in the interim. Issuing Process with the correlation value moves that creation to the front of the server's processing queue.

The server may respond to Process by raising the service priority of the targeted operations, or by any other means that satisfies the semantic: the next Poll will not return "Operation Pending." The server may return an error or a success for the original operation, but not "pending."

## Implementation Notes

Process does not override the Batch Order Option specified in the original batch header. If the original batch required in-order processing, that constraint still applies. Process affects when the server completes an operation, not the logical order of a batch.

## Related Concepts

See [Synchronous and Asynchronous Operations](synchronous-and-asynchronous-operations.md) and [Full Async](full-async.md).
