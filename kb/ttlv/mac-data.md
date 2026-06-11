---
title: MAC Data
category: ttlv
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "7.20"
v1_source_section: "2.1.13"
status: reviewed
related: ["data", "signature-data", "authenticated-encryption-tag"]
keywords: ["MAC data", "message authentication code", "HMAC", "MAC verify"]
tag_hex: "4200C6"
xml_element: "MACData"
---

# MAC Data

## Overview

The MAC bytes exchanged by [MAC](../operations/mac.md) (output) and
[MAC Verify](../operations/mac-verify.md) (input) — the symmetric-key
counterpart of [Signature Data](signature-data.md).

## Encoding (Tag / Type / Length / Value)

Tag `4200C6`, Byte String.

## Fields & Structure

Opaque bytes whose length is determined by the MAC algorithm — e.g. 32 bytes
for HMAC-SHA256, or the cipher block size for CMAC. The algorithm comes from
the key's [Cryptographic Algorithm](../attributes/cryptographic-algorithm.md)
(for the HMAC-* values) or from
[Cryptographic Parameters](../attributes/cryptographic-parameters.md). Not
to be confused with the [Authenticated Encryption
Tag](authenticated-encryption-tag.md), which belongs to AEAD encryption, or
with the MAC/Signature field inside
[Key Wrapping Data](key-wrapping-data.md).

## Examples

MAC request: HMAC-SHA256 key identifier, Data = a manifest file's bytes.
Response: MAC Data = the 32-byte tag, which a later MAC Verify checks.

## Related

[Data](data.md) · [MAC](../operations/mac.md) ·
[MAC Verify](../operations/mac-verify.md) ·
[Authenticated Encryption Tag](authenticated-encryption-tag.md)
