---
title: State
category: attribute
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "3.22"
status: draft
related: ["activation-date", "deactivation-date", "compromise-date", "destroy-date", "revocation-reason"]
keywords: ["state", "lifecycle", "pre-active", "active", "deactivated", "compromised", "destroyed", "SP 800-57"]
---

# State

## Purpose

Where the object sits in its lifecycle. KMIP adopts the NIST SP 800-57 key
lifecycle: a key is born, may be used, is retired, and is eventually
destroyed — and the server polices which uses are legal in each phase.

## Data Type & Structure

An Enumeration with six values:

| State | May the key be used? |
|---|---|
| Pre-Active | No cryptographic use at all. |
| Active | Full use within the [usage mask](cryptographic-usage-mask.md) (and the process/protect date window for symmetric keys). |
| Deactivated | No new protection (no encrypt/sign/wrap); processing existing data (decrypt/verify) only under exceptional, specially-permitted circumstances. |
| Compromised | Same restrictions as Deactivated, plus the taint: only clients trusted to handle compromised material should process with it. |
| Destroyed | Nothing; material is gone, some metadata may remain. |
| Destroyed Compromised | Nothing; the compromise record is kept for audit. |

## Constraints

- Always present; single instance; never client-writable — Modify Attribute
  on State is explicitly forbidden. Only these transitions exist:
  1. *(creation)* → Pre-Active; if the create/register request carried an
     [Activation Date](activation-date.md) already in the past, straight on
     to Active.
  2. Pre-Active → Destroyed ([Destroy](../operations/destroy.md)).
  3. Pre-Active → Compromised ([Revoke](../operations/revoke.md), reason
     Key Compromise).
  4. Pre-Active → Active: activation date arrives, is modified into the
     past, or an explicit [Activate](../operations/activate.md).
  5. Active → Compromised (Revoke with compromise reason).
  6. Active → Deactivated: deactivation date arrives, is modified into the
     past, or Revoke with a non-compromise reason.
  7. Deactivated → Destroyed (Destroy, or server policy).
  8. Deactivated → Compromised (Revoke with compromise reason).
  9. Compromised → Destroyed Compromised (Destroy).
  10. Destroyed → Destroyed Compromised (Revoke with compromise reason).

## Applies To (Object Types)

All cryptographic objects.

## Set / Modified By

Server only, as a side effect of operations
([Create](../operations/create.md) /
[Create Key Pair](../operations/create-key-pair.md) /
[Register](../operations/register.md) /
[Derive Key](../operations/derive-key.md),
[Activate](../operations/activate.md), [Revoke](../operations/revoke.md),
[Destroy](../operations/destroy.md),
[Certify](../operations/certify.md) and the re-key/re-certify family) or of
date attributes crossing "now".

## Related Attributes

[Activation Date](activation-date.md) ·
[Deactivation Date](deactivation-date.md) ·
[Compromise Date](compromise-date.md) · [Destroy Date](destroy-date.md) ·
[Revocation Reason](revocation-reason.md)
