---
title: Split Key
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.9"
status: reviewed
related: ["symmetric-key"]
keywords: ["split key", "key splitting", "Shamir", "XOR", "key threshold", "Join Split Key", "Create Split Key", "420089", "SplitKey"]
tag_hex: "420089"
xml_text: "SplitKey"
---

# Split Key

## Overview

KMIP supports threshold-based key splitting: a base key is divided into N parts, and any K of those parts (K ≤ N, the threshold) are sufficient to reconstruct the original key. The server can generate the split key from a new or existing base key, and can later reconstruct the base key from a sufficient number of parts.

## Guidance

A client initiates splitting via Create Split Key, specifying N (total parts), K (threshold), and the algorithm (XOR or Shamir's Secret Sharing). Providing the Unique Identifier of an existing key causes the server to split that key; omitting it triggers server-side key generation.

After creation, the client should link the split key parts to each other using Previous Link and Next Link attributes forming a circular chain, and optionally use a Parent Link from each part to the original base key. This makes the complete set of parts discoverable via attribute traversal.

Reconstruction requires a Join Split Key request containing at least K part identifiers; the server rejoins the parts and returns the Unique Identifier of the restored key object.

## Implementation Notes

Split key parts are independent managed objects with their own lifecycle states. Clients should manage the lifecycle of all parts consistently — activating and deactivating them together as a group. If a base key was supplied by the client for splitting, the relationship between the base key and the generated parts must be tracked via Link attributes.

## Related Concepts

See [Split Key](../../objects/split-key.md) for the object structure.
