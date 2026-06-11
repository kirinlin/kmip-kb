---
title: Server Policy
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-2.5"
status: draft
related: ["authorization-for-revoke-recover-destroy-and-archive-operations", "island-of-trust"]
keywords: ["server policy", "conformance", "access control", "operation refusal", "trust relationship"]
---

# Server Policy

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

A conformant KMIP server may nonetheless refuse to execute a requested operation or reject a client-settable attribute if its server policy prohibits it. KMIP conformance describes what the protocol supports; server policy governs what a specific deployment allows.

## Guidance

Server policy can reflect many considerations: the trust level established with a particular client, performance constraints, regulatory requirements, or operational rules. A server is not obligated to perform every KMIP-compliant operation that a client requests. The protocol defines the mechanism; deployment policy defines the boundaries within which that mechanism may be exercised.

Clients should handle refusals gracefully and interpret `Operation Not Supported` or `Permission Denied` result reasons as signals of policy enforcement rather than protocol errors.

## Implementation Notes

Servers typically express policy through access control lists, role-based permissions, and attribute-level constraints. The SetConstraints and GetConstraints operations (added in v2.1) allow sufficiently privileged clients to inspect and modify cryptographic parameter constraints programmatically. For operations like Revoke, Recover, Destroy, and Archive, elevated authentication and authorisation may be required by server policy beyond what the protocol mandates.

## Related Concepts

See [Authorization for Revoke, Recover, Destroy and Archive Operations](authorization-for-revoke-recover-destroy-and-archive-operations.md) for guidance on operations with particularly strong policy implications.
