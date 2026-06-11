---
title: Result Status
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "9.19"
v1_source_section: "6.9"
status: draft
related: ["result-reason", "result-message", "batch-error-continuation-option"]
keywords: ["result status", "success", "operation failed", "operation pending", "operation undone"]
tag_hex: "42007F"
xml_element: "ResultStatus"
---

# Result Status

## Overview

The verdict on each batch item — the one field present in every response
item. Four outcomes:

| Value | Meaning |
|---|---|
| Success (0) | Done as requested. |
| Operation Failed (1) | Did not happen; see [Result Reason](result-reason.md). |
| Operation Pending (2) | Running asynchronously; claim the outcome later via the [Asynchronous Correlation Value](asynchronous-correlation-value.md). |
| Operation Undone (3) | It succeeded, then was rolled back because a later item in an `Undo` batch failed. |

## Encoding (Tag / Type / Length / Value)

Tag `42007F`, Enumeration, in every response batch item.

## Fields & Structure

Failure obliges the server to add a Result Reason (and permits a
[Result Message](result-message.md)); Pending obliges it to add the
asynchronous correlation value; Undone appears only when the request chose
the `Undo` [batch error continuation](batch-error-continuation-option.md).
A successful item instead carries its Response Payload.

## Examples

A three-item Undo batch where item 2 fails: item 1 reports Operation Undone,
item 2 Operation Failed with its reason, item 3 is never attempted.

## Related

[Result Reason](result-reason.md) · [Result Message](result-message.md) ·
[Error Handling](../concepts/error-handling.md)
