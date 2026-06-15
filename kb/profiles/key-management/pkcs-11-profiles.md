---
title: PKCS#11 Profiles
category: profile
spec_version: "2.1"
spec_versions: ["2.0", "2.1"]
source_section: "prof-5.18"
status: reviewed
related: ["base-profiles", "cryptographic-profiles"]
keywords: ["PKCS#11", "CKA", "CKM", "token", "slot", "HSM bridge", "cryptoki", "KMIP operation"]
---

# PKCS#11 Profiles

## Overview

The PKCS#11 Profiles define how KMIP wraps PKCS#11 API calls as a KMIP operation, allowing an application that uses the standard PKCS#11 (Cryptoki) interface to communicate with a remote KMIP server as if it were a local HSM or software token. This bridges the large installed base of PKCS#11-aware applications to KMIP-managed key material.

## Encoding

PKCS#11 function calls are transported as a KMIP PKCS#11 operation containing a direct binary serialization of the PKCS#11 parameters:
- CK_BYTE is a single byte; CK_ULONG and CK_LONG are 8-byte big-endian values.
- Pointer-to-structure parameters are inlined; variable-length arrays are preceded by a 4-byte big-endian element count.
- Templates (CK_ATTRIBUTE arrays) are preceded by a 4-byte count; each attribute carries a one-byte value-indicator flag and a one-byte count-indicator flag before the value bytes.
- Mechanism type is encoded as an 8-byte big-endian number followed by a one-byte flag indicating whether a parameter field follows.

A subset of PKCS#11 functions is not encapsulated because they involve pointer semantics or API-level infrastructure (`C_Initialize` does not pass `pInitArgs`, `C_GetFunctionList` is not used, `C_GetInterface` is not used, `C_WaitForSlotEvent` is not used). `C_Initialize` sends a single byte encoding the version (currently 1).

## Client

A PKCS#11 Client extends the [Baseline Client](../base-encoding/base-profiles.md) and conforms to the PKCS#11 Encoding specification.

## Server

A PKCS#11 Server extends the [Baseline Server](../base-encoding/base-profiles.md) and conforms to the PKCS#11 Encoding specification.

## Mandatory Test Cases

`PKCS11-M-1-21` validates the PKCS#11 encoding round-trip for a basic operation sequence.

## Implications for Implementers

- This profile enables drop-in KMIP support for applications that already use a PKCS#11 library. The KMIP client acts as a PKCS#11 "stub" that translates Cryptoki calls to KMIP PKCS#11 operations.
- The encoding version byte in `C_Initialize` must be set to 1 for conformant implementations. Future versions may increment this.
- Applications that depend on PKCS#11 multi-threading callbacks (`pInitArgs` in `C_Initialize`) will not be able to use those callbacks via KMIP — the profile intentionally omits them.
- CK_ULONG is 8 bytes in this encoding regardless of the native platform width (some PKCS#11 implementations treat it as 4 bytes on 32-bit platforms). Ensure the serialization layer normalizes to 8 bytes.

## Related Concepts

[Base Profiles](../base-encoding/base-profiles.md) ·
[Cryptographic Profiles](cryptographic-profiles.md)
