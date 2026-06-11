---
title: Extractable
category: attribute
spec_version: "2.1"
spec_versions: ["1.4", "2.0", "2.1"]
source_section: "4.23"
v1_source_section: "3.50"
status: reviewed
related: ["never-extractable", "sensitive", "always-sensitive"]
keywords: ["extractable", "non-exportable key", "key extraction", "PKCS#11 parity"]
tag_hex: "420122"
xml_element: "Extractable"
---

# Extractable

## Purpose

The export switch: when False, the object's material cannot be retrieved by
[Get](../operations/get.md) at all — wrapped or not (result reason
`Not Extractable`). The key exists only to be *used in place* via the
server's [cryptographic operations](../operations/encrypt.md). Added in 1.4,
mirroring PKCS#11's CKA_EXTRACTABLE.

## Data Type & Structure

A Boolean. Defaults to True: absent a client-supplied value, the server sets
True at creation/registration.

## Constraints

- Always has a value (1.4 objects); single instance; not deletable.
- Modifiable by client and server in both directions; the irreversible
  history lives in [Never Extractable](never-extractable.md).
- Stricter than [Sensitive](sensitive.md): Sensitive still permits wrapped
  export, Extractable=False permits none.

## Applies To (Object Types)

All managed objects.

## Set / Modified By

Client or server; set implicitly (with the default) whenever an object is
created or registered.

## Related Attributes

[Never Extractable](never-extractable.md) · [Sensitive](sensitive.md) ·
[Always Sensitive](always-sensitive.md)
