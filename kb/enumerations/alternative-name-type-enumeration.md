---
title: Alternative Name Type Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.2"
status: reviewed
related: ["alternative-name", "name-type-enumeration", "unique-identifier"]
keywords: ["alternative name", "name type", "URI", "DNS name", "X.500", "object identity", "serial number", "4200C1", "AlternativeNameType"]
tag_hex: "4200C1"
xml_text: "AlternativeNameType"
---

# Alternative Name Type Enumeration

## Overview

The Alternative Name Type enumeration classifies each entry in the [Alternative Name](../attributes/alternative-name.md) attribute, which allows a managed object to carry additional identifiers beyond its server-assigned Unique Identifier. Because different systems use different conventions for naming objects — serial numbers, directory distinguished names, DNS hostnames, email addresses, URIs — this enumeration tells consumers how to interpret and route the string they receive. A single object can carry multiple Alternative Name entries, each with its own type.

## Fields & Structure

| Value | Hex | XML Text | Description |
|---|---|---|---|
| Uninterpreted Text String | `0x00000001` | `UninterpretedTextString` |  |
| URI | `0x00000002` | `URI` |  |
| Object Serial Number | `0x00000003` | `ObjectSerialNumber` |  |
| Email Address | `0x00000004` | `EmailAddress` |  |
| DNS Name | `0x00000005` | `DNSName` |  |
| X.500 Distinguished Name | `0x00000006` | `X_500DistinguishedName` |  |
| IP Address | `0x00000007` | `IPAddress` |  |

- **Uninterpreted Text String**: The name carries no defined format or external semantics. Used for application-specific labels, internal tracking identifiers, or any free-form string that does not conform to a standard naming scheme.
- **URI**: The name is a Uniform Resource Identifier, enabling the object to be addressed via URL or URN in REST-oriented or web-services integrations.
- **Object Serial Number**: A vendor- or manufacturer-assigned serial number, commonly applied to physical devices such as HSMs or self-encrypting drives.
- **Email Address**: An RFC 5321-style email address, relevant when the object is associated with a user account or a service identity.
- **DNS Name**: A fully qualified domain name. Common in TLS/PKI environments where a certificate or key is tied to a specific hostname.
- **X.500 Distinguished Name**: An LDAP/X.500-formatted DN string, enabling integration with directory services and certificate authorities that use DN-based identity.
- **IP Address**: A dotted-decimal IPv4 or colon-separated IPv6 address, used when the object corresponds to a specific network endpoint.

## Examples

A TLS certificate stored in KMIP might carry an Alternative Name with type **DNS Name** set to `api.example.com` so that applications can search for it by hostname rather than opaque UUID. The same certificate might carry a second Alternative Name entry with type **X.500 Distinguished Name** for lookup via an enterprise LDAP directory, and a third with type **URI** for addressing via a REST management API.

## Related

- [Alternative Name attribute](../attributes/alternative-name.md) — the attribute that uses this enumeration
- [Name Type Enumeration](name-type-enumeration.md) — the analogous type enumeration for the Name attribute
