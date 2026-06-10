---
title: Destroy Date
category: attribute
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "3.28"
status: draft
related: ["state", "compromise-date", "deactivation-date"]
keywords: ["destroy date", "destroyed state", "key destruction", "audit"]
---

# Destroy Date

## Purpose

When the object's key material was destroyed — the audit-trail record of the
transition into Destroyed (or Destroyed Compromised)
[state](state.md). The metadata, including this attribute, may outlive the
material it describes, depending on server retention policy.

## Data Type & Structure

A Date-Time.

## Constraints

- Absent until destruction happens; single instance; immutable and not
  deletable once written.
- Records when destruction *actually occurred*, which can lag the client's
  [Destroy](../operations/destroy.md) request if server policy defers the
  act.

## Applies To (Object Types)

All cryptographic objects, plus opaque objects.

## Set / Modified By

Server only, implicitly during [Destroy](../operations/destroy.md) — or when
the server destroys the object on its own initiative (policy or
administrative action outside the protocol).

## Related Attributes

[State](state.md) · [Compromise Date](compromise-date.md) ·
[Deactivation Date](deactivation-date.md)
