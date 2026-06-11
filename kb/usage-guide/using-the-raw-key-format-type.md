---
title: Using the "Raw" Key Format Type
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.26"
status: reviewed
related: ["key-format-type", "key-block"]
keywords: ["Raw key format", "byte string", "symmetric key", "opaque format", "proxy environment"]
---

# Using the "Raw" Key Format Type

## Overview

The "Raw" Key Format Type is intended for keys that contain nothing but raw cryptographic key material, encoded as a plain byte string with no surrounding structure. It is the closest KMIP equivalent to an opaque key, and is intended for use with symmetric keys.

## Guidance

Raw format is appropriate when the client consumer is not KMIP-aware and simply needs the key bytes without any KMIP-specific encoding overhead. This is common in proxy deployments where a KMIP-enabled proxy retrieves a key on behalf of an appliance or legacy system that expects raw key bytes.

Raw format should not be applied to asymmetric keys, where the standard structured formats (PKCS#8, X.509 SubjectPublicKeyInfo, etc.) are the correct choices.

## Implementation Notes

Choosing Raw format means the client receives only the key bytes, with no algorithm or length metadata embedded in the key material. The client is therefore responsible for knowing the algorithm and length from context (e.g., from the attributes returned separately via Get Attributes). Both Raw and Opaque Key Format Types present the key without embedded metadata, but they carry different semantics: Opaque signals a server-unknown encoding, while Raw means the client and server agree that the value is simply the key bytes with no wrapper.

## Related Concepts

See [Key Format Type](key-format-type.md) and [Key Encoding](key-encoding.md).
