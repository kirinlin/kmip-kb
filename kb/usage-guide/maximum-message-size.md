---
title: Maximum Message Size
category: usage-guide
spec_version: "2.1"
spec_versions: ["2.0", "2.1"]
source_section: "ug-3.54"
status: draft
related: ["large-responses", "batched-requests-and-responses"]
keywords: ["Maximum Response Size", "batch", "message size", "error response", "cumulative size check"]
---

# Maximum Message Size

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

When a server processes batch requests, it checks the cumulative size of the response after each batch item. If the total response would exceed the Maximum Response Size specified in the request, the server returns a maximum-message-size error at the point of overflow rather than continuing to process remaining items.

## Guidance

This per-item check (rather than a final check after all items) allows the client to know precisely which items completed before the size limit was hit. The server should not include attribute values or other detailed information in the error response itself, keeping the error response compact.

The Locate operation also supports a Maximum Items count to limit the number of returned identifiers, providing an additional control for large result sets.

## Implementation Notes

Clients performing large batches should size their requests to leave headroom below the Maximum Response Size limit, accounting for the overhead of TTLV encoding for each item's response. A safe strategy is to keep batch sizes moderate and test empirically against the target server to find the practical limit before deploying in production.

## Related Concepts

See [Large Responses](large-responses.md) and [Handling Large Locate Result Sets](handling-large-locate-result-sets.md).
