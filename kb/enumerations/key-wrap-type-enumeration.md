---
title: Key Wrap Type Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["2.0","2.1"]
source_section: "11.29"
status: reviewed
related: ["key-block", "key-wrapping-data", "wrapping-method-enumeration", "encoding-option-enumeration", "get"]
keywords: ["key wrap type", "wrapped", "not wrapped", "key wrapping", "key block", "transport", "4200F8", "KeyWrapType"]
tag_hex: "4200F8"
xml_text: "KeyWrapType"
tag_type: "Enumeration"
---

# Key Wrap Type Enumeration

## Overview

The Key Wrap Type enumeration indicates whether and how the key material in a [Key Block](../structures/key-block.md) is currently wrapped. Key wrapping is the process of encrypting or integrity-protecting key material under another key for storage or transport; the wrap type lets consumers determine immediately whether they are receiving plaintext key bytes or an encrypted blob that must first be unwrapped before use. A transitional state is also defined for use during in-place re-wrapping operations.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Not Wrapped | `00000001` | `NotWrapped` | The key material is present in plaintext form (subject only to transport-layer protection). The client receives raw key bytes and can use them directly. |
| As Registered | `00000002` | `AsRegistered` |  |

## Examples

A client that registered a key wrapped under a Key Encryption Key receives it back with type **As Registered That Is** when it supplies no wrapping specification in the Get request, allowing it to retrieve the original wrapped blob. A client that wants the key in cleartext for local use requests it with an unwrapping specification and receives the key with type **Not Wrapped** in the response.

## Related

- [Key Block structure](../structures/key-block.md) — the container that carries this field
- [Key Wrapping Data structure](../structures/key-wrapping-data.md) — describes the wrapping parameters used when the key is wrapped
- [Wrapping Method Enumeration](wrapping-method-enumeration.md) — specifies how the wrapping was applied
- [Encoding Option Enumeration](encoding-option-enumeration.md) — controls whether the Key Value was TTLV-encoded before wrapping
- [Get operation](../operations/get.md) — retrieves key material; clients can specify wrapping behaviour
