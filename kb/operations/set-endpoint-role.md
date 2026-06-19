---
title: Set Endpoint Role
category: operation
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "6.1.54"
status: reviewed
related: ["query", "login", "protocol-version"]
keywords: ["set endpoint role", "endpoint role", "client role", "key management client", "key management server", "proxy", "role negotiation"]
---

# Set Endpoint Role

## Purpose

`Set Endpoint Role` (client-initiated, §6.1.54) allows a client to declare its endpoint role to the server at connection time or during a session. The client announces whether it is acting as a Key Management Client, a Key Management Server, a Proxy, or another defined role enumeration value. This declaration helps the server tailor its behavior — for example, granting additional capabilities to a client that identifies itself as an intermediary key management server, or adjusting policy for a proxy that aggregates requests from many downstream clients.

The server-initiated counterpart — where the server instructs the client which role to assume — is the `Set Endpoint Role` server-to-client operation at §6.2.5 (see [Set Endpoint Role (server-to-client)](server-to-client/set-endpoint-role.md)).

Both forms were introduced in v2.1.

## Request Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Endpoint Role | `420151` | `EndpointRole` | Yes | An enumeration value indicating the role the client is claiming. Standard values include Key Management Client, Key Management Server, and Proxy. The full set of valid values is defined in the KMIP v2.1 Endpoint Role enumeration. |

## Response Fields

The response contains only the standard result status — no payload fields are returned on success.

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Result Status | `42007F` | `ResultStatus` | Yes | Confirms whether the server accepted the declared role. A server that does not recognize or support the declared role may return an error or may silently accept it; behavior is server-dependent. |

## Behavior & Server Requirements

The server records the declared role for the current session or connection context. Subsequent operations by the same client may be evaluated against role-based policies. For example, a client declaring itself a Key Management Server might be granted access to operations — such as wrapping keys for distribution — that are not available to ordinary clients.

The server is not required to trust or act on the client's self-declared role. Servers that enforce strong role governance should validate the role claim against the authenticated identity (e.g., confirming that the certificate presented at authentication is issued to an entity authorized to act as a key management server) rather than accepting any client's self-declaration unconditionally.

If neither the client nor the server calls `Set Endpoint Role`, both parties operate under their default role (typically Key Management Client for the connecting party and Key Management Server for the accepting party).

`Set Endpoint Role` may be called at any time during a session, though best practice is to call it immediately after [`Login`](login.md) or at connection setup.

## Errors

Uses centralized error handling per the [error handling](../concepts/error-handling.md) conventions. Common failure causes include:

- The supplied Endpoint Role value is not a valid enumeration member.
- The calling client is not authorized to claim the specified role based on its authenticated identity.
- The server does not support the `Set Endpoint Role` operation — returns Operation Not Supported.

## Examples

A KMIP proxy that sits between application servers and a root key management server declares its role after connecting:

```
Operation: Set Endpoint Role
  Endpoint Role: Proxy
```

The server acknowledges with `Result Status: Success` and subsequently applies proxy-specific policies to the session, such as allowing the client to perform key-wrapping operations for distribution to downstream clients.

## Related Operations

[Set Endpoint Role (server-to-client)](server-to-client/set-endpoint-role.md) · [Login](login.md) · [Query](query.md)
