---
title: PKCS#11 Output Parameters
category: ttlv
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "7.29"
status: reviewed
related: ["pkcs-11-function", "pkcs-11-input-parameters", "pkcs-11-interface", "pkcs-11-return-code", "pkcs-11"]
keywords: ["PKCS#11 output", "Cryptoki output", "function result", "ciphertext output", "signature output", "PKCS11 tunnel output"]
---

# PKCS#11 Output Parameters

## Overview

PKCS#11 Output Parameters carries the output data returned by a PKCS#11 Cryptoki function call tunneled through the KMIP [PKCS#11](../operations/pkcs-11.md) operation. After the server executes the requested function on the underlying token, it serializes any output buffers — ciphertext, signature, decrypted plaintext, derived key material, and so on — into this structure and returns it in the KMIP response.

This structure is the "out" side of the tunneled call; [PKCS#11 Input Parameters](pkcs-11-input-parameters.md) is the "in" side.

## Encoding (Tag / Type / Length / Value)

PKCS#11 Output Parameters encodes as a Structure.

| Field | Tag | XML Element | Type | Required |
|---|---|---|---|---|
| PKCS#11 Parameters | `420296` |  | Byte String | No |
| Data | `4200C2` | `Data` | Byte String | No |

Fields are conditionally present depending on the function called; some functions produce only a return code with no output buffers.

## Fields & Structure

**PKCS#11 Parameters** is an opaque byte string carrying any output parameter structs the Cryptoki function populated — for example, a `CK_MECHANISM` with filled-in output fields or an output length value required by certain multi-step functions.

**Data** carries the primary output buffer: the ciphertext resulting from C_Encrypt, the signature from C_Sign, the plaintext from C_Decrypt, or the digest from C_Digest. For multi-part operations (C_EncryptFinal, C_DecryptFinal) the final accumulated output appears here.

The client receives these byte strings and unpacks them according to the same conventions used to construct the [PKCS#11 Input Parameters](pkcs-11-input-parameters.md). The [PKCS#11 Return Code](pkcs-11-return-code.md) in the same response payload indicates whether the function call succeeded at the Cryptoki level.

## Examples

After sending a C_Encrypt request for AES-CBC, the server returns a PKCS#11 operation response with PKCS#11 Output Parameters containing a Data byte string that is the resulting ciphertext, plus a PKCS#11 Return Code of CKR_OK. The client extracts the ciphertext from the Data field and uses it as needed.

## Related

[PKCS#11 Function](pkcs-11-function.md) · [PKCS#11 Input Parameters](pkcs-11-input-parameters.md) · [PKCS#11 Interface](pkcs-11-interface.md) · [PKCS#11 Return Code](pkcs-11-return-code.md) · [PKCS#11 Operation](../operations/pkcs-11.md)
