---
title: Locating Keys in Specific States
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-4.1"
status: reviewed
related: ["id-placeholder", "key-state-and-times"]
keywords: ["Locate", "key state", "date range", "ActivationDate", "DeactivationDate", "CompromiseDate", "range match"]
---

# Locating Keys in Specific States

## Overview

The Locate operation supports time-based queries that can find objects by the exact time of a state transition, the range of times during which a transition occurred, the state at a specific point in time, or the state during an entire time window. This enables powerful key inventory and audit queries.

## Guidance

KMIP's Locate allows a date/time attribute to appear once (for exact match) or twice (for range match, specifying a lower and upper bound). By combining date-range criteria across the four state-transition timestamps — activation, deactivation, compromise, and destruction, a client can express complex queries:

- **Exact transition match**: Locate keys whose Activation Date equals time t — `Locate(ActivationDate(t))`.
- **Range transition match**: Locate keys activated between t and t' — `Locate(ActivationDate(t), ActivationDate(t'))`.
- **State at a specific time**: Finding objects that were Active at time t requires three constraints: Activation Date ≤ t (upper bound t), Deactivation Date > t (lower bound t+1). Any absent upper date is treated as MAX_INT.
- **State during a time range**: Similar to the above but extending the bounds to cover the full range t to t'.

For the Destroyed-Compromised state (which has two entry transitions: Destroy Date and Compromise Date), two separate Locate requests are needed because KMIP does not support OR conditions.

## Implementation Notes

Performing time-range state queries requires careful construction of the dual-attribute criteria. Test these queries against a known dataset before deploying in production; edge cases (keys without a Deactivation Date, future-dated keys) can produce surprising results. The server treats a missing upper date as MAX_INT for range matching purposes.

## Related Concepts

See [Key State and Times](../lifecycle/key-state-and-times.md) and [ID Placeholder](id-placeholder.md).
