---
title: PKCS#11 Return Code Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "11.39"
status: reviewed
related: ["pkcs-11-return-code", "pkcs-11-function-enumeration", "pkcs-11-interface"]
keywords: ["pkcs11", "CKR", "return code", "Cryptoki error", "PKCS11 error code", "42015D", "PKCS_11ReturnCode"]
tag_hex: "42015D"
xml_text: "PKCS_11ReturnCode"
tag_type: "Enumeration"
---

# PKCS#11 Return Code Enumeration

## Overview

The PKCS#11 Return Code enumeration carries the `CKR_*` status code returned by a Cryptoki function call tunneled through the KMIP [PKCS#11 operation](../operations/pkcs-11.md). The KMIP operation itself may succeed (the tunneling completed without error) while the underlying PKCS#11 call returns a non-zero CKR code indicating a Cryptoki-level failure. Clients must inspect both the KMIP result status and the PKCS#11 Return Code to fully evaluate the outcome.

## Encoding (Tag / Type / Length / Value)

Encoded as a Long Integer (TTLV type `03`) carrying the raw CKR_* numeric value from the PKCS#11 standard.

## Fields & Structure

Key CKR values that appear in practice:

- **CKR_OK** (0): Success. The Cryptoki function completed without error.
- **CKR_GENERAL_ERROR**: Catch-all for unspecified failures within the token or PKCS#11 implementation.
- **CKR_FUNCTION_FAILED**: The specific function failed for a reason the token could not categorise more precisely.
- **CKR_ATTRIBUTE_VALUE_INVALID / CKR_ATTRIBUTE_TYPE_INVALID / CKR_ATTRIBUTE_READ_ONLY**: Attribute errors during object creation or modification.
- **CKR_KEY_HANDLE_INVALID / CKR_KEY_SIZE_RANGE / CKR_KEY_TYPE_INCONSISTENT**: Key-related errors during wrap, unwrap, or derive.
- **CKR_MECHANISM_INVALID / CKR_MECHANISM_PARAM_INVALID**: The requested mechanism is not supported or its parameters are malformed.
- **CKR_TOKEN_NOT_PRESENT / CKR_TOKEN_NOT_RECOGNIZED**: Physical token errors.
- **CKR_USER_NOT_LOGGED_IN / CKR_PIN_INCORRECT / CKR_PIN_LOCKED**: Authentication errors at the PKCS#11 layer.
- **CKR_DATA_INVALID / CKR_ENCRYPTED_DATA_INVALID / CKR_SIGNATURE_INVALID / CKR_SIGNATURE_LEN_RANGE**: Data integrity errors during crypto operations.
- **CKR_BUFFER_TOO_SMALL**: The output buffer specified was insufficient; the caller should retry with a larger buffer.
- **CKR_OPERATION_ACTIVE / CKR_OPERATION_NOT_INITIALIZED**: Session state errors.

## Examples

A tunneled C_Sign that fails because the session has not been logged in returns KMIP Success with PKCS#11 Return Code = **CKR_USER_NOT_LOGGED_IN**. The client detects this from the Return Code and performs a C_Login before retrying.

## Related

[PKCS#11 Return Code structure](../structures/pkcs-11-return-code.md) · [PKCS#11 Function Enumeration](pkcs-11-function-enumeration.md) · [PKCS#11 operation](../operations/pkcs-11.md)
