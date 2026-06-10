---
title: Sensitive
category: attribute
spec_version: "1.4"
spec_versions: ["1.4"]
source_section: "3.48"
status: draft
related: ["always-sensitive", "extractable", "never-extractable", "cryptographic-usage-mask"]
keywords: ["sensitive", "wrapped export only", "key extraction", "PKCS#11 parity"]
---

# Sensitive

## Purpose

When True, the object's material may leave the server **only wrapped**: a
plaintext [Get](../operations/get.md) is refused (result reason
`Sensitive`), but a Get with a
[Key Wrapping Specification](../ttlv/key-wrapping-specification.md)
succeeds. Added in 1.4 to mirror PKCS#11's CKA_SENSITIVE and close the gap
for HSM-backed deployments.

## Data Type & Structure

A Boolean. Defaults to False: if the client does not supply a value at
creation/registration, the server sets False explicitly.

## Constraints

- Always has a value (1.4 objects); single instance; not deletable.
- Modifiable by client and server — including True→False, which is why the
  server separately tracks [Always Sensitive](always-sensitive.md) as the
  tamper-evident history bit.
- Orthogonal to [Extractable](extractable.md): Sensitive forbids *plaintext*
  export; Extractable=False forbids export altogether.

## Applies To (Object Types)

All managed objects.

## Set / Modified By

Client or server; set implicitly (with the default) whenever an object is
created or registered.

## Related Attributes

[Always Sensitive](always-sensitive.md) · [Extractable](extractable.md) ·
[Never Extractable](never-extractable.md)
