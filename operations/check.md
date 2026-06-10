---
title: Check
category: operation
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.10"
status: draft
related: ["locate", "get", "obtain-lease", "get-usage-allocation", "cryptographic-usage-mask"]
keywords: ["check", "policy check", "usage check", "batch", "pre-flight"]
---

# Check

## Purpose

`Check` asks the server, ahead of time, whether the client is permitted to use
an object in a particular way. It is meant to be used inside a batch — typically
between a [Locate](locate.md) (or a create/derive/certify operation) and a
[Get](get.md) — as a pre-flight test so the batch can stop early if policy would
reject the intended use.

## Request Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | No | The object to check; the ID Placeholder is used when omitted. |
| Usage Limits Count | No | An amount of usage the client wants to confirm is available. |
| Cryptographic Usage Mask | No | The operations the client intends to perform with the object. |
| Lease Time | No | A lease duration the client wants to confirm the server would grant. |

These fields are sent as plain objects, not wrapped in an Attribute structure.

## Response Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | Yes (unless failure) | The object's identifier, returned when the check passes. |
| Usage Limits Count | No | Returned when the requested usage exceeds what policy allows. |
| Cryptographic Usage Mask | No | Returned when the requested usage is rejected by policy. |
| Lease Time | No | Returned when the requested lease exceeds what the server would grant. |

## Behavior & Server Requirements

If the client is permitted the requested use, the server returns the object's
[Unique Identifier](../attributes/unique-identifier.md). If not, it clears the
ID Placeholder, withholds the identifier, and returns just those request values
that caused the denial — so the client learns precisely what was rejected and
can adapt. Each field has a distinct meaning: the
[usage mask](../attributes/cryptographic-usage-mask.md) states the operations
the client means to perform right now (which may be narrower than a mask used in
a preceding [Locate](locate.md)); the usage count reserves nothing but confirms
availability; and the [lease time](../attributes/lease-time.md) confirms a lease
*could* be granted without actually granting one (that is
[Obtain Lease](obtain-lease.md)'s job). Because `Check` is meant for batches,
the batch order option should be set so operations run in sequence, and only the
Stop or Undo error-continuation behaviors should be used.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). A policy
denial is reported through the returned offending fields rather than as an error;
genuine errors include an unknown object or insufficient permission.

## Related Operations

[Locate](locate.md) · [Get](get.md) · [Obtain Lease](obtain-lease.md) ·
[Get Usage Allocation](get-usage-allocation.md)
