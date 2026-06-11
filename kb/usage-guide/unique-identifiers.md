---
title: Unique Identifiers
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.31"
status: reviewed
related: ["id-placeholder"]
keywords: ["Unique Identifier", "custom format", "out-of-band configuration", "object identification"]
---

# Unique Identifiers

## Overview

KMIP uses Unique Identifiers to identify managed objects. If a deployment requires Unique Identifiers in a specific format (such as UUIDs, sequential integers, or application-defined strings), this requirement must be communicated to the server through out-of-band registration or configuration — KMIP itself does not include a protocol mechanism for clients to specify or negotiate identifier formats.

## Guidance

By default, server implementations choose their own Unique Identifier format. Clients that need specific identifier formats (for cross-system correlation, audit integration, or legacy compatibility) should configure the server out-of-band and test that the expected format is produced before deploying in production.

## Implementation Notes

Clients should treat Unique Identifiers as opaque strings and not attempt to parse or generate them unless the deployment contract explicitly specifies a format. Assuming a particular identifier format (e.g., that all UUIDs will be lowercase) is a common source of interoperability bugs.

## Related Concepts

See [ID Placeholder](id-placeholder.md) for how Unique Identifiers are used across batch items.
