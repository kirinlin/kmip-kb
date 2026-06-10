---
title: Key Wrapping Specification
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "7.18"
v1_source_section: "2.1.6"
status: draft
related: ["key-wrapping-data", "key-block", "key-value"]
keywords: ["key wrapping specification", "wrapped key request", "get wrapped", "encoding option"]
---

# Key Wrapping Specification

## Overview

How a client *asks* for a key to be returned wrapped: included in the request
payload of operations that can deliver keys (notably
[Get](../operations/get.md)). The server performs the wrapping it describes
and returns the result with a matching
[Key Wrapping Data](key-wrapping-data.md) in the
[Key Block](key-block.md).

## Encoding (Tag / Type / Length / Value)

Structure, tag `420047`:

| Field | Tag | Type | Required |
|---|---|---|---|
| Wrapping Method | `42009E` | Enumeration | Yes |
| Encryption Key Information | `420036` | Structure | At least one of the two key-information fields |
| MAC/Signature Key Information | `42004E` | Structure | (see above) |
| Attribute Name | `42000A` | Text String | No; repeatable — attributes to bundle inside the wrapped [Key Value](key-value.md) |
| Encoding Option | `4200A3` | Enumeration | No; absent ⇒ TTLV Encoding |

## Fields & Structure

The key-information structures name the wrapping key by Unique Identifier
and may carry
[Cryptographic Parameters](../attributes/cryptographic-parameters.md). A
matching rule applies: if parameters are given, they must equal one of the
stored Cryptographic Parameters instances on the wrapping key; if omitted,
the server uses the instance with the lowest index; if the key has no
matching (or any) instance, the request fails. Choosing No Encoding means the
bare key bytes are wrapped, which rules out bundling attributes.

## Examples

Exporting a TDE key under a transport KEK: Get with a Key Wrapping
Specification of Wrapping Method = Encrypt, Encryption Key Information naming
the KEK, Attribute Names `"Cryptographic Algorithm"` and
`"Cryptographic Usage Mask"` so the receiving system learns the key's
parameters from inside the wrapped blob.

## Related

[Key Wrapping Data](key-wrapping-data.md) · [Key Block](key-block.md) ·
[Get](../operations/get.md)
