---
title: Register
category: operation
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.43"
v1_source_section: "4.3"
status: draft
related: ["create", "create-key-pair", "import", "get", "symmetric-key", "certificate", "secret-data"]
keywords: ["register", "import object", "store key", "client-supplied key", "provisioning"]
---

# Register

## Purpose

`Register` hands the server an object that the client already possesses — one it
generated itself or obtained elsewhere — so the server takes over managing it.
It mirrors [Create](create.md), except the client supplies the actual object
rather than asking the server to generate it. Any managed object type can be
registered: keys, certificates, secret data, split keys, opaque objects, and
(in earlier versions) templates.

## Request Fields

| Field | Required | Description |
|---|---|---|
| Object Type | Yes | The type of object being handed over. |
| Template-Attribute | Yes | The attributes to associate with the object, given individually and/or via named templates. |
| Managed Object | Yes | The object itself (for example a [Symmetric Key](../objects/symmetric-key.md), [Certificate](../objects/certificate.md), private/public key, split key, secret data, or opaque object). The object and its attributes may be supplied in wrapped form. |

## Response Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | Yes | The identifier the server assigns to the registered object. |
| Template-Attribute | No | Attributes the server set implicitly that were not in the request. |

## Behavior & Server Requirements

The server stores the supplied object, assigns it a fresh [Unique Identifier](../attributes/unique-identifier.md),
sets the object's [Initial Date](../attributes/initial-date.md) to the current
time, and copies the identifier into the ID Placeholder. When registering a
cryptographic object, the request must also carry the algorithm and length
(unless that information is already embedded in the key block) along with the
usage mask; certificates additionally require their certificate length and
digital signature algorithm (unless embedded in the certificate itself).

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Common
causes: a missing required attribute for the object type, an object that does
not match its declared type, malformed key/certificate material, or
insufficient permission.

## Examples

A client that has generated its own AES key locally registers it by sending
Object Type = Symmetric Key, the key block holding the raw bytes, and attributes
for algorithm, length, and usage mask. The server returns a Unique Identifier
the client can use thereafter.

## Related Operations

[Create](create.md) · [Create Key Pair](create-key-pair.md) ·
[Import](import.md) · [Get](get.md)
