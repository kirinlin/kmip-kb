---
title: Processing Stage Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "11.40"
status: reviewed
related: ["asynchronous-request", "asynchronous-correlation-values", "query-asynchronous-requests"]
keywords: ["processing stage", "async status", "asynchronous", "pending", "completed", "cancelled", "420175", "ProcessingStage"]
tag_hex: "420175"
xml_text: "ProcessingStage"
tag_type: "Enumeration"
---

# Processing Stage Enumeration

## Overview

The Processing Stage enumeration reports the current state of an asynchronous operation when a client calls [Query Asynchronous Requests](../operations/query-asynchronous-requests.md). The asynchronous execution model lets a server acknowledge receipt of an operation immediately and process it in the background; the Processing Stage tells the polling client how far along the operation is.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Submitted | `00000001` | `Submitted` |  |
| In Process | `00000002` | `InProcess` |  |
| Completed | `00000003` | `Completed` |  |

- **Server Processing**: The server has accepted the operation and is currently working on it. The client should poll again later.
- **Completed**: The operation has finished. The response for the original operation is available in the [Asynchronous Request](../structures/asynchronous-request.md) structure, and the client can retrieve it. Once retrieved, the correlation value is typically invalidated.
- **Cancelled**: The operation was stopped before completion, either because the client issued a Cancel or the server aborted it. No result is available.

## Examples

A client that submitted a large key-generation batch operation polls with Query Asynchronous Requests and receives **Server Processing**, indicating the keys are still being generated. After a few seconds it polls again and receives **Completed**, at which point it fetches the key identifiers from the response.

## Related

[Asynchronous Request](../structures/asynchronous-request.md) · [Asynchronous Correlation Values](../structures/asynchronous-correlation-values.md) · [Query Asynchronous Requests](../operations/query-asynchronous-requests.md)
