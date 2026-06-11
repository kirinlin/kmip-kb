---
title: Usage Allocation
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.32"
status: reviewed
related: ["key-state-and-times"]
keywords: ["usage allocation", "Get Usage Allocation", "encryption usage", "tape encryption", "allocation loss", "stable storage"]
---

# Usage Allocation

## Overview

The Usage Allocation mechanism allows a server to track how much of a key's permitted cryptographic usage has been pre-allocated to clients. Clients request a usage allocation and must manage that allocation carefully, because client failures during a usage period (power loss, crash) can result in the allocated usage being permanently lost.

## Guidance

Usage allocations should be as small as practical. It is preferable to make multiple smaller allocation requests than a single large one, to minimise the amount of usage that would be lost if the client fails during the allocated period. Conservative allocation policies on both the client and server sides reduce the risk of wasted allocation.

Critical guidance: if power loss or crash occurs during a tape encryption session that consumed allocated usage, the remaining allocation may be unrecoverable. In such cases, the entire session may need to be re-encrypted with a different key if the server cannot issue additional allocation.

## Implementation Notes

Implementations that rely on usage allocation should cache allocation state on stable storage at the client — a volatile cache is insufficient, because the allocation is lost on crash even if the server's allocation counter was updated. Stable-storage caching allows the client to recover and reconcile usage state after a restart.

## Related Concepts

See [Key State and Times](key-state-and-times.md) for the lifecycle context of usage-bounded keys.
