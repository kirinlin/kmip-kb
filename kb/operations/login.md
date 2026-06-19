---
title: Login
category: operation
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "6.1.30"
status: reviewed
related: ["logout", "delegated-login", "authentication", "query", "protocol-version"]
keywords: ["login", "session", "authentication", "session ticket", "stateful session", "credential", "session management"]
---

# Login

## Purpose

`Login` establishes an authenticated, stateful session at the KMIP protocol layer. A client sends its credentials in the request; the server validates them and returns a session ticket (handle). The client includes this ticket in the Authentication field of subsequent requests, avoiding the overhead of re-sending full credentials with every message. This is particularly valuable when credential verification is computationally expensive — for example, when credentials involve certificate chain validation or an external identity provider lookup.

`Login` was introduced in v2.1 alongside [`Logout`](logout.md) and [`Delegated Login`](delegated-login.md) to give KMIP a first-class session model. Prior to v2.1, clients re-authenticated with every request; v2.1 implementations may support both modes.

## Request Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Authentication | `42000C` | `Authentication` | Yes | The credential the client wishes to authenticate with. This is the standard [Authentication](../concepts/authentication.md) structure — it may contain a username/password, a certificate, a token, or another credential type the server supports. |

## Response Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Session Handle |  |  | Yes | An opaque, server-issued token representing the authenticated session. The client passes this value in the Authentication field of subsequent requests to assert its identity without re-sending the full credential. |

## Behavior & Server Requirements

The server validates the supplied credential using its configured authentication mechanism. On success, it allocates a session, records the authenticated identity and session metadata (creation time, expiry, associated access controls), and returns the Session Handle.

The handle is opaque to the client — it has no defined structure that clients should parse or construct. Its sole purpose is to be echoed back in later requests.

Sessions have a server-configured lifetime. If a session expires, subsequent requests bearing the expired handle are rejected with an authentication error, prompting the client to call `Login` again. Servers may also enforce concurrent-session limits per identity.

A client that successfully calls `Login` should always pair it with a [`Logout`](logout.md) when done, to release server resources and invalidate the handle immediately rather than waiting for timeout.

Servers that support session-based authentication must advertise this via [`Query`](query.md). Servers that do not support `Login` return Operation Not Supported; clients must then re-authenticate per request as in pre-v2.1 behavior.

A client may call `Login` while already holding an active session. The server either returns the same handle (if the session is still valid) or creates a new session, according to server policy.

## Errors

Uses centralized error handling per the [error handling](../concepts/error-handling.md) conventions. Common failure causes include:

- The credential is invalid, expired, or does not match any known identity.
- The server does not support the supplied credential type.
- The identity has reached the maximum number of concurrent sessions.
- The server does not support `Login` — returns Operation Not Supported.
- The server's session store is unavailable.

## Examples

A service that rotates encryption keys once per hour authenticates at startup and reuses the session ticket for all rotation calls during its run:

```
Operation: Login
  Authentication:
    Credential Type: Username and Password
    Credential Value:
      Username: "keymgr-svc"
      Password: <service password>
```

The server responds with a Session Handle, e.g. `"session-9f3a"`. All subsequent requests from this client include:

```
Authentication:
  Session Handle: "session-9f3a"
```

When the service shuts down it calls [`Logout`](logout.md) to invalidate the session.

## Related Operations

[Logout](logout.md) · [Delegated Login](delegated-login.md) · [Query](query.md)
