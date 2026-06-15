---
title: Data
category: structures
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "7.9"
v1_source_section: "2.1.10"
status: reviewed
related: ["data-length", "signature-data", "mac-data", "correlation-value"]
keywords: ["data", "payload", "encrypt", "decrypt", "sign", "cryptographic operations", "4200C2"]
tag_hex: "4200C2"
xml_text: "Data"
---

# Data

## Overview

The plaintext/ciphertext payload field of the cryptographic-service
operations added in 1.2: [Encrypt](../operations/encrypt.md),
[Decrypt](../operations/decrypt.md), [Sign](../operations/sign.md),
[Signature Verify](../operations/signature-verify.md),
[MAC](../operations/mac.md) / [MAC Verify](../operations/mac-verify.md), and
[Hash](../operations/hash.md) all move their input and output bytes in Data
fields.

## Encoding (Tag / Type / Length / Value)

Tag `4200C2`, Byte String. No internal structure — meaning comes from the
operation: Encrypt takes plaintext Data in and returns ciphertext Data;
Decrypt the reverse; Sign takes the data to sign (returning
[Signature Data](signature-data.md)); Hash returns the digest as Data.

## Fields & Structure

A single opaque byte sequence. In streaming (multi-part) usage (1.3+), each
request carries one chunk of Data, tied together by a
[Correlation Value](correlation-value.md) with
[Init](init-indicator.md) / [Final Indicator](final-indicator.md) flags.

## Examples

Encrypt request: Unique Identifier of an AES key, Cryptographic Parameters
(GCM, tag length 16), Data = 1 KiB of plaintext. Response: Data = the
ciphertext, IV, and the [authentication tag](authenticated-encryption-tag.md).

## Related

[Data Length](data-length.md) · [Signature Data](signature-data.md) ·
[MAC Data](mac-data.md) · [Correlation Value](correlation-value.md)
