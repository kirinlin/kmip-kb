---
title: Messages
category: index
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: ""
status: reviewed
related: ["message-structure", "batch-item", "protocol-version", "credential"]
keywords: ["messages", "request", "response", "message header", "batch", "protocol version"]
---

# Messages

The KMIP request/response envelope and the fields that make it up: how a message
is framed, batched, authenticated, versioned, and how results are reported.
Covers v2.1 §8 (Messages) and §9 (Message Data Structures); the v1.x message
contents/format sections (§6–§7) map here too. The composite payloads carried
inside live under [Data Structures](../structures/index.md), and the byte-level
[TTLV encoding](../encoding/index.md) underlies all of it.

## Framing

- [Message Structure](message-structure.md) — request/response message, header,
  and batch item layout.
- [Batch Item](batch-item.md) · [Batch Count](batch-count.md) ·
  [Unique Batch Item ID](unique-batch-item-id.md) ·
  [Batch Order Option](batch-order-option.md) ·
  [Batch Error Continuation Option](batch-error-continuation-option.md)

## Header fields

- [Protocol Version](protocol-version.md) · [Operation](operation.md) ·
  [Maximum Response Size](maximum-response-size.md) · [Time Stamp](time-stamp.md)
- [Asynchronous Indicator](asynchronous-indicator.md) ·
  [Asynchronous Correlation Value](asynchronous-correlation-value.md)
- [Client Correlation Value](client-correlation-value.md) /
  [Server Correlation Value](server-correlation-value.md) (1.4)
- [Message Extension](message-extension.md)

## Authentication

- [Authentication](authentication.md) · [Credential](credential.md) ·
  [Nonce](nonce.md) (1.2+) ·
  [Attestation Capable Indicator](attestation-capable-indicator.md) (1.2+)

## Results

- [Result Status](result-status.md) · [Result Reason](result-reason.md) ·
  [Result Message](result-message.md)
