---
title: Mutating Attributes
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.17"
status: draft
related: ["attributes", "key-state-and-times"]
keywords: ["mutating attributes", "server mutation", "backdated attributes", "clock skew", "Invalid Field", "Result Reason"]
---

# Mutating Attributes

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

KMIP prohibits servers from silently modifying client-supplied attribute values. If a server cannot accept an attribute value provided by a client, it must return an error with "Invalid Field" as the Result Reason; it may not substitute an alternative value without the client's knowledge.

## Guidance

The most common scenario where this matters is time-related attributes. If a client sets a time attribute to its perceived "current time" but the server's clock is ahead, the server may see the value as backdated. Servers are not required to fail such requests, but a server that lacks backdated attribute support will return an error.

For clients in clock-skew environments that need to set a time attribute to "right now," the recommended approach is to trigger the corresponding state-change operation (e.g., issuing Activate rather than explicitly setting the Activation Date) so that the server uses its own clock. This avoids any attribute value being set by the client at all.

## Implementation Notes

If no clock-skew-safe alternative exists and backdated attribute values are rejected, clients must account for potential clock drift in their time attribute values (e.g., by subtracting an estimated maximum skew before submitting). The object's current State and the Time Stamp in each response header offer reference points for diagnosing clock-related problems.

## Related Concepts

See [Attributes](attributes.md) and [Key State and Times](key-state-and-times.md).
