---
title: Reducing Multiple Requests Through the Use of Batch
category: usage-guide
spec_version: "2.1"
spec_versions: ["2.0", "2.1"]
source_section: "ug-3.53"
status: draft
related: ["batched-requests-and-responses", "id-placeholder"]
keywords: ["batch", "round trips", "Locate and Get", "atomicity", "undo", "continue", "Batch Undo Capability"]
---

# Reducing Multiple Requests Through the Use of Batch

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

KMIP's batching mechanism reduces the number of round trips required for common multi-step workflows. A Locate followed by a Get — two operations frequently combined in practice — can be expressed as a single batched message.

## Guidance

Batch operations are not guaranteed to be atomic. The Batch Error Continuation option controls error handling: the server can stop, continue, or attempt to undo previously completed items. The optional "undo" mode requires server support (discoverable via Query Capability Information / Batch Undo Capability) and does not guarantee true atomicity — it is an attempt to reverse completed items, not a transactional guarantee.

Similarly, "continue" mode (Batch Continue Capability) allows the server to proceed past a failing item without stopping. Clients should verify server support before relying on either mode.

## Implementation Notes

Even without undo or continue support, batching provides meaningful latency reduction for common patterns. The most important optimisations are Locate+Get (finding and retrieving a key in one round trip) and Create+Activate (creating and activating a key in one round trip). These can be implemented using the ID Placeholder to chain the results without knowing the Unique Identifier in advance.

## Related Concepts

See [Batched Requests and Responses](batched-requests-and-responses.md) and [ID Placeholder](id-placeholder.md).
