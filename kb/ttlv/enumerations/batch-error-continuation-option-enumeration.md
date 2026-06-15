---
title: Batch Error Continuation Option Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.5"
status: reviewed
related: ["result-status-enumeration", "result-reason-enumeration", "asynchronous-indicator-enumeration"]
keywords: ["batch", "error handling", "continue", "stop", "undo", "rollback", "batch item", "request header", "42000E", "BatchErrorContinuationOption"]
tag_hex: "42000E"
xml_text: "BatchErrorContinuationOption"
---

# Batch Error Continuation Option Enumeration

## Overview

The Batch Error Continuation Option enumeration, carried in the Request Header, governs what the KMIP server should do when it encounters a failure partway through processing a multi-item batch. KMIP allows a single request message to contain multiple operations — for example, creating a key and immediately activating it. If the first operation succeeds but the second fails, the server needs to know whether to keep going, stop immediately, or attempt to undo the work already done. This enumeration provides those three modes.

## Fields & Structure

| Value | Hex | XML Text | Description |
|---|---|---|---|
| Continue | `0x00000001` | `Continue` |  |
| Stop | `0x00000002` | `Stop` |  |
| Undo | `0x00000003` | `Undo` |  |

- **Continue**: The server processes all batch items regardless of individual failures. Each failed item returns its own error result, but subsequent items are still attempted. Useful when the operations are logically independent and partial success is acceptable.
- **Stop**: The server halts processing as soon as it encounters a failed item. Operations that have already been completed remain committed; items after the failure are not attempted. The response includes results only for items that were actually processed.
- **Undo**: The server attempts to roll back any operations that succeeded before the failure was encountered, then stops. This provides a best-effort transactional semantic. Note that not all operations can be reversed by the server, and the undo is advisory rather than a guaranteed atomic transaction.

## Examples

A provisioning workflow that creates a key pair, registers a certificate, and links the two objects would typically use **Stop** — if the certificate registration fails, there is no point activating the keys, and the partial state should be left for the client to resolve rather than continuing blindly.

## Related

- [Result Status Enumeration](result-status-enumeration.md) — indicates per-item success or failure
- [Result Reason Enumeration](result-reason-enumeration.md) — detailed error reason for each failed batch item
- [Asynchronous Indicator Enumeration](asynchronous-indicator-enumeration.md) — per-item async control, complementary to batch-level error handling
