---
title: KMIP Knowledge Base
category: index
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: ""
status: reviewed
related: ["operations", "objects", "attributes", "encoding", "profiles"]
keywords: ["KMIP", "knowledge base", "index", "key management", "OASIS", "TTLV", "v2.1", "v1.x"]
---

# KMIP Knowledge Base

An independently written knowledge base for the OASIS **Key Management
Interoperability Protocol (KMIP)**, covering the **1.x** (v1.0–v1.4) and **2.x**
(v2.0–v2.1) families with **v2.1** as the baseline. Every article is original
prose — summaries, explanations, implementation guidance, and machine-readable
metadata — structured for LLM wikis, RAG, Graph RAG, and coding agents.

Each category below has its own `index.md` indexing its articles.

## Protocol surface

- [Operations](operations/index.md) — everything a client can ask a server to
  do (v2.1 §6.1; v1.x §4), plus the [server-to-client](operations/server-to-client/index.md)
  operations (§6.2). Create, register, get, locate, the cryptographic services,
  lifecycle, and protocol housekeeping.
- [Objects](objects/index.md) — the Managed Objects operations act on: keys,
  certificates, secret data, and the shared structures they are built on
  (v2.1 §2; v1.x §2.2).
- [Attributes](attributes/index.md) — the metadata KMIP keeps about every
  managed object (v2.1 §4; v1.x §3).
- [Messages](messages/index.md) — the request/response envelope: framing,
  batching, authentication, versioning, and result reporting (v2.1 §8–§9).

## Encoding and structure

- [TTLV Encoding](encoding/index.md) — KMIP's binary Tag/Type/Length/Value wire
  shape (v2.1 §10.1; v1.x §9), plus enumerations and bit masks.
- [Enumerations](enumerations/index.md) — the named value sets used throughout
  the protocol (§11).
- [Data Structures](structures/index.md) — composite TTLV structures reused
  across objects, attributes, and operation payloads.

## Cross-cutting and guidance

- [Concepts](concepts/index.md) — topics that apply to every exchange:
  authentication, transport, error handling.
- [Profiles](profiles/index.md) — how conformance works; named server and
  client profiles from the separate OASIS profiles document (v2.1 §14; v1.x §12).
- [Usage Guide](usage-guide/index.md) — implementation guidance distilled from
  the non-normative OASIS KMIP Usage Guide.
- [Workflows](workflows/index.md) — end-to-end flows that chain operations into
  protocol-level recipes.
- [Examples](examples/index.md) — worked, original request/response examples.

## Reference material

- [Versions](versions/index.md) — machine-readable per-version section maps and
  delta notes between releases.
- [Mappings](mappings/index.md) — cross-reference tables to other standards and
  across KMIP's own versions.
- [References](references/index.md) — vocabulary and citations from §1 of the
  spec.
