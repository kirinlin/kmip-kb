---
title: Batch Item
category: messages
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "9.7"
v1_source_section: "6.15"
status: reviewed
related: ["batch-count", "operation", "message-structure", "operations"]
keywords: ["batch item", "request payload", "response payload", "message body", "42000F", "BatchItem"]
tag_hex: "42000F"
xml_text: "BatchItem"
tag_type: "Structure"
---

# Batch Item

## Overview

The unit of work inside a message: each batch item is one operation request
or one operation result. Every message body is a sequence of these — usually
one, but up to whatever the server tolerates.

## Encoding (Tag / Type / Length / Value)

Structure, tag `42000F`. Request-side contents:

| Field | Tag | XML Text | Required |
|---|---|---|---|
| [Operation](operation.md) | `42005C` | `Operation` | Yes |
| [Unique Batch Item ID](unique-batch-item-id.md) | `420093` | `UniqueBatchItemID` | When Batch Count > 1 |
| Request Payload (`420079`) | `420079` | `RequestPayload` | Yes — contents defined per operation |
| [Message Extension](message-extension.md) | `420051` | `MessageExtension` | No |

Response-side contents:

| Field | Tag | XML Text | Required |
|---|---|---|---|
| Operation | `42005C` | `Operation` | Echoed when the request had one |
| Unique Batch Item ID | `420093` | `UniqueBatchItemID` | Echoed when present in the request |
| [Result Status](result-status.md) | `42007F` | `ResultStatus` | Yes |
| [Result Reason](result-reason.md) | `42007E` | `ResultReason` | On failure |
| [Result Message](result-message.md) | `42007D` | `ResultMessage` | No |
| [Asynchronous Correlation Value](asynchronous-correlation-value.md) | `420006` | `AsynchronousCorrelationValue` | When status is Pending |
| Response Payload (`42007C`) | `42007C` | `ResponsePayload` | When not a failure |
| Message Extension | `420051` | `MessageExtension` | No |

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
[Operations (message format)](../structures/operations.md)
