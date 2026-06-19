---
title: Query
category: operation
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.40"
v1_source_section: "4.25"
status: reviewed
related: ["discover-versions", "profile-information", "rng-parameters"]
keywords: ["query", "capabilities", "server information", "feature discovery", "supported operations"]
---

# Query

## Purpose

`Query` lets a client interrogate a server about its capabilities — which
operations and object types it supports, what profiles and validations it
asserts, vendor details, and more. It is the main feature-discovery operation,
and servers should allow even unauthenticated clients to call it.

## Request Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Query Function | `420074` | `QueryFunction` | Yes (may repeat) | One or more selectors naming the categories of information to return. |

The Query Function values select what the response contains. Defined selectors
cover supported operations, supported object types, server information,
application namespaces, an extension list and extension map, attestation types,
RNGs, validations, profiles, capabilities, and client registration methods.

## Response Fields

The response carries only the items that correspond to the requested selectors
(and that the server actually supports); it is empty when there is nothing to
report. Possible items include:

| Field | Tag | XML Text | Description |
|---|---|---|---|
| Operation | `42005C` | `Operation` | An operation the server supports. |
| Object Type | `420057` | `ObjectType` | A managed object type the server supports. |
| Vendor Identification | `42009D` | `VendorIdentification` | A text string identifying the vendor (returned with server information). |
| Server Information | `420088` | `ServerInformation` | A vendor-specific structure of additional detail. |
| Application Namespace | `420003` | `ApplicationNamespace` | A namespace the server can generate values for. |
| Extension Information | `4200A4` | `ExtensionInformation` | A description of a supported extension object. |
| Attestation Type | `4200C7` | `AttestationType` | An attestation type the server supports. |
| RNG Parameters | `4200D9` | `RNGParameters` | A random number generator the server supports. |
| Profile Information | `4200EB` | `ProfileInformation` | A profile the server supports, and how. |
| Validation Information | `4200DF` | `ValidationInformation` | A formal validation the server asserts. |
| Capability Information | `4200F7` | `CapabilityInformation` | A capability of the server. |
| Client Registration Method | `4200F6` | `ClientRegistrationMethod` | A client registration method the server supports. |

## Behavior & Server Requirements

Each selector governs one part of the response, returned only if requested and
supported. A couple of special cases: when both the extension list and the
extension map are requested, the server answers only the map and ignores the
list; and when RNG details are requested but the server cannot describe its
generator, it returns RNG parameters with an algorithm of "unspecified". Items
the server does not support are simply absent.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). `Query` is
designed to succeed broadly; an unsupported selector yields no corresponding
items rather than an error.

## Examples

A client that wants to know what a server can do sends `Query` with the
"Query Operations" and "Query Objects" selectors and receives the lists of
supported operations and object types, which it can use to decide how to
proceed.

## Related Operations

[Discover Versions](discover-versions.md)
