---
title: Initial Date
category: attribute
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.25"
v1_source_section: "3.23"
status: draft
related: ["original-creation-date", "activation-date", "last-change-date", "state"]
keywords: ["initial date", "creation time", "registration time", "lifecycle dates"]
---

# Initial Date

## Purpose

When the *server* first took custody of the object — the timestamp of
creation or registration, i.e. of the transition from non-existence to
Pre-Active. Note the distinction from
[Original Creation Date](original-creation-date.md) (1.2+): for an object
generated elsewhere and registered later, Initial Date is the registration
moment, not the original birth.

## Data Type & Structure

A Date-Time (POSIX seconds, like all KMIP timestamps).

## Constraints

- Always present, on every object type — including non-cryptographic ones
  like templates; single instance.
- Immutable and not deletable: it is a historical fact.

## Applies To (Object Types)

All managed objects.

## Set / Modified By

Server-set, implicitly, by every object-creating operation:
[Create](../operations/create.md),
[Create Key Pair](../operations/create-key-pair.md),
[Register](../operations/register.md),
[Derive Key](../operations/derive-key.md),
[Certify](../operations/certify.md) /
[Re-certify](../operations/re-certify.md),
[Re-key](../operations/re-key.md) /
[Re-key Key Pair](../operations/re-key-key-pair.md).

## Related Attributes

[Original Creation Date](original-creation-date.md) ·
[Activation Date](activation-date.md) ·
[Last Change Date](last-change-date.md) · [State](state.md)
