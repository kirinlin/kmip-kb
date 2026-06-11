---
title: Certificate Renewal, Update, and Re-key
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.41"
status: reviewed
related: ["certify-and-re-certify", "private-key"]
keywords: ["certificate renewal", "certificate update", "certificate re-key", "Re-certify", "Certify", "RFC 3647", "RFC 4949"]
---

# Certificate Renewal, Update, and Re-key

## Overview

KMIP aligns its certificate lifecycle terminology with IETF RFC 3647 and RFC 4949 to provide precise vocabulary for the three ways a certificate can be replaced:

- **Certificate Renewal**: A new certificate is issued with the same key pair and same information, updated serial number and validity dates only.
- **Certificate Update**: A new certificate is issued due to changes in the subject information other than the key pair.
- **Certificate Re-key**: A new key pair is generated and a new certificate is issued certifying the new public key.

## Guidance

KMIP supports Certificate Renewal via the Re-certify operation. Certificate Update is supported by submitting a new certificate request via the Certify operation with updated subject information. Certificate Re-key requires two operations in sequence: Re-key Key Pair to generate the replacement key pair, followed by Certify to issue a new certificate for the new public key.

## Implementation Notes

The terminology distinctions matter for compliance reporting: many PKI policies distinguish between renewal, update, and re-key in terms of the approval workflow, key ceremony requirements, and audit trail. Implementing the correct KMIP operation sequence for each scenario ensures that the resulting certificate objects reflect the correct type of change.

## Related Concepts

See [Certify and Re-certify](certify-and-re-certify.md) and [Using Offset in Re-key and Re-certify Operations](using-offset-in-re-key-and-re-certify-operations.md).
