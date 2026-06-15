---
title: PKCS#11
category: operation
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "6.1.37"
status: reviewed
related: ["query", "get", "export", "process", "pkcs-11-interface", "pkcs-11-function", "pkcs-11-input-parameters", "pkcs-11-output-parameters", "pkcs-11-return-code"]
keywords: ["PKCS#11", "PKCS11", "CKA", "token", "slot", "C_Encrypt", "C_Sign", "C_Decrypt", "PKCS11 tunnel", "cryptoki", "hardware token", "HSM"]
---

# PKCS#11

## Purpose

`PKCS#11` tunnels a PKCS#11 (Cryptoki) function call over the KMIP protocol. It allows PKCS#11-aware clients to use a KMIP server as though it were a PKCS#11 token, delegating all function dispatch to the server side. Rather than requiring a local PKCS#11 library or hardware token driver, the client sends the function name and its arguments to the KMIP server, which executes the function against keys it manages and returns the output.

This enables existing PKCS#11 application stacks to operate against a centralized KMIP key store without client-side HSM drivers, while the KMIP server enforces its normal access controls and audit logging on every call.

`PKCS#11` was introduced in v2.1. Servers that support it advertise the capability in their [`Query`](query.md) response.

## Request Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| PKCS#11 Interface | `420159` | `PKCS_11Interface` | Yes | Identifies the PKCS#11 slot, token, or session context on the server against which the function should be dispatched. Corresponds to the [PKCS#11 Interface](../structures/pkcs-11-interface.md) structure. |
| PKCS#11 Function | `42015A` | `PKCS_11Function` | Yes | The name of the Cryptoki function to invoke (e.g., `C_Encrypt`, `C_Sign`, `C_GenerateKey`). Encoded in the [PKCS#11 Function](../structures/pkcs-11-function.md) structure. |
| PKCS#11 Input Parameters | `42015B` | `PKCS_11InputParameters` | No | The arguments to the specified Cryptoki function, encoded in the [PKCS#11 Input Parameters](../structures/pkcs-11-input-parameters.md) structure. The content and encoding of these parameters mirrors the PKCS#11 standard for the named function. |

## Response Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| PKCS#11 Output Parameters | `42015C` | `PKCS_11OutputParameters` | No | The output arguments produced by the Cryptoki function, encoded in the [PKCS#11 Output Parameters](../structures/pkcs-11-output-parameters.md) structure. Present when the function produces output (e.g., ciphertext from `C_Encrypt`). |
| PKCS#11 Return Code | `42015D` | `PKCS_11ReturnCode` | Yes | The Cryptoki return code (CKR_*) produced by the function execution on the server, encoded in the [PKCS#11 Return Code](../structures/pkcs-11-return-code.md) structure. A value of `CKR_OK` indicates success. Non-OK codes are returned within a successful KMIP response; they are not translated to KMIP error codes. |

## Behavior & Server Requirements

The server maps the PKCS#11 Interface to an internal session or token context, locates the function dispatcher for the named function, and executes the call with the supplied input parameters. The PKCS#11 return code is always included in the response — a CKR_* failure is a normal PKCS#11-level error, not a KMIP-level error, and the KMIP Result Status in the response header will still be `Success` in those cases.

The server applies its normal KMIP access controls before executing the function. A PKCS#11 call that would access a key the client is not permitted to use is rejected at the KMIP authorization layer before the PKCS#11 function is dispatched, returning a KMIP permission error rather than a Cryptoki error.

Key material referenced by PKCS#11 handles is never returned to the client; the key stays inside the server. This makes the `PKCS#11` operation a server-side crypto facility, not a key-export mechanism.

Servers are not required to support all PKCS#11 functions. They must return `CKR_FUNCTION_NOT_SUPPORTED` for any Cryptoki function they do not implement.

## Errors

Uses centralized error handling per the [error handling](../concepts/error-handling.md) conventions. Distinct error layers apply:

- KMIP-level errors (returned in the KMIP Result Status): the server does not support the `PKCS#11` operation; the client lacks KMIP permission to use the specified interface or key; the request is malformed.
- PKCS#11-level errors (returned in the PKCS#11 Return Code field within a successful KMIP response): the named function is not supported (`CKR_FUNCTION_NOT_SUPPORTED`); the input parameters are wrong for the function (`CKR_ARGUMENTS_BAD`); the function failed for a cryptographic reason (`CKR_DATA_INVALID`, `CKR_ENCRYPTED_DATA_INVALID`, etc.).

## Examples

A client application built on a PKCS#11 shim library needs to decrypt data using a server-managed RSA private key:

```
Operation: PKCS#11
  PKCS#11 Interface:
    Slot ID: 1
    Session Handle: <server-assigned session handle>
  PKCS#11 Function: C_Decrypt
  PKCS#11 Input Parameters:
    Key Object Handle: <PKCS#11 handle for the RSA key>
    Mechanism: CKM_RSA_PKCS_OAEP
    Encrypted Data: <ciphertext bytes>
```

The server decrypts the data using the referenced key and responds:

```
PKCS#11 Output Parameters:
  Data: <plaintext bytes>
PKCS#11 Return Code: CKR_OK
```

## Related Operations

[Process](process.md) · [Get](get.md) · [Export](export.md) · [Query](query.md)
