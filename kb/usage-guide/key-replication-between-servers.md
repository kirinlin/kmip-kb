---
title: Key Replication Between Servers
category: usage-guide
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "ug-4.11"
status: draft
related: ["key-state-and-times", "unique-identifiers"]
keywords: ["key replication", "multi-server", "fault tolerance", "consistency", "conflict resolution", "partition"]
---

# Key Replication Between Servers

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

Key management systems may consist of multiple servers for fault tolerance, performance, and geographic distribution. Each server should hold the same managed objects and attributes, with operations on one server replicated to all others. This section addresses the architectural considerations for maintaining consistency across a replicated server cluster.

## Guidance

When servers are intermittently connected, writes to one node may not propagate to peers before the next request arrives. This creates consistency challenges:

- A key may have different State values on different servers (e.g., Active on one, Compromised on another after a split-brain period).
- Two different keys on different servers may have been assigned the same Name attribute.
- Link attributes (forward and backward) may be inconsistent across servers.

The key management system must be designed to detect and resolve such inconsistencies when servers reconnect, in a way that complies with the KMIP specification. For example, a state conflict must be resolved to a state that is valid per the KMIP state machine.

## Implementation Notes

Multi-server KMIP deployments typically use one of two replication models: strong consistency (consensus-based, where all servers must agree before an operation is committed) or eventual consistency (operations are committed locally and replicated asynchronously). Strong consistency provides simpler reasoning but higher latency and reduced availability during partitions. Eventual consistency provides better availability but requires a conflict resolution strategy. KMIP compliance must be maintained through the resolution process — states must remain valid, and Unique Identifiers must not be reassigned.

## Related Concepts

See [Key State and Times](key-state-and-times.md) and [Unique Identifiers](unique-identifiers.md) for the attributes most at risk during consistency failures.
