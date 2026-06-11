---
title: Reliable Message Delivery
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-2.9"
status: draft
related: ["message-security"]
keywords: ["reliable delivery", "transport", "TCP", "message delivery", "protocol design"]
---

# Reliable Message Delivery

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

KMIP explicitly delegates reliable message delivery to the underlying transport protocol and does not provide its own delivery-guarantee mechanisms. This is a deliberate design simplification that keeps the KMIP protocol layer focused on key management semantics.

## Guidance

In practice, KMIP over TLS/TCP inherits TCP's reliable ordered delivery guarantee. If a deployment uses a less reliable transport, the implementer is responsible for ensuring that any delivery guarantees required by the business use case are provided by the transport layer or by application-level retry logic, not by KMIP itself.

## Implementation Notes

This design means KMIP has no built-in message acknowledgement, sequence numbering, or duplicate detection. All of these concerns belong to the transport or application layer. Clients that cannot tolerate duplicate or lost operations must handle them at their own layer.

## Related Concepts

See [Message Security](message-security.md) for transport-layer security considerations.
