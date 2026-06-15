---
title: Ticket
category: structures
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "7.39"
status: reviewed
related: ["login", "logout", "delegated-login", "authentication", "message-structure"]
keywords: ["ticket", "session ticket", "delegation ticket", "ticket type", "ticket value", "token authentication"]
---

# Ticket

## Overview

A Ticket is a compact, server-issued credential that a client receives after authenticating via the [Login](../operations/login.md) operation. In subsequent requests, the client presents the Ticket in the Authentication field of the KMIP message header instead of repeating its full credentials. This avoids transmitting long-lived secrets on every request and allows the server to implement session lifetimes and revocable tokens.

Tickets are also central to the delegated authentication model: a client that has obtained a Ticket can pass it (or a derived ticket) to another party via [Delegated Login](../operations/delegated-login.md), allowing that party to act on its behalf within the bounds of the delegated privileges.

## Encoding (Tag / Type / Length / Value)

Ticket encodes as a Structure.

| Field | Tag | XML Element | Type | Required |
|---|---|---|---|---|
| Ticket Type | `420233` | `TicketType` | Enumeration | Yes |
| Ticket Value | `420234` | `TicketValue` | Byte String | Yes |

Both fields are required. The Ticket Type distinguishes different ticket uses; the Ticket Value is the opaque byte-string token issued by the server.

## Fields & Structure

**Ticket Type** is an Enumeration that classifies the ticket's purpose. Common values include:

- *Login* — the standard session ticket issued by the Login operation.
- *Delegated Login* — a ticket derived for delegation, issued by the Delegated Login operation.

The type tells the server which credential-processing path to apply when the ticket is presented.

**Ticket Value** is an opaque byte string whose internal structure is entirely server-defined. Clients treat it as an uninterpreted handle. The server may encode session identifiers, expiry times, and integrity-protection data into the value using its own format.

Tickets have a server-controlled lifetime. The server may impose expiry, idle timeouts, or explicit revocation via [Logout](../operations/logout.md). Once a ticket expires or is revoked, subsequent requests using it will be rejected with an authentication failure.

## Examples

After a successful Login, a client receives a Ticket with Ticket Type = Login and Ticket Value = a 32-byte server-generated token. On subsequent Create, Get, and Locate operations, the client places this Ticket in the Credential field of the Authentication structure instead of sending its username and password. The server validates the token and processes the request. When the session ends, the client calls Logout with the Ticket to invalidate it server-side.

## Related

[Login](../operations/login.md) · [Logout](../operations/logout.md) · [Delegated Login](../operations/delegated-login.md) · [Authentication](../messages/authentication.md) · [Message Structure](../messages/message-structure.md)
