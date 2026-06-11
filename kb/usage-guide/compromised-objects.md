---
title: Compromised Objects
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.4"
status: reviewed
related: ["revocation-reason-codes", "authorization-for-revoke-recover-destroy-and-archive-operations"]
keywords: ["compromise", "revoke", "key compromise", "CA compromise", "linked objects", "state", "Revocation Reason"]
---

# Compromised Objects

## Overview

When a cryptographic object is believed to have been compromised, the client submits a Revoke request carrying the Key Compromise (or CA Compromise) reason code. A Compromise Occurrence Date should accompany the request; if the exact time is unknown, it should use the Initial Date as a conservative estimate.

## Guidance

KMIP does not require servers to automatically propagate compromise status to linked objects. When a private key is revoked as compromised, the paired public key and any associated certificates remain independently Active unless explicitly revoked. The reverse also holds: revoking a public key does not automatically change the state of its private counterpart. Clients are responsible for checking the state of related objects and revoking them as appropriate, either by inspecting Link attributes or by independently revoking each object that may be affected.

## Implementation Notes

The absence of automatic compromise propagation is a deliberate protocol choice that avoids unexpected side effects from server-side automation. Deployments with strict security requirements should implement client-side workflows that systematically revoke all linked objects when a compromise is detected. The Compromise Occurrence Date is important for audit purposes and for determining the scope of data re-encryption requirements.

## Related Concepts

See [Revocation Reason Codes](revocation-reason-codes.md) for the full list of Revocation Reason values and their semantics.
