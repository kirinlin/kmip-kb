---
title: Validity Indicator Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.2","1.3","1.4","2.0","2.1"]
source_section: "11.63"
status: reviewed
related: ["validate", "certificate"]
keywords: ["validity indicator", "valid", "invalid", "unknown", "validate", "certificate validation", "42009B", "ValidityIndicator"]
tag_hex: "42009B"
xml_text: "ValidityIndicator"
---

# Validity Indicator Enumeration

## Overview

The Validity Indicator enumeration conveys the result of a [Validate](../operations/validate.md) operation. After checking a certificate's signature, revocation status, chain trust, and expiry, the server returns one of three verdict values to tell the client whether the presented certificate (or managed object) is currently valid, definitively invalid, or in a state where validity cannot be determined.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Unspecified | `00000001` | `Unspecified` |  |
| NIST CMVP | `00000002` | `NISTCMVP` |  |
| Common Criteria | `00000003` | `CommonCriteria` |  |

- **Valid**: The certificate or object passed all validation checks: the signature verifies, the chain of trust is intact, the certificate has not expired, and it has not been revoked. The client may proceed with confidence.
- **Invalid**: One or more validation checks failed — the certificate is expired, the signature does not verify, it has been revoked, or the issuing CA is untrusted. The client should not rely on this certificate.
- **Unknown**: The server cannot determine validity with certainty — for example, it cannot reach the OCSP responder or CRL distribution point to check revocation, or the certificate has an unsupported extension that the server cannot evaluate. The client must decide whether to accept the unknown verdict based on its own risk tolerance.

## Examples

A TLS termination proxy that validates client certificates via KMIP receives **Valid** for a currently enrolled enterprise client certificate and proceeds. For a certificate where the OCSP check times out, it receives **Unknown** and may apply a configurable "fail open" or "fail closed" policy.

## Related

[Validate](../operations/validate.md) · [Certificate](../objects/certificate.md)
