---
title: Result Reason
category: messages
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "9.18"
v1_source_section: "6.10"
status: reviewed
related: ["result-status", "result-message", "batch-item"]
keywords: ["result reason", "error code", "item not found", "permission denied", "general failure", "42007E", "ResultReason"]
tag_hex: "42007E"
xml_text: "ResultReason"
tag_type: "Enumeration"
---

# Result Reason

## Overview

The machine-readable *why* behind a failed batch item — mandatory whenever
[Result Status](result-status.md) is Operation Failed, optional decoration
on success. The spec fixes which reason each error condition maps to, per
operation — v2.x embeds these rules in each operation's definition; v1.x
collected them in §11 — so clients can branch on it reliably.

## Encoding (Tag / Type / Length / Value)

Tag `42007E`, Enumeration. The 1.4 value set:

Item Not Found (1) · Response Too Large (2) · Authentication Not Successful
(3) · Invalid Message (4) · Operation Not Supported (5) · Missing Data (6) ·
Invalid Field (7) · Feature Not Supported (8) · Operation Canceled By
Requester (9) · Cryptographic Failure (A) · Illegal Operation (B) ·
Permission Denied (C) · Object Archived (D) · Index Out of Bounds (E) ·
Application Namespace Not Supported (F) · Key Format Type Not Supported
(10) · Key Compression Type Not Supported (11) · Encoding Option Error
(12, 1.1+) · Key Value Not Present (13, 1.2+) · Attestation Required (14,
1.2+) · Attestation Failed (15, 1.2+) · Sensitive (16, 1.4) · Not
Extractable (17, 1.4) · Object Already Exists (18, 1.4) · General Failure
(100).

## Fields & Structure

Highlights of the semantics: *Missing Data* = a required field was absent;
*Invalid Field* = present but bad; *Illegal Operation* = valid request,
impossible with those parameters; *Index Out of Bounds* = more attribute
instances than the server allows; *Object Archived* = run
[Recover](../operations/recover.md) first; the 1.4 trio maps to the
[Sensitive](../attributes/sensitive.md) /
[Extractable](../attributes/extractable.md) controls and to
[Import](../operations/import.md) collisions. *General Failure* is the
catch-all of last resort.

## Examples

A Get for a plaintext copy of a Sensitive-flagged key fails with Result
Status = Operation Failed, Result Reason = Sensitive; retried with a
[Key Wrapping Specification](../structures/key-wrapping-specification.md) it succeeds.

## Related

[Result Status](result-status.md) · [Result Message](result-message.md) ·
[Error Handling](../concepts/error-handling.md)
