---
title: Message Extension
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "9.13"
v1_source_section: "6.16"
status: reviewed
related: ["batch-item", "extension-information", "ttlv-encoding"]
keywords: ["message extension", "vendor extension", "criticality indicator", "vendor identification"]
tag_hex: "420051"
xml_element: "MessageExtension"
---

# Message Extension

## Overview

The hook for vendor-proprietary additions to protocol messages: an optional
structure that can trail any [batch item](batch-item.md), carrying arbitrary
vendor content plus a flag that says whether understanding it is mandatory.

## Encoding (Tag / Type / Length / Value)

Structure, tag `420051`:

| Field | Tag | XML Element | Type | Required |
|---|---|---|---|---|
| Vendor Identification | `42009D` | `VendorIdentification` | Text String | Yes — uniquely names the vendor |
| Criticality Indicator | `420026` | `CriticalityIndicator` | Boolean | Yes |
| Vendor Extension | `42009C` | `VendorExtension` | Structure | Yes — the vendor-specific content |

## Fields & Structure

The criticality rule mirrors X.509 extensions: a receiver that does not
understand the extension must reject the whole message if the indicator is
True (failing with `Feature Not Supported`), and may simply ignore the
extension if False. The Vendor Identification lets a receiver decide whether
the contents are even parseable before trying. Tags inside the Vendor
Extension typically come from the Extensions range (`540000`–`54FFFF`,
discoverable via [Extension Information](extension-information.md)).

## Examples

A vendor attaches non-critical telemetry: Message Extension { Vendor
Identification = `"Acme"`, Criticality Indicator = False, Vendor Extension {
0x540010: request latency budget } }. Foreign servers ignore it; Acme
servers honor it.

## Related

[Batch Item](batch-item.md) ·
[Extension Information](extension-information.md) ·
[TTLV Encoding](ttlv-encoding.md)
