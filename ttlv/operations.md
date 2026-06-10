---
title: Operations (Message Format)
category: ttlv
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "7.2"
status: draft
related: ["message-structure", "batch-item", "result-status", "authentication"]
keywords: ["request header", "response header", "header fields", "message format"]
---

# Operations (Message Format)

## Overview

Spec §7.2 pins down exactly which fields may appear in the four framing
structures — request/response header and request/response batch item — and
when each is required. This page summarizes the header layouts; the batch
item layouts live on [Batch Item](batch-item.md).

## Encoding (Tag / Type / Length / Value)

**Request Header** (`420077`), in order:

| Field | Required |
|---|---|
| [Protocol Version](protocol-version.md) | Yes |
| [Maximum Response Size](maximum-response-size.md) | No |
| [Client](client-correlation-value.md) / [Server Correlation Value](server-correlation-value.md) | No (1.4) |
| [Asynchronous Indicator](asynchronous-indicator.md) | No |
| [Attestation Capable Indicator](attestation-capable-indicator.md), Attestation Type(s) | No (1.2+) |
| [Authentication](authentication.md) | No |
| [Batch Error Continuation Option](batch-error-continuation-option.md) | No (default Stop) |
| [Batch Order Option](batch-order-option.md) | No (default False) |
| [Time Stamp](time-stamp.md) | No |
| [Batch Count](batch-count.md) | Yes |

**Response Header** (`42007A`), in order: Protocol Version (required),
[Time Stamp](time-stamp.md) (required), [Nonce](nonce.md) (no),
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

[Message Structure](message-structure.md) · [Batch Item](batch-item.md) ·
[Result Status](result-status.md)
