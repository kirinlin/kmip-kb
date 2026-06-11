---
title: Returning Related Objects
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.3"
status: reviewed
related: ["get"]
keywords: ["related objects", "key pair", "certificate", "Get", "link attribute", "multiple requests"]
---

# Returning Related Objects

## Overview

A single KMIP Get operation returns exactly one managed object. When a client needs multiple related objects — for example a private key and its associated certificate — it must issue separate Get requests for each.

## Guidance

The Key Block carries one object with its associated attributes. There is no batch-Get that returns multiple objects in a single response item. Clients that routinely need correlated sets of objects (a key pair, a chain of certificates) should use the Link attribute to navigate from one object's identifier to the related identifiers and then fetch each in turn, possibly within a single batch request.

## Implementation Notes

In practice, the common pattern is to use Locate to find an object matching known attributes, then use the Link attributes on the located object to discover related object IDs, and finally issue a batch of Get requests. This can be expressed efficiently as a single batched message containing a Locate followed by multiple Gets using the ID Placeholder or explicit Unique Identifiers.

## Related Concepts

See [Batched Requests and Responses](batched-requests-and-responses.md) and [ID Placeholder](id-placeholder.md) for the mechanisms that make multi-object retrieval efficient.
