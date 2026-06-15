---
title: Objects
category: structures
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "7.21"
status: reviewed
related: ["object-types", "unique-identifier", "query", "locate", "message-structure"]
keywords: ["objects structure", "object list", "query response", "unique identifier list", "managed objects summary"]
tag_hex: "42014E"
xml_element: "Objects"
---

# Objects

## Overview

Objects is a wrapper structure used in response payloads — most notably in [Query](../operations/query.md) responses — to bundle a collection of managed object references. Each entry in the structure associates a Unique Identifier with an Object Type, giving the client a compact index of which objects exist on the server without requiring a full Get of each one.

The structure is the response-side counterpart to a Locate or batch-query workflow: Locate returns Unique Identifiers that the client can then look up; Objects pre-packages a summary (identifier plus type) so the client can quickly determine what kinds of objects are present.

## Encoding (Tag / Type / Length / Value)

Objects encodes as a Structure containing one or more Object entries, each of which is itself a small Structure.

| Field | Tag | XML Element | Type | Required |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Text String | One per object |
| Object Type | `420057` | `ObjectType` | Enumeration | One per object |

The Unique Identifier and Object Type appear as siblings within a repeating unit. Depending on encoding context they may be grouped in a per-object sub-structure or interspersed in sequence; implementations must pair them by position.

## Fields & Structure

**Unique Identifier** is the server-assigned string that uniquely identifies the managed object on the server. It is the primary key for all subsequent operations — Get, Activate, Destroy, and so on.

**Object Type** classifies the object: Symmetric Key, Private Key, Public Key, Certificate, Secret Data, etc. Clients can use this to determine whether they care about a given object before fetching its full representation.

The Objects structure is a summary view. It does not carry attribute values, key material, or any other object data beyond identification and type. Clients needing more information must issue separate Get or Get Attributes requests for the objects they are interested in.

## Examples

A Query response might include an Objects structure listing three entries:

- Unique Identifier = `"uid-001"`, Object Type = Symmetric Key
- Unique Identifier = `"uid-002"`, Object Type = Certificate
- Unique Identifier = `"uid-003"`, Object Type = Private Key

A client that only processes symmetric keys can immediately filter to `"uid-001"` without fetching the certificate or private key.

## Related

[Object Types](object-types.md) · [Unique Identifier](../attributes/unique-identifier.md) · [Query](../operations/query.md) · [Locate](../operations/locate.md) · [Message Structure](../messages/message-structure.md)
