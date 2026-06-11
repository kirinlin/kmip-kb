---
title: Protection Storage Mask
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.29"
status: draft
related: ["server-policy"]
keywords: ["Protection Storage Mask", "storage", "HSM", "data sovereignty", "geographic constraint", "preference"]
---

# Protection Storage Mask

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

The Protection Storage Mask attribute allows a client to specify an ordered list of preferences for how the server should store and protect key material. The server must meet one of the specified preferences in its entirety; if it cannot, the request fails.

## Guidance

This attribute is useful when a deployment has specific requirements for how keys are stored — for example, requiring key material to remain on hardware security modules, or requiring it to stay within a particular geographic boundary (data sovereignty requirements). The client provides preferences in priority order; the server satisfies the first preference it can meet.

## Implementation Notes

The specific values available in the Protection Storage Mask are enumeration-defined and reflect hardware/software storage tier options. Clients operating in regulated environments should specify this attribute explicitly rather than accepting server defaults, to ensure compliance with storage requirements. If the server cannot meet any specified preference, it returns an Operation Failed error.

## Related Concepts

See [Server Policy](server-policy.md) for the policy context around storage and protection decisions.
