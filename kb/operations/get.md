---
title: Get
category: operation
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.19"
v1_source_section: "4.11"
status: reviewed
related: ["locate", "get-attributes", "register", "key-wrapping-specification", "symmetric-key"]
keywords: ["get", "retrieve object", "fetch key", "key wrapping", "PKCS#12", "key format"]
---

# Get

## Purpose

`Get` retrieves a single managed object by its identifier, returning the object
itself along with its type. It is how a client obtains key material,
certificates, and other objects after locating or creating them. The returned
object may optionally be wrapped for protection in transit.

## Request Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | No | The object to retrieve; the ID Placeholder is used when omitted. |
| Key Format Type | `420042` | `KeyFormatType` | No | The format in which the client wants the key returned. |
| Key Wrap Type | `4200F8` | `KeyWrapType` | No | The wrap form to apply to the key bytes that come back. |
| Key Compression Type | `420041` | `KeyCompressionType` | No | How elliptic-curve public keys should be compressed. |
| Key Wrapping Specification | `420047` | `KeyWrappingSpecification` | No | The keys and parameters for wrapping the returned object. Not allowed when the object is a Template. |

## Response Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Object Type | `420057` | `ObjectType` | Yes | The type of the returned object. |
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes | The object's identifier. |
| Managed Object |  |  | Yes | The object itself (key, certificate, secret data, opaque object, etc.). |

## Behavior & Server Requirements

Only one object is returned per `Get`. A client can always retrieve a key in the
same format in which it was registered; servers may additionally offer format
conversions but are not required to. Requesting the PKCS#12 format is a special
case: the identifier must name a private key, the response is an
[RFC 7292] PKCS#12 container protected by the secret-data object that the
private key points to via its Secret Data link. The certificate chain is built by stepping
from the private key to its public key, then to that key's base certificate, and
on up the chain certificate by certificate — it is an error if more than one
valid chain exists.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: an unknown object, a requested format the server cannot produce, an
invalid wrapping specification, or insufficient permission.

## Examples

After a [Locate](locate.md) returns a key's identifier, the client issues
`Get` with that identifier (or relies on the ID Placeholder when the two are
batched) and receives the key object. To receive it wrapped, the client adds a
Key Wrapping Specification naming the wrapping key.

## Related Operations

[Locate](locate.md) · [Get Attributes](get-attributes.md) ·
[Register](register.md)
