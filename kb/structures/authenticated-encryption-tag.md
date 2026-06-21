---
title: Authenticated Encryption Tag
category: structures
spec_version: "2.1"
spec_versions: ["1.4", "2.0", "2.1"]
source_section: "7.4"
v1_source_section: "2.1.23"
status: reviewed
related: ["authenticated-encryption-additional-data", "data", "mac-data"]
keywords: ["authentication tag", "GCM tag", "AEAD", "integrity", "4200FF", "AuthenticatedEncryptionTag"]
tag_hex: "4200FF"
xml_text: "AuthenticatedEncryptionTag"
tag_type: "Byte String"
---

# Authenticated Encryption Tag

## Overview

The integrity tag of an AEAD operation (1.4): produced by an authenticated
[Encrypt](../operations/encrypt.md), required by the matching
[Decrypt](../operations/decrypt.md), which verifies it before releasing
plaintext. The SP 800-38D (GCM) model, surfaced as a first-class protocol
field.

## Encoding (Tag / Type / Length / Value)

Tag `4200FF`, Byte String. Its length is governed by the Tag Length field of
[Cryptographic Parameters](../attributes/cryptographic-parameters.md)
(mandatory for GCM/CCM), commonly 16 bytes.

## Fields & Structure

Output of encryption, input to decryption — unlike [MAC Data](mac-data.md),
it is inseparable from the ciphertext and the
[AAD](authenticated-encryption-additional-data.md): change any of the three
and Decrypt fails with a cryptographic error rather than returning forged
plaintext.

## Examples

AES-GCM Encrypt response: Data = ciphertext, IV (server-generated via Random
IV), Authenticated Encryption Tag = 16 bytes. The client stores all three
and presents them together to Decrypt.

## Related

[Authenticated Encryption Additional Data](authenticated-encryption-additional-data.md) ·
[Data](data.md) · [Decrypt](../operations/decrypt.md)
