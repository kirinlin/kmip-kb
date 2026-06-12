---
title: Defaults Information
category: ttlv
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "7.11"
status: reviewed
related: ["object-defaults", "set-defaults", "get-constraints", "attribute", "object-type"]
keywords: ["defaults information", "server defaults", "object defaults", "default attributes", "set defaults"]
---

# Defaults Information

## Overview

Defaults Information is the top-level structure that carries the server's current default attribute settings — one entry per object type. When a client creates a managed object without supplying a complete attribute set, the server fills in any missing attributes using the defaults recorded here. Defaults Information is both the structure returned by a Get Defaults response and the payload used in a [Set Defaults](../operations/set-defaults.md) request to update those settings.

Understanding the server's defaults is important for clients that do not want to specify every attribute on every Create call, and for auditors who need to know what attribute values were in effect when a given object was created.

## Encoding (Tag / Type / Length / Value)

Defaults Information encodes as a Structure containing one or more Object Defaults entries.

| Field | Tag | Type | Required |
|---|---|---|---|
| Object Defaults | `420236` | Structure | One or more |

Each Object Defaults child describes the default attributes for one object type. The structure may contain separate entries for Symmetric Key, Private Key, Public Key, Secret Data, Certificate, and other supported object types.

## Fields & Structure

The repeating child is an [Object Defaults](object-defaults.md) structure. Each Object Defaults entry specifies an Object Type Enumeration (which type of object these defaults apply to) and a collection of Attribute structures that the server will apply when creating objects of that type without explicit values for those attributes.

The server maintains these defaults persistently. A privileged client may update them via Set Defaults, and any client may read them. Changes take effect for objects created after the update; pre-existing objects are not retroactively modified.

If no entry exists for a particular object type, the server applies built-in defaults (which may vary by implementation) or requires the client to supply all mandatory attributes explicitly.

## Examples

A server's Defaults Information might contain two Object Defaults entries: one for Symmetric Keys (Cryptographic Algorithm = AES, Cryptographic Length = 256, Cryptographic Usage Mask = Encrypt | Decrypt) and one for Private Keys (Cryptographic Algorithm = RSA, Cryptographic Length = 2048). A client that calls Create with Object Type = Symmetric Key and no Algorithm or Length specified will receive a key with those default values applied by the server.

## Related

[Object Defaults](object-defaults.md) · [Set Defaults](../operations/set-defaults.md) · [Get Constraints](../operations/get-constraints.md) · [Attribute](attribute.md)
