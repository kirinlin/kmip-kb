---
title: Authentication
category: concept
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4"]
source_section: "8"
status: draft
related: ["transport", "error-handling", "credential", "kmip-server-implementation-conformance"]
keywords: ["authentication", "TLS", "client certificate", "credential", "identity", "mutual authentication"]
---

# Authentication

## Overview

KMIP deliberately keeps authentication out of the message format. The 1.x
specifications do not define a login handshake or password exchange of their
own; instead they require that the channel carrying KMIP messages already
authenticate both ends, and they delegate the concrete mechanism to the
companion profiles document. In practice this means mutual TLS: the baseline
profiles require servers and clients to negotiate TLS with client
certificates, so by the time the first KMIP request arrives the server already
knows who is talking.

## Details

Two layers cooperate:

1. **Channel authentication** — established by the [transport](transport.md)
   (TLS with mutual certificate verification per the profiles). This is the
   normative anchor: §8 of the spec simply points at the profiles document for
   the required mechanisms.
2. **In-message identity claims** — the optional
   [Authentication](../ttlv/authentication.md) structure in the request
   header, which carries one or more [Credential](../ttlv/credential.md)
   structures (Username and Password, Device, or — from 1.2 — Attestation).
   These let a client supply an application-level identity on top of the TLS
   identity, for example when many users share one TLS-authenticated
   connection.

Servers decide by policy which requests need authentication: none, some, or
all. The spec recommends that [Query](../operations/query.md) remain usable
without authentication so that clients can probe server capabilities before
enrolling. When credentials fail to validate, the server fails the batch item
with the `Authentication Not Successful`
[result reason](../ttlv/result-reason.md).

## Implications for Implementers

- Treat the TLS identity as primary. A Credential in the header refines or
  supplements it; it is not a substitute for channel authentication.
- Decide explicitly how to reconcile a TLS client certificate with a
  Username/Password or Device credential that names someone else — the spec
  leaves this to server policy, and interoperability problems often hide here.
- Device credentials identify machines (serial numbers, network or media
  identifiers, optionally a shared secret); at least one identifying field
  must be present and the combination must be unique on the server.
- Attestation credentials (1.2+) involve a server-issued
  [Nonce](../ttlv/nonce.md) and TPM/SAML evidence; only advertise support if
  you can actually validate the evidence.

## Related Concepts

[Transport](transport.md) · [Error Handling](error-handling.md) ·
[Authentication structure](../ttlv/authentication.md) ·
[Credential](../ttlv/credential.md)
