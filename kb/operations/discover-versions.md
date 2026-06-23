---
title: Discover Versions
category: operation
spec_version: "2.1"
spec_versions: ["1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.16"
v1_source_section: "4.26"
status: reviewed
related: ["query", "protocol-version"]
keywords: ["discover versions", "protocol version", "version negotiation", "compatibility"]
xml_text: "DiscoverVersions"
---

# Discover Versions

## Purpose

`Discover Versions` lets a client find out which protocol versions a server
supports, so the two can agree on a common version. It was introduced in
KMIP 1.1.

## Request Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Protocol Version | `420069` | `ProtocolVersion` | No (may repeat) | The versions the client supports, listed most-preferred first. |

## Response Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Protocol Version | `420069` | `ProtocolVersion` | No (may repeat) | The versions the server supports, listed most-preferred first. |

## Behavior & Server Requirements

When the client lists its supported versions, the server returns only those it
shares with the client, and should list every shared version. If there is no
overlap (and the request-header version is not among the client's list), the
server returns an empty list. When the client supplies no versions at all, the
server should return its full set of supported versions. In every case the
returned versions are ordered by preference.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). A lack of
common version is conveyed by an empty list rather than an error.

## Related Operations

[Query](query.md)
