---
title: Revocation Reason
category: attribute
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.47"
v1_source_section: "3.31"
status: draft
related: ["state", "compromise-date", "deactivation-date"]
keywords: ["revocation reason", "revoke", "key compromise", "superseded", "audit"]
---

# Revocation Reason

## Purpose

Why the object was revoked. The reason code is not just bookkeeping — it
steers the [state machine](state.md): a Key Compromise reason sends the
object to Compromised, any other reason to Deactivated.

## Data Type & Structure

A structure:

| Field | Type | Required |
|---|---|---|
| Revocation Reason Code | Enumeration | Yes — the coded cause |
| Revocation Message | Text String | No — free-text detail for audit/logging (e.g. which laptop was stolen) |

Reason codes mirror X.509 CRL reasons: Unspecified, Key Compromise, CA
Compromise, Affiliation Changed, Superseded, Cessation of Operation,
Privilege Withdrawn.

## Constraints

- Absent until a revocation happens; single instance; clients cannot modify
  or delete it (the server may update it).

## Applies To (Object Types)

All cryptographic objects, plus opaque objects.

## Set / Modified By

Server only, implicitly as part of [Revoke](../operations/revoke.md) — the
client proposes the reason in the request payload and the server records it
here.

## Related Attributes

[State](state.md) · [Compromise Date](compromise-date.md) ·
[Compromise Occurrence Date](compromise-occurrence-date.md) ·
[Deactivation Date](deactivation-date.md)
