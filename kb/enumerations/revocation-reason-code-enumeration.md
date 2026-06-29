---
title: Revocation Reason Code Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.48"
status: reviewed
related: ["revocation-reason", "revoke", "state-enumeration"]
keywords: ["revocation reason", "key compromise", "CA compromise", "superseded", "cessation", "privilege withdrawn", "revoke", "420082", "RevocationReasonCode"]
tag_hex: "420082"
xml_text: "RevocationReasonCode"
tag_type: "Enumeration"
---

# Revocation Reason Code Enumeration

## Overview

The Revocation Reason Code enumeration classifies why a managed object is being revoked. It appears in the Revocation Reason structure sent with a [Revoke](../operations/revoke.md) operation and is stored in the [Revocation Reason attribute](../attributes/revocation-reason.md) after the fact. The values align closely with X.509 certificate revocation reason codes, enabling consistent audit trails across PKI and non-PKI key management.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Unspecified | `00000001` | `Unspecified` | The reason is not categorised. Used when a more specific code is not applicable or not known. |
| Key Compromise | `00000002` | `KeyCompromise` | The private key or secret has been disclosed to an unauthorised party, or there is a credible risk that it has been. The most critical revocation reason; objects are typically moved to the Compromised state. |
| CA Compromise | `00000003` | `CACompromise` | The issuing Certificate Authority has been compromised. Triggers bulk revocation of all certificates issued by the compromised CA. |
| Affiliation Changed | `00000004` | `AffiliationChanged` | The subject's organisational affiliation has changed — for example, an employee has left the organisation. Applies primarily to certificates. |
| Superseded | `00000005` | `Superseded` | The object has been replaced by a newer version (rotation, re-key, re-certify). The predecessor is deactivated or revoked in favour of the successor. |
| Cessation of Operation | `00000006` | `CessationOfOperation` | The entity for which the key was created no longer needs or uses it — operations have ceased. The key was not compromised. |
| Privilege Withdrawn | `00000007` | `PrivilegeWithdrawn` | The permissions or privileges associated with the key or certificate have been explicitly revoked, even if the key material itself is uncompromised. |

## Examples

When a service account is terminated, the associated signing key is revoked with **Privilege Withdrawn**. When a laptop private key is exposed by ransomware, the corresponding certificate is revoked with **Key Compromise**.

## Related

[Revocation Reason attribute](../attributes/revocation-reason.md) · [Revoke](../operations/revoke.md) · [State Enumeration](state-enumeration.md)
