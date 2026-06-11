---
title: Concepts
category: index
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: ""
status: reviewed
related: ["authentication", "transport", "error-handling"]
keywords: ["concepts", "authentication", "transport", "error handling"]
---

# Concepts

Cross-cutting topics that apply to every KMIP exchange rather than to one
operation or object type.

- [Authentication](authentication.md) — how clients and servers establish
  identity: channel (TLS) authentication plus optional in-message credentials.
- [Transport](transport.md) — the secured channel KMIP messages travel over;
  TLS requirements live in the profiles, port 5696 by convention.
- [Error Handling](error-handling.md) — per-batch-item status/reason/message
  reporting and batch continuation semantics.

Closely related material lives elsewhere: the key lifecycle is described
under the [State](../attributes/state.md) attribute, and message framing
under [ttlv/](../ttlv/index.md).
