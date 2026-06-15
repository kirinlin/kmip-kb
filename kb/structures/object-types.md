---
title: Object Types
category: structures
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "7.24"
status: reviewed
related: ["objects", "query", "locate", "object-type", "server-information"]
keywords: ["object types", "supported object types", "object type list", "query response", "locate filter", "420167", "ObjectTypes"]
tag_hex: "420167"
xml_text: "ObjectTypes"
---

# Object Types

## Overview

Object Types is a structure that carries a list of Object Type Enumeration values. It has two distinct uses in the KMIP protocol:

1. In [Query](../operations/query.md) responses, the server includes an Object Types structure to advertise which kinds of managed objects it supports — telling clients whether they can expect to store Symmetric Keys, Certificates, Secret Data, and so on.
2. In [Locate](../operations/locate.md) requests, a client may supply an Object Types filter to restrict the search to objects of specific types.

## Encoding (Tag / Type / Length / Value)

Object Types encodes as a Structure containing one or more Object Type Enumeration values.

| Field | Tag | XML Element | Type | Required |
|---|---|---|---|---|
| Object Type | `420057` | `ObjectType` | Enumeration | One or more |

Each Enumeration child corresponds to one supported or targeted object type. The order of entries is not significant.

## Fields & Structure

The Object Type Enumeration values mirror the object classes defined in the KMIP Objects section:

- Symmetric Key
- Public Key
- Private Key
- Split Key
- Certificate
- Secret Data
- Opaque Object
- PGP Key
- Certificate Request

A server that does not support a particular object type omits it from the Query response list. Clients should check this list before attempting to register or create objects of a type that may be unsupported.

When used as a Locate filter the structure lists the acceptable types; the server returns only objects whose Object Type attribute matches one of the listed values.

## Examples

A Query response for a server that supports symmetric keys, asymmetric key pairs, and certificates (but not Split Keys or PGP Keys) would include an Object Types structure with three entries: Symmetric Key, Public Key, Private Key, and Certificate.

A Locate request restricted to certificates only would include an Object Types structure containing a single entry: Certificate.

## Related

[Objects](objects.md) · [Query](../operations/query.md) · [Locate](../operations/locate.md) · [Object Type (attribute)](../attributes/object-type.md) · [Server Information](server-information.md)
