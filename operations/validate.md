---
title: Validate
category: operation
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.24"
status: draft
related: ["certify", "certificate", "signature-verify"]
keywords: ["validate", "certificate chain", "validity indicator", "trust", "path validation"]
---

# Validate

## Purpose

`Validate` asks the server to check a certificate chain and report whether it is
valid. Server support is optional — a server that does not implement it returns
an error. Exactly one chain is validated per request.

## Request Fields

| Field | Required | Description |
|---|---|---|
| Certificate | No (may repeat) | One or more certificate objects supplied inline. |
| Unique Identifier | No (may repeat) | One or more identifiers of managed certificate objects. |
| Validity Date | No | The date at which the chain must be valid; the current time is assumed when omitted. |

The inline certificates and the referenced certificates together make up the
chain to be checked.

## Response Fields

| Field | Required | Description |
|---|---|---|
| Validity Indicator | Yes | Whether the chain is valid, invalid, or indeterminate. |

## Behavior & Server Requirements

How validation is performed — the policy applied, the order in which the chain
is processed, and which trust anchors terminate it — is entirely up to the
server and outside the scope of the protocol. The client simply receives the
verdict. A chain that fails to validate is reported through the Validity
Indicator rather than as an error.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: the operation not being supported, more than one chain supplied, or an
unknown certificate identifier.

## Related Operations

[Certify](certify.md) · [Signature Verify](signature-verify.md)
