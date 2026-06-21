---
title: Profile Information
category: structures
spec_version: "2.1"
spec_versions: ["1.3", "1.4", "2.0", "2.1"]
source_section: "7.31"
v1_source_section: "2.1.19"
status: reviewed
related: ["capability-information", "validation-information", "kmip-server-implementation-conformance"]
keywords: ["profile information", "profile name", "server URI", "conformance discovery", "4200EB", "ProfileInformation"]
tag_hex: "4200EB"
xml_text: "ProfileInformation"
tag_type: "Structure"
---

# Profile Information

## Overview

A runtime advertisement of conformance: each instance names one
[profile](../profiles/index.md) the implementation supports, optionally with
the endpoint where that profile is served. Returned by
[Query](../operations/query.md) (Query Profiles) from 1.3 onward — by servers
and, via the [server-to-client
Query](../operations/server-to-client/query.md), by clients.

## Encoding (Tag / Type / Length / Value)

Structure, tag `4200EB`:

| Field | Tag | XML Text | Type | Required |
|---|---|---|---|---|
| Profile Name | `4200EC` | `ProfileName` | Enumeration | Yes |
| Server URI | `4200ED` | `ServerURI` | Text String | No |
| Server Port | `4200EE` | `ServerPort` | Integer | No |

## Fields & Structure

The Profile Name enumeration is a long registry (over a hundred values)
enumerating every published profile variant — baseline server/client,
symmetric key lifecycle, tape library, suite B, storage arrays, HTTPS/JSON/
XML bindings, and so on, each in client and server flavors. The URI/port
fields matter when one vendor endpoint speaks different profiles on
different listeners.

## Examples

Query (Profiles) answer: two Profile Information structures — { Baseline
Server Basic KMIP v2.1 } and { Symmetric Key Lifecycle Server KMIP v2.1,
Server URI `tls://kms.example.com`, Server Port 5696 }.

## Related

[Capability Information](capability-information.md) ·
[Validation Information](validation-information.md) ·
[Server conformance](../profiles/kmip-server-implementation-conformance.md)
