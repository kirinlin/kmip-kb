---
title: Archive Operations
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.38"
status: draft
related: ["authorization-for-revoke-recover-destroy-and-archive-operations"]
keywords: ["Archive", "Recover", "off-line storage", "State attribute", "operational efficiency"]
---

# Archive Operations

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

The Archive operation moves a managed object to off-line storage, and the Recover operation returns an archived object to on-line availability. After archival, the recommended practice is for the server to retain at minimum the Unique Identifier and State attributes for operational efficiency, allowing clients to locate and retrieve the archived object later via Recover.

## Guidance

The Archive/Recover pair supports long-term retention of objects that are not needed for active use but must be preserved for compliance or future use. Servers typically implement archival by moving key material to lower-cost or offline storage tiers while keeping minimal metadata on-line.

Because Archive is an operation that may have irreversible consequences for key availability, servers should apply the same elevated authentication and authorisation considerations described for Revoke, Destroy, and Recover.

## Implementation Notes

What attributes are retained in the minimal on-line record after archival is server-defined. Clients that need more than Unique Identifier and State to be retrievable should confirm with the server's documentation which attributes are retained before relying on attribute queries against archived objects.

## Related Concepts

See [Authorization for Revoke, Recover, Destroy and Archive Operations](authorization-for-revoke-recover-destroy-and-archive-operations.md).
