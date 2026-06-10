---
title: Batch Item
category: ttlv
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.15"
status: draft
related: ["batch-count", "operation", "message-structure", "operations"]
keywords: ["batch item", "request payload", "response payload", "message body"]
---

# Batch Item

## Overview

The unit of work inside a message: each batch item is one operation request
or one operation result. Every message body is a sequence of these — usually
one, but up to whatever the server tolerates.

## Encoding (Tag / Type / Length / Value)

Structure, tag `42000F`. Request-side contents:

| Field | Required |
|---|---|
| [Operation](operation.md) | Yes |
| [Unique Batch Item ID](unique-batch-item-id.md) | When Batch Count > 1 |
| Request Payload (`420079`) | Yes — contents defined per operation |
| [Message Extension](message-extension.md) | No |

Response-side contents:

| Field | Required |
|---|---|
| Operation | Echoed when the request had one |
| Unique Batch Item ID | Echoed when present in the request |
| [Result Status](result-status.md) | Yes |
| [Result Reason](result-reason.md) | On failure |
| [Result Message](result-message.md) | No |
| [Asynchronous Correlation Value](asynchronous-correlation-value.md) | When status is Pending |
| Response Payload (`42007C`) | When not a failure |
| Message Extension | No |

## Fields & Structure

The payloads are where each operation's fields (documented across
[operations/](../operations/index.md)) actually live. Items in one batch
share the header's authentication and options, and can chain through the ID
Placeholder when executed [in order](batch-order-option.md).

## Examples

A Get request batch item: Operation = Get, Request Payload { Unique
Identifier = `"f0c1..."` }. Its response item: Operation = Get, Result
Status = Success, Response Payload { Object Type, Unique Identifier, the
Symmetric Key object }.

## Related

[Batch Count](batch-count.md) · [Operation](operation.md) ·
[Message Structure](message-structure.md) ·
[Operations (message format)](operations.md)
