---
title: Deactivation Date
category: attribute
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.18"
v1_source_section: "3.27"
status: draft
related: ["state", "activation-date", "protect-stop-date", "revocation-reason"]
keywords: ["deactivation date", "deactivated state", "expiry", "lifecycle dates"]
---

# Deactivation Date

## Purpose

The scheduled end of the object's working life — the trigger for the
Active → Deactivated [state](state.md) transition. After it, the object stops
applying protection; processing already-protected data is reserved for
exceptional, specially-authorized situations.

## Data Type & Structure

A Date-Time. Functions as the key's expiry: reaching it, moving it into the
past via [Modify Attribute](../operations/modify-attribute.md), or a
[Revoke](../operations/revoke.md) with a non-compromise reason all deactivate
the object.

## Constraints

- Optional; single instance; not deletable.
- Modifiable by client or server only while the object is Pre-Active or
  Active; immutable once deactivation has occurred.
- For symmetric keys, [Protect Stop Date](protect-stop-date.md) must not be
  later than this date.

## Applies To (Object Types)

All cryptographic objects (and formerly templates).

## Set / Modified By

Client or server. Implicitly set by [Create](../operations/create.md),
[Create Key Pair](../operations/create-key-pair.md),
[Register](../operations/register.md),
[Derive Key](../operations/derive-key.md),
[Revoke](../operations/revoke.md),
[Certify](../operations/certify.md) /
[Re-certify](../operations/re-certify.md),
[Re-key](../operations/re-key.md) /
[Re-key Key Pair](../operations/re-key-key-pair.md).

## Related Attributes

[State](state.md) · [Activation Date](activation-date.md) ·
[Protect Stop Date](protect-stop-date.md) ·
[Revocation Reason](revocation-reason.md)
