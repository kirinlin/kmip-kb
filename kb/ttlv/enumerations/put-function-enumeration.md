---
title: Put Function Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.43"
status: reviewed
related: ["unique-identifier"]
keywords: ["put function", "put operation", "new object", "replace object", "Push operation"]
tag_hex: "420070"
xml_element: "PutFunction"
---

# Put Function Enumeration

## Overview

The Put Function enumeration controls the semantics of the `Put` operation — a server-to-client push operation defined in the KMIP server-to-client interaction model. It indicates whether the object being pushed to the client should be treated as a brand-new registration or as a replacement for an existing object the client already holds.

## Encoding (Tag / Type / Length / Value)

Encoded as a 4-byte integer (TTLV type `05`, Enumeration).

## Fields & Structure

- **New**: The object is being introduced to the client for the first time. The client should register it as a new managed object. If the client already holds an object with the same Unique Identifier, this is an error.
- **Replace**: The object supersedes an existing one the client holds with the same Unique Identifier. The client should update its copy. Useful for proactive key distribution where the server rotates keys and pushes replacements.

## Examples

A key management server that rotates a symmetric key and pushes it to a storage appliance uses Put Function = **Replace** so the appliance overwrites its cached copy rather than registering a second copy of the same key. A first-time provisioning of a new signing certificate uses **New**.

## Related

[Unique Identifier](../../attributes/unique-identifier.md)
