---
title: Logout
category: operation
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "6.1.31"
status: reviewed
related: ["login", "delegated-login", "authentication", "query"]
keywords: ["logout", "session termination", "session invalidation", "session handle", "end session", "disconnect"]
---

# Logout

## Purpose

`Logout` terminates an active KMIP session that was established by a prior [`Login`](login.md) or [`Delegated Login`](delegated-login.md). The client presents the session handle it received at login; the server invalidates that handle immediately. Any subsequent request that references the invalidated handle is rejected with an authentication error, regardless of whether the original session's expiry time had been reached.

Calling `Logout` is the correct way to end a session cleanly. Relying on session timeout to clean up is acceptable but leaves the handle valid longer than necessary and wastes server session resources.

## Request Fields

`Logout` carries no payload fields beyond the standard message header. The session to terminate is identified by the Session Handle embedded in the Authentication field of the request.

| Field | Required | Description |
|---|---|---|
| Authentication (Session Handle) | Yes | The session ticket issued at [`Login`](login.md) time, supplied in the standard Authentication field. This is how the server identifies which session to invalidate. |

## Response Fields

The response contains only the standard result status. No payload fields are returned on success.

| Field | Required | Description |
|---|---|---|
| Result Status | Yes | Confirms that the session was successfully invalidated. |

## Behavior & Server Requirements

The server looks up the session associated with the provided handle. If the session exists and is currently active, the server marks it as terminated and releases any server-side resources allocated to it (memory, any held locks, cached credential material, etc.).

If the handle does not correspond to any active session — because it already expired or was already logged out — the server may return success (idempotent behavior) or an error, depending on server policy. Clients should not rely on either behavior; they should track session state themselves.

`Logout` applies only to the session identified by the presented handle. If the same identity has multiple concurrent sessions (obtained through separate `Login` calls), only the session matching the supplied handle is terminated; other sessions remain active.

Servers that support `Login` must support `Logout`. A server that does not support session management returns Operation Not Supported for both operations.

## Errors

Uses centralized error handling per the [error handling](../concepts/error-handling.md) conventions. Common failure causes include:

- The Authentication field does not contain a session handle, or the handle is malformed.
- The session handle is not recognized (already expired, already logged out, or was never valid).
- The server does not support session management — returns Operation Not Supported.

## Examples

A batch processing job logs in at the start, performs all its key management work, and logs out when done:

```
Operation: Login
  Authentication: <credentials>
→ Session Handle: "session-b2c7"

  ... many operations using Session Handle "session-b2c7" ...

Operation: Logout
  Authentication:
    Session Handle: "session-b2c7"
→ Result Status: Success
```

After the `Logout` response, any attempt to use `"session-b2c7"` returns an authentication failure.

## Related Operations

[Login](login.md) · [Delegated Login](delegated-login.md) · [Query](query.md)
