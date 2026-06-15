---
title: Flow Control
category: usage-guide
spec_version: "2.1"
spec_versions: ["2.0", "2.1"]
source_section: "ug-3.51"
status: reviewed
related: ["using-notify-and-put-operations"]
keywords: ["Flow Control", "endpoint role", "intermittent client", "server-to-client delivery", "polling"]
---

# Flow Control

## Overview

Flow Control (also described as "Endpoint Role") provides a uniform mechanism for delivering data from the server to clients that are intermittently available or not directly reachable. It ensures that data pushed via Notify or Put can still be delivered even when the client cannot maintain a persistent connection.

## Guidance

For clients that are unavailable at the time a server-initiated operation would normally be sent, the server buffers the data and delivers it when the client reconnects and polls. This is equivalent in outcome to the client polling for the information, but with lower latency when the client is available and reliable delivery when it is not.

## Implementation Notes

Flow Control is particularly relevant for IoT devices and mobile clients that connect intermittently. The implementation requires the server to maintain a queue of pending server-initiated operations per client. Clients should poll for pending deliveries on reconnection. The specific mechanism for signalling to the server that a client is reconnecting and ready to receive buffered operations is implementation-defined.

## Related Concepts

See [Using Notify and Put Operations](using-notify-and-put-operations.md).
