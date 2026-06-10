---
title: TTLV & Message Structures
category: index
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: ""
status: draft
related: ["ttlv-encoding", "message-structure", "key-block", "batch-item"]
keywords: ["TTLV", "base objects", "message contents", "message format", "encoding"]
---

# TTLV & Message Structures

Everything about KMIP's wire shape: the binary encoding (§9), the base
objects that compose managed objects and payloads (§2.1), and the message
contents/format machinery (§6–§7).

## Encoding & framing

- [TTLV Encoding](ttlv-encoding.md) — the Tag/Type/Length/Value scheme
  itself.
- [Message Structure](message-structure.md) — request/response framing.
- [Operations (message format)](operations.md) — header and field layouts.
- [Batch Item](batch-item.md) · [Batch Count](batch-count.md) ·
  [Unique Batch Item ID](unique-batch-item-id.md) ·
  [Batch Order Option](batch-order-option.md) ·
  [Batch Error Continuation Option](batch-error-continuation-option.md)

## Key material containers (§2.1)

- [Key Block](key-block.md) → [Key Value](key-value.md) →
  [Transparent Key Structures](transparent-key-structures.md)
- [Key Wrapping Data](key-wrapping-data.md) ·
  [Key Wrapping Specification](key-wrapping-specification.md)

## Attribute & identity plumbing

- [Attribute](attribute.md) ·
  [Template-Attribute Structures](template-attribute-structures.md)
- [Authentication](authentication.md) · [Credential](credential.md) ·
  [Nonce](nonce.md) (1.2+) ·
  [Attestation Capable Indicator](attestation-capable-indicator.md) (1.2+)

## Header fields & results

- [Protocol Version](protocol-version.md) · [Operation](operation.md) ·
  [Maximum Response Size](maximum-response-size.md) ·
  [Time Stamp](time-stamp.md)
- [Result Status](result-status.md) · [Result Reason](result-reason.md) ·
  [Result Message](result-message.md)
- [Asynchronous Indicator](asynchronous-indicator.md) ·
  [Asynchronous Correlation Value](asynchronous-correlation-value.md)
- [Client](client-correlation-value.md) /
  [Server Correlation Value](server-correlation-value.md) (1.4)
- [Message Extension](message-extension.md) ·
  [Extension Information](extension-information.md) (1.1+)

## Cryptographic-service payload fields (1.2+)

- [Data](data.md) · [Data Length](data-length.md) ·
  [Signature Data](signature-data.md) · [MAC Data](mac-data.md)
- Streaming (1.3+): [Correlation Value](correlation-value.md) ·
  [Init Indicator](init-indicator.md) ·
  [Final Indicator](final-indicator.md)
- AEAD (1.4):
  [Authenticated Encryption Additional Data](authenticated-encryption-additional-data.md) ·
  [Authenticated Encryption Tag](authenticated-encryption-tag.md)

## Discovery structures (1.3+)

- [RNG Parameters](rng-parameters.md) ·
  [Profile Information](profile-information.md) ·
  [Validation Information](validation-information.md) ·
  [Capability Information](capability-information.md)
