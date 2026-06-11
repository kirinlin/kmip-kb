---
title: Interoperable Key Naming for Tape
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-4.3"
status: reviewed
related: ["application-specific-information"]
keywords: ["tape", "LTO", "KAD", "Key Associated Data", "ASI", "Application Specific Information", "LIBRARY-LTO", "key identifier"]
---

# Interoperable Key Naming for Tape

## Overview

This section defines interoperable methods for creating, storing, and retrieving key identifiers used by KMIP-compliant tape libraries, ensuring that a tape cartridge encrypted by one library can be decrypted by a different library sharing the same KMIP key manager.

## Guidance

Tape library interoperability relies on the KMIP Tape Library Profile in combination with the Application Specific Information (ASI) attribute. Key identifiers are KMIP strings composed of hexadecimal character pairs. These strings are stored in ASI Application Data under a standardised namespace (LIBRARY-LTO is preferred). The numeric encoding of the identifier travels with the tape cartridge in its Key Associated Data (KAD) field, enabling future retrieval.

Two algorithms establish the bijective mapping between the ASI string (KMIP side) and the KAD bytes (tape side):

- **Algorithm 1** (ASI → KAD, used when writing): Takes the hex-character string, converts character pairs to byte values, and fills authenticated and unauthenticated KAD fields in right-to-left order (authenticated KAD is filled first from the rightmost characters).
- **Algorithm 2** (KAD → ASI, used when reading): Reads the unauthenticated KAD bytes first, then the authenticated bytes, and converts each byte to two hex characters to reconstruct the KMIP key identifier string.

## Implementation Notes

LTO4 supports 44 bytes of combined KAD (12 bytes authenticated, 32 unauthenticated), sufficient for an 88-character hex key identifier. LTO5 and later support 92 bytes of KAD (60 bytes authenticated, 32 unauthenticated), sufficient for a 184-character hex identifier. Implementations must handle both sizes.

The interoperability guarantee depends on: (a) both parties using the same KAD byte-ordering algorithm, and (b) both parties using the same Application Namespace (LIBRARY-LTO4 / LIBRARY-LTO5 etc.) for the ASI lookup. Deviating from either breaks cross-library key retrieval.

## Related Concepts

See [Application Specific Information](application-specific-information.md) for the ASI attribute model.
