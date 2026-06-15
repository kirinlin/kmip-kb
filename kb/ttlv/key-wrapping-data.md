---
title: Key Wrapping Data
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "3.3"
v1_source_section: "2.1.5"
status: reviewed
related: ["key-wrapping-specification", "key-block", "key-value"]
keywords: ["key wrapping data", "wrapping method", "encryption key information", "MAC signature", "encoding option"]
tag_hex: "420046"
xml_element: "KeyWrappingData"
---

# Key Wrapping Data

## Overview

The *descriptor* that accompanies a wrapped key: it sits in the
[Key Block](key-block.md) whenever the [Key Value](key-value.md) is
encrypted, MACed/signed, or both, and records exactly how the protection was
applied so the receiver can undo or verify it. (Its request-side twin — how a
client *asks* for wrapping — is the
[Key Wrapping Specification](key-wrapping-specification.md).)

## Encoding (Tag / Type / Length / Value)

Structure, tag `420046`:

| Field | Tag | XML Element | Type | Required |
|---|---|---|---|---|
| Wrapping Method | `42009E` | `WrappingMethod` | Enumeration | Yes |
| Encryption Key Information | `420036` | `EncryptionKeyInformation` | Structure | One of these two key-information fields must appear |
| MAC/Signature Key Information | `42004E` | `MACSignatureKeyInformation` | Structure | (see above) |
| MAC/Signature | `42004D` | `MACSignature` | Byte String | No |
| IV/Counter/Nonce | `42003D` | `IVCounterNonce` | Byte String | If the wrapping method needs one |
| Encoding Option | `4200A3` | `EncodingOption` | Enumeration | No; absent ⇒ TTLV Encoding (1.1+) |

Both key-information structures contain a Unique Identifier (`420094`,
required — the wrapping/MACing key) and optional
[Cryptographic Parameters](../attributes/cryptographic-parameters.md)
(`42002B`).

## Fields & Structure

Wrapping methods: Encrypt only, MAC/sign only, the two combined orderings
(encrypt-first or MAC/sign-first), TR-31, plus extensions. The wrapping algorithm comes
from the wrapping key's own
[Cryptographic Algorithm](../attributes/cryptographic-algorithm.md); mode,
padding, and hash come from the Cryptographic Parameters embedded here or,
failing that, from the wrapping key's stored parameters. Unless the method
says otherwise, what gets wrapped is the entire Key Value structure — the
Encoding Option (added in 1.1) distinguishes wrapping the TTLV-encoded
structure (attributes included) from wrapping just the raw key bytes
(No Encoding, in which case attributes are forbidden).

## Examples

A Key Block delivering an AES key wrapped under a KEK: Wrapping Method =
Encrypt, Encryption Key Information naming the KEK's unique identifier with
Cryptographic Parameters specifying NISTKeyWrap mode, Encoding Option =
No Encoding, and the Key Value as one opaque byte string.

## Related

[Key Wrapping Specification](key-wrapping-specification.md) ·
[Key Block](key-block.md) · [Key Value](key-value.md)
