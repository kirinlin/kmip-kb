---
title: Usage Limits
category: attribute
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.59"
v1_source_section: "3.21"
status: draft
related: ["lease-time", "cryptographic-usage-mask", "state"]
keywords: ["usage limits", "usage allocation", "byte limit", "key exhaustion", "quota"]
tag_hex: "420095"
xml_element: "UsageLimits"
---

# Usage Limits

## Purpose

A budget for how much *protection* a key may apply over its lifetime —
bytes encrypted, objects wrapped — enforced through
[Get Usage Allocation](../operations/get-usage-allocation.md). Only
protection counts against the budget: decrypting, verifying, and unwrapping
(processing already-protected data) are never limited, so a drained key can
still recover everything it protected.

## Data Type & Structure

A structure of three required fields:

| Field | Type | Meaning |
|---|---|---|
| Usage Limits Total | Long Integer | Lifetime budget, fixed once the key starts protecting. |
| Usage Limits Count | Long Integer | Budget still unspent. |
| Usage Limits Unit | Enumeration | What is being counted: `Byte` or `Object`. |

## Constraints

- Optional (a key without it is unlimited, policy permitting); single
  instance.
- The Count is server-owned arithmetic: clients can never set or modify it,
  and a Count supplied in a create/register request is ignored.
- The Total and Unit are client-correctable via
  [Modify Attribute](../operations/modify-attribute.md) only until the first
  Get Usage Allocation changes the Count; after that the attribute is frozen
  and not deletable.

## Applies To (Object Types)

Keys (and formerly templates).

## Set / Modified By

Server (all three fields) or client (Total/Unit only) at creation; implicitly
set by [Create](../operations/create.md),
[Create Key Pair](../operations/create-key-pair.md),
[Register](../operations/register.md),
[Derive Key](../operations/derive-key.md),
[Re-key](../operations/re-key.md) /
[Re-key Key Pair](../operations/re-key-key-pair.md), and decremented by
[Get Usage Allocation](../operations/get-usage-allocation.md).

## Related Attributes

[Lease Time](lease-time.md) ·
[Cryptographic Usage Mask](cryptographic-usage-mask.md) · [State](state.md)
