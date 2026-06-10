---
title: Message Structure
category: ttlv
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4"]
source_section: "7.1"
status: draft
related: ["operations", "batch-item", "protocol-version", "ttlv-encoding"]
keywords: ["message structure", "request message", "response message", "header", "framing"]
---

# Message Structure

## Overview

The outermost framing of every KMIP exchange: a Request Message or Response
Message is one TTLV structure containing a header followed by one or more
[batch items](batch-item.md). Field order is fixed — everything appears in
the order the spec tables prescribe.

## Encoding (Tag / Type / Length / Value)

| Message | Tag | Contents |
|---|---|---|
| Request Message | `420078` | Request Header (`420077`) + Batch Item × N |
| Response Message | `42007B` | Response Header (`42007A`) + Batch Item × N |

The header field layouts (what goes in a request header vs a response
header) are detailed under [Operations (message format)](operations.md).

## Fields & Structure

Headers carry the per-message machinery —
[Protocol Version](protocol-version.md), options, identity, and
[Batch Count](batch-count.md) — while batch items carry the per-operation
payloads. Because the top-level structure declares its total length up
front, a reader can frame complete messages off a stream by reading the
8-byte tag/type/length prefix and then exactly that many bytes.
[Server-to-client operations](../operations/server-to-client/index.md) reuse
the request format with a few client-only header fields disallowed.

## Examples

The smallest useful request: Request Message { Request Header { Protocol
Version {1, 4}, Batch Count = 1 }, Batch Item { Operation = Query, Request
Payload { Query Function = Query Operations } } }.

## Related

[Operations (message format)](operations.md) · [Batch Item](batch-item.md) ·
[Protocol Version](protocol-version.md) ·
[TTLV Encoding](ttlv-encoding.md)
