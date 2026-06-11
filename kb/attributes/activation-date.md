---
title: Activation Date
category: attribute
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.1"
v1_source_section: "3.24"
status: reviewed
related: ["state", "initial-date", "deactivation-date", "process-start-date"]
keywords: ["activation date", "active state", "lifecycle dates", "activate"]
tag_hex: "420001"
xml_element: "ActivationDate"
---

# Activation Date

## Purpose

The moment the object may begin cryptographic service — the trigger for the
Pre-Active → Active [state](state.md) transition. Before this instant the
object must not be used for any cryptographic purpose.

## Data Type & Structure

A Date-Time. May be in the future (scheduled activation), now, or — in a
create/register request — already in the past, in which case the object goes
straight to Active (or the server rejects the request, per policy).

## Constraints

- Optional until activation happens; single instance; never deletable.
- Freely settable/modifiable **only while the object is Pre-Active**. Once
  the activation transition has occurred the date is frozen for both sides.
- An explicit [Activate](../operations/activate.md) stamps it with the
  operation's arrival time; modifying it to a past date activates
  immediately.

## Applies To (Object Types)

All cryptographic objects (and formerly templates).

## Set / Modified By

Client or server. Implicitly set by [Create](../operations/create.md),
[Create Key Pair](../operations/create-key-pair.md),
[Register](../operations/register.md),
[Derive Key](../operations/derive-key.md),
[Activate](../operations/activate.md),
[Certify](../operations/certify.md) /
[Re-certify](../operations/re-certify.md),
[Re-key](../operations/re-key.md) /
[Re-key Key Pair](../operations/re-key-key-pair.md) (re-keys compute the
replacement's dates from the original's offsets).

## Related Attributes

[State](state.md) · [Initial Date](initial-date.md) ·
[Deactivation Date](deactivation-date.md) ·
[Process Start Date](process-start-date.md)
