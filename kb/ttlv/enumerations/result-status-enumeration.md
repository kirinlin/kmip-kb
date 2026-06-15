---
title: Result Status Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.47"
status: reviewed
related: ["result-reason-enumeration", "message-structure", "error-handling", "asynchronous-request"]
keywords: ["result status", "success", "operation failed", "operation pending", "operation undone", "batch response"]
tag_hex: "42007F"
xml_element: "ResultStatus"
---

# Result Status Enumeration

## Overview

The Result Status enumeration is the top-level success or failure indicator in every batch item response. It appears in every KMIP response alongside an optional Result Reason and Result Message, giving clients a structured way to distinguish success from the various categories of failure without parsing free-text messages.

## Encoding (Tag / Type / Length / Value)

Encoded as a 4-byte integer (TTLV type `05`, Enumeration), tag `420092`.

## Fields & Structure

- **Success**: The operation completed without error. The response payload carries the operation's results.
- **Operation Failed**: The operation did not complete due to an error. Result Reason and Result Message provide details.
- **Operation Pending**: The operation was accepted but has not yet completed — it is being processed asynchronously. The response carries an Asynchronous Correlation Value that the client uses to poll via [Query Asynchronous Requests](../../operations/query-asynchronous-requests.md).
- **Operation Undone**: The operation was rolled back. Used when a batch request specifies the Undo error-continuation option and an earlier operation in the batch failed, causing the server to reverse previously completed operations in the same batch.

## Examples

A successful Create operation returns **Success** and a Unique Identifier. A Create that fails because the server cannot generate the requested algorithm returns **Operation Failed** with Result Reason = Feature Not Supported. A Create submitted with the Asynchronous Indicator returns **Operation Pending** with a correlation value.

## Related

[Result Reason Enumeration](result-reason-enumeration.md) · [Error Handling](../../concepts/error-handling.md) · [Asynchronous Request](../../structures/asynchronous-request.md) · [Message Structure](../../messages/message-structure.md)
