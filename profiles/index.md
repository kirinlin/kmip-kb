---
title: Profiles
category: index
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "14"
v1_source_section: "12"
status: draft
related: ["kmip-server-implementation-conformance", "kmip-client-implementation-conformance"]
keywords: ["profiles", "conformance", "baseline", "interoperability"]
---

# Profiles

How conformance works in KMIP: the spec's §14 (v1.x §12) defers to the
separate OASIS profiles document ([KMIP-Prof]), which defines named server and
client profiles — baseline messaging plus use-case bundles (symmetric key
lifecycle, asymmetric keys, cryptographic services, tape libraries, ...) with
test cases.

- [KMIP Server Implementation Conformance](kmip-server-implementation-conformance.md)
  — what it means for a server to conform (v2.1 §14.2).
- [KMIP Client Implementation Conformance](kmip-client-implementation-conformance.md)
  — the client-side counterpart (v2.1 §14.1).

Runtime discovery of what a peer actually implements goes through
[Query](../operations/query.md) and, from 1.3,
[Profile Information](../ttlv/profile-information.md).
