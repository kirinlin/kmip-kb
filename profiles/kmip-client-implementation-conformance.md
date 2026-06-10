---
title: KMIP Client Implementation Conformance
category: profile
spec_version: "2.1"
spec_versions: ["1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "14.1"
v1_source_section: "12.2"
status: draft
related: ["kmip-server-implementation-conformance", "query", "discover-versions"]
keywords: ["conformance", "client profile", "baseline client", "KMIP-Prof", "interoperability"]
---

# KMIP Client Implementation Conformance

## Overview

Mirroring the [server clause](kmip-server-implementation-conformance.md),
the client-conformance clause (v2.1 §14.1; v1.x §12.2) makes client
conformance a property of the profiles document: a client conforms to KMIP by
meeting at least one client profile in [KMIP-Prof], and claiming a profile
commits the client to every normative statement in that profile's clauses and
subclauses.

## Details

Client profiles are deliberately lighter than server profiles. A **Baseline
Client** must form well-encoded requests, negotiate TLS as the profile
requires, handle the standard [response
structure](../ttlv/message-structure.md) including failures, and tolerate
fields it does not recognize from newer minor versions. On top of that,
use-case profiles (symmetric key client, storage client, cryptographic
services client, and so on) prescribe which operations the client must be
able to issue and which objects and attributes it must handle. A client need
not support everything a server offers — it only has to do its claimed
profile correctly.

## Implications for Implementers

- Pick the narrowest profile that covers your use case and claim that;
  there is no obligation to implement the whole protocol surface.
- Be liberal in what you accept within a major version: servers at a higher
  minor version may return fields you do not know, and the spec requires you
  to skip them rather than fail.
- Use [Discover Versions](../operations/discover-versions.md) and
  [Query](../operations/query.md) at connection setup instead of hard-coding
  server capabilities.
- Interop matrices published from OASIS plugfests are organized by these
  profiles — useful when checking whether a vendor pairing has been
  demonstrated.

## Related Concepts

[KMIP Server Implementation Conformance](kmip-server-implementation-conformance.md) ·
[Query](../operations/query.md) ·
[Discover Versions](../operations/discover-versions.md)
