---
title: Key Shredding
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.3", "1.4", "2.0", "2.1"]
source_section: "ug-4.9"
status: reviewed
related: ["cryptographic-shredding-erasure"]
keywords: ["key shredding", "data sanitisation", "overwrite", "forensics", "Shredding Algorithm", "Query Capabilities", "NIST SP 800-88"]
---

# Key Shredding

## Overview

Key shredding goes beyond standard key destruction (making a key inaccessible to the application) by destroying the key in a manner that prevents forensic recovery from storage media. Typical shredding methods involve overwriting key material with random data following a recognised data sanitisation standard such as NIST SP 800-88 or DoD 5220.22-M.

## Guidance

KMIP does not impose requirements on which shredding method a client or server uses. However, using the Query operation with the Query Capabilities function allows clients to retrieve a Capability Information object that includes the Shredding Algorithm, allowing clients to discover what destruction methods the server supports before selecting one.

## Implementation Notes

In HSM-based deployments, the hardware security module's own key destruction mechanism provides the strongest shredding guarantee. For software key stores, the effectiveness of overwrite-based shredding depends on the storage medium: SSDs and some flash storage may not guarantee overwrite due to wear-levelling, making physical destruction the only reliable shredding method for the highest assurance requirements.

## Related Concepts

See [Cryptographic Shredding (Erasure)](cryptographic-shredding-erasure.md) for the higher-level shredding workflow.
