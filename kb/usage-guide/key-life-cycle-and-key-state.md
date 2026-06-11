---
title: Key Life-cycle and Key State
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-2.11"
status: reviewed
related: ["key-state-and-times", "symmetric-key-lifecycle-profiles"]
keywords: ["key lifecycle", "key state", "NIST SP 800-57", "activation", "deactivation", "cryptoperiod"]
---

# Key Life-cycle and Key State

## Overview

KMIP implements a key lifecycle model based on NIST SP 800-57 key state definitions. Each managed cryptographic object moves through a sequence of states — Pre-Active, Active, Deactivated, Compromised, Destroyed, and Destroyed-Compromised — with state transitions triggered by operations or explicit attribute updates.

## Guidance

The lifecycle design ensures that keys are used only within their intended cryptoperiods and that keys reaching the end of their life are properly deactivated and eventually destroyed. The KMIP spec defines the lifecycle in terms of state transitions and the operations or time-based events that drive those transitions. The KMIP-Prof Symmetric Key Lifecycle Profile provides a concrete implementation template for the most common use case.

Section 3.16 of the UG provides detailed guidance on the time-related attributes (Activation Date, Deactivation Date, Process Start Date, Protect Stop Date, etc.) that govern when a key transitions between states.

## Implementation Notes

Clients must respect the state machine: an Active key cannot be destroyed without first being Revoked or Deactivated. Servers enforce state-transition rules and will return an error if a client attempts an operation that is invalid for the current state. Clients that need fine-grained control over cryptoperiods should set both process dates (Process Start Date / Protect Stop Date) and lifecycle dates (Activation Date / Deactivation Date) to distinguish between when a key may be used to apply protection versus when it may still be used for processing already-protected data.

## Related Concepts

See [Key State and Times](key-state-and-times.md) for implementation guidance on time attributes, and the profiles at [kb/profiles/](../profiles/) for conformance requirements.
