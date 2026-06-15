---
title: Server Correlation Value
category: messages
spec_version: "2.1"
spec_versions: ["1.4", "2.0", "2.1"]
source_section: "9.10"
v1_source_section: "6.19"
status: reviewed
related: ["client-correlation-value", "correlation-value", "message-structure"]
keywords: ["server correlation value", "request ID", "audit", "logging", "420106", "ServerCorrelationValue"]
tag_hex: "420106"
xml_text: "ServerCorrelationValue"
---

# Server Correlation Value

## Overview

The server-side twin of the
[Client Correlation Value](client-correlation-value.md) (1.4): a string the
server mints per exchange — ideally globally unique — and logs, giving every
request a citable server-side identifier for audits and support cases.

## Encoding (Tag / Type / Length / Value)

Tag `420106`, Text String, in the header.

## Fields & Structure

Appears in *response* headers of normal client-initiated operations, and in
the server's *request* headers for
[server-to-client](../operations/server-to-client/index.md) operations. All
SHOULD-level: a server may omit it, but one that emits and logs unique
values gives operators a request ID to quote, much like an HTTP `X-Request-Id`.

## Examples

A failed Re-key response carries Server Correlation Value =
`"kms-prod-3:9f31c2"`; the client surfaces it in its error report, and the
server operator jumps straight to the relevant log entries.

## Related

[Client Correlation Value](client-correlation-value.md) ·
[Message Structure](message-structure.md)
