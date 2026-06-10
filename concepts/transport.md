---
title: Transport
category: concept
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "10"
status: draft
related: ["authentication", "error-handling", "ttlv-encoding", "message-structure"]
keywords: ["transport", "TLS", "channel security", "port 5696", "confidentiality", "integrity"]
---

# Transport

## Overview

The KMIP specification says almost nothing about transport on purpose: §10 is
a single requirement that clients and servers maintain a channel providing
confidentiality, integrity, and authenticity, with the concrete mechanism
defined in the profiles document. The protocol itself is just
[TTLV-encoded](../ttlv/ttlv-encoding.md)
[messages](../ttlv/message-structure.md) exchanged over that secured channel.

## Details

In every published 1.x profile the required channel is TLS. The profiles pin
the acceptable TLS versions and cipher suites per KMIP version (TLS 1.0 was
still allowed in early profiles; later profiles require TLS 1.2 with
mandatory cipher suites) and require certificate-based mutual authentication —
see [Authentication](authentication.md). IANA has registered TCP port 5696
for KMIP, and that is the conventional listener for raw TTLV-over-TLS,
although deployments may use any agreed port. The spec also anticipates other
encodings and bindings (the message-encoding section is explicitly plural),
and OASIS later published HTTPS, JSON, and XML bindings in the profiles
family.

KMIP is a request/response protocol: the client opens the connection and
issues requests; the server answers. [Server-to-client
operations](../operations/server-to-client/index.md) (Notify, Put) require a
channel the server can initiate, which the spec leaves entirely to
out-of-band configuration.

## Implications for Implementers

- Never run KMIP over plaintext TCP, even in a lab — every conformance
  profile assumes the channel provides the security properties the messages
  themselves lack (requests carry key material in the clear at the TTLV
  layer).
- Stream parsing matters: TTLV messages are self-delimiting via their length
  fields, and multiple requests may arrive back-to-back on one connection.
  Read the eight-byte tag/type/length prefix, then exactly `length` bytes.
- Respect [Maximum Response Size](../ttlv/maximum-response-size.md) — small
  embedded clients use it to keep responses inside their buffer budget.
- Long-lived connections are normal; clients commonly batch many operations
  per connection rather than reconnecting per request.

## Related Concepts

[Authentication](authentication.md) · [Error Handling](error-handling.md) ·
[TTLV Encoding](../ttlv/ttlv-encoding.md) ·
[Message Structure](../ttlv/message-structure.md)
