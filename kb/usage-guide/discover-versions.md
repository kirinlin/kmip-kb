---
title: Discover Versions
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.4", "2.0", "2.1"]
source_section: "ug-3.44"
status: reviewed
related: ["query"]
keywords: ["Discover Versions", "protocol version negotiation", "version compatibility", "smart client", "dumb client"]
---

# Discover Versions

## Overview

The Discover Versions operation allows a client and server to negotiate a KMIP protocol version that both parties support. It handles both "smart" clients (which request the full list and pick the best common version) and "dumb" clients (which simply pick the first version the server returns).

## Guidance

In the smart client pattern, the client sends an empty Discover Versions request payload, and the server returns all supported versions. The client then picks the highest mutually supported version and uses it for all subsequent requests.

In the dumb client pattern, the client sends a Discover Versions request with its supported versions in the payload. If the server supports one of them, it returns that version. If the server supports none of the client's listed versions but can still communicate using the message-header version, it returns an empty list rather than an error.

## Implementation Notes

Discover Versions should be called once at connection setup before any other operations. Clients that skip version negotiation may send requests in a version the server does not support. When no payload match exists, the version carried in the request message header serves as the fallback, ensuring graceful degradation rather than an outright error.

## Related Concepts

See [Query](query.md) for the broader mechanism for discovering server capabilities.
