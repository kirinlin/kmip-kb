---
title: Result Reason Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.46"
status: reviewed
related: ["result-status-enumeration", "message-structure", "error-handling"]
keywords: ["result reason", "error code", "failure reason", "item not found", "operation not supported", "permission denied"]
---

# Result Reason Enumeration

## Overview

The Result Reason enumeration provides the specific error code within a failed batch item response. Where [Result Status](result-status-enumeration.md) conveys the broad outcome (success vs. failure vs. pending), Result Reason pinpoints why a failure occurred. Both appear in every batch item response alongside an optional Result Message text string, giving clients structured error information they can respond to programmatically.

## Encoding (Tag / Type / Length / Value)

Encoded as a 4-byte integer (TTLV type `05`, Enumeration), tag `42007A`.

## Fields & Structure

Common reasons include:

- **Item Not Found**: The Unique Identifier in the request does not correspond to any managed object on the server. The most frequent error for well-formed but referentially-invalid requests.
- **Response Too Large**: The server cannot return all requested data within a single response message. The client must use paging or narrow its request.
- **Authentication Not Successful**: The credential supplied is invalid, expired, or otherwise rejected by the authentication mechanism.
- **Invalid Message**: The request structure is malformed at the TTLV or message-structure level.
- **Operation Not Supported**: The server does not implement the requested operation.
- **Missing Data**: A required field is absent from the request.
- **Invalid Field**: A field value is syntactically or semantically incorrect.
- **Feature Not Supported**: The server supports the operation in general but not the specific combination of parameters or options requested.
- **Operation Cancelled**: The operation was terminated by a Cancel request.
- **Permission Denied**: The authenticated principal does not have the right to perform the operation on the target object.
- **Object Already Exists**: A Create or Register request conflicts with an existing object.
- **Wrong Key Lifecycle State**: The operation is not permitted given the object's current state (e.g., using a Deactivated key for encryption).
- **Constraint Violation**: An attribute-based constraint rule was violated.
- **Cryptographic Failure**: A cryptographic operation (sign, verify, encrypt) failed — for example, an invalid signature.
- **Protection Storage Unavailable**: The server cannot store the object in the protection environment required by the Protection Storage Mask attribute.

## Examples

A Get request for a non-existent key returns Result Status = **Operation Failed**, Result Reason = **Item Not Found**. A Destroy request on a key that is still Active returns Result Reason = **Wrong Key Lifecycle State**.

## Related

[Result Status Enumeration](result-status-enumeration.md) · [Error Handling](../../concepts/error-handling.md) · [Message Structure](../message-structure.md)
