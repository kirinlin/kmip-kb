---
title: Mappings
category: index
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: ""
status: reviewed
related: []
keywords: ["mappings", "version differences", "cross-reference", "PKCS#11", "X.509"]
---

# Mappings

Cross-reference tables connecting KMIP to other standards and across its own
versions.

No mapping tables have been authored yet. Candidates, roughly in priority
order:

- **Version deltas** — which operations, attributes, and base objects each
  1.x release added or deprecated (the per-page `spec_versions` front matter
  already encodes this per item; a consolidated table belongs here, next to
  the machine-readable TOC in [versions/](../versions/index.md)).
- **X.509 Key Usage ↔ Cryptographic Usage Mask** — the bit-for-bit
  correspondence summarized in
  [Cryptographic Usage Mask](../attributes/cryptographic-usage-mask.md).
- **Transparent key fields ↔ PKCS#1 / FIPS 186 / X9.42 parameter names** —
  summarized in
  [Transparent Key Structures](../ttlv/transparent-key-structures.md).
- **PKCS#11 ↔ KMIP** — attribute and mechanism correspondence for
  implementers bridging the two APIs.
