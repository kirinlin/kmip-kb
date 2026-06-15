---
title: Server Information
category: ttlv
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "7.37"
status: reviewed
related: ["query", "profile-version", "protocol-version", "object-types", "protection-storage-masks"]
keywords: ["server information", "server name", "server version", "vendor identification", "server instance", "conformance clause"]
---

# Server Information

## Overview

Server Information is a structure embedded in [Query](../operations/query.md) responses that provides metadata about the KMIP server itself. Clients use it to learn the server's identity, version, vendor, and conformance posture — information that helps clients make decisions about which features to use, how to correlate audit records, and whether the server meets the requirements of a particular deployment.

## Encoding (Tag / Type / Length / Value)

Server Information encodes as a Structure. All fields are optional but servers are expected to populate the ones that are meaningful for their deployment.

| Field | Tag | XML Element | Type | Required |
|---|---|---|---|---|
| Server Name | `420244` | `ServerName` | Text String | No |
| Server Serial Number | `420245` | `ServerSerialNumber` | Text String | No |
| Server Version | `420246` | `ServerVersion` | Text String | No |
| Server Load | `420247` | `ServerLoad` | Text String | No |
| Product Name | `420248` | `ProductName` | Text String | No |
| Build Level | `420249` | `BuildLevel` | Text String | No |
| Build Date | `42024A` | `BuildDate` | Text String | No |
| Cluster Info | `42024B` | `ClusterInfo` | Text String | No |
| Alternative Failover Endpoints | `42024C` |  | Structure | No (repeating) |
| Vendor Identification | `420099` | `VendorIdentification` | Text String | No |
| Server Instance Information | `42024F` |  | Text String | No |
| Conformance Clause | `42020B` |  | Enumeration | No (repeating) |

## Fields & Structure

**Server Name** is a human-readable display name for this server instance — typically the product name or a deployment-assigned label.

**Server Serial Number** uniquely identifies the physical or virtual server instance, useful for correlating log entries from multiple servers in a cluster.

**Server Version** is a free-form version string for the server software — separate from the KMIP protocol version and the profile version.

**Vendor Identification** is the organization name of the server vendor, mirroring the field used in the KMIP 1.x Query response.

**Server Instance Information** carries deployment-specific metadata (data center location, environment tag, etc.) that administrators find useful.

**Conformance Clause** is a repeating Enumeration listing the KMIP conformance clauses the server claims to satisfy. Multiple entries are common for servers that conform to both Baseline and Complete tiers, for example.

**Alternative Failover Endpoints** carries connection details for standby or replica servers that clients can fall back to if the primary becomes unavailable.

## Examples

A Query response from a commercial HSM appliance might include Server Information with Server Name = `"ACME KMS v4.2"`, Vendor Identification = `"ACME Corp"`, Server Version = `"4.2.1-build-1234"`, Conformance Clause = Baseline Server, and Server Instance Information = `"DC1-rack7-unit3"`. A monitoring system uses the serial number and instance information to distinguish this server from its cluster peers in centralized log analysis.

## Related

[Query](../operations/query.md) · [Profile Version](profile-version.md) · [Protocol Version](protocol-version.md) · [Object Types](object-types.md) · [Protection Storage Masks](protection-storage-masks.md)
