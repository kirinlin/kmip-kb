---
title: Compromise Occurrence Date
category: attribute
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.11"
v1_source_section: "3.29"
status: reviewed
related: ["compromise-date", "revocation-reason", "state", "initial-date"]
keywords: ["compromise occurrence date", "incident time", "key compromise", "forensics", "420021", "CompromiseOccurrenceDate"]
tag_hex: "420021"
xml_text: "CompromiseOccurrenceDate"
tag_type: "Date-Time"
---

# Compromise Occurrence Date

## Purpose

The best estimate of when the compromise *actually happened* — as opposed to
[Compromise Date](compromise-date.md), which records when the server found
out. The gap between the two bounds the forensic window: everything the key
protected after the occurrence date is suspect.

## Data Type & Structure

A Date-Time. When no estimate is possible, the convention is to fall back to
the object's [Initial Date](initial-date.md) — assume the worst, i.e. that
the object was never trustworthy.

## Constraints

- Absent unless the object has been declared compromised; single instance;
  immutable and not deletable once set.

## Applies To (Object Types)

All cryptographic objects, plus opaque objects.

## Set / Modified By

Server only, implicitly during a [Revoke](../operations/revoke.md) whose
reason is Key Compromise (the client supplies the estimated date in the
Revoke request payload).

## Related Attributes

[Compromise Date](compromise-date.md) ·
[Revocation Reason](revocation-reason.md) · [State](state.md) ·
[Initial Date](initial-date.md)
