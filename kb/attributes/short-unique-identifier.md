---
title: Short Unique Identifier
category: attribute
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "4.56"
status: reviewed
related: ["unique-identifier", "name", "object-type", "locate"]
keywords: ["short unique identifier", "abbreviated id", "short id", "compact identifier", "text string", "alias", "420136", "ShortUniqueIdentifier"]
tag_hex: "420136"
xml_text: "ShortUniqueIdentifier"
---

# Short Unique Identifier

## Purpose

Short Unique Identifier is a server-assigned abbreviated form of the full [Unique Identifier](unique-identifier.md). While a KMIP Unique Identifier may be a long UUID, a URI, or any other opaque string, the Short Unique Identifier provides a compact alternative — for example a 16-character base64 token or a numeric short code — for use in display interfaces, log entries, or API contexts where brevity matters. It carries no normative status for addressing objects; the full Unique Identifier remains the canonical key.

## Data Type & Structure

A Text String. The format and length are implementation-defined. Servers guarantee uniqueness of the Short Unique Identifier within their namespace; interoperability across servers is not guaranteed since different servers may generate different short forms from the same underlying Unique Identifier. The attribute is assigned at object creation and does not change over the object's lifetime.

## Constraints

Single-instance. Optional; assigned by the server when the implementation supports abbreviated identifiers. Not directly settable by clients. Because it is advisory, clients must not rely on it as the sole addressing mechanism; all KMIP request messages that identify objects must use the full Unique Identifier.

## Applies To (Object Types)

All managed object types: [Symmetric Key](../objects/symmetric-key.md), [Public Key](../objects/public-key.md), [Private Key](../objects/private-key.md), [Secret Data](../objects/secret-data.md), [Certificate](../objects/certificate.md), [Opaque Object](../objects/opaque-object.md), and others.

## Set / Modified By

Set by the server at object creation or registration. Not modifiable by clients.

## Related Attributes

[Unique Identifier](unique-identifier.md) · [Name](name.md)
