---
title: Message Extensions
category: usage-guide
spec_version: "2.1"
spec_versions: ["2.0", "2.1"]
source_section: "ug-3.55"
status: reviewed
related: ["vendor-extensions"]
keywords: ["Message Extension", "vendor extension", "optional structure", "KMIP message", "multiple extensions"]
---

# Message Extensions

## Overview

Any KMIP request or response may include one or more Message Extension optional structures. Message Extensions allow implementations to attach vendor-specific data to any KMIP message without disrupting standard KMIP message processing.

## Guidance

Multiple Message Extensions may be present in a single message. Each extension is identified by an extension name and contains vendor-defined data. Clients and servers that do not understand a given extension should ignore it (the protocol does not require extensions to be parseable by non-aware parties).

## Implementation Notes

Message Extensions are the transport mechanism for vendor-specific negotiation, diagnostics, or operational data that does not belong in the KMIP-defined request/response payload. They should not be used to carry security-critical information that both parties must agree on, since extension handling is optional and a non-aware server may silently ignore them. For mandatory vendor features, custom attributes or a proprietary extension of the operation payload is more appropriate.

## Related Concepts

See [Vendor Extensions](vendor-extensions.md) for the broader extension model.
