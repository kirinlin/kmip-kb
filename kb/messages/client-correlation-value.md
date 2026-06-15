---
title: Client Correlation Value
category: messages
spec_version: "2.1"
spec_versions: ["1.4", "2.0", "2.1"]
source_section: "9.9"
v1_source_section: "6.18"
status: reviewed
related: ["server-correlation-value", "correlation-value", "message-structure"]
keywords: ["client correlation value", "request tracing", "logging", "observability"]
tag_hex: "420105"
xml_element: "ClientCorrelationValue"
---

# Client Correlation Value

## Overview

A 1.4 observability field: a client-chosen string in the message header that
tags the exchange for tracing — a transaction ID, a tenant tag, a
request-chain identifier. Servers are encouraged to log it, turning
cross-system debugging from log archaeology into a string match.

## Encoding (Tag / Type / Length / Value)

Tag `420105`, Text String, in the header. Need not be unique.

## Fields & Structure

Direction follows who initiates: the client puts it in *request* headers of
normal operations, and it appears in the client's *response* headers for
[server-to-client](../operations/server-to-client/index.md) operations. It
carries no protocol semantics — purely for correlation across logs, unlike
the [streaming](../structures/correlation-value.md) and
[asynchronous](asynchronous-correlation-value.md) correlation values, which
drive protocol state.

## Examples

An application sets Client Correlation Value = `"order-svc:txn-58122"` on
every KMIP call made while processing one business transaction; when a
decrypt fails, the server log line is findable by that string.

## Related

[Server Correlation Value](server-correlation-value.md) ·
[Message Structure](message-structure.md)
