---
title: Key Block
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.12"
status: reviewed
related: ["key-block", "key-value"]
keywords: ["Key Block", "Key Value", "Key Wrapping Data", "Key Value Type", "attributes in Key Value", "wrapping"]
tag_hex: "420040"
xml_element: "KeyBlock"
---

# Key Block

## Overview

The Key Block is the KMIP structure used to deliver a key from server to client (or from client to server during registration). It consists of three logical components: the Key Value Type (specifying how the key material is encoded), the Key Value (the key material itself plus optional bound attributes), and the Key Wrapping Data (present only when the client requests wrapping or registers a wrapped key).

## Guidance

Any attribute may optionally be included inside the Key Value and cryptographically bound to the key material via signing, MACing, encryption, or a combination. Including attributes inside the Key Value provides integrity protection: a recipient can verify that the attributes were not tampered with independently of the key material. Commonly bound attributes include Unique Identifier, Cryptographic Algorithm, Cryptographic Length, Cryptographic Usage Mask, and date attributes.

The Key Wrapping Data is only present when wrapping was requested (via Key Wrapping Specification in a Get) or when the client registers an already-wrapped key (via Key Wrapping Data in the Register request).

## Implementation Notes

Clients that do not request wrapping receive the key in plaintext within the Key Value. Clients requiring wrapped delivery must specify a Key Wrapping Specification in the Get request payload, referencing the wrapping key and parameters. The transport always protects the Key Block via TLS; wrapping provides an additional application-level layer, which is particularly valuable in proxy environments where the transport may be terminated by an intermediary.

## Related Concepts

See [Key Block](../ttlv/key-block.md) for the TTLV encoding details and [Using Wrapped Keys with KMIP](using-wrapped-keys-with-kmip.md) for wrapping examples.
