---
title: Result Message Text
category: usage-guide
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "ug-3.56"
status: reviewed
related: ["result-reasons"]
keywords: ["Result Message", "Result Status", "Result Reason", "internationalisation", "error message", "language"]
---

# Result Message Text

## Overview

KMIP specifies the Result Status and Result Reason as normative enumerated values, and the Result Message as a normative field. However, the text content of Result Messages is implementation-defined. Vendors are recommended to implement language support for Result Message text to facilitate internationalisation.

## Guidance

The normative enumeration values for Result Status and Result Reason ensure consistent machine-readable error signalling across implementations. The Result Message provides a human-readable explanation whose content is entirely up to the implementation. Clients should base their error-handling logic on Result Status and Result Reason, not on Result Message text, since message text is non-standardised.

KMIP does not define a mechanism for clients to request a specific language for Result Message content.

## Implementation Notes

Implementations targeting international deployments should implement language selection for Result Message text, using an appropriate mechanism (e.g., Accept-Language header in HTTP transport, or an out-of-band session configuration). Do not parse Result Message text programmatically; use Result Reason for machine-readable error classification.

## Related Concepts

See [Result Reasons](result-reasons.md) for the machine-readable error classification.
