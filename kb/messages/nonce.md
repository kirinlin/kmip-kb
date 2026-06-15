---
title: Nonce
category: messages
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "9.14"
v1_source_section: "2.1.14"
status: reviewed
related: ["credential", "attestation-capable-indicator", "message-structure"]
keywords: ["nonce", "attestation", "replay protection", "challenge"]
tag_hex: "4200C8"
xml_element: "Nonce"
---

# Nonce

## Overview

A server-issued random challenge, introduced in 1.2 for the attestation flow:
the server hands the client a Nonce (in a response header), and the client
folds it into the Attestation [Credential](credential.md) of its next
request, proving the attestation evidence is fresh rather than replayed.

## Encoding (Tag / Type / Length / Value)

Structure, tag `4200C8`:

| Field | Tag | XML Element | Type | Required |
|---|---|---|---|---|
| Nonce ID | `4200C9` | `NonceID` | Byte String | Yes — server-assigned handle for this challenge |
| Nonce Value | `4200CA` | `NonceValue` | Byte String | Yes — the random bytes |

## Fields & Structure

The ID lets the server match a returned nonce against the challenge it
issued (it may have several outstanding); the value is the unpredictable
part. Appears in the [response header](message-structure.md) when a server
demands attestation (`Attestation Required` flow) and inside the Attestation
Credential's value on the way back.

## Examples

A client Gets a high-value key: the server fails the first attempt with
`Attestation Required` and a Nonce in the response header; the client retries
with an Attestation Credential containing that Nonce plus a TPM Quote
covering it.

## Related

[Credential](credential.md) ·
[Attestation Capable Indicator](attestation-capable-indicator.md) ·
[Message Structure](message-structure.md)
