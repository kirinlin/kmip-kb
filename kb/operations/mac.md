---
title: MAC
category: operation
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.32"
v1_source_section: "4.33"
status: draft
related: ["mac-verify", "sign", "cryptographic-parameters", "symmetric-key"]
keywords: ["mac", "message authentication code", "hmac", "cmac", "integrity"]
---

# MAC

## Purpose

`MAC` has the server compute a message authentication code over client-supplied
data using a managed key. Added in KMIP 1.2, it produces a keyed integrity tag
(such as HMAC or CMAC) while keeping the key server-side.

## Request Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | No | The MAC key; the ID Placeholder is used when omitted. |
| Cryptographic Parameters | No | The algorithm to use for the MAC. |
| Data | Yes (single-part) | The data to authenticate, as a byte string. |
| Correlation Value | No | Ties this call to an in-progress multi-part operation. |
| Init Indicator | No | Marks the first call of a multi-part operation. |
| Final Indicator | No | Marks the last call of a multi-part operation. |

## Response Fields

| Field | Required | Description |
|---|---|---|
| Unique Identifier | Yes | The key that was used. |
| MAC Data | Yes (single-part) | The computed MAC, as a byte string. |
| Correlation Value | No | A handle to pass to subsequent calls of a multi-part operation. |

## Behavior & Server Requirements

The [cryptographic parameters](../attributes/cryptographic-parameters.md) may be
omitted and taken from the key's attributes when present. Like the other
cryptographic operations, `MAC` supports both one-shot and streamed processing
through a Correlation Value with Init and Final indicators, and reports its
outcome via the result status in the response header.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: required parameters missing and not derivable from the key, an unknown
key, or a key whose usage mask does not permit MAC generation.

## Related Operations

[MAC Verify](mac-verify.md) · [Sign](sign.md)
