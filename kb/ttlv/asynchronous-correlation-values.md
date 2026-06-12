---
title: Asynchronous Correlation Values
category: ttlv
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "7.1"
status: reviewed
related: ["asynchronous-request", "asynchronous-correlation-value", "query-asynchronous-requests", "message-structure"]
keywords: ["asynchronous", "correlation values", "pending operations", "async batch", "polling"]
---

# Asynchronous Correlation Values

## Overview

When a client submits a batch request and one or more operations are processed asynchronously, the server issues a unique byte-string handle — an Asynchronous Correlation Value — for each pending item. The Asynchronous Correlation Values structure bundles a set of these handles into a single container, making it possible to reference or poll multiple outstanding async operations in one message.

This structure appears in two main places: in the response when operations have been accepted for background processing (advertising which items are still pending), and in the [Query Asynchronous Requests](../operations/query-asynchronous-requests.md) operation where the client presents the handles it received earlier to ask for status updates.

## Encoding (Tag / Type / Length / Value)

Asynchronous Correlation Values encodes as a Structure containing one or more Asynchronous Correlation Value byte strings.

| Field | Tag | Type | Required |
|---|---|---|---|
| Asynchronous Correlation Value | `420006` | Byte String | One or more |

The inner items repeat — one per pending operation being referenced. Their ordering within the structure is not semantically significant.

## Fields & Structure

Each child element is an opaque, server-assigned byte string. Clients must treat correlation values as uninterpreted handles and must not rely on any particular encoding, length, or internal structure. The server defines their scope and lifetime; typically they are valid only within the session that generated them.

There is no fixed upper bound on how many values the structure may carry. In practice the count equals the number of batch items that are in a pending asynchronous state at the time the structure is generated.

## Examples

A client submits a five-item batch. Three items complete synchronously; two are accepted asynchronously. The server returns an Asynchronous Correlation Values structure holding two byte-string handles. The client stores them and later sends a Query Asynchronous Requests payload that includes both handles, asking the server for the current Processing Stage of each pending operation.

## Related

[Asynchronous Correlation Value](asynchronous-correlation-value.md) · [Asynchronous Request](asynchronous-request.md) · [Query Asynchronous Requests](../operations/query-asynchronous-requests.md) · [Message Structure](message-structure.md)
