---
title: Endpoint Role Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "11.19"
status: reviewed
related: ["set-endpoint-role", "profile-version", "profile-name-enumeration"]
keywords: ["endpoint role", "KMIP server", "KMIP client", "proxy", "replication", "storage array", "topology"]
---

# Endpoint Role Enumeration

## Overview

The Endpoint Role enumeration identifies the functional role of a KMIP endpoint within a key management topology. Modern KMIP deployments are not always simple client-server pairs: a key management system may include proxies that bridge protocol versions, replication partners that synchronise key material across sites, or storage devices that act as both a KMIP client (requesting keys) and a managed entity. This enumeration allows servers and clients to declare and negotiate their roles, supporting policy-based access control and routing decisions.

## Encoding (Tag / Type / Length / Value)

Encoded as a 4-byte integer (TTLV type `05`, Enumeration). Appears in the Set Endpoint Role operation request and in Profile Version structures that describe endpoint capabilities.

## Fields & Structure

- **Storage Array Client**: An endpoint that represents a storage controller or self-encrypting drive array. It acts as a KMIP client for the purpose of requesting encryption keys from the server, but its primary function is data storage rather than key management.
- **KMIP Client**: A general-purpose KMIP client — typically an application, middleware, or device driver — that submits key management requests on behalf of applications.
- **KMIP Server**: A full key management server that stores managed objects, enforces policies, and serves responses to KMIP clients.
- **KMIP Proxy**: An intermediary that forwards KMIP requests between clients and servers, potentially translating between protocol versions or aggregating clients behind a single authenticated identity.
- **Replication Source**: An endpoint that acts as the origin in a key replication relationship, pushing key objects to one or more replication destinations.
- **Replication Destination**: An endpoint that receives replicated key objects from a Replication Source. It holds copies of key material for availability or geographic redundancy.

## Examples

A cloud key management service deployed in two data centres might configure each instance as both a **Replication Source** and a **Replication Destination**, forming a bidirectional sync pair. A thin VM agent that proxies requests from applications to the central KMIP server would declare itself as a **KMIP Proxy**.

## Related

- [Set Endpoint Role operation](../../operations/set-endpoint-role.md) — the operation that assigns an endpoint role
- [Profile Name Enumeration](profile-name-enumeration.md) — conformance profiles constrain which roles an endpoint may claim
