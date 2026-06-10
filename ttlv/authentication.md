---
title: Authentication
category: ttlv
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.6"
status: draft
related: ["credential", "message-structure", "nonce"]
keywords: ["authentication structure", "request header", "credential container"]
---

# Authentication

## Overview

The request-header slot for identity claims: a container of one or more
[Credential](credential.md) structures. Whether any request needs it is
server policy — some servers authenticate nothing beyond TLS, some demand it
everywhere; the spec recommends leaving
[Query](../operations/query.md) usable without it.

## Encoding (Tag / Type / Length / Value)

Structure, tag `42000C`, containing:

| Field | Tag | Type | Required |
|---|---|---|---|
| Credential | `420023` | Structure | Yes; repeatable |

(In 1.0–1.1 exactly one Credential was carried; 1.2 made it repeatable so an
identity credential and an attestation credential can travel together.)

## Fields & Structure

This structure supplements — never replaces — channel
[authentication](../concepts/authentication.md). Typical pattern: TLS client
certificate identifies the application, a Username-and-Password Credential
identifies the end user inside it. Validation failure yields the
`Authentication Not Successful` [result reason](result-reason.md).

## Examples

Request header: Protocol Version, Authentication { Credential { Username and
Password: alice / *** } }, Batch Count = 1 — followed by the operation batch
item.

## Related

[Credential](credential.md) ·
[Authentication concept](../concepts/authentication.md) ·
[Message Structure](message-structure.md)
