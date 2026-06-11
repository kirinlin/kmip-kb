---
title: Non-Cryptographic Objects
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.8"
status: draft
related: ["secret-data"]
keywords: ["Secret Data", "password", "key derivation", "non-cryptographic", "attributes", "Cryptographic Usage Mask"]
---

# Non-Cryptographic Objects

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

KMIP allows clients to register Secret Data objects that are used for non-cryptographic purposes — such as passwords, PINs, or data used to derive keys. Even when used non-cryptographically, these objects are still treated as cryptographic objects by the protocol, and the server applies the standard set of server-managed attributes to them.

## Guidance

Despite the non-cryptographic use intent, the protocol applies the same attribute management rules to Secret Data objects as to keys: the server applies its full set of mandatory server-managed attributes at registration — assigning a Unique Identifier, an Object Type, a Digest, an initial State, creation timestamps, and more. Clients may also set the Cryptographic Usage Mask for Secret Data objects, even if the attribute seems semantically relevant only to cryptographic operations.

This consistency in attribute handling simplifies server implementation and ensures that Secret Data objects participate fully in lifecycle management, auditing, and access control.

## Implementation Notes

Implementations that use KMIP to store passwords or secrets for non-cryptographic purposes should be aware that the server will treat these objects as cryptographic objects for policy purposes (lifecycle management, access control, audit). This is generally desirable for security, but clients should ensure that the attributes set on registration accurately reflect intended usage to avoid unexpected lifecycle transitions.

## Related Concepts

See [Secret Data](../objects/secret-data.md) for the object definition.
