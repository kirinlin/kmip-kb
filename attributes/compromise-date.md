---
title: Compromise Date
category: attribute
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "3.30"
status: draft
related: ["compromise-occurrence-date", "revocation-reason", "state", "destroy-date"]
keywords: ["compromise date", "compromised state", "revoke", "incident response"]
---

# Compromise Date

## Purpose

When the object entered the Compromised (or Destroyed Compromised)
[state](state.md) — i.e. when the key-management system *learned* of the
compromise, not when the breach occurred (that is
[Compromise Occurrence Date](compromise-occurrence-date.md)).

## Data Type & Structure

A Date-Time.

## Constraints

- Absent unless a compromise transition has happened (state transitions 3,
  5, 8, or 10 in the lifecycle); single instance; immutable; not deletable.

## Applies To (Object Types)

All cryptographic objects, plus opaque objects.

## Set / Modified By

Server only — implicitly when it processes a
[Revoke](../operations/revoke.md) with reason Key Compromise, or when policy
or out-of-band administration marks the object compromised.

## Related Attributes

[Compromise Occurrence Date](compromise-occurrence-date.md) ·
[Revocation Reason](revocation-reason.md) · [State](state.md) ·
[Destroy Date](destroy-date.md)
