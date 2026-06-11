---
title: Never Extractable
category: attribute
spec_version: "2.1"
spec_versions: ["1.4", "2.0", "2.1"]
source_section: "4.33"
v1_source_section: "3.51"
status: draft
related: ["extractable", "always-sensitive", "sensitive"]
keywords: ["never extractable", "history flag", "audit", "PKCS#11 parity"]
tag_hex: "420123"
xml_element: "NeverExtractable"
---

# Never Extractable

## Purpose

The audit companion to [Extractable](extractable.md): True only if
Extractable has been False for the object's whole life. It answers the
compliance question "could this key's material *ever* have left the
server?" — KMIP's CKA_NEVER_EXTRACTABLE.

## Data Type & Structure

A Boolean.

## Constraints

- Always has a value (1.4 objects); single instance; not deletable.
- Server-computed only; clients cannot write it. Recomputed whenever
  Extractable is set or changed — a single Extractable=True moment latches
  it False permanently.

## Applies To (Object Types)

All managed objects.

## Set / Modified By

Server only, implicitly whenever the Extractable attribute is set or
modified.

## Related Attributes

[Extractable](extractable.md) · [Always Sensitive](always-sensitive.md) ·
[Sensitive](sensitive.md)
