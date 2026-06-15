---
title: Support for "Intelligent Clients" and "Key Using Devices"
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-2.7"
status: reviewed
related: ["using-notify-and-put-operations"]
keywords: ["intelligent client", "key using device", "device credential", "IoT", "constrained device", "protocol subset"]
---

# Support for "Intelligent Clients" and "Key Using Devices"

## Overview

KMIP is designed to support a broad spectrum of client capability, from fully capable intelligent clients (such as workstations or enterprise applications) that can use every KMIP feature, down to simple key-using devices (such as self-encrypting drives or tape libraries) that need only a small subset of the protocol.

## Guidance

Intelligent clients can request any KMIP operation and use the full protocol. Less capable devices may rely on a subset of operations — typically Create, Register, Get, and Activate — and may use simplified message representations. The KMIP Profiles document defines a set of conformance profiles tailored to specific device types and use cases, which specify which operations and message formats are required or optional.

## Implementation Notes

In environments with constrained devices, a proxy pattern is common: an intelligent proxy communicates with the KMIP server using the full protocol on behalf of simpler devices that speak a proprietary or simplified protocol locally. The Device Credential type in the authentication structure is specifically designed to support this pattern by allowing the proxy to identify the downstream device to the server.

## Related Concepts

See [Using Notify and Put Operations](../messaging/using-notify-and-put-operations.md) for the server-to-client push mechanism that benefits constrained-device deployments.
