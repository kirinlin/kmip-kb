---
title: Authentication
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.1"
status: reviewed
related: ["credential", "transport"]
keywords: ["authentication", "TLS", "credential", "username password", "device credential", "attestation", "identity"]
tag_hex: "42000C"
xml_element: "Authentication"
---

# Authentication

## Overview

Authentication in KMIP operates on two levels: channel-level authentication provided by TLS (establishing server identity and optionally client identity via certificates) and an optional KMIP-level Credential structure carried in the Request Header (providing additional client identity information). Both levels can be used together, and a server may require both.

## Guidance

A conformant KMIP implementation uses the chosen authentication suite from KMIP-Prof to authenticate clients. The optional Authentication structure in the Request Header carries a Credential object that allows the client to supply supplementary identity information — such as a username and password — beyond what the TLS certificate provides. This is useful when a single TLS certificate authenticates a machine or service account used by multiple human users, and the server needs to identify the individual requestor.

When both a TLS client certificate and a Credential structure are present, the server verifies that the username in the certificate and the username in the Credential agree; if they differ, authentication fails. If authentication fails entirely, the server should return "authentication not successful" in preference to any other error to prevent status-code probing.

## Implementation Notes

Three Credential Types are defined: Username and Password (the simplest, pairing a username with an optional password), Device Credential (for devices identified by hardware serial number, MAC address, machine identifier, or media identifier — used in proxy/aggregator deployments such as tape libraries), and Attestation (for integrity measurement of the client environment). The Device Credential supports four optional identifying fields that are unique in aggregate, allowing the server to enforce uniqueness rules across combinations of identifiers.

## Related Concepts

See [Authorization for Revoke, Recover, Destroy and Archive Operations](authorization-for-revoke-recover-destroy-and-archive-operations.md) for how authentication feeds into operation-level authorisation.
