---
title: PKCS#11 Function
category: ttlv
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "7.26"
status: reviewed
related: ["pkcs-11-interface", "pkcs-11-input-parameters", "pkcs-11-output-parameters", "pkcs-11-return-code", "pkcs-11"]
keywords: ["PKCS#11", "PKCS11 function", "CKF", "cryptoki function", "token function", "tunnel"]
---

# PKCS#11 Function

## Overview

PKCS#11 Function is a structure that identifies which PKCS#11 Cryptoki function is being tunneled over the KMIP [PKCS#11](../operations/pkcs-11.md) operation. KMIP's PKCS#11 operation allows a client to send PKCS#11 function calls to a server-side token without requiring a direct PKCS#11 library connection — the KMIP transport acts as the tunnel and the server translates KMIP PKCS#11 messages into actual Cryptoki calls on the underlying token.

This structure names the function (as an enumeration corresponding to the standard `C_*` functions) so the server knows which token entry point to invoke.

## Encoding (Tag / Type / Length / Value)

PKCS#11 Function encodes as a Structure.

| Field | Tag | XML Element | Type | Required |
|---|---|---|---|---|
| PKCS#11 Function Enumeration | `420292` |  | Enumeration | Yes |

The single required field is the function selector enumeration.

## Fields & Structure

**PKCS#11 Function Enumeration** maps to the standard PKCS#11 function names. The enumeration covers the major cryptographic and session-management functions from the Cryptoki specification, including (but not limited to):

- `C_Encrypt` / `C_EncryptUpdate` / `C_EncryptFinal`
- `C_Decrypt` / `C_DecryptUpdate` / `C_DecryptFinal`
- `C_Sign` / `C_SignUpdate` / `C_SignFinal`
- `C_Verify` / `C_VerifyUpdate` / `C_VerifyFinal`
- `C_DigestUpdate` / `C_DigestFinal`
- `C_GenerateKey` / `C_GenerateKeyPair`
- `C_WrapKey` / `C_UnwrapKey` / `C_DeriveKey`
- `C_GetMechanismList` / `C_GetMechanismInfo`

The actual input and output parameters for the selected function are carried in separate [PKCS#11 Input Parameters](pkcs-11-input-parameters.md) and [PKCS#11 Output Parameters](pkcs-11-output-parameters.md) structures within the same PKCS#11 operation payload.

## Examples

A client that needs to perform an RSA-PKCS1-v1.5 signature tunneled through KMIP sends a PKCS#11 operation whose payload includes a PKCS#11 Function structure with Enumeration = C_Sign, a PKCS#11 Interface structure identifying the target token, and a PKCS#11 Input Parameters structure containing the serialized CK_MECHANISM and data buffer. The server invokes C_Sign on the underlying Cryptoki library and returns the signature in PKCS#11 Output Parameters.

## Related

[PKCS#11 Interface](pkcs-11-interface.md) · [PKCS#11 Input Parameters](pkcs-11-input-parameters.md) · [PKCS#11 Output Parameters](pkcs-11-output-parameters.md) · [PKCS#11 Return Code](pkcs-11-return-code.md) · [PKCS#11 Operation](../operations/pkcs-11.md)
