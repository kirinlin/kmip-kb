---
title: Get Usage Allocation
category: operation
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.23"
v1_source_section: "4.18"
status: reviewed
related: ["check", "usage-limits", "activate", "encrypt", "sign"]
keywords: ["get usage allocation", "usage limits", "protection quota", "metering"]
---

# Get Usage Allocation

## Purpose

`Get Usage Allocation` reserves part of an object's
[usage limits](../attributes/usage-limits.md) so the client may apply
cryptographic protection with it. It applies only to objects that can be used to
*apply* protection (encrypting, signing, and the like) and that carry a usage
limits attribute; using protected data — decrypting or verifying — is never
metered and needs no allocation.

## Request Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | No | The object to allocate against; the ID Placeholder is used when omitted. |
| Usage Limits Count | Yes | How many usage-limit units the client wants to reserve for protection. |

## Response Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | Yes | The object's identifier. |

## Behavior & Server Requirements

An object that has a usage-limits attribute must not be used to apply protection
until an allocation has been obtained. The request may only be made while
protection is enabled for the object — that is, after its activation date and
before its protect-stop date. The server treats the whole allocated amount as
consumed, so once it is used up the client must obtain a new allocation before
continuing. An error is returned when the target lacks a usage-limits attribute,
cannot apply protection, or when the requested amount is not available.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: the object has no usage-limits attribute or cannot apply protection, the
requested amount exceeds what remains, the object is outside its protection
window, or insufficient permission.

## Related Operations

[Check](check.md) · [Activate](activate.md) · [Encrypt](encrypt.md) ·
[Sign](sign.md)
