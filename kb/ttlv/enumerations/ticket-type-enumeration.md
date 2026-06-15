---
title: Ticket Type Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "11.57"
status: reviewed
related: ["ticket", "login", "logout", "delegated-login", "authentication"]
keywords: ["ticket type", "session ticket", "login ticket", "delegation ticket", "authentication ticket"]
---

# Ticket Type Enumeration

## Overview

The Ticket Type enumeration classifies the nature of a session [Ticket](../../structures/ticket.md) issued by the [Login](../../operations/login.md) or [Delegated Login](../../operations/delegated-login.md) operations. A ticket is an opaque, server-issued token that a client presents in place of full credentials in subsequent requests. The type tells the server (and any auditing infrastructure) what kind of session the ticket represents.

## Encoding (Tag / Type / Length / Value)

Encoded as a 4-byte integer (TTLV type `05`, Enumeration).

## Fields & Structure

- **Login**: The ticket was issued as a result of a successful [Login](../../operations/login.md) operation. It represents a standard authenticated session for the principal who logged in. This is the only baseline-defined value in KMIP v2.1.

Additional ticket types may be defined by vendor extensions or future specification revisions to represent delegation tickets, impersonation tokens, or time-limited one-time-use tokens.

## Examples

After a successful Login, the server returns a Ticket with Ticket Type = **Login** and a Ticket Value byte string. The client includes this ticket in the Authentication field of subsequent requests.

## Related

[Ticket structure](../../structures/ticket.md) · [Login](../../operations/login.md) · [Logout](../../operations/logout.md) · [Delegated Login](../../operations/delegated-login.md)
