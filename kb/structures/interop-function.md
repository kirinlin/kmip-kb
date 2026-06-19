---
title: Interop Function
category: structures
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "7.15"
status: reviewed
related: ["interop-identifier", "interop", "message-structure"]
keywords: ["interop function", "interoperability test", "test function", "interop operation", "KMIP testing", "420160", "InteropFunction"]
tag_hex: "420160"
xml_text: "InteropFunction"
---

# Interop Function

## Overview

Interop Function is a structure that identifies and parameterizes a single test function within a KMIP interoperability test scenario. It is a payload component of the [Interop](../operations/interop.md) operation — the mechanism by which two KMIP implementations can verify they produce identical results for a well-defined cryptographic or protocol operation.

Each Interop Function entry names a specific function (via an enumeration) and carries the input data that function should process. The result returned by the server can be compared against the expected output to confirm interoperability.

## Encoding (Tag / Type / Length / Value)

Interop Function encodes as a Structure.

| Field | Tag | XML Text | Type | Required |
|---|---|---|---|---|
| Interop Function Enumeration | `420280` |  | Enumeration | Yes |
| Data | `4200C2` | `Data` | Byte String | No |

The Data field carries the serialized input arguments for the function being invoked. Its content and format are defined by the specific function enumeration value.

## Fields & Structure

**Interop Function Enumeration** identifies which test function to execute. The set of defined function values corresponds to specific named test scenarios in the KMIP Interoperability Test Cases documents — for example, functions for encrypting a known plaintext, decrypting ciphertext, generating a MAC, or performing a key wrap/unwrap round-trip.

**Data** is the binary input payload for the function. For encryption test functions it might be the plaintext; for MAC functions it might be the message. The function definition dictates interpretation.

When the server executes the function, it uses the parameters embedded in the Data field along with any key referenced by the enclosing Interop operation's context. The response carries the function output, which the test harness compares against a known-good reference value.

## Examples

An interoperability tester sends an Interop operation containing an Interop Function with Interop Function Enumeration = EncryptSingle and Data = a 16-byte test plaintext. The server encrypts the plaintext using the key identified in the Interop request context and returns the ciphertext. The tester compares the ciphertext against the reference value from the shared test vector document to confirm interoperability.

## Related

[Interop Identifier](interop-identifier.md) · [Interop](../operations/interop.md) · [Message Structure](../messages/message-structure.md)
