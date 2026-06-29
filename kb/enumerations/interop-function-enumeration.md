---
title: Interop Function Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "11.22"
status: reviewed
related: ["interop", "interop-function", "interop-identifier", "query-function-enumeration"]
keywords: ["interop", "interoperability", "test function", "conformance testing", "KMIP interop", "420160", "InteropFunction"]
tag_hex: "420160"
xml_text: "InteropFunction"
tag_type: "Enumeration"
---

# Interop Function Enumeration

## Overview

The Interop Function enumeration names the specific interoperability test function to invoke via the [Interop](../operations/interop.md) operation. The Interop operation is designed to support conformance and interoperability testing by allowing one KMIP endpoint to invoke named test scenarios on another, verifying that both parties implement a given set of operations consistently. Each enumeration value corresponds to a named test function that exercises a particular KMIP capability, such as creating a key, locating it by attribute, or destroying it. This makes automated KMIP conformance test suites expressible within the protocol itself.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Begin | `00000001` | `Begin` |  |
| End | `00000002` | `End` |  |
| Reset | `00000003` | `Reset` |  |

## Examples

A KMIP client vendor running an interoperability test with a server vendor's implementation would submit an Interop request specifying **Create** to verify that both sides handle a Create operation identically, then follow up with **Get** and **Destroy** to confirm the full lifecycle round-trip. The Interop Identifier field distinguishes among different test vectors for the same operation name.

## Related

- [Interop operation](../operations/interop.md) — the operation that accepts this enumeration
- [Interop Function structure](../structures/interop-function.md) — the TTLV structure pairing this enumeration with an identifier
- [Interop Identifier structure](../structures/interop-identifier.md) — qualifies which test instance of the named function to run
- [Query Function Enumeration](query-function-enumeration.md) — servers advertise supported interop functions via Query
