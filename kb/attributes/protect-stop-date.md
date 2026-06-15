---
title: Protect Stop Date
category: attribute
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.41"
v1_source_section: "3.26"
status: reviewed
related: ["process-start-date", "deactivation-date", "activation-date", "state"]
keywords: ["protect stop date", "encryption cutoff", "symmetric key", "lifecycle dates", "420068", "ProtectStopDate"]
tag_hex: "420068"
xml_text: "ProtectStopDate"
---

# Protect Stop Date

## Purpose

For symmetric keys, the moment after which the key must stop *applying*
protection — no more encryption or wrapping — even though it may remain
Active and continue to decrypt. The standard crypto-period pattern: cut off
new ciphertext production early so that everything the key protected ages
out before the key itself is deactivated.

## Data Type & Structure

A Date-Time. Must be equal to or earlier than the
[Deactivation Date](deactivation-date.md) — never later.

## Constraints

- Optional; single instance; not deletable.
- Modifiable by client or server only while the object is Pre-Active or
  Active and the date has not yet been reached; frozen afterwards.
- Complements [Process Start Date](process-start-date.md): between Protect
  Stop and Deactivation the key is decrypt/verify-only.

## Applies To (Object Types)

Symmetric keys and split keys of symmetric keys (and formerly templates).

## Set / Modified By

Client or server; implicitly set by [Create](../operations/create.md),
[Register](../operations/register.md),
[Derive Key](../operations/derive-key.md), and
[Re-key](../operations/re-key.md).

## Related Attributes

[Process Start Date](process-start-date.md) ·
[Deactivation Date](deactivation-date.md) ·
[Activation Date](activation-date.md) · [State](state.md)
