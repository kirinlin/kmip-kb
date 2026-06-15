---
title: Protocol Version
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "9.16"
v1_source_section: "6.1"
status: reviewed
related: ["message-structure", "discover-versions"]
keywords: ["protocol version", "version negotiation", "major minor", "backward compatibility"]
tag_hex: "420069"
xml_element: "ProtocolVersion"
---

# Protocol Version

## Overview

The version stamp at the top of every request and response header, ensuring
both sides interpret the message the same way. KMIP's compatibility contract
hangs on it: implementations must remain backward compatible *within* a
major version (a 2.1 server must serve 2.0 requests; a 1.4 server must serve
1.0 requests), while compatibility across major versions is optional.

## Encoding (Tag / Type / Length / Value)

Structure, tag `420069`:

| Field | Tag | XML Element | Type |
|---|---|---|---|
| Protocol Version Major | `42006A` | `ProtocolVersionMajor` | Integer |
| Protocol Version Minor | `42006B` | `ProtocolVersionMinor` | Integer |

## Fields & Structure

For these spec families: Major = 2, Minor = 0–1 (baseline) or Major = 1,
Minor = 0–4. A major-version mismatch is a
hard error (`Invalid Message`, see
[error handling](../concepts/error-handling.md)); a minor mismatch is
tolerated, with unknown newer fields ignored. Clients learn what a server
speaks via [Discover Versions](../operations/discover-versions.md) (1.1+) or
by probing with [Query](../operations/query.md).

## Examples

A 2.1-capable client talking to an unknown server opens with Discover
Versions at Protocol Version { 2, 1 }; if the server answers with { 2, 0 }
first in its list, the client pins subsequent requests to { 2, 0 }.

## Related

[Message Structure](message-structure.md) ·
[Discover Versions](../operations/discover-versions.md)
