---
title: PKCS#12 Key Format
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.27"
status: draft
related: ["private-key", "certificate"]
keywords: ["PKCS#12", "keystore", "private key", "certificate chain", "Friendly Name", "password protection", "PBE"]
---

# PKCS#12 Key Format

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

KMIP supports PKCS#12 as a Key Format Type to allow a private key and its associated certificate chain to be registered in, or retrieved from, a KMIP server as a single PKCS#12 blob. This addresses the common scenario of importing PKI material from or exporting it to environments that use PKCS#12 as their native keystore format.

## Guidance

When registering a PKCS#12 blob, the client links a SecretData object containing the PBE password to the private key via a Link attribute with LinkType of PKCS#12 Password Link. The server decrypts and verifies the blob, registers the private key, registers the certificate chain, and creates the appropriate PKCS#12 Certificate Links. The Unique Identifier returned by the server is that of the private key.

For multi-key PKCS#12 blobs, the client specifies which key to register using the PKCS#12 Friendly Name attribute. Registering multiple keys from the same blob requires issuing multiple Register requests, each specifying a different Friendly Name.

When retrieving a PKCS#12 blob (Get with Key Format Type PKCS#12), the server traverses the link structure to reassemble the private key with its certificate chain and re-wraps it using the SecretData on the password link.

## Implementation Notes

KMIP's PKCS#12 support targets the basic forms of the standard. Not all PKCS#12 features are represented in the KMIP model; complex PKCS#12 structures with multiple key bags, vendor-specific PBE algorithms, or non-standard attributes may not survive a round-trip through a KMIP server without loss of information.

## Related Concepts

See [Private Key](../objects/private-key.md) and [Certificate](../objects/certificate.md) for the underlying object types.
