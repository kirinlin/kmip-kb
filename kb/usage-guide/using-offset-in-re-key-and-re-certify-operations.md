---
title: Using Offset in Re-key and Re-certify Operations
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.40"
status: draft
related: ["key-rotation", "certify-and-re-certify", "key-state-and-times"]
keywords: ["offset", "Re-key", "Re-key Key Pair", "Re-certify", "Activation Date", "forward-dating", "interval"]
---

# Using Offset in Re-key and Re-certify Operations

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

An optional offset interval is supported by the key and certificate renewal operations (Re-key, Re-key Key Pair, Re-certify). The offset controls when the newly created object becomes active relative to the request time. This allows pre-issuing a replacement key or certificate before the current one expires, providing a managed handover window.

## Guidance

For Re-key and Re-key Key Pair, the offset is the interval between the request time and when the replacement key becomes active. Subsequent time attributes — Process Start Date, Protect Stop Date, Deactivation Date — for the new object are then computed by applying the same relative intervals used by its predecessor. This preserves the relative structure of the old key's lifecycle.

For Re-certify, the offset specifies the duration between the new certificate's Initial Date and its Activation Date, again with subsequent dates derived from the old certificate's intervals.

An important edge case arises when relative dates calculated from the predecessor's intervals end up earlier than the successor's Initial Date. KMIP permits forward-dating in this scenario to prevent contradictory lifecycle states.

## Implementation Notes

Offset-based re-keying allows controlled key overlap: the old key's Protect Stop Date can be set to coincide with the new key's Activation Date, ensuring continuous coverage. This is the recommended approach for high-availability encryption deployments that cannot tolerate even a brief window without an active key.

## Related Concepts

See [Key State and Times](key-state-and-times.md) and [Key Rotation](key-rotation.md).
