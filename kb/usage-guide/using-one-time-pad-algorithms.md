---
title: Using One Time Pad Algorithms
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-4.7"
status: draft
related: ["cryptographic-services"]
keywords: ["One Time Pad", "OTP", "Cryptographic Algorithm enumeration", "key material unknown to server"]
---

# Using One Time Pad Algorithms

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

KMIP includes One Time Pad (OTP) as an enumerated Cryptographic Algorithm value. OTP key material can be managed on the server without the server having to understand how it will be applied, and it need not be disclosed to the client if the server itself performs the cryptographic computation.

## Guidance

OTP keys are managed like any other symmetric key in KMIP. The One Time Pad algorithm value in the enumeration allows clients and servers to clearly identify when key material is intended for one-time-pad use. Test cases and examples for OTP usage in combination with KMIP cryptographic service operations are in the KMIP Test Cases document.

## Implementation Notes

The security of OTP depends on keys being used exactly once and being of equal length to the plaintext. KMIP does not enforce these constraints; compliance with OTP security requirements is the client's responsibility. The protocol-level support means OTP key material can be managed (registered, lifecycle-tracked, retrieved) with the same mechanisms as any other key type.

## Related Concepts

See [Cryptographic Services](cryptographic-services.md) for the operations in which OTP keys can be used.
