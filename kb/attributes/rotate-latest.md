---
title: Rotate Latest
category: attribute
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "4.52"
status: reviewed
related: ["rotate-automatic", "rotate-date", "rotate-generation", "rotate-interval", "rotate-name", "re-key"]
keywords: ["rotate latest", "latest rotation", "current key version", "key family head", "boolean", "420172", "RotateLatest"]
tag_hex: "420172"
xml_text: "RotateLatest"
---

# Rotate Latest

## Purpose

Rotate Latest identifies whether an object is the head of its rotation family — the most recently generated key in a sequence of rotated keys. In a key family where rotation has occurred multiple times, only one member carries `true`; predecessors carry `false` or have the attribute absent. This flag lets clients and policy engines locate the current active key in a family without traversing linked-object chains.

## Data Type & Structure

A Boolean. `true` means this key is the most recently produced member of its rotation family. `false` means a newer version exists. The attribute may be absent on keys that have never been rotated or that predate v2.1.

## Constraints

Single-instance. Optional. Updated by the server after each rotation: the newly created key receives `true`, and the predecessor is updated to `false`. Clients should not set this directly; its integrity depends on the server maintaining it consistently across the rotation family. Meaningful only when [Rotate Name](rotate-name.md) is also set, which ties members of a family together.

## Applies To (Object Types)

[Symmetric Key](../objects/symmetric-key.md), [Private Key](../objects/private-key.md), [Secret Data](../objects/secret-data.md).

## Set / Modified By

Set and maintained by the server during rotation operations. Read-only for clients in practice.

## Related Attributes

[Rotate Name](rotate-name.md) · [Rotate Generation](rotate-generation.md) · [Rotate Automatic](rotate-automatic.md)
