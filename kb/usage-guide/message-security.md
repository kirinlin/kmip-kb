---
title: Message Security
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-2.2"
status: draft
related: ["authentication", "transport"]
keywords: ["TLS", "confidentiality", "integrity", "replay protection", "key wrapping", "authentication suite"]
---

# Message Security

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

KMIP relies on the authentication suite defined in KMIP-Prof to verify client identity and depends on the underlying transport protocol — typically TLS — to provide confidentiality, integrity, message authentication, and replay protection for all KMIP messages.

## Guidance

KMIP does not define its own transport security layer; it delegates that responsibility entirely to the transport protocol. Within the protocol, KMIP provides a separate wrapping mechanism that can cryptographically protect a Key Value independent of the transport. This Key Block wrapping is designed for importing and exporting managed cryptographic objects, not as a replacement for transport-level security.

Deployments must select and correctly configure an authentication suite from KMIP-Prof and pair it with a suitably hardened TLS configuration.

## Implementation Notes

Because KMIP defers to external transport and authentication mechanisms, the effective security of a deployment depends heavily on correct TLS configuration, certificate management, and authentication suite selection. Key wrapping adds a defence-in-depth layer for key material in transit, but does not eliminate the need for strong transport security. Weak transport configuration invalidates much of the protocol's security model.

## Related Concepts

See [Authentication](../concepts/authentication.md) and [Transport](../concepts/transport.md) for the spec-side coverage of client identity and transport configuration.
