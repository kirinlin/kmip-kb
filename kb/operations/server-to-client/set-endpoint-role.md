---
title: Set Endpoint Role (server-to-client)
category: operation
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "6.2.5"
status: reviewed
related: ["query", "login", "discover-versions", "protocol-version"]
keywords: ["set endpoint role", "server-to-client", "endpoint role", "role assignment", "server-initiated", "proxy", "key management server"]
---

# Set Endpoint Role (server-to-client)

## Purpose

`Set Endpoint Role` (server-to-client, §6.2.5) is the server-initiated form: the server instructs the connecting client which endpoint role to assume, rather than the client self-declaring its own role. The server sends an Endpoint Role enumeration value and the client is expected to adopt that role for the session. This allows a centrally managed environment to assign roles authoritatively based on server-side policy or the client's authenticated identity, without relying on client self-declaration.

The client-initiated counterpart — where the client announces its own role — is the `Set Endpoint Role` client operation at §6.1.54 (see [Set Endpoint Role (client-initiated)](../set-endpoint-role.md)).

Both forms were introduced in v2.1.

## Request Fields (server-to-client)

The server sends the following in the server-initiated message:

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Endpoint Role | `420151` | `EndpointRole` | Yes | The role enumeration value the server is assigning to the client. Standard values include Key Management Client, Key Management Server, and Proxy. |

## Response Fields (client response)

The client acknowledges the role assignment:

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Result Status | `42007F` | `ResultStatus` | Yes | `Success` if the client accepts and can operate in the assigned role; an error if the client cannot or will not accept the role. |

## Behavior & Server Requirements

The server sends this message when it wants to authoritatively assign a role to the connected client — typically immediately after authentication or after [`Login`](../login.md). The client receives the role instruction, adjusts its behavior accordingly (for example, enabling proxy-mode request batching), and responds.

If the client cannot operate in the assigned role — because it lacks the necessary capabilities or because the role conflicts with its configuration — it should respond with an appropriate error. The server may then terminate the connection or fall back to a default role.

This server-to-client pattern is particularly useful in architectures where the server maintains a directory mapping client identities to approved roles, ensuring consistent role assignment even if clients do not call the client-initiated `Set Endpoint Role` operation.

A client that does not implement the server-to-client message model cannot participate in server-driven role assignment. Such clients operate under the default role only.

## Errors

Common failure causes:

- The client does not recognize or cannot operate in the assigned Endpoint Role — the client returns an error.
- The Endpoint Role value in the message is not a valid enumeration member — the client should return an invalid field error.
- The client does not implement the server-to-client message model — the server handles the lack of response according to its timeout and session policy.

## Examples

A server that manages both regular clients and KMIP proxy nodes uses the authenticated certificate subject to determine the appropriate role and sends it to the client at session start:

```
Server → Client:
  Operation: Set Endpoint Role
  Endpoint Role: Proxy
```

The client, which is indeed a KMIP proxy, accepts the role:

```
Client → Server:
  Result Status: Success
```

The server then applies proxy-specific policies — such as allowing the client to wrap keys for distribution to its downstream fleet — for the remainder of the session.

## Related Operations

[Set Endpoint Role (client-initiated)](../set-endpoint-role.md) · [Discover Versions (server-to-client)](discover-versions.md) · [Login](../login.md) · [Query](../query.md)
