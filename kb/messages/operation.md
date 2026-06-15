---
title: Operation
category: messages
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "9.15"
v1_source_section: "6.2"
status: reviewed
related: ["batch-item", "operations", "message-structure"]
keywords: ["operation field", "operation enumeration", "batch item", "request type", "42005C", "Operation"]
tag_hex: "42005C"
xml_text: "Operation"
---

# Operation

## Overview

The field in each [batch item](batch-item.md) that says *which* operation the
item performs — the dispatcher key for the whole protocol. The request
payload that follows is interpreted entirely according to this value.

## Encoding (Tag / Type / Length / Value)

Tag `42005C`, Enumeration. The Operation enumeration assigns a value to every
operation in the spec's operations chapters (v2.1 §6.1 client / §6.2
server-to-client; v1.x §4 / §5) — Create = 1, Create Key Pair = 2, Register = 3,
Re-key = 4, ... through the 1.2 cryptographic services, up to Export (1.4)
and Import (1.4) — plus the server-to-client Notify/Put/Query values.

## Fields & Structure

Required in every request batch item. In response batch items it must echo
the request's value when present; the one case it is omitted is the
cannot-even-parse error response (see
[error handling](../concepts/error-handling.md)). Servers advertise their
supported subset through [Query](../operations/query.md) (Query Operations).

## Examples

A batch item performing a Get carries Operation = 10 (Get) followed by a
Request Payload containing the Unique Identifier.

## Related

[Batch Item](batch-item.md) · [Operations (message format)](../structures/operations.md) ·
[operations/ index](../operations/index.md)
