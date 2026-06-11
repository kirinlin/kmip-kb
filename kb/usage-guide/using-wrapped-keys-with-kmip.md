---
title: Using Wrapped Keys with KMIP
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-4.2"
status: draft
related: ["key-block", "extractable-and-sensitive-attributes"]
keywords: ["wrapped key", "Key Wrapping Specification", "Key Wrapping Data", "Register wrapped key", "Get wrapped key", "Encoding Option", "Key Wrap Type"]
---

# Using Wrapped Keys with KMIP

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

KMIP allows key material to be wrapped (encrypted) both when registering a key on the server and when retrieving one. Wrapping provides an application-level layer of protection for key material, particularly valuable in proxy environments where the transport terminates at an untrusted intermediary.

## Guidance

**Getting a wrapped key**: Add a Key Wrapping Specification to the Get request, identifying the wrapping key by Unique Identifier and supplying the relevant Cryptographic Parameters. The server wraps the Key Value (key material plus optionally bound attributes) using the wrapping key and returns the wrapped bytes in the Key Block, along with Key Wrapping Data identifying the mechanism.

**Registering a wrapped key**: Include the wrapped key in the Key Block of the Register Request Payload along with the Key Wrapping Data identifying the wrapping key. The server unwraps the key before storing it if the wrapping key is known to it, or stores the wrapped bytes as an opaque object if it cannot unwrap.

**Wrapping methods**: Encrypt (the entire Key Value is encrypted), MAC/sign (the Key Value is returned in plaintext but with a MAC or signature), and combinations. When wrapping method is MAC/sign, the Key Value is plaintext in the response — clients that assume wrapped means encrypted will be surprised.

**Key Wrap Type**: In a Get request, Wrap Type=Not Wrapped returns the key unwrapped regardless of how it was registered; As Registered returns it in the same form as it was registered.

**Encoding Option**: Allows clients to request that only the raw key bytes (not the TTLV-encoded Key Value) be wrapped. This is useful for non-KMIP-aware end clients in proxy environments, but removes attribute-binding security.

## Implementation Notes

Before wrapping, the server verifies that the wrapping key has the appropriate Cryptographic Usage Mask bits set (Wrap Key for encryption-based wrapping, MAC Generate/Sign for MAC/sign wrapping). If not, the operation fails. Clients should check the Cryptographic Usage Mask of proposed wrapping keys before attempting wrapped retrieval to avoid avoidable round trips.

The Encoding Option should be used only in controlled environments (direct client-server TLS, trusted proxies, or when the key material itself carries embedded metadata). Removing TTLV encoding removes the attribute-binding protection that prevents replay attacks and attribute substitution.

## Related Concepts

See [Key Block](key-block.md) and [Extractable and Sensitive Attributes](extractable-and-sensitive-attributes.md).
