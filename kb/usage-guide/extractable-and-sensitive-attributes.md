---
title: Extractable and Sensitive Attributes
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.24"
status: draft
related: ["attributes", "use-of-meta-data-only-mdo-keys"]
keywords: ["Extractable", "Sensitive", "Always Sensitive", "Never Extractable", "PKCS#11", "key export control"]
---

# Extractable and Sensitive Attributes

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

KMIP provides four attributes — Sensitive, Always Sensitive, Extractable, and Never Extractable — that control and track whether a cryptographic object may be exported from the server and whether it must be wrapped when exported. These attributes are modelled on similar attributes in PKCS#11.

## Guidance

- **Sensitive**: If true, the object can only leave the server in wrapped (encrypted) form via a Get operation. A key with Sensitive=true that is requested without a wrapping specification will be refused.
- **Always Sensitive**: Tracks whether the object has ever had Sensitive=true during its lifetime. Once set to true, Always Sensitive cannot be set back to false, preserving the audit history.
- **Extractable**: If false, the object is never allowed to leave the server at all, regardless of wrapping.
- **Never Extractable**: Tracks whether extraction has ever been restricted. Analogous to Always Sensitive.

## Implementation Notes

These attributes are particularly important for keys that must remain hardware-bound (Extractable=false) or that should only be used in wrapped form (Sensitive=true). Implementers using KMIP as a complement to an HSM environment should set these attributes during registration to enforce the desired containment policy.

## Related Concepts

See [Use of Meta-Data Only (MDO) Keys](use-of-meta-data-only-mdo-keys.md) for the extreme case of a key that never leaves the client.
