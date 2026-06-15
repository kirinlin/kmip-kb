---
title: Lease Time
category: attribute
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.30"
v1_source_section: "3.20"
status: reviewed
related: ["usage-limits", "state", "last-change-date"]
keywords: ["lease time", "interval", "obtain lease", "caching", "time-limited use", "420049", "LeaseTime"]
tag_hex: "420049"
xml_text: "LeaseTime"
---

# Lease Time

## Purpose

Caps how long a client may keep using a fetched object before checking back.
A client that holds a lease must call
[Obtain Lease](../operations/obtain-lease.md) again once it lapses — giving
the server a periodic chance to say "this key was revoked, stop using it"
even to clients that cache key material locally.

## Data Type & Structure

An Interval (seconds). The stored value is the *maximum initial* lease length
the server grants for this object — not a countdown of time remaining. Each
Obtain Lease response grants a lease no longer than this value.

## Constraints

- Optional; single instance.
- Read-only for clients; only the server sets or changes it.
- A client without a valid lease is expected not to use the object, and
  Obtain Lease is the only sanctioned renewal path.

## Applies To (Object Types)

All cryptographic objects.

## Set / Modified By

Server-set (per policy) when the object is created or registered — implicitly
by [Create](../operations/create.md),
[Create Key Pair](../operations/create-key-pair.md),
[Register](../operations/register.md),
[Derive Key](../operations/derive-key.md),
[Certify](../operations/certify.md) /
[Re-certify](../operations/re-certify.md),
[Re-key](../operations/re-key.md) /
[Re-key Key Pair](../operations/re-key-key-pair.md) — and adjustable by the
server later. Servers can also grant leases when
[pushing](../operations/server-to-client/put.md) objects.

## Related Attributes

[Usage Limits](usage-limits.md) · [State](state.md) ·
[Last Change Date](last-change-date.md)
