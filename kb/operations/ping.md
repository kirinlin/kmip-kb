---
title: Ping
category: operation
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "6.1.36"
status: reviewed
related: ["query", "interop", "protocol-version"]
keywords: ["ping", "health check", "liveness", "connectivity test", "server status", "keepalive"]
---

# Ping

## Purpose

`Ping` tests whether a KMIP server is reachable and responding without performing any management operation. An empty or minimal request triggers a success response, confirming that the server is alive and the transport connection is functional. `Ping` is lighter weight than [`Query`](query.md) for pure connectivity checks: `Query` returns a potentially large response carrying capability lists, while `Ping` returns only a result status.

`Ping` was introduced in v2.1 and is useful in monitoring agents, load balancers, and connection-pool health checks that need to verify server availability frequently without incurring meaningful load.

## Request Fields

`Ping` carries no mandatory payload fields. The request body may be empty.

| Field | Required | Description |
|---|---|---|
| Correlation Value | No | An opaque client-chosen value that the server echoes back in the response. Allows a caller to correlate a specific ping request with its response when multiple concurrent pings are in flight. |

## Response Fields

| Field | Required | Description |
|---|---|---|
| Correlation Value | No | Present if the request included a Correlation Value; echoed back unchanged. |

## Behavior & Server Requirements

The server processes the request by returning a success result as quickly as possible. It performs no object lookups, no attribute evaluations, and no state changes. The round-trip latency of a successful `Ping` reflects transport overhead plus the server's minimal dispatch cost.

If [Authentication](../concepts/authentication.md) is required by the server, `Ping` must include valid credentials just like any other operation. A server may choose to accept `Ping` unauthenticated as a connectivity probe — this is a server policy decision and must be documented by the implementation.

`Ping` may be included in a batch request alongside other operations, in which case its response appears at the corresponding position in the batch response. This lets a client verify connectivity and perform operations in a single round-trip.

Servers must support `Ping`; it is not optional in v2.1.

## Errors

Uses centralized error handling per the [error handling](../concepts/error-handling.md) conventions. `Ping` has very few error cases:

- The request requires authentication and none was supplied — returns authentication failure.
- The server is overloaded and rejects the request — returns an appropriate busy or throttle error.

A transport-level failure (TCP connection refused, TLS handshake error) is never represented as a KMIP error response — those are indicated by the absence of any response.

## Examples

A monitoring daemon pings the KMIP server every 30 seconds to confirm availability:

```
Operation: Ping
  Correlation Value: "monitor-tick-20260612-030000"
```

Response:

```
Operation: Ping (Response)
  Result Status: Success
  Correlation Value: "monitor-tick-20260612-030000"
```

A connection pool manager sends a `Ping` before handing an idle connection to a new requestor to ensure the connection is still alive:

```
Operation: Ping
  (no fields)
→ Result Status: Success
```

## Related Operations

[Query](query.md) · [Interop](interop.md)
