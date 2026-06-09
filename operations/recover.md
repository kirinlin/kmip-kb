---
title: Recover
category: operation
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4"]
source_section: "4.23"
status: draft
related: ["archive", "get", "poll"]
keywords: ["recover", "unarchive", "restore object", "archive retrieval"]
---

# Recover

## Purpose

`Recover` brings an archived object back online so it can be used again. It is
the inverse of [Archive](archive.md).

## Request Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | No | The object to recover; the ID Placeholder is used when omitted. |

## Response Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | Yes | The object's identifier. |

## Behavior & Server Requirements

Retrieving an object from the archive can take time, so this operation may
return asynchronously and require [Poll](poll.md) to collect the result. Once
the response arrives, the object is online again and can be fetched with
[Get](get.md). Servers should restrict the operation to the owner or an
authorized security officer and enforce strong authentication.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: an unknown object, an object that is not archived, or insufficient
permission.

## Related Operations

[Archive](archive.md) · [Get](get.md) · [Poll](poll.md)
