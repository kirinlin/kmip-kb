---
title: Versions
category: index
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4"]
source_section: ""
status: draft
related: []
keywords: ["versions", "TOC", "1.0", "1.1", "1.2", "1.3", "1.4", "deltas"]
---

# Versions

Machine-readable per-version section maps, plus (planned) delta notes between
the 1.x releases.

- [1.4-toc.yaml](1.4-toc.yaml) — generated map from every KMIP 1.4 spec
  section to its knowledge-base document. Regenerate with
  `python scripts/build_kb_scaffold.py --toc-only`.

The headline changes per release, as reflected in each page's
`spec_versions` front matter:

- **1.1** — Discover Versions, Re-key Key Pair; X.509-specific certificate
  attributes (deprecating the generic ones), Certificate Length, Digital
  Signature Algorithm, Fresh; Extension Information; Encoding Option.
- **1.2** — cryptographic services (Encrypt/Decrypt, Sign/Verify, MAC,
  RNG, Hash), split-key operations, attestation (Nonce, credential type),
  PGP Key object; Alternative Name, Key Value Present/Location, Original
  Creation Date.
- **1.3** — streaming crypto (Correlation Value, Init/Final Indicator),
  server-to-client Query, RNG/Profile/Validation/Capability Information,
  Random Number Generator attribute; Template and Operation Policy
  deprecated.
- **1.4** — Import/Export, AEAD fields, client/server correlation values,
  PKCS#12, Sensitive/Always Sensitive, Extractable/Never Extractable,
  Description and Comment, Key Wrap Type, Mask Generator parameters.
