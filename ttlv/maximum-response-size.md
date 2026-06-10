---
title: Maximum Response Size
category: ttlv
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4"]
source_section: "6.3"
status: draft
related: ["message-structure", "result-reason", "batch-count"]
keywords: ["maximum response size", "response too large", "buffer limit", "constrained client"]
---

# Maximum Response Size

## Overview

A request-header field by which the client declares the biggest response (in
bytes) it can absorb — the protocol's accommodation for small-footprint
clients with fixed buffers. A server whose answer would not fit must fail
with `Response Too Large` instead of sending it.

## Encoding (Tag / Type / Length / Value)

Tag `420050`, Integer, in the request header only.

## Fields & Structure

Optional; meant for requests that can plausibly return large replies
([Locate](../operations/locate.md) over many objects,
[Query](../operations/query.md), a [Get](../operations/get.md) of a large
certificate chain). The error response itself must, of course, fit within
the declared limit — one reason error responses are minimal.

## Examples

An embedded client with a 8 KiB receive buffer sends Maximum Response Size =
8192 on every Query; against a server with hundreds of extensions, the Query
fails fast with `Response Too Large` rather than overflowing the client.

## Related

[Message Structure](message-structure.md) ·
[Result Reason](result-reason.md) ·
[Error Handling](../concepts/error-handling.md)
