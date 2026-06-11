---
title: Extensible Protocol
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-2.4"
status: draft
related: ["vendor-extensions"]
keywords: ["vendor extensions", "interoperability", "custom attributes", "private extensions"]
---

# Extensible Protocol

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

KMIP is designed to be extensible: implementations may add vendor-specific or private extensions without breaking interoperability with the core protocol. Any objects, attributes, and operations that are included in an implementation must, however, be implemented exactly as the specification defines them.

## Guidance

Extensions in KMIP fall into several categories: vendor-defined enumerations within reserved ranges, custom attributes with client-defined ("x-" prefix) or server-defined ("y-" prefix) names, and proprietary Message Extension structures that can be appended to any request or response. Extensions allow vendors to differentiate their implementations and transmit information not yet standardised in KMIP.

The key constraint is consistency: if a vendor chooses to support a KMIP-defined operation or attribute, that feature must conform exactly to the spec, regardless of whether it is optional or mandatory. Partial or deviant implementations of standard features are not permitted.

## Implementation Notes

When relying on vendor extensions for interoperability between two different vendors' implementations, both sides must agree on the extension semantics out-of-band — there is no KMIP-level negotiation for extension semantics. Clients should use the Query operation to discover which extensions a given server supports before attempting to use them.

## Related Concepts

See [Vendor Extensions](vendor-extensions.md) for guidance on how to register and use KMIP extensions, and [Message Extensions](message-extensions.md) for the protocol mechanism for attaching vendor structures to messages.
