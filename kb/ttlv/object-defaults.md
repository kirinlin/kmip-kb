---
title: Object Defaults
category: ttlv
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "7.22"
status: reviewed
related: ["defaults-information", "set-defaults", "attribute", "object-type"]
keywords: ["object defaults", "default attributes", "object type defaults", "server defaults", "attribute defaults"]
---

# Object Defaults

## Overview

Object Defaults is the per-object-type unit inside a [Defaults Information](defaults-information.md) structure. Each Object Defaults entry binds an Object Type to a set of default attribute values that the server applies when an object of that type is created without those attributes being explicitly specified by the client.

Servers maintain one Object Defaults entry per supported object type. A privileged client can update these defaults via the [Set Defaults](../operations/set-defaults.md) operation, which submits a Defaults Information structure containing one or more Object Defaults entries.

## Encoding (Tag / Type / Length / Value)

Object Defaults encodes as a Structure.

| Field | Tag | XML Element | Type | Required |
|---|---|---|---|---|
| Object Type | `420057` | `ObjectType` | Enumeration | Yes |
| Attribute | `420008` | `Attribute` | Structure | Zero or more |

The Object Type identifies the managed object category these defaults apply to. The repeating Attribute children are the default attribute name/value pairs for that type.

## Fields & Structure

**Object Type** is an Enumeration identifying which kind of managed object these defaults cover — Symmetric Key, Private Key, Public Key, Certificate, Secret Data, Opaque Object, and similar values from the Object Type enumeration.

**Attribute** children follow the standard [Attribute](attribute.md) encoding. Any attribute legal for the given object type may appear here. If a client creates an object of this type without specifying one of these attributes, the server uses the value from the matching Object Defaults entry.

Server implementations may impose constraints on which attributes can be defaulted and which must always be supplied explicitly by clients. Mandatory attributes (such as Object Type itself and Unique Identifier) are not meaningful as defaults since the server generates or requires them independently.

## Examples

An Object Defaults entry for Symmetric Keys might carry: Cryptographic Algorithm = AES, Cryptographic Length = 256, Cryptographic Usage Mask = Encrypt | Decrypt | Wrap Key. A client that calls Create with only Object Type = Symmetric Key and no further attributes will receive an AES-256 key with those usage bits already set.

A second entry for Private Keys might set Cryptographic Algorithm = EC and Cryptographic Length = 384 as the organization's preferred asymmetric defaults.

## Related

[Defaults Information](defaults-information.md) · [Set Defaults](../operations/set-defaults.md) · [Attribute](attribute.md) · [Object Type](../attributes/object-type.md)
