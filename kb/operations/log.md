---
title: Log
category: operation
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "6.1.29"
status: reviewed
related: ["query", "ping", "log-message", "authentication"]
keywords: ["log", "audit log", "log message", "audit trail", "client logging", "event logging"]
---

# Log

## Purpose

`Log` submits a client-generated entry to the server's audit log. Rather than maintaining a separate client-side log that must later be correlated with server-side records, a client can use `Log` to write events directly into the centralized key management audit trail. This is useful for recording application-level events — such as a key being used to encrypt a specific document, or a policy decision being made — alongside the server's own record of KMIP operations, without requiring the client to maintain its own logging infrastructure.

`Log` was introduced in v2.1 and uses the [Log Message](../ttlv/log-message.md) structure as its primary payload.

## Request Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Log Message | `420141` | `LogMessage` | Yes | The [Log Message](../ttlv/log-message.md) structure carrying the content of the log entry. Includes the log message text; may also carry a log level indicator and a timestamp. |

## Response Fields

The response carries only the standard result status. No payload fields are returned on success.

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Result Status | `42007F` | `ResultStatus` | Yes | Indicates whether the server accepted and persisted the log entry. |

## Behavior & Server Requirements

The server appends the supplied log entry to its audit log using the same facilities as its own internally generated records. The server records the identity of the calling client alongside the client-supplied message so that entries are attributable and cannot be repudiated.

The server may impose length limits on the message text or restrict which clients are permitted to write to the audit log. If a client exceeds the message length limit or lacks the required permission, the server returns an appropriate error without partially committing the entry.

Servers are not required to support `Log`. A server that does should advertise this capability in its [`Query`](query.md) response so that clients can determine whether client-side logging to the server is available before attempting the operation.

Log entries submitted via this operation are subject to the same retention and integrity guarantees as server-generated audit records. The server must not allow a client to modify or delete entries it has submitted.

## Errors

Uses centralized error handling per the [error handling](../concepts/error-handling.md) conventions. Common failure causes include:

- The server's audit log is unavailable or full.
- The calling client lacks permission to write to the audit log.
- The Log Message exceeds the server's allowed maximum size.
- The server does not support the `Log` operation — returns Operation Not Supported.

## Examples

An application that uses a managed AES key to encrypt a backup file can record this usage event directly in the key server's log:

```
Operation: Log
  Log Message:
    Message: "Backup encryption completed for job ID 20260612-0031"
    Log Level: Informational
    Date-Time: 2026-06-12T02:15:00Z
```

A security monitoring system that detects an anomalous number of decryption requests might write a warning-level entry:

```
Operation: Log
  Log Message:
    Message: "Anomaly detected: 1200 decrypt calls in 60s by client 'svc-analytics'"
    Log Level: Warning
    Date-Time: 2026-06-12T03:00:00Z
```

## Related Operations

[Query](query.md) · [Ping](ping.md)
