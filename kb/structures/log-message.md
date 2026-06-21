---
title: Log Message
category: structures
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "7.19"
status: reviewed
related: ["log", "message-structure"]
keywords: ["log message", "audit log", "log operation", "log level", "log text", "server log", "420141", "LogMessage"]
tag_hex: "420141"
xml_text: "LogMessage"
tag_type: "Text String"
---

# Log Message

## Overview

Log Message is the payload structure for the [Log](../operations/log.md) operation. A client sends a Log request carrying a Log Message to instruct the server to record an entry in its audit or operational log. This mechanism lets clients annotate the server's log stream with application-level events — for example, recording that a particular key was used to encrypt a specific document, linking the server's key-management audit trail to higher-level business events.

The server is responsible for persisting the log entry and associating it with the session context (and thus the authenticated identity of the client).

## Encoding (Tag / Type / Length / Value)

Log Message encodes as a Structure.

| Field | Tag | XML Text | Type | Required |
|---|---|---|---|---|
| Log Message (Text String) | `42009F` | `LogMessage` | Text String | Yes |
| Log Operation | `420271` |  | Enumeration | No |
| Log Level | `4200A2` |  | Enumeration | No |
| Date Time | `420034` |  | Date-Time | No |

The Text String child carries the actual log message content. The other fields provide severity, category, and timestamp metadata.

## Fields & Structure

**Log Message (Text String)** is the human-readable body of the log entry. The content is application-defined; KMIP imposes no schema on the text.

**Log Operation** is an enumeration that categorizes the reason for the log entry — for example, whether the client is recording a key-use event, an administrative action, or a debug trace. This field helps the server index or filter log records.

**Log Level** is an enumeration indicating the severity or importance of the message (Debug, Info, Warning, Error, Critical are typical values). Servers may use this to filter or route log entries to different storage locations.

**Date Time** is the client-supplied timestamp for the event being logged. Because clients have their own clocks, this timestamp may differ slightly from the server's internal log timestamp. The server typically records both.

## Examples

After encrypting a document using a stored key, a client sends a Log request with Log Message = `"Encrypted document ID=99234 using key UID=abc-1234"`, Log Level = Info, and Date Time = current UTC time. The server appends this entry to its audit log tagged with the client's authenticated identity. A compliance auditor reviewing the log can correlate key-use events with specific business actions.

## Related

[Log](../operations/log.md) · [Message Structure](../messages/message-structure.md)
