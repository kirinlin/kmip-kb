---
title: Result Message
category: messages
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "9.17"
v1_source_section: "6.11"
status: reviewed
related: ["result-status", "result-reason"]
keywords: ["result message", "error text", "diagnostics", "logging", "42007D", "ResultMessage"]
tag_hex: "42007D"
xml_text: "ResultMessage"
---

# Result Message

## Overview

The human-readable companion to [Result Reason](result-reason.md): free-form
text a server may attach to a response batch item to explain a failure in
words — for operator logs, support tickets, end-user display.

## Encoding (Tag / Type / Length / Value)

Tag `42007D`, Text String (UTF-8, like all KMIP strings).

## Fields & Structure

Optional, and meaningful mainly on non-success statuses. Its content is
entirely server-defined — two servers can describe the same failure
completely differently — which is exactly why client *logic* must key off
Result Reason and treat this field as display-only.

## Examples

Result Status = Operation Failed, Result Reason = Invalid Field, Result
Message = `"Cryptographic Length 137 is not valid for algorithm AES"` — the
reason drives the client's error path, the message lands in the log.

## Related

[Result Status](result-status.md) · [Result Reason](result-reason.md) ·
[Error Handling](../concepts/error-handling.md)
