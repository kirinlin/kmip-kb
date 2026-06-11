---
title: Server-to-Client Operations
category: index
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.2"
v1_source_section: "5"
status: reviewed
related: ["notify", "put", "query"]
keywords: ["server-to-client", "push", "notify", "put", "query"]
---

# Server-to-Client Operations

Operations the **server** initiates, outside the normal request/response
flow. They presuppose a channel the server can open toward the client,
configured by mechanisms the spec does not define.

- [Notify](notify.md) — tell a client that an object's attributes changed.
- [Put](put.md) — push a managed object (new or replacement) to a client.
- [Query](query.md) — interrogate a client's capabilities (added in 1.3).

All three reuse the standard [message structure](../../ttlv/message-structure.md)
with a few client-only header fields disallowed, and the client — not the
server — returns the response.
