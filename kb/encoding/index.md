---
title: TTLV Encoding
category: index
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: ""
status: reviewed
related: ["ttlv-encoding", "cryptographic-usage-mask", "protection-storage-mask", "storage-status-mask"]
keywords: ["TTLV", "encoding", "enumerations", "bit masks", "wire format"]
---

# TTLV Encoding

KMIP's wire shape: the binary Tag/Type/Length/Value scheme (v2.1 §10.1; v1.x §9)
and the two value-encoding kinds that ride on top of it — enumerations (named
value sets, §11) and bit masks (named bit sets, §12). The composite structures
that this scheme serializes live in their own categories: see
[Data Structures](../structures/index.md) (v2.1 §3/§5/§7) and
[Messages](../messages/index.md) (v2.1 §8/§9).

## Encoding

- [TTLV Encoding](ttlv-encoding.md) — the Tag/Type/Length/Value scheme itself:
  tags, item types, length and value layout, padding, and ordering rules.

## Enumerations (§11)

- [Enumerations](enumerations/index.md) — named value sets used in enumerated
  TTLV fields (Object Type, Cryptographic Algorithm, State, Result Reason, …).

## Bit masks (§12)

- [Cryptographic Usage Mask](cryptographic-usage-mask.md) — permitted
  cryptographic operations for a key.
- [Protection Storage Mask](protection-storage-mask.md) — acceptable
  server-side protection levels (2.0+).
- [Storage Status Mask](storage-status-mask.md) — online/archival storage
  status filter for Locate.
