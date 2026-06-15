---
title: Rotate Name Type Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "11.51"
status: reviewed
related: ["rotate-name"]
keywords: ["rotate name type", "rotation group", "rotation identifier format", "text string", "URI", "420171", "RotateNameType"]
tag_hex: "420171"
xml_text: "RotateNameType"
---

# Rotate Name Type Enumeration

## Overview

The Rotate Name Type enumeration classifies the format or interpretation of the value stored in the [Rotate Name attribute](../../attributes/rotate-name.md). It is the type discriminator that tells consumers how to parse or display the Rotate Name value — whether it is a free-form text label or a structured identifier such as a URI.

## Fields & Structure

| Value | Hex | XML Text | Description |
|---|---|---|---|
| Uninterpreted Text String | `0x00000001` | `UninterpretedTextString` |  |
| URI | `0x00000002` | `URI` |  |

- **Uninterpreted Text String**: The Rotate Name value is an opaque human-readable label with no required structure — for example, "payment-keys" or "tls-server-certs-2024". Clients display it as-is.
- **URI**: The Rotate Name value is a Uniform Resource Identifier that provides a globally namespaced, dereferenceable (or at least unique) identifier for the rotation group — for example, `urn:example:key-family:payment-aes-256`.

## Examples

An enterprise key management system that uses descriptive names internally sets Rotate Name Type = **Uninterpreted Text String** with a value like "db-column-encryption". A multi-vendor ecosystem that needs globally unique key family identifiers uses **URI** with a domain-scoped URN.

## Related

[Rotate Name attribute](../../attributes/rotate-name.md)
