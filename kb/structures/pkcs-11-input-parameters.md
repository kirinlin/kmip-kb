---
title: PKCS#11 Input Parameters
category: structures
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "7.27"
status: reviewed
related: ["pkcs-11-function", "pkcs-11-interface", "pkcs-11-output-parameters", "pkcs-11-return-code", "pkcs-11"]
keywords: ["PKCS#11 input", "Cryptoki parameters", "CK_MECHANISM", "function arguments", "PKCS11 tunnel input", "42015B", "PKCS_11InputParameters"]
tag_hex: "42015B"
xml_text: "PKCS_11InputParameters"
---

# PKCS#11 Input Parameters

## Overview

PKCS#11 Input Parameters carries the serialized input arguments for the PKCS#11 function call being tunneled over the KMIP [PKCS#11](../operations/pkcs-11.md) operation. Because PKCS#11 Cryptoki functions accept C-language structs and byte buffers, KMIP encodes them as an opaque byte string, leaving interpretation to the server-side Cryptoki adapter.

This structure is the "in" side of the function call — providing the mechanism parameters, data buffers, and any other inputs the function requires. The "out" side is [PKCS#11 Output Parameters](pkcs-11-output-parameters.md).

## Encoding (Tag / Type / Length / Value)

PKCS#11 Input Parameters encodes as a Structure.

| Field | Tag | XML Element | Type | Required |
|---|---|---|---|---|
| PKCS#11 Parameters | `420296` |  | Byte String | No |
| Data | `4200C2` | `Data` | Byte String | No |

Both fields are optional in general; specific function calls define which are required. Multiple Data or parameter fields may appear for functions that accept multiple inputs.

## Fields & Structure

**PKCS#11 Parameters** is an opaque byte string carrying the serialized mechanism or parameter struct for the function being called — for example, a serialized `CK_MECHANISM` for encryption functions, or a `CK_RSA_PKCS_PSS_PARAMS` for PSS-mode signing. The serialization format follows the conventions established in the KMIP PKCS#11 tunneling profile.

**Data** carries the primary data buffer — the plaintext for C_Encrypt, the message digest for C_Sign, or the ciphertext for C_Decrypt, depending on the function. For functions that require separate update calls (C_EncryptUpdate, C_DecryptUpdate), successive PKCS#11 operations each carry their respective data chunk.

The client constructs these byte strings according to the PKCS#11 function's calling convention and the KMIP encoding rules for PKCS#11 tunneling. The server unpacks them, constructs the actual Cryptoki call, and returns results via [PKCS#11 Output Parameters](pkcs-11-output-parameters.md).

## Examples

For a C_Encrypt call using AES-CBC, the PKCS#11 Input Parameters structure contains a Parameters byte string encoding the CK_MECHANISM with mechanism type CKM_AES_CBC and an IV, plus a Data byte string containing the plaintext to encrypt. The server extracts these, calls C_Encrypt on the underlying token, and returns the ciphertext in the output parameters of the response.

## Related

[PKCS#11 Function](pkcs-11-function.md) · [PKCS#11 Interface](pkcs-11-interface.md) · [PKCS#11 Output Parameters](pkcs-11-output-parameters.md) · [PKCS#11 Return Code](pkcs-11-return-code.md) · [PKCS#11 Operation](../operations/pkcs-11.md)
