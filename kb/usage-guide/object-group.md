---
title: Object Group
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.28"
status: draft
related: ["attributes", "locate"]
keywords: ["Object Group", "Fresh", "group member", "round robin", "key pool", "Locate"]
---

# Object Group

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

The Object Group attribute allows multiple managed objects to be associated under a common group name. Clients and servers can use groups to manage pools of related objects — for example, a pool of pre-generated symmetric keys available for assignment — and to retrieve "fresh" (not yet used) or "default" group members via the Locate operation.

## Guidance

The **Fresh** attribute tracks whether a group member has been retrieved via Get. New group members are typically registered with Fresh=true; once retrieved via Get, the server sets Fresh=false. The **Object Group Member** flag in a Locate request specifies whether to return a Group Member Fresh (an unretrieved key) or Group Member Default (a server-policy-selected key, e.g., via round robin).

Group membership is managed by adding or deleting the Object Group attribute. The server may also pre-define groups and add objects automatically based on server policy.

## Implementation Notes

Group semantics — particularly what "default" means and the algorithm for selecting a fresh member when the pool is exhausted — are largely server-policy-defined. Clients that rely on group behaviour should document their expectations and verify them against the specific server implementation. The Fresh attribute is server-managed after initial object registration; clients cannot reset it.

## Related Concepts

See [Attributes](attributes.md) and the Locate operation in [kb/operations/](../operations/).
