---
title: Vendor Extensions
category: usage-guide
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "ug-3.59"
status: draft
related: ["extensible-protocol", "message-extensions"]
keywords: ["vendor extensions", "custom attributes", "x- prefix", "y- prefix", "TTLV tags", "extension registration"]
---

# Vendor Extensions

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

KMIP provides several extension points for vendor-specific differentiation: reserved enumeration ranges, reserved TTLV tag ranges (0x54xxxx), client-defined attributes with an "x-" prefix, and server-defined attributes with a "y-" prefix. Extensions allow vendor implementations to communicate information not yet standardised in the specification.

## Guidance

A common use for extensions is structured vendor attribute definitions using KMIP TTLV encoding. Instead of packing vendor data into an opaque byte string, a vendor can define a structured TTLV attribute layout that other KMIP-aware tools may at least identify (even if they cannot interpret it), enabling better tooling support and forward compatibility.

Extension semantics must be agreed upon out-of-band between the client and server vendor. KMIP provides no protocol mechanism for negotiating extension semantics at runtime. Clients should use the Query Extension List and Query Extension Map functions to discover which extensions a server supports.

## Implementation Notes

Extensions should be registered with the KMIP Technical Committee to avoid tag collisions and to allow future standardisation. The registration procedure (documented in §4.4) involves submitting a description of the extension — including proposed tag values, names, types, use cases, and example messages — to the KMIP TC for review and ballot. Unregistered extensions risk collision with extensions from other vendors or with future KMIP spec additions.

## Related Concepts

See [Extensible Protocol](extensible-protocol.md) and [Registering Extension Information](registering-extension-information.md).
