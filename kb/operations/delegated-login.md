---
title: Delegated Login
category: operation
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "6.1.12"
status: reviewed
related: ["login", "logout", "authentication", "query"]
keywords: ["delegated login", "delegation", "impersonation", "credential", "session", "proxy login", "on behalf of", "service account"]
---

# Delegated Login

## Purpose

`Delegated Login` allows one authenticated principal to establish a KMIP session on behalf of a second principal. The calling client holds a delegation token or credential that authorizes it to act for the delegated identity, and the server creates a session as though the delegated party had initiated a normal [`Login`](login.md) directly. This enables proxy architectures, service-account flows, and workload-identity scenarios where an intermediary — such as a key broker or orchestration layer — manages multiple user or device sessions without each downstream entity connecting to the KMIP server independently.

`Delegated Login` was introduced in v2.1 as part of the same session-management addition that brought [`Login`](login.md) and [`Logout`](logout.md).

## Request Fields

| Field | Required | Description |
|---|---|---|
| Authentication | Yes | The credential of the delegating principal — the client making the call. This is the standard message-level [Authentication](../concepts/authentication.md) field and identifies who is performing the delegation. |
| Delegated Credential | Yes | The token, certificate, or credential structure that authorizes the caller to represent the delegated identity. The server uses this to determine the identity of the session being established. |

## Response Fields

| Field | Required | Description |
|---|---|---|
| Session Handle | Yes | A server-issued session ticket representing the delegated session, equivalent to what the delegated principal would receive from a direct [`Login`](login.md). The proxy uses this handle in the Authentication field of subsequent requests made on behalf of the delegated party. |

## Behavior & Server Requirements

The server first authenticates the calling client using the standard request credential, then validates the Delegated Credential to confirm the delegation chain is legitimate. If both succeed, the server creates a new session scoped to the delegated identity, governed by that identity's access controls and policies — not the delegating client's.

The resulting session is independent of the delegating client's own session. It must be explicitly terminated via [`Logout`](logout.md) using the session handle returned here, or it expires according to the server's session timeout policy.

Servers are not required to support `Delegated Login`. A server that does must advertise the capability in its [`Query`](query.md) response. Implementations must enforce the principle of least privilege: a delegated session cannot acquire permissions beyond those the delegated principal holds, regardless of the delegating client's own privilege level.

Audit logs should record both the delegating principal and the delegated identity, ensuring that actions taken via a delegated session are fully attributable to the delegated party rather than the intermediary.

## Errors

Uses centralized error handling per the [error handling](../concepts/error-handling.md) conventions. Common failure causes include:

- The Delegated Credential is invalid, expired, or has been revoked.
- The calling client is not authorized to delegate on behalf of the target identity.
- The server does not support `Delegated Login` — returns Operation Not Supported.
- The delegated identity does not exist or is not permitted to hold sessions on this server.
- The maximum number of concurrent sessions for the delegated identity has been reached.

## Examples

A key broker managing sessions for a fleet of IoT devices authenticates to the KMIP server with its own service certificate, then calls `Delegated Login` for each device, presenting that device's identity token as the Delegated Credential. The broker receives a per-device session handle and uses it in all subsequent requests on behalf of that device.

When a device is decommissioned, the broker calls [`Logout`](logout.md) with that device's session handle, cleanly terminating the delegated session without affecting the broker's own session or any other device sessions.

## Related Operations

[Login](login.md) · [Logout](logout.md) · [Query](query.md)
