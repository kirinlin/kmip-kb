---
title: Default Crypto Parameters
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.21"
status: reviewed
related: ["attributes", "constraints"]
keywords: ["default crypto parameters", "Cryptographic Algorithm", "CryptographicLength", "CryptographicUsageMask", "SetDefaults", "Query Defaults Information"]
---

# Default Crypto Parameters

## Overview

Servers may supply default values for required cryptographic parameters such as Cryptographic Algorithm, Cryptographic Length, and Cryptographic Usage Mask. When a client omits these parameters, the server uses its defaults rather than failing the request.

## Guidance

Default parameters are discoverable by clients via the Query operation with the Query Defaults Information function. From v2.1, the SetDefaults operation allows sufficiently privileged clients to change or clear the set of object defaults. ObjectDefaults can now be scoped to specific Object Groups, and a single default can apply to more than one Object Type (e.g., both Symmetric Key and Split Key).

This mechanism reduces the boilerplate in client requests for common object types and simplifies deployment of devices that create keys with well-known parameters.

## Implementation Notes

Clients that need deterministic behaviour — particularly in multi-vendor environments — should always specify cryptographic parameters explicitly rather than relying on server defaults. Server defaults may differ between vendors or between versions of the same product. Use Query Defaults Information to discover current defaults programmatically if client code must adapt to different server configurations.

## Related Concepts

See [Constraints](../messaging/constraints.md) for how servers limit acceptable parameter values, and [Attributes](../attributes/attributes.md) for general attribute management.
