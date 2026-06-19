---
title: PKCS#11 Interface
category: structures
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "7.28"
status: reviewed
related: ["pkcs-11-function", "pkcs-11-input-parameters", "pkcs-11-output-parameters", "pkcs-11"]
keywords: ["PKCS#11 interface", "token selection", "slot ID", "Cryptoki library", "PKCS11 interface name", "HSM slot", "420159", "PKCS_11Interface"]
tag_hex: "420159"
xml_text: "PKCS_11Interface"
---

# PKCS#11 Interface

## Overview

PKCS#11 Interface is a structure that identifies which PKCS#11 token or slot the tunneled function call should target on the server side. Because a KMIP server may have access to multiple cryptographic tokens — different hardware security modules, different software keystores, or different slots within the same HSM — the client must indicate which one should handle the operation. PKCS#11 Interface provides that targeting information.

## Encoding (Tag / Type / Length / Value)

PKCS#11 Interface encodes as a Structure.

| Field | Tag | XML Text | Type | Required |
|---|---|---|---|---|
| PKCS#11 Interface Name | `420293` |  | Text String | Yes |
| PKCS#11 Slot ID | `420297` |  | Long Integer | No |

The interface name is the primary selector. The slot ID further discriminates when a named library exposes multiple slots.

## Fields & Structure

**PKCS#11 Interface Name** is a Text String that identifies the PKCS#11 provider on the server side. The value is server-defined and typically corresponds to the filename of the Cryptoki shared library (`"libpkcs11.so"`, a device label, or a logical name registered with the server). The server must be configured with a mapping from interface names to actual Cryptoki library instances.

**PKCS#11 Slot ID** is an optional Long Integer that selects a specific slot within the library. Slots map to individual tokens (physical HSM partitions, smart card slots, software keystore instances, etc.). When absent, the server uses the default slot configured for the named library.

Clients discover valid interface names and slot IDs from the server's Query response or through out-of-band configuration. Using an unknown name or an invalid slot ID results in an operation failure.

## Examples

A client needs to sign data using an RSA key resident on a specific HSM partition. The server hosts two HSM partitions: slot 0 for production keys and slot 1 for development keys. The client sends a PKCS#11 operation with PKCS#11 Interface carrying Interface Name = `"production-hsm"` and Slot ID = `0`. The server routes the C_Sign call to the correct token partition.

## Related

[PKCS#11 Function](pkcs-11-function.md) · [PKCS#11 Input Parameters](pkcs-11-input-parameters.md) · [PKCS#11 Output Parameters](pkcs-11-output-parameters.md) · [PKCS#11 Operation](../operations/pkcs-11.md)
