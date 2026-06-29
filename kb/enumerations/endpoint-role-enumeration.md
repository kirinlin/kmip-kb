---
title: Endpoint Role Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "11.19"
status: reviewed
related: ["set-endpoint-role", "profile-version", "profile-name-enumeration"]
keywords: ["endpoint role", "KMIP server", "KMIP client", "proxy", "replication", "storage array", "topology", "420151", "EndpointRole"]
tag_hex: "420151"
xml_text: "EndpointRole"
tag_type: "Enumeration"
---

# Endpoint Role Enumeration

## Overview

The Endpoint Role enumeration identifies the functional role of a KMIP endpoint within a key management topology. Modern KMIP deployments are not always simple client-server pairs: a key management system may include proxies that bridge protocol versions, replication partners that synchronise key material across sites, or storage devices that act as both a KMIP client (requesting keys) and a managed entity. This enumeration allows servers and clients to declare and negotiate their roles, supporting policy-based access control and routing decisions.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Client | `00000001` | `Client` |  |
| Server | `00000002` | `Server` |  |

## Examples

A cloud key management service deployed in two data centres might configure each instance as both a **Replication Source** and a **Replication Destination**, forming a bidirectional sync pair. A thin VM agent that proxies requests from applications to the central KMIP server would declare itself as a **KMIP Proxy**.

## Related

- [Set Endpoint Role operation](../operations/set-endpoint-role.md) — the operation that assigns an endpoint role
- [Profile Name Enumeration](profile-name-enumeration.md) — conformance profiles constrain which roles an endpoint may claim
