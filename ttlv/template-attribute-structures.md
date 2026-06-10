---
title: Template-Attribute Structures
category: ttlv
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "2.1.8"
status: draft
related: ["attribute", "template", "name"]
keywords: ["template-attribute", "common template-attribute", "private key template-attribute", "public key template-attribute"]
---

# Template-Attribute Structures

## Overview

The wrapper that carries desired attributes in object-creating requests and
server-set attributes back in their responses. Four identically-shaped
variants exist; the names route attributes in two-object operations:
**Template-Attribute** (the general one), and for
[Create Key Pair](../operations/create-key-pair.md) /
[Re-key Key Pair](../operations/re-key-key-pair.md) the **Common**,
**Private Key**, and **Public Key Template-Attribute** variants that apply
to both halves, the private key only, and the public key only.

## Encoding (Tag / Type / Length / Value)

Structures with tags `420091` (Template-Attribute), `42001F` (Common),
`420065` (Private Key), `42006E` (Public Key):

| Field | Tag | Type | Required |
|---|---|---|---|
| Name | `420053` | Structure | No; repeatable — a [Template](../objects/template.md) reference (deprecated) |
| Attribute | `420008` | Structure | No; repeatable |

## Fields & Structure

The Name fields reference stored Template objects by their
[Name](../attributes/name.md) attribute; the server merges the named
templates' attributes with the individually supplied Attribute structures.
Since 1.3 the Template object — and therefore the Name field here — is
deprecated: supply individual attributes instead. In responses, the server
uses a Template-Attribute to report attributes it set implicitly (e.g.
server-chosen [Unique Identifier](../attributes/unique-identifier.md) is
returned in the payload proper, but defaults like usage masks appear here).

## Examples

A [Create](../operations/create.md) request for an AES key carries one
Template-Attribute holding three Attribute structures: Cryptographic
Algorithm = AES, Cryptographic Length = 256, Cryptographic Usage Mask =
Encrypt | Decrypt.

## Related

[Attribute](attribute.md) · [Template object](../objects/template.md) ·
[Create](../operations/create.md)
