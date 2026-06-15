---
title: Encoding Option Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["2.0","2.1"]
source_section: "11.18"
status: reviewed
related: ["key-wrapping-data", "key-block", "wrapping-method-enumeration", "key-value"]
keywords: ["encoding option", "key wrapping", "TTLV encoding", "no encoding", "key value", "wrapped key", "4200A3", "EncodingOption"]
tag_hex: "4200A3"
xml_text: "EncodingOption"
---

# Encoding Option Enumeration

## Overview

The Encoding Option enumeration controls how the [Key Value](../../structures/key-value.md) structure is represented when it is wrapped. When a key is wrapped for transport or storage under a wrapping key, the server must decide whether to wrap just the raw key bytes or the full TTLV-encoded Key Value structure (which includes the key material plus any associated attributes). Wrapping the full TTLV structure preserves attribute data alongside the key so that it can be recovered when unwrapped, whereas wrapping raw bytes produces a more compact result compatible with simpler key exchange protocols. This enumeration appears in the Key Wrapping Specification.

## Fields & Structure

| Value | Hex | XML Text | Description |
|---|---|---|---|
| No Encoding | `0x00000001` | `NoEncoding` |  |
| TTLV Encoding | `0x00000002` | `TTLVEncoding` |  |

- **No Encoding**: The raw key material bytes are wrapped directly without any TTLV framing. The wrapping input is the key value as a plain byte string. This produces a compact, format-agnostic wrapped blob that can be exchanged with non-KMIP systems that expect bare wrapped key bytes.
- **TTLV Encoding**: The full TTLV-encoded Key Value structure — which includes the key material along with any accompanying attributes such as cryptographic parameters or IV/nonce data — is serialised as a byte string and then wrapped. When the recipient unwraps the blob, they recover the complete Key Value structure and can reconstruct the KMIP key object with all its context intact.

## Examples

A KMIP client requesting a symmetric key wrapped for export to a hardware security appliance that uses a proprietary key-wrapping format would specify **No Encoding** to obtain just the wrapped key bytes. A KMIP-to-KMIP key migration scenario where the receiving server needs to recreate the full key object would use **TTLV Encoding** so that cryptographic parameters and initialization vectors travel alongside the key material.

## Related

- [Key Wrapping Data structure](../../structures/key-wrapping-data.md) — the structure that records how a key was wrapped, including the encoding option used
- [Key Value structure](../../structures/key-value.md) — the structure that is optionally TTLV-encoded before wrapping
- [Key Block structure](../../structures/key-block.md) — the outer container for wrapped key material
- [Wrapping Method Enumeration](wrapping-method-enumeration.md) — specifies the cryptographic wrapping technique
