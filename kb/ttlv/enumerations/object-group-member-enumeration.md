---
title: Object Group Member Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.33"
status: reviewed
related: ["locate", "state-enumeration"]
keywords: ["object group", "group member", "fresh", "default", "key rotation", "object group attribute"]
---

# Object Group Member Enumeration

## Overview

The Object Group Member enumeration records the status of a managed object within a named object group, specifically whether the object is the current default member (the one that should be used for new operations) or a non-default member (an older version that is still retained). Object groups are used to manage key rotation: as new key versions are created, they join the group as the fresh default and older versions are marked as non-default. The [Locate](../../operations/locate.md) operation can filter on this attribute to retrieve only the current-generation key for a given group name.

## Encoding (Tag / Type / Length / Value)

Encoded as a 4-byte integer (TTLV type `05`, Enumeration). Appears in the Object Group Member attribute on managed objects that belong to a named object group.

## Fields & Structure

- **Group Member Fresh**: The object is the current active member of its group — the one that new encryption or signing operations should use. When a key is rotated, the new key is marked **Group Member Fresh** and the previous key is either removed from this status or marked with the non-default value.
- **Group Member Default**: The object is a member of the group but is not the currently preferred version. It may still be used for decryption or verification of data encrypted or signed with it, but new operations should use the fresh member. This is the typical state for retired-but-still-decryptable key versions.

## Examples

A key rotation policy that retains the previous three key versions for data decryption would mark the newest AES key as **Group Member Fresh** and the three preceding versions as **Group Member Default**. A Locate query specifying **Group Member Fresh** in a group named `tenant-xyz-data-key` returns only the current encryption key.

## Related

- [Locate operation](../../operations/locate.md) — uses Object Group Member as a filter criterion
- [State Enumeration](state-enumeration.md) — complements group membership in controlling key lifecycle
