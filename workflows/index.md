---
title: Workflows
category: index
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: ""
status: draft
related: []
keywords: ["workflows", "lifecycle", "key rotation", "provisioning"]
---

# Workflows

End-to-end flows that chain [operations](../operations/index.md) together —
the protocol-level recipes a client actually runs.

No workflow pages have been authored yet. Planned flows:

- **Provision a symmetric key** —
  [Create](../operations/create.md) →
  [Activate](../operations/activate.md) →
  [Get](../operations/get.md), with the
  [ID Placeholder](../operations/create.md) carrying the identifier through
  a single batch.
- **Bring your own key** — [Register](../operations/register.md) (optionally
  wrapped) → verify via [Get Attributes](../operations/get-attributes.md).
- **Key rotation** — [Locate](../operations/locate.md) →
  [Re-key](../operations/re-key.md) → deactivate the predecessor; link
  traversal via the [Link](../attributes/link.md) attribute.
- **Compromise response** — [Revoke](../operations/revoke.md) (reason
  Compromised) → [Destroy](../operations/destroy.md), and what happens to
  [State](../attributes/state.md) along the way.
- **Certificate enrollment** —
  [Create Key Pair](../operations/create-key-pair.md) →
  [Certify](../operations/certify.md) → renewal via
  [Re-certify](../operations/re-certify.md).
