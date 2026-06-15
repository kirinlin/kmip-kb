---
title: Asynchronous Request
category: structures
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "7.2"
status: reviewed
related: ["asynchronous-correlation-values", "asynchronous-correlation-value", "query-asynchronous-requests", "message-structure", "batch-item"]
keywords: ["asynchronous", "async request", "processing stage", "correlation value", "pending"]
---

# Asynchronous Request

## Overview

An Asynchronous Request structure pairs a single Asynchronous Correlation Value with a Processing Stage Enumeration to describe where a previously submitted asynchronous operation currently stands. It is the per-operation unit of status that a Query Asynchronous Requests response assembles into a list — one Asynchronous Request entry per outstanding handle the client asked about.

The Processing Stage indicates whether the operation is still being executed (Pending), has finished successfully (Completed), was cancelled (Cancelled), or encountered another terminal condition. Clients loop over these entries to determine which operations they can act on and which still require waiting.

## Encoding (Tag / Type / Length / Value)

Asynchronous Request encodes as a Structure.

| Field | Tag | XML Element | Type | Required |
|---|---|---|---|---|
| Asynchronous Correlation Value | `420006` | `AsynchronousCorrelationValue` | Byte String | Yes |
| Processing Stage | `42006C` | `ProcessingStage` | Enumeration | Yes |

Both fields are mandatory. The correlation value links the status entry back to a specific batch item; the processing stage communicates the outcome or current state.

## Fields & Structure

**Asynchronous Correlation Value** is the opaque byte-string handle the server assigned when the operation was first accepted. It identifies which pending item this status entry describes.

**Processing Stage** is an enumeration whose principal values are:

- *Completed* — the operation finished and its result is available.
- *Pending* — the operation is still being processed; the client should poll again later.
- *Cancelled* — the operation was cancelled before it could finish.

Servers may define additional vendor extension values for intermediate states.

When the stage is Completed, the actual result of the operation (the response payload that would have been returned synchronously) is retrieved through a separate mechanism — the server holds it until the client fetches it or it expires.

## Examples

A client receives a correlation value `0xA3F1...` after submitting an asynchronous Create. On a subsequent Query Asynchronous Requests call it includes that value. The response contains an Asynchronous Request entry with the same correlation value and Processing Stage = Pending, indicating the key generation is still in progress. On the next poll the stage returns Completed, and the client can now retrieve the created object's Unique Identifier.

## Related

[Asynchronous Correlation Values](asynchronous-correlation-values.md) · [Asynchronous Correlation Value](../messages/asynchronous-correlation-value.md) · [Query Asynchronous Requests](../operations/query-asynchronous-requests.md) · [Batch Item](../messages/batch-item.md)
