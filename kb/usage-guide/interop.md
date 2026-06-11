---
title: Interop
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.4", "2.0", "2.1"]
source_section: "ug-3.45"
status: draft
related: ["client-and-server-correlation-values"]
keywords: ["interoperability testing", "test case identifier", "server log", "KMIP TC", "automated testing"]
---

# Interop

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

The Interop mechanism allows a client to indicate to the server which interoperability test case is being executed, enabling the server to annotate its log entries with the test case identifier. This supports automated comparison of server logs against expected results during formal KMIP interoperability testing events.

## Guidance

The KMIP Technical Committee uses this mechanism during interoperability testing to correlate client-side test executions with server-side log entries. A client participating in interoperability testing sets the test case identifier in the appropriate request field; the server logs it alongside its normal audit records.

## Implementation Notes

This feature is specifically designed for use during TC-hosted interoperability testing. In production deployments, the Client Correlation Value (§3.52) is the more general mechanism for tagging requests with application-level identifiers.

## Related Concepts

See [Client and Server Correlation Values](client-and-server-correlation-values.md).
