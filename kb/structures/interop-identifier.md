---
title: Interop Identifier
category: structures
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "7.16"
status: reviewed
related: ["interop-function", "interop", "message-structure"]
keywords: ["interop identifier", "interoperability test suite", "test case name", "interop test identifier"]
tag_hex: "420161"
xml_element: "InteropIdentifier"
---

# Interop Identifier

## Overview

Interop Identifier is a structure that names the interoperability test suite or test case being exercised in an [Interop](../operations/interop.md) operation. It ties the low-level function calls within the Interop payload to a published, named test case so that both parties — the client and the server — are unambiguously referring to the same scenario from the KMIP Interoperability Test Cases documentation.

The identifier is primarily informational metadata: the server uses it for logging, the test harness uses it for result correlation, and human operators use it when reviewing interop test reports.

## Encoding (Tag / Type / Length / Value)

Interop Identifier encodes as a Structure.

| Field | Tag | XML Element | Type | Required |
|---|---|---|---|---|
| Interop Function Enumeration | `420280` |  | Enumeration | Yes |
| Interop Identifier Text | `420281` |  | Text String | No |

The Interop Function Enumeration scopes the identifier to a function family. The optional Text String carries a human-readable name or version qualifier for the specific test case within that family.

## Fields & Structure

**Interop Function Enumeration** names the category of test being identified. It mirrors the enumeration used in the [Interop Function](interop-function.md) structure and provides the primary machine-readable label.

**Interop Identifier Text** is an optional human-readable string — typically the exact test case name from the KMIP Interoperability Test Cases document (such as `"CS-BC-M-1-13"` for a particular baseline conformance test). Its value is informational; implementations should not vary behavior based on this string.

Together the two fields allow a test harness to record exactly which named scenario is being tested, making it straightforward to cross-reference results against a test plan or certification report.

## Examples

An automated conformance test driver sends an Interop operation with an Interop Identifier containing Interop Function Enumeration = Create and Interop Identifier Text = `"KMIP-TC-2.1-Create-AES-256"`. The server logs the name alongside the operation result. The driver uses the same name to match the response against the expected output in its test database.

## Related

[Interop Function](interop-function.md) · [Interop](../operations/interop.md) · [Message Structure](../messages/message-structure.md)
