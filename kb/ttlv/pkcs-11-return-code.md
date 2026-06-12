---
title: PKCS#11 Return Code
category: ttlv
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "7.30"
status: reviewed
related: ["pkcs-11-function", "pkcs-11-output-parameters", "pkcs-11", "error-handling"]
keywords: ["PKCS#11 return code", "CKR", "Cryptoki return value", "CKR_OK", "error code", "PKCS11 status"]
---

# PKCS#11 Return Code

## Overview

PKCS#11 Return Code carries the `CKR_*` return value from a PKCS#11 Cryptoki function call that was tunneled through the KMIP [PKCS#11](../operations/pkcs-11.md) operation. The Cryptoki standard defines an extensive set of `CKR_*` status codes — `CKR_OK` (zero) for success and non-zero values for various error conditions. The PKCS#11 Return Code structure surfaces this value in the KMIP response so the client can determine whether the Cryptoki function succeeded independently of the KMIP-level result status.

A KMIP response may carry a Result Status of Success even when the PKCS#11 Return Code is non-zero: the KMIP transport worked correctly, but the Cryptoki function itself failed.

## Encoding (Tag / Type / Length / Value)

PKCS#11 Return Code encodes as a Structure containing a single Long Integer.

| Field | Tag | Type | Required |
|---|---|---|---|
| PKCS#11 Return Code Value | `420298` | Long Integer | Yes |

The Long Integer value corresponds numerically to the Cryptoki `CKR_*` constant. Clients map this value back to the appropriate named constant from the PKCS#11 specification or their Cryptoki header.

## Fields & Structure

The single **PKCS#11 Return Code Value** Long Integer holds the raw Cryptoki return code. Common values include:

- `0x00000000` (CKR_OK) — the function completed successfully.
- `0x00000020` (CKR_ARGUMENTS_BAD) — incorrect arguments were supplied.
- `0x00000030` (CKR_BUFFER_TOO_SMALL) — an output buffer was insufficient.
- `0x000000B0` (CKR_KEY_HANDLE_INVALID) — the key handle was not valid.
- `0x000001B0` (CKR_MECHANISM_INVALID) — the mechanism is not supported.

The full list of `CKR_*` values is defined in the PKCS#11 specification; clients should handle both known and unknown non-zero values gracefully.

When the PKCS#11 Return Code is non-zero, the [PKCS#11 Output Parameters](pkcs-11-output-parameters.md) may be absent or may carry partial data depending on the function and the point of failure.

## Examples

A client requests a C_Decrypt operation on data that was encrypted with a different key. The server executes the Cryptoki call, which returns CKR_ENCRYPTED_DATA_INVALID. The KMIP response carries Result Status = Success (the KMIP operation itself completed without error) but PKCS#11 Return Code Value = `0x00000040` (CKR_ENCRYPTED_DATA_INVALID). The client parses the return code and reports the decryption failure to the caller.

## Related

[PKCS#11 Function](pkcs-11-function.md) · [PKCS#11 Output Parameters](pkcs-11-output-parameters.md) · [PKCS#11 Operation](../operations/pkcs-11.md) · [Error Handling](../concepts/error-handling.md)
