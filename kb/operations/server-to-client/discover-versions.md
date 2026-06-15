---
title: Discover Versions (server-to-client)
category: operation
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "6.2.1"
status: reviewed
related: ["query", "protocol-version", "set-endpoint-role", "login"]
keywords: ["discover versions", "server-to-client", "protocol version", "version negotiation", "server-initiated", "proactive negotiation"]
---

# Discover Versions (server-to-client)

## Purpose

`Discover Versions` (server-to-client, §6.2.1) is the server-initiated form of version discovery. Rather than waiting for the client to ask which protocol versions the server supports, the server proactively pushes its supported version list to the client. This allows the server to drive version negotiation — for example, after a server upgrade or when the server detects that the client is using a sub-optimal protocol version.

The information conveyed is the same as what a client receives when it sends a client-initiated [`Query`](../query.md) with a Protocol Version query function, but here the server sends it without being asked.

Server-to-client operations in KMIP v2.1 travel in the same TTLV message framing as client-to-server operations, with the direction indicated by message headers. A server-to-client `Discover Versions` appears as a server-generated request to which the client is expected to respond.

## Request Fields (server-to-client)

The server sends the following in the server-initiated message:

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Protocol Version | `420069` | `ProtocolVersion` | Yes (one or more) | One or more [Protocol Version](../../ttlv/protocol-version.md) structures, each identifying a KMIP major.minor version the server is willing to use. Ordered from most to least preferred. |

## Response Fields (client response)

The client acknowledges the server's version advertisement:

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Protocol Version | `420069` | `ProtocolVersion` | Yes | The single [Protocol Version](../../ttlv/protocol-version.md) value the client selects from the server's list. Indicates the version the client will use for subsequent communication. |

## Behavior & Server Requirements

The server may send a `Discover Versions` message at any point where it needs to (re-)negotiate the protocol version — typically at connection establishment, after a server reload, or when rolling out an upgrade. The client processes the list and responds with its chosen version.

If the client cannot support any of the versions in the server's list, it should respond with an error indicating version incompatibility. The connection may then be terminated.

Version negotiation is not strictly required on every connection; many deployments statically configure both endpoints to use the same version. `Discover Versions` (server-to-client) is the dynamic alternative for environments where version flexibility is needed.

Clients that do not implement server-to-client message handling cannot participate in server-initiated version negotiation.

## Errors

Common failure causes:

- The client does not support any version in the server's list — the client returns a version mismatch error.
- The client does not implement the server-to-client message model and ignores or rejects the message — the server must handle the absence of a response gracefully.

## Examples

After upgrading from KMIP v2.0 to v2.1 support, a server sends a `Discover Versions` message to an existing client connection to negotiate the new version:

```
Server → Client:
  Operation: Discover Versions
  Protocol Version: 2.1
  Protocol Version: 2.0
  Protocol Version: 1.4
```

The client supports v2.1 and responds:

```
Client → Server:
  Protocol Version: 2.1
```

Both sides then switch to using v2.1 message encoding for subsequent communication on this connection.

## Related Operations

[Query](../query.md) · [Set Endpoint Role (server-to-client)](set-endpoint-role.md) · [Protocol Version](../../ttlv/protocol-version.md)
