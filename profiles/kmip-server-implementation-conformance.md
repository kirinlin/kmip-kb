---
title: KMIP Server Implementation Conformance
category: profile
spec_version: "2.1"
spec_versions: ["1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "14.2"
v1_source_section: "12.1"
status: draft
related: ["kmip-client-implementation-conformance", "query", "discover-versions", "profile-information"]
keywords: ["conformance", "server profile", "baseline server", "KMIP-Prof", "interoperability"]
---

# KMIP Server Implementation Conformance

## Overview

The KMIP specification does not itself enumerate what a server must implement.
The server-conformance clause (v2.1 §14.2; v1.x §12.1) delegates entirely to
the companion profiles document ([KMIP-Prof]): a server conforms to KMIP by
conforming to at least one server
profile defined there, and once it claims a profile it must satisfy every
normative statement in that profile's clauses and subclauses.

## Details

This indirection is a deliberate design change. KMIP 1.0 carried its own
"Server Baseline Implementation Conformance Profile" inside the spec; from
1.1 onward the conformance clauses moved out to the profiles document so
profiles could evolve independently. The profiles document defines a
**Baseline Server** clause (message framing, required header fields,
[Query](../operations/query.md) and
[Discover Versions](../operations/discover-versions.md) support, TLS
authentication) and stacks more specific profiles on top — symmetric key
lifecycle, asymmetric key lifecycle, cryptographic services, tape library,
opaque object, and others, each with its own mandatory operations, objects,
and attributes plus test cases.

A server may implement any superset: profiles state minimums, not ceilings.
What a given server actually supports is discoverable at runtime through
Query (operations, objects, and — from 1.3 —
[Profile Information](../ttlv/profile-information.md),
[capabilities](../ttlv/capability-information.md), and
[validations](../ttlv/validation-information.md)).

## Implications for Implementers

- "Implements KMIP" is not a testable claim; "conforms to the Baseline Server
  profile of [KMIP-Prof] 2.1" is. State the profile(s) and version you claim.
- Build conformance checks against the profile test cases — OASIS publishes
  request/response transcripts per profile, and interop events exercise them.
- Advertise claimed profiles via Query so clients can adapt without
  configuration.
- Mind version skew: a 2.1 server claiming a profile must still answer 2.0
  clients per its backward-compatibility obligations within the same major
  version.

## Related Concepts

[KMIP Client Implementation Conformance](kmip-client-implementation-conformance.md) ·
[Query](../operations/query.md) ·
[Profile Information](../ttlv/profile-information.md)
