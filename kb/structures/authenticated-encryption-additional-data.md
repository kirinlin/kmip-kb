---
title: Authenticated Encryption Additional Data
category: structures
spec_version: "2.1"
spec_versions: ["1.4", "2.0", "2.1"]
source_section: "7.3"
v1_source_section: "2.1.22"
status: reviewed
related: ["authenticated-encryption-tag", "data", "cryptographic-parameters"]
keywords: ["AAD", "additional authenticated data", "GCM", "CCM", "AEAD", "4200FE", "AuthenticatedEncryptionAdditionalData"]
tag_hex: "4200FE"
xml_text: "AuthenticatedEncryptionAdditionalData"
tag_type: "Byte String"
---

# Authenticated Encryption Additional Data

## Overview

The AAD input for AEAD modes (GCM, CCM), added in 1.4 alongside full
authenticated-encryption support in [Encrypt](../operations/encrypt.md) /
[Decrypt](../operations/decrypt.md): bytes that are authenticated by the tag
but not encrypted — typically headers or context identifiers that must
remain readable yet tamper-evident.

## Encoding (Tag / Type / Length / Value)

Tag `4200FE`, Byte String.

## Fields & Structure

Supplied by the client in the Encrypt request; the same bytes must be
presented again in the matching Decrypt request or tag verification fails.
KMIP transports the AAD but never stores it — managing it (and the
requirement that it match) is the application's problem. The companion
output/input is the
[Authenticated Encryption Tag](authenticated-encryption-tag.md); mode and
tag length come from
[Cryptographic Parameters](../attributes/cryptographic-parameters.md).

## Examples

Encrypting a database page with AES-GCM: Data = the page, Authenticated
Encryption Additional Data = the page header (page number, version). Any
later tampering with the stored header makes the Decrypt fail
authentication.

## Related

[Authenticated Encryption Tag](authenticated-encryption-tag.md) ·
[Data](data.md) · [Encrypt](../operations/encrypt.md)
