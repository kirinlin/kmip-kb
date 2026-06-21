---
title: Always Sensitive
category: attribute
spec_version: "2.1"
spec_versions: ["1.4", "2.0", "2.1"]
source_section: "4.3"
v1_source_section: "3.49"
status: reviewed
related: ["sensitive", "never-extractable", "extractable"]
keywords: ["always sensitive", "history flag", "audit", "PKCS#11 parity", "420121", "AlwaysSensitive"]
tag_hex: "420121"
xml_text: "AlwaysSensitive"
tag_type: "Boolean"
---

# Always Sensitive

## Purpose

The audit companion to [Sensitive](sensitive.md): True only if Sensitive has
been True for the object's entire life. Because Sensitive itself is
mutable, this server-maintained history bit is what lets an auditor assert
"this key was never eligible for plaintext export" — the KMIP analogue of
PKCS#11's CKA_ALWAYS_SENSITIVE.

## Data Type & Structure

A Boolean. (The spec's encoding table labels the row "Sensitive" — editorial
slip; the attribute is Always Sensitive.)

## Constraints

- Always has a value (1.4 objects); single instance; not deletable.
- Entirely server-computed: clients can read it but never write it. The
  server re-evaluates it whenever Sensitive is set or changed; one
  Sensitive=False moment latches it False forever.

## Applies To (Object Types)

All managed objects.

## Set / Modified By

Server only, implicitly whenever the Sensitive attribute is set or modified.

## Related Attributes

[Sensitive](sensitive.md) · [Never Extractable](never-extractable.md) ·
[Extractable](extractable.md)
