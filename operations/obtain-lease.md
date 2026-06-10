---
title: Obtain Lease
category: operation
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.17"
status: draft
related: ["check", "get-attributes", "lease-time", "last-change-date"]
keywords: ["obtain lease", "lease time", "cache expiry", "client caching"]
---

# Obtain Lease

## Purpose

`Obtain Lease` requests a new lease for an object. A lease bounds how long a
client may rely on its cached copy of the object's information before it must be
renewed, giving the server a way to keep clients from using stale objects
indefinitely.

## Request Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | No | The object to lease; the ID Placeholder is used when omitted. |

## Response Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | Yes | The object's identifier. |
| Lease Time | Yes | How long (in seconds) the object may be used before a new lease is needed. |
| Last Change Date | Yes | When the object's contents or attributes last changed. |

## Behavior & Server Requirements

A returned [lease time](../attributes/lease-time.md) of zero means no lease
limit applies and the object may be used with no renewal required. When a lease
does expire, the client must stop using the associated cryptographic object
until it obtains a fresh one. The server may also refuse to grant a lease, in
which case it returns an error. The accompanying
[Last Change Date](../attributes/last-change-date.md) lets the client decide
whether its cached attributes are stale by comparing it against when those
attributes were last fetched.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: the server declines to issue a lease, an unknown object, or insufficient
permission.

## Related Operations

[Check](check.md) · [Get Attributes](get-attributes.md)
