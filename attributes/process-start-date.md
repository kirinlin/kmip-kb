---
title: Process Start Date
category: attribute
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "3.25"
status: draft
related: ["protect-stop-date", "activation-date", "deactivation-date", "state"]
keywords: ["process start date", "decryption window", "symmetric key", "lifecycle dates"]
---

# Process Start Date

## Purpose

For symmetric keys, the earliest moment the key may *process*
already-protected data — decrypt, unwrap, verify — as distinct from applying
protection. Together with [Protect Stop Date](protect-stop-date.md) it
implements the SP 800-57 idea that a key's protect period and process period
need not coincide: you might allow encryption from day 1 but only permit
decryption services starting later, or (more commonly) stop encryption early
while decryption continues.

## Data Type & Structure

A Date-Time. Must be equal to or later than the
[Activation Date](activation-date.md) — never earlier.

## Constraints

- Optional; single instance; not deletable.
- Modifiable by client or server only while the object is Pre-Active or
  Active **and** the date itself has not yet arrived; after that it is
  frozen.
- Subject to the [usage mask](cryptographic-usage-mask.md) as always — the
  date opens a window, it does not grant abilities the mask withholds.

## Applies To (Object Types)

Symmetric keys and split keys of symmetric keys (and formerly templates).

## Set / Modified By

Client or server; implicitly set by [Create](../operations/create.md),
[Register](../operations/register.md),
[Derive Key](../operations/derive-key.md), and
[Re-key](../operations/re-key.md).

## Related Attributes

[Protect Stop Date](protect-stop-date.md) ·
[Activation Date](activation-date.md) ·
[Deactivation Date](deactivation-date.md) · [State](state.md)
