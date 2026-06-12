---
title: Interop
category: operation
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "6.1.26"
status: reviewed
related: ["query", "ping", "interop-function", "interop-identifier"]
keywords: ["interop", "interoperability", "conformance", "test", "protocol validation", "interop function", "interop identifier"]
---

# Interop

## Purpose

`Interop` is a v2.1 operation that allows a client to invoke a named interoperability test function on the server. It provides a standardized channel for conformance testing, protocol validation, and vendor-specific interoperability exercises without requiring out-of-band communication or non-KMIP tooling. A client identifies the test to run via an [Interop Identifier](../ttlv/interop-identifier.md) and optionally parameterizes it with an [Interop Function](../ttlv/interop-function.md) and associated input data; the server executes the test and returns the result.

Servers that advertise interop capability in their [`Query`](query.md) response support this operation. Servers that do not advertise it must return Operation Not Supported.

## Request Fields

| Field | Required | Description |
|---|---|---|
| Interop Identifier | Yes | Names the interoperability scenario or test suite to invoke on the server. The [Interop Identifier](../ttlv/interop-identifier.md) structure encodes the test namespace and identifier. |
| Interop Function | No | Specifies the particular function within the named test to execute. The [Interop Function](../ttlv/interop-function.md) structure provides additional resolution when a test scenario contains multiple sub-functions. |
| Data | No | Input data for the interop function, such as a plaintext to encrypt or a message to sign, depending on the scenario being tested. |

## Response Fields

| Field | Required | Description |
|---|---|---|
| Interop Identifier | Yes | Echoes the identifier from the request for correlation. |
| Data | No | Output data produced by the interop function, such as ciphertext, a digest, or a signature result. |

## Behavior & Server Requirements

The server dispatches the request to the handler registered for the supplied Interop Identifier. If the identifier is recognized and the server supports the identified scenario, it executes the function and returns the result. If the identifier is not recognized, the server returns an error indicating that the specific interop function is not supported — distinct from a general Operation Not Supported response.

Interop functions are typically defined by KMIP test cases, industry working groups, or bilateral agreements between implementors. The KMIP specification does not enumerate all valid identifiers; the set is extensible and implementation-defined beyond those standardized by OASIS test case documents.

Results are deterministic for a given input — the `Interop` operation is not a side-effecting management operation and does not alter any managed objects. It is safe to call as part of a batch request alongside other operations.

Servers should log `Interop` calls in their audit trail so that conformance testing activity is recorded.

## Errors

Uses centralized error handling per the [error handling](../concepts/error-handling.md) conventions. Common failure causes include:

- The Interop Identifier refers to a test scenario the server does not support — the server returns an appropriate error code rather than a generic failure.
- The server does not support the `Interop` operation at all — returns Operation Not Supported.
- The supplied Data is malformed or the wrong size for the specified function.
- The Interop Function is not valid within the context of the supplied Interop Identifier.

## Examples

A test harness validating a new KMIP server implementation runs a symmetric encryption round-trip test to confirm the server produces the expected ciphertext for a known plaintext and key:

```
Operation: Interop
  Interop Identifier:
    Interop Scenario: "KMIP-Symmetric-Encrypt-AES-256-GCM"
  Interop Function:
    Function Name: "Encrypt"
  Data: <known plaintext bytes>
```

The server responds with the ciphertext, which the test harness compares against the expected output from the KMIP test case suite.

## Related Operations

[Query](query.md) · [Ping](ping.md)
