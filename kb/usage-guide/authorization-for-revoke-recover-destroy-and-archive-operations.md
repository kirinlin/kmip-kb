---
title: Authorization for Revoke, Recover, Destroy and Archive Operations
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.2"
status: draft
related: ["authentication", "server-policy"]
keywords: ["authorization", "revoke", "destroy", "archive", "recover", "access control", "security officer"]
---

# Authorization for Revoke, Recover, Destroy and Archive Operations

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

Revoke, Recover, Destroy, and Archive are operations with significant and potentially irreversible impact on key availability and security. KMIP guidance specifically calls for elevated authentication and authorisation before these operations are executed, even if the client passes standard authentication.

## Guidance

Elevated authorisation checks apply to all four operations. The server should confirm that the requestor is the object owner, a security officer, or another identity with explicit authorisation before proceeding. The server may require additional authentication steps beyond the initial channel-level authentication before completing the request.

Crucially, even a fully authenticated and authorised request for these operations should be treated as a "hint" to the key management system: the server retains the right to refuse based on server policy, regardless of who asked.

## Implementation Notes

The specific mechanism for enforcing these authorisation requirements is outside the scope of KMIP and left to server policy. Implementations should document which identities are authorised for these operations and under what conditions. In multi-tenant deployments, extra care is needed to prevent one tenant from revoking or destroying objects belonging to another.

## Related Concepts

See [Authentication](authentication.md) for how client identity is established, and [Server Policy](server-policy.md) for the broader policy framework.
