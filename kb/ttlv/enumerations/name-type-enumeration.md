---
title: Name Type Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.31"
status: reviewed
related: ["name", "alternative-name-type-enumeration", "locate"]
keywords: ["name type", "URI", "text string", "name attribute", "object name", "420054", "NameType"]
tag_hex: "420054"
xml_text: "NameType"
---

# Name Type Enumeration

## Overview

The Name Type enumeration classifies each entry in the [Name](../../attributes/name.md) attribute, which allows a managed object to carry one or more human-readable or machine-interpretable names alongside its server-assigned Unique Identifier. Different deployments use names differently: some treat them as free-form labels, others assign URIs for web service addressability. The type field tells consumers how to interpret the name string when performing Locate queries or displaying object metadata.

## Fields & Structure

| Value | Hex | XML Text | Description |
|---|---|---|---|
| Uninterpreted Text String | `0x00000001` | `UninterpretedTextString` |  |
| URI | `0x00000002` | `URI` |  |

- **Uninterpreted Text String**: The name is a plain human-readable label with no defined format or external semantics. This is the most common type in practice — administrators assign meaningful names like `"prod-db-encryption-key-2024"` that help humans identify objects in key management consoles. No external validation of the string is required.
- **URI**: The name is a Uniform Resource Identifier, allowing the object to be addressed and referenced via a standard URL or URN. Useful in microservice architectures where key names correspond to service identities or where key references appear in policy documents by URI.

## Examples

A key created for database column encryption might receive a Name attribute with type **Uninterpreted Text String** and value `"customer-pii-column-key"` so that database administrators can identify it in audit logs. A cloud-native application might assign a **URI**-type name like `urn:example:keystore:tenant:acme:key:data-at-rest-v3` to make the key addressable within a larger service mesh policy framework.

## Related

- [Name attribute](../../attributes/name.md) — the attribute that uses this enumeration
- [Alternative Name Type Enumeration](alternative-name-type-enumeration.md) — the analogous enumeration for the Alternative Name attribute
- [Locate operation](../../operations/locate.md) — searches for objects by Name attribute value and type
