---
title: Application Specific Information
category: attribute
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.4"
v1_source_section: "3.36"
status: reviewed
related: ["object-group", "custom-attribute", "name"]
keywords: ["application specific information", "application namespace", "application data", "ASI", "420004", "ApplicationSpecificInformation"]
tag_hex: "420004"
xml_text: "ApplicationSpecificInformation"
---

# Application Specific Information

## Purpose

Lets applications stamp their own usage metadata onto an object under a
namespace — e.g. namespace `ssl` with data `www.example.com`, or a tape
library namespace with a volume identifier. Heavily used by storage
ecosystems to find "the key for *this* volume" via
[Locate](../operations/locate.md).

## Data Type & Structure

A structure:

| Field | Tag | XML Element | Required | Type |
|---|---|---|---|---|
| Application Namespace | `420003` | `ApplicationNamespace` | Yes | Text String |
| Application Data | `420002` | `ApplicationData` | No | Text String |

There is a twist when Application Data is omitted *by the client*: if the
server supports that namespace (advertised through
[Query](../operations/query.md)'s application-namespaces function), it must
generate a suitable data value itself — useful for server-assigned
identifiers; if it does not support the namespace, the request fails with
`Application Namespace Not Supported`.

## Constraints

- Optional; multi-instance (one instance per namespace/data pairing).
- Namespace registries are a server/ecosystem convention; KMIP does not
  define the names.

## Applies To (Object Types)

All managed objects.

## Set / Modified By

Client normally; server only in the omitted-data case above. Client-
modifiable and deletable. Carried to successor objects implicitly by
[Re-key](../operations/re-key.md),
[Re-key Key Pair](../operations/re-key-key-pair.md), and
[Re-certify](../operations/re-certify.md).

## Related Attributes

[Object Group](object-group.md) · [Custom Attribute](custom-attribute.md) ·
[Name](name.md)
