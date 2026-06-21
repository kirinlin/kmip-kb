---
title: PKCS#11 Function Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "11.38"
status: reviewed
related: ["pkcs-11-function", "pkcs-11-interface", "pkcs-11-input-parameters", "pkcs-11-output-parameters", "pkcs-11-return-code-enumeration"]
keywords: ["pkcs11", "cryptoki", "CK function", "C_Encrypt", "C_Sign", "C_GenerateKey", "PKCS11 function", "42015A", "PKCS_11Function"]
tag_hex: "42015A"
xml_text: "PKCS_11Function"
tag_type: "Enumeration"
---

# PKCS#11 Function Enumeration

## Overview

The PKCS#11 Function enumeration names the PKCS#11 Cryptoki API functions that can be tunneled over KMIP via the [PKCS#11 operation](../operations/pkcs-11.md). Each value corresponds to a `C_*` function from the PKCS#11 standard. When a KMIP client calls the PKCS#11 operation, it selects the function to invoke from this enumeration and passes the corresponding input parameters; the server executes the Cryptoki call against its internal token and returns the output.

## Fields & Structure

The enumeration covers the full Cryptoki function set, including (among others):

**Session management**: C_OpenSession, C_CloseSession, C_GetSessionInfo, C_Login, C_Logout.

**Object management**: C_CreateObject, C_CopyObject, C_DestroyObject, C_GetObjectSize, C_GetAttributeValue, C_SetAttributeValue, C_FindObjectsInit, C_FindObjects, C_FindObjectsFinal.

**Key generation and management**: C_GenerateKey, C_GenerateKeyPair, C_WrapKey, C_UnwrapKey, C_DeriveKey.

**Cryptographic operations**: C_EncryptInit, C_Encrypt, C_EncryptUpdate, C_EncryptFinal, C_DecryptInit, C_Decrypt, C_DecryptUpdate, C_DecryptFinal, C_SignInit, C_Sign, C_SignUpdate, C_SignFinal, C_VerifyInit, C_Verify, C_VerifyUpdate, C_VerifyFinal, C_DigestInit, C_Digest, C_DigestUpdate, C_DigestFinal.

**Token and slot info**: C_GetInfo, C_GetSlotList, C_GetSlotInfo, C_GetTokenInfo, C_GetMechanismList, C_GetMechanismInfo.

## Examples

A KMIP client that implements a PKCS#11 provider uses the PKCS#11 operation with Function = **C_Sign** to have the server sign data using a private key that never leaves the server, returning the signature to the client as PKCS#11 Output Parameters.

## Related

[PKCS#11 Function structure](../structures/pkcs-11-function.md) · [PKCS#11 operation](../operations/pkcs-11.md) · [PKCS#11 Return Code Enumeration](pkcs-11-return-code-enumeration.md)
