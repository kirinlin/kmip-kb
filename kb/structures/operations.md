---
title: Operations (Message Format)
category: structures
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "7.25"
v1_source_section: "7.2"
status: reviewed
related: ["message-structure", "batch-item", "result-status", "authentication"]
keywords: ["request header", "response header", "header fields", "message format"]
---

# Operations (Message Format)

## Overview

The spec's message-format sections (v2.1 §8.1–§8.6; v1.x §7) pin down exactly
which fields may appear in the four framing structures — request/response
header and request/response batch item — and
when each is required. This page summarizes the header layouts; the batch
item layouts live on [Batch Item](../messages/batch-item.md).

## Encoding (Tag / Type / Length / Value)

**Request Header** (`420077`, `RequestHeader`), in order:

| Field | Tag | XML Text | Required |
|---|---|---|---|
| [Protocol Version](../messages/protocol-version.md) | `420069` | `ProtocolVersion` | Yes |
| [Maximum Response Size](../messages/maximum-response-size.md) | `420050` | `MaximumResponseSize` | No |
| [Client](../messages/client-correlation-value.md) / [Server Correlation Value](../messages/server-correlation-value.md) |  |  | No (1.4) |
| [Asynchronous Indicator](../messages/asynchronous-indicator.md) | `420007` | `AsynchronousIndicator` | No |
| [Attestation Capable Indicator](../messages/attestation-capable-indicator.md), Attestation Type(s) |  |  | No (1.2+) |
| [Authentication](../messages/authentication.md) | `42000C` | `Authentication` | No |
| [Batch Error Continuation Option](../messages/batch-error-continuation-option.md) | `42000E` | `BatchErrorContinuationOption` | No (default Stop) |
| [Batch Order Option](../messages/batch-order-option.md) | `420010` | `BatchOrderOption` | No (default False) |
| [Time Stamp](../messages/time-stamp.md) | `420092` | `TimeStamp` | No |
| [Batch Count](../messages/batch-count.md) | `42000D` | `BatchCount` | Yes |

**Response Header** (`42007A`, `ResponseHeader`), in order: Protocol Version (required),
[Time Stamp](../messages/time-stamp.md) (required), [Nonce](../messages/nonce.md) (no),
Attestation Type(s) (required in an `Attestation Required` failure when the
client declared capability), Client/Server Correlation Value (no, 1.4),
Batch Count (required).

## Fields & Structure

A batched request whose client allows async may receive a mixed response —
some items final, some `Operation Pending`. Field order is normative
everywhere; receivers may rely on it.

## Examples

A header exercising the options: Protocol Version {1, 4}, Maximum Response
Size 65536, Asynchronous Indicator True, Authentication {username
credential}, Batch Error Continuation Option Continue, Batch Order Option
True, Batch Count 4.

## Related

[Message Structure](../messages/message-structure.md) · [Batch Item](../messages/batch-item.md) ·
[Result Status](../messages/result-status.md)
