---
title: Elliptic Curve Cryptography (ECC) Recommended Curve Mapping
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.14"
status: reviewed
related: ["private-key", "public-key"]
keywords: ["ECC", "elliptic curve", "OID", "curve mapping", "NIST curves", "Brainpool", "SECP", "SECT", "Curve25519"]
---

# Elliptic Curve Cryptography (ECC) Recommended Curve Mapping

## Overview

KMIP defines recommended ECC curves drawn from multiple standards bodies (NIST FIPS 186-4, ANSI X9.62, SEC2, ECC-Brainpool, RFC 5639, RFC 7748). Because the same mathematical curve is sometimes known by different names in different standards, KMIP provides a canonical mapping table that associates each supported curve with its KMIP enumeration value, its Object Identifier (OID), and all known synonyms.

## Guidance

When encoding or decoding a curve identifier in a KMIP message, implementations should use the KMIP enumeration value as the canonical form. The OID provides a globally unique identifier that can be used for cross-system interoperability. Where multiple synonym names appear in the table, any synonym should map to the same KMIP enumeration.

Notable entries include P-256 (SECP256R1 / ANSIX9P256V1, OID 1.2.840.10045.3.1.7), Curve25519 (also known as X25519, OID 1.3.101.110), and the full Brainpool family.

## Implementation Notes

Implementations that need to interoperate with systems using OID-based curve identification (such as X.509 certificates) should maintain a bidirectional mapping between OIDs and KMIP enumeration values. The KMIP mapping table covers all curves defined in the supported standards; curves from other standards are not included and would require vendor extension treatment.

## Related Concepts

See [Private Key](../../objects/private-key.md) and [Public Key](../../objects/public-key.md) for how curve selection is represented in the managed objects.
