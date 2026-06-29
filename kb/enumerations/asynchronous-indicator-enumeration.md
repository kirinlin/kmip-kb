---
title: Asynchronous Indicator Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.3"
status: reviewed
related: ["asynchronous-request", "query-asynchronous-requests", "cancel", "poll", "batch-error-continuation-option-enumeration"]
keywords: ["asynchronous", "async", "synchronous", "correlation value", "batch", "non-blocking", "420007", "AsynchronousIndicator"]
tag_hex: "420007"
xml_text: "AsynchronousIndicator"
tag_type: "Enumeration"
---

# Asynchronous Indicator Enumeration

## Overview

The Asynchronous Indicator enumeration controls whether a particular batch item should be processed asynchronously or synchronously. When a client submits a potentially long-running operation such as a cryptographic key generation, it may prefer not to block waiting for completion. Setting the indicator to the asynchronous value tells the server to queue the work and immediately return a correlation value that the client can later use to retrieve the result. This enumeration applies per-item within a batch, giving fine-grained control over which operations block and which do not.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Mandatory | `00000001` | `Mandatory` |  |
| Optional | `00000002` | `Optional` |  |
| Prohibited | `00000003` | `Prohibited` |  |

## Examples

A client generating a large RSA key pair over a slow HSM might specify **Asynchronous** on the Create Key Pair batch item, receive a correlation value immediately, and poll for the result once processing completes — freeing the client thread to handle other work in the interim.

## Related

- [Asynchronous Request structure](../structures/asynchronous-request.md) — carries the Asynchronous Correlation Value
- [Query Asynchronous Requests operation](../operations/query-asynchronous-requests.md) — retrieves the result of a pending async operation
- [Cancel operation](../operations/cancel.md) — cancels a queued asynchronous operation
- [Poll operation](../operations/poll.md) — server-push notification of async completion
- [Batch Error Continuation Option Enumeration](batch-error-continuation-option-enumeration.md) — governs batch-level error handling
