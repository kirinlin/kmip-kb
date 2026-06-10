---
title: Error Handling
category: concept
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "11"
status: draft
related: ["result-status", "result-reason", "result-message", "batch-error-continuation-option", "batch-item"]
keywords: ["error handling", "result status", "result reason", "failure", "batch errors", "invalid message"]
---

# Error Handling

## Overview

KMIP reports errors per batch item, not per connection. Every response batch
item carries a [Result Status](../ttlv/result-status.md) (Success, Operation
Failed, Operation Pending, or Operation Undone); failures additionally carry
a machine-readable [Result Reason](../ttlv/result-reason.md) and may carry a
human-readable [Result Message](../ttlv/result-message.md). Section 11 of the
spec is a catalogue that pins down exactly which Result Reason a server
returns for each error condition, operation by operation — the goal is that
two conforming servers fail the same bad request the same way.

## Details

The general rules (spec §11.1) cover conditions any message can hit:

- A request whose **major protocol version** differs from the server's, or a
  message that cannot be parsed at all, gets a response with a header and a
  single batch item that has no Operation, Result Status `Operation Failed`,
  and reason `Invalid Message`. A minor-version mismatch is benign: unknown
  fields from a newer minor version are ignored.
- Duplicate fields and malformed payloads → `Invalid Message`; an unknown
  field at the same version → `Invalid Field`.
- Policy violations → `Permission Denied`; unimplemented operations →
  `Operation Not Supported`; an unsupported optional feature →
  `Feature Not Supported`.
- A response that would exceed the request's
  [Maximum Response Size](../ttlv/maximum-response-size.md) →
  `Response Too Large`.
- A critical [Message Extension](../ttlv/message-extension.md) the receiver
  does not understand → `Feature Not Supported`.
- Attestation cases (1.2+): missing attestation data yields
  `Attestation Required` if the client declared itself attestation-capable,
  otherwise `Permission Denied`; invalid evidence yields `Attestation Failed`.

For multi-item batches, the
[Batch Error Continuation Option](../ttlv/batch-error-continuation-option.md)
governs what happens after the first failure: `Stop` (default) returns
results for the items already done and drops the rest; `Continue` processes
every item regardless; `Undo` rolls back completed items, which then report
the `Operation Undone` status. Versions 1.0–1.4 grew the Result Reason list
over time (1.4 added reasons such as `Sensitive`, `Not Extractable`, and
`Object Already Exists`), so the reasons a server can emit depend on the
negotiated version.

## Implications for Implementers

- Clients should branch on Result Reason, not on Result Message text — the
  message is free-form and server-specific.
- Servers must pick the section-11 reason for a given failure rather than
  defaulting everything to `General Failure`; test suites check this.
- Only advertise `Undo` support if you can genuinely roll back partial
  batches; servers that cannot must reject requests asking for it.
- An asynchronous flow ends in the same statuses: `Operation Pending` plus an
  [Asynchronous Correlation Value](../ttlv/asynchronous-correlation-value.md)
  now, the final status later via [Poll](../operations/poll.md).

## Related Concepts

[Result Status](../ttlv/result-status.md) ·
[Result Reason](../ttlv/result-reason.md) ·
[Result Message](../ttlv/result-message.md) ·
[Batch Error Continuation Option](../ttlv/batch-error-continuation-option.md)
