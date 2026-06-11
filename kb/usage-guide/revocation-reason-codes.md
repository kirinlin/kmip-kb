---
title: Revocation Reason Codes
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.30"
status: draft
related: ["compromised-objects", "authorization-for-revoke-recover-destroy-and-archive-operations"]
keywords: ["Revocation Reason", "Key Compromise", "CA Compromise", "unspecified", "affiliation changed", "X.509", "RFC 5280"]
---

# Revocation Reason Codes

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

The Revocation Reason attribute used in the Revoke operation is aligned with the CRL Reason Codes defined in X.509 and RFC 5280, with three exclusions. The excluded values are those specific to certificate suspension, attribute certificates, or operational patterns not applicable to KMIP's scope.

## Guidance

The alignment with X.509 reason codes means that KMIP revocation semantics are compatible with established PKI practices. The excluded codes are:

- **certificateHold / removeFromCRL**: Certificate suspension is out of scope for KMIP.
- **aaCompromise**: Specific to attribute authority certificates — a certificate type KMIP does not manage.

The **privilegeWithdrawn** code is included despite being applicable to attribute certificates, as it is also applicable to public key certificates. In KMIP context, it applies only to public key certificates.

## Implementation Notes

When reporting a Key Compromise, the client should supply a Compromise Occurrence Date if known. If the exact compromise time cannot be determined, the Initial Date is the appropriate conservative fallback. The precision of the Compromise Occurrence Date affects the scope of data that may need to be re-encrypted.

## Related Concepts

See [Compromised Objects](compromised-objects.md) for the full revocation workflow.
