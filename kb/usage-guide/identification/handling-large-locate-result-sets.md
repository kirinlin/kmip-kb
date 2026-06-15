---
title: Handling Large Locate Result Sets
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.4", "2.0", "2.1"]
source_section: "ug-3.46"
status: reviewed
related: ["large-responses", "id-placeholder"]
keywords: ["Locate", "Offset Items", "Maximum Items", "Located Items", "pagination", "result set"]
---

# Handling Large Locate Result Sets

## Overview

When a Locate operation matches a large number of objects, the Offset Items and Maximum Items fields allow a client to page through the result set incrementally. The server may also return the total count of matching objects in the Located Items field, enabling the client to plan its pagination strategy.

## Guidance

To paginate: issue a first Locate with Maximum Items set to the desired page size and Offset Items set to 0. Subsequent pages use incrementally larger Offset Items values. The Located Items count (when returned) tells the client the total size of the result set.

The KMIP specification does not require results to be returned in any particular order. If objects are created, modified, or deleted between paginated Locate requests, the page boundaries may shift: items may be duplicated across pages or missed entirely. This is an inherent limitation of paginated queries without server-side cursor support.

## Implementation Notes

Stable pagination requires a stable result set. If items are being actively created or destroyed during a paginated traversal, clients should either accept approximate results or lock down the object pool for the duration. For large administrative tasks (audits, bulk exports), scheduling them during maintenance windows reduces interference from concurrent modifications.

## Related Concepts

See [Large Responses](../messaging/large-responses.md) and [ID Placeholder](id-placeholder.md).
