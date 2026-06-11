---
title: Result Reasons
category: usage-guide
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "ug-3.57"
status: draft
related: ["result-message-text"]
keywords: ["Result Reason", "error diagnosis", "error codes", "self-diagnosis", "Result Status"]
---

# Result Reasons

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

Additional Result Reason values were added in KMIP 2.1 to provide finer-grained error information to clients. Previously, many common error conditions resolved to a single generic Result Reason; the expanded set enables clients to self-diagnose error situations without contacting the server administrator.

## Guidance

Clients should map specific Result Reason values to actionable recovery procedures. For example, distinguishing between "Item Not Found" and "Permission Denied" allows a client to determine whether a retry with different credentials or a different query is appropriate, versus whether the object truly does not exist.

The expanded Result Reason set improves the adoption of new KMIP capabilities by making it clear to clients why a particular request failed, especially for optional features that may not be supported by all servers.

## Implementation Notes

New Result Reason values added in v2.1 may not be present in older server implementations. Clients targeting multiple protocol versions should treat unrecognised Result Reason values as generic failures and fall back to server-contact-based diagnosis. Keep Result Reason handling in a single, well-tested function that is easy to update as new values are added.

## Related Concepts

See [Result Message Text](result-message-text.md).
