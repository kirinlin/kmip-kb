---
title: Constraints
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.22"
status: draft
related: ["default-crypto-parameters", "server-policy"]
keywords: ["constraints", "SetConstraints", "GetConstraints", "algorithm constraints", "key length", "Object Group"]
tag_hex: "420168"
xml_element: "Constraints"
---

# Constraints

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

A KMIP server may be configured to accept only certain cryptographic parameter combinations. Constraints restrict which algorithms, key lengths, or other parameters are permitted, and can be scoped to specific Object Types or Object Groups. Clients can inspect active constraints via GetConstraints and privileged clients can modify them via SetConstraints.

## Guidance

Constraints are expressed as a Constraints object that specifies ObjectTypes, ObjectGroups, and Attributes that the server will enforce. For example, a server might be constrained to accept only ECDSA public keys with a Cryptographic Length of 521. Any Create or Register request that violates a constraint will be rejected.

This mechanism is useful for enforcing organisational cryptographic policy through the key management system rather than relying on client compliance.

## Implementation Notes

Constraints and Defaults work together: Defaults supply values when parameters are omitted, while Constraints validate that whatever values are present (whether client-specified or defaulted) are within the permitted range. A well-configured deployment uses both: Defaults to simplify client requests, Constraints to ensure policy is enforced regardless of what any client sends.

## Related Concepts

See [Default Crypto Parameters](default-crypto-parameters.md) and [Server Policy](server-policy.md).
