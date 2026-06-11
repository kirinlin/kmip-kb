---
title: Using KMIP for PGP Keys
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-4.5"
status: reviewed
related: ["pgp-key", "application-specific-information"]
keywords: ["PGP", "OpenPGP", "RFC 4880", "PGP Key object", "Alternative Name", "Link attribute", "web of trust"]
---

# Using KMIP for PGP Keys

## Overview

KMIP supports the PGP Key managed object type as an opaque blob containing a PGP key as defined in RFC 4880. This allows PGP keys to move between PGP environments and KMIP-managed environments. KMIP servers do not need to understand the internal structure of PGP keys to store and retrieve them.

## Guidance

PGP-enabled clients are expected to extract key identifiers (User IDs) from the PGP Key blob and populate them as Alternative Name attributes on the KMIP object. This enables KMIP Locate queries to find PGP keys by name even though the server cannot parse the key blob.

PGP key rings contain multiple sub-keys with different roles (signing, encryption, binding). The Link attribute supports parent/child, previous/next relationships that model these structural dependencies:

- Private and public key sub-pairs → child links from the PGP Key object.
- Additional Decryption Keys (ADKs) → child links, connected to each other via previous/next links.

KMIP servers are not expected to create PGP keys; PGP-enabled clients perform key creation and register the resulting objects.

## Implementation Notes

KMIP does not represent all PGP policy information (supported algorithms, trust levels, expiry embedded in the key packet) within standard KMIP attributes. Policy information can be stored as opaque data inside the PGP Key value or coordinated out-of-band. This limits the extent to which a KMIP server can enforce PGP-specific policies, but provides sufficient capability for key storage, retrieval, and portability between PGP environments.

## Related Concepts

See [PGP Key](../objects/pgp-key.md) and [Application Specific Information](application-specific-information.md).
