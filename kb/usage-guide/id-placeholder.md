---
title: ID Placeholder
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.5"
status: draft
related: ["batched-requests-and-responses", "reducing-multiple-requests-through-the-use-of-batch"]
keywords: ["ID placeholder", "batch", "pipeline", "unique identifier", "request chaining"]
---

# ID Placeholder

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

The ID Placeholder is a server-side temporary variable, scoped to a single batch execution, that holds the Unique Identifier of a recently created or located object. By omitting the Unique Identifier in a subsequent batch item, a client implicitly uses the ID Placeholder — enabling result-chaining within a single batch request without knowing the identifier in advance.

## Guidance

Certain operations (Create, Register, Locate, Certify, Re-key, etc.) set the ID Placeholder as a side effect of successful completion. Other operations (Get, Activate, Revoke, Destroy, etc.) read from the ID Placeholder when no explicit Unique Identifier is supplied. This allows a client to, for example, Create a key and then immediately Activate it in one batch, without needing to parse an intermediate response.

In addition to the implicit placeholder, KMIP supports explicit cross-batch-item references: a client can specify the result of a particular batch item by enumeration type or index integer, providing more precise and readable chaining.

## Implementation Notes

If an operation that sets the ID Placeholder fails, the placeholder is not updated, and downstream batch items that depend on it will fail as well. Batch Error Continuation options determine whether the batch stops or continues after such a failure. The ID Placeholder is reset at the start of each batch; it does not persist across separate request messages.

## Related Concepts

See [Batched Requests and Responses](batched-requests-and-responses.md) and [Reducing Multiple Requests Through the Use of Batch](reducing-multiple-requests-through-the-use-of-batch.md).
