---
title: Query (Server-to-Client)
category: operation
spec_version: "2.1"
spec_versions: ["1.3", "1.4", "2.0", "2.1"]
source_section: "6.2.4"
v1_source_section: "5.3"
status: reviewed
related: ["notify", "put", "query", "discover-versions", "capability-information", "profile-information"]
keywords: ["query", "server-to-client", "client capabilities", "interrogate client", "client registration"]
---

# Query (Server-to-Client)

## Purpose

Added in KMIP 1.3, this is the mirror image of the client-to-server
[Query](../query.md): the server interrogates the client to learn what the
client can do — which operations and object types it supports, which
profiles, RNGs, validations, attestation types, and registration methods.
It supports scenarios such as client registration, where a server must size
up a device before provisioning it.

## Request Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Query Function | `420074` | `QueryFunction` | Yes (repeatable) | What to ask about: operations, objects, server information, extension list/map, attestation types, RNGs, validations, profiles, capabilities, or client registration methods. |

## Response Fields

All response fields are optional and appear only when requested (and
supported by the client):

| Field | Tag | XML Element | Description |
|---|---|---|---|
| Operation (repeatable) | `42005C` | `Operation` | Operations the client supports. |
| Object Type (repeatable) | `420057` | `ObjectType` | Managed object types the client supports. |
| Vendor Identification / Server Information |  |  | Vendor string and vendor-specific structure. |
| Extension Information (repeatable) | `4200A4` | `ExtensionInformation` | Vendor [extensions](../../structures/extension-information.md) the client understands; the map variant adds tags and types. |
| Attestation Type (repeatable) | `4200C7` | `AttestationType` | Attestation evidence formats the client can produce. |
| RNG Parameters (repeatable) | `4200D9` | `RNGParameters` | The client's [random number generators](../../structures/rng-parameters.md). |
| Profile Information (repeatable) | `4200EB` | `ProfileInformation` | [Profiles](../../structures/profile-information.md) the client conforms to. |
| Validation Information (repeatable) | `4200DF` | `ValidationInformation` | Formal [validations](../../structures/validation-information.md) (e.g. FIPS 140) the client asserts. |
| Capability Information (repeatable) | `4200F7` | `CapabilityInformation` | [Capabilities](../../structures/capability-information.md) such as streaming or asynchronous support. |
| Client Registration Method (repeatable) | `4200F6` | `ClientRegistrationMethod` | Registration methods the client supports. |

## Behavior & Server Requirements

The exchange runs over a server-initiated channel like [Notify](notify.md)
and [Put](put.md). The spec recommends that clients answer this Query even
from servers that have not authenticated, since its whole point is feature
discovery. A client with nothing to report for the requested functions
returns an empty payload. If both the extension-list and extension-map
functions are requested at once, only the map answer is returned.

## Errors

Uses the centralized [error handling](../../concepts/error-handling.md); the
client fails the batch item if it cannot satisfy the request.

## Examples

During enrollment of a new appliance, the server sends Query with Query
Function = Query Operations + Query Client Registration Methods. The
appliance answers that it supports Get, Put responses, and the
Server Pre-Generated registration method, letting the server choose how to
provision its first keys.

## Related Operations

[Query (client-to-server)](../query.md) · [Notify](notify.md) ·
[Put](put.md) · [Discover Versions](../discover-versions.md)
