---
title: Asymmetric Concepts with Symmetric Keys
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.10"
status: draft
related: ["cryptographic-usage-mask"]
keywords: ["Cryptographic Usage Mask", "MAC", "asymmetric concepts", "usage separation", "MAC Generate", "MAC Verify", "Translate"]
---

# Asymmetric Concepts with Symmetric Keys

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

Some symmetric key uses require separating the roles of two parties even though both use the same cryptographic primitive. For example, MAC generation and MAC verification both use the "encrypt" operation internally, but policy should prevent the verifying party from generating new MACs. KMIP addresses this with paired Cryptographic Usage Mask values that distinguish functionally complementary but policy-separate roles.

## Guidance

The Cryptographic Usage Mask provides paired permissions for MAC (MAC Generate / MAC Verify), financial cryptogram operations (Generate Cryptogram / Validate Cryptogram), and key translation (Translate Encrypt / Translate Decrypt, Translate Wrap / Translate Unwrap). Each key should be assigned only the permissions appropriate to its role.

Using `MAC Generate` and `MAC Verify` as an example: a server-side key gets MAC Verify; a client-side key gets MAC Generate. Even though both use the same underlying operation, the usage mask enforces the policy separation that the security model requires.

## Implementation Notes

The Translate Encrypt/Decrypt masks address a specific need in financial networks where data encrypted under one key must be re-encrypted under a different key without exposing the plaintext. The atomic translate operation prevents the plaintext from ever being accessible during the re-encryption, which Translate Wrap/Unwrap extends to key material.

## Related Concepts

See the Cryptographic Usage Mask attribute documentation in [kb/attributes/](../attributes/).
