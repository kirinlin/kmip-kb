---
title: Key Rotation
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.11"
status: draft
related: ["key-state-and-times"]
keywords: ["key rotation", "Re-key", "automatic rotation", "RotateAutomatic", "RotateGeneration", "RotateLatest"]
---

# Key Rotation

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

Key rotation — replacing an active key with a new one — is a fundamental key management practice. KMIP supports both manual rotation (client-initiated Re-key or Re-key Key Pair operations) and, from v2.1, automatic rotation driven by server policy via the RotateAutomatic attribute.

## Guidance

For manual rotation, the client issues a Re-key or Re-key Key Pair request referencing the current key. The server creates a new key with appropriate lifecycle attributes, typically deriving the new key's dates from the old key's dates plus an optional offset interval.

For automatic rotation, the client sets the RotateAutomatic attribute on the key and optionally configures rotation parameters. The server then rotates the key according to its policy without requiring client intervention.

Two additional attributes support rotation tracking: RotateGeneration (an integer identifying which generation a key belongs to in a rotation series) and RotateLatest (a boolean indicating whether this key is the most recently generated in the series). Together these allow efficient navigation of a rotation history.

## Implementation Notes

Automatic rotation is a v2.1 addition. Clients targeting older versions must implement rotation manually. In both cases, the Deactivation Date of the old key and the Activation Date of the new key should be coordinated to avoid a gap in coverage or an overlap that violates usage policy.

## Related Concepts

See [Key State and Times](key-state-and-times.md) for the time attributes that govern the rotation schedule.
