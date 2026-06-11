---
title: Large Responses
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-2.10"
status: draft
related: ["maximum-message-size", "handling-large-locate-result-sets"]
keywords: ["maximum response size", "large response", "Locate", "truncation", "pagination"]
---

# Large Responses

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

For operations that might produce large responses, KMIP provides a mechanism for the client to declare an upper bound on response size. If the actual response would exceed that bound, the server returns a "maximum message size exceeded" error rather than a truncated or oversized response.

## Guidance

Clients specify the Maximum Response Size in the request header. For Locate operations, an additional Maximum Items field limits the number of unique identifiers returned. The server signals an oversized response with an error code rather than returning partial data, so clients know definitively that they did not receive the full result.

## Implementation Notes

When a maximum size error is received, the client's options are to issue a narrower query (using more specific Locate criteria), request the result in pages using the Offset Items and Maximum Items fields of the Locate operation, or increase the Maximum Response Size. For batch operations, the server applies the cumulative size check after each batch item rather than at the end, allowing it to identify exactly where the response exceeded the limit.

## Related Concepts

See [Maximum Message Size](maximum-message-size.md) for batch-specific considerations, and [Handling Large Locate Result Sets](handling-large-locate-result-sets.md) for the pagination pattern.
