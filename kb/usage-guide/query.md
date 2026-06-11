---
title: Query
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.4", "2.0", "2.1"]
source_section: "ug-3.48"
status: reviewed
related: ["discover-versions"]
keywords: ["Query", "Query Function", "Capability Information", "extensions", "profiles", "RNGs", "validations", "Client Registration Methods"]
---

# Query

## Overview

Query comes in two directions: a Client-to-Server variant and a symmetric Server-to-Client variant. Both are conceptually similar — a request for capability or state information — but the parameters differ because some concepts apply only to one side. Clients typically use Client-to-Server Query to discover server capabilities before using optional features.

## Guidance

The Query Function enumeration controls what information is returned. Key query functions include:

- **Query Extensions**: Lists the vendor-specific tags and operations the server supports.
- **Query RNGs**: Lists the random number generators available.
- **Query Validations**: Lists external validations (FIPS 140, Common Criteria) applicable to the server.
- **Query Profiles**: Lists the KMIP Profiles the server supports from each spec version.
- **Query Capabilities**: Lists optional spec features and alternate behaviours the server supports.
- **Query Client Registration Methods**: Lists supported automated client registration approaches.

## Implementation Notes

Query does not enumerate which operations require authentication. The practical approach is to attempt the desired operation and handle any authentication error that comes back. Test cases for the various Query functions are in the KMIP Test Cases document. Query is the primary tool for writing adaptive client code that works across multiple server implementations.

## Related Concepts

See [Discover Versions](discover-versions.md) for protocol version negotiation.
