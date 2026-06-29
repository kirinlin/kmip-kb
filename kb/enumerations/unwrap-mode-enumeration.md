---
title: Unwrap Mode Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["2.0","2.1"]
source_section: "11.59"
status: reviewed
related: ["key-wrapping-data", "key-block", "get", "cryptographic-parameters"]
keywords: ["unwrap mode", "key unwrap", "MAC verify", "decrypt", "key extraction", "wrap mode", "4200F2", "UnwrapMode"]
tag_hex: "4200F2"
xml_text: "UnwrapMode"
tag_type: "Enumeration"
---

# Unwrap Mode Enumeration

## Overview

The Unwrap Mode enumeration controls whether the server actively unwraps received key material or stores it in its wrapped form. When a client registers or imports a key that arrives inside a Key Block, Unwrap Mode indicates whether the server should decrypt and verify the wrapping before storing the inner key, or preserve the outer Key Block as-is without processing the wrapping. The choice determines whether the stored object is a plaintext key or an opaque wrapped blob that can be forwarded or later retrieved in wrapped form.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Unspecified | `00000001` | `Unspecified` | No explicit unwrap mode is indicated; the server applies its default handling for wrapped key material. |
| Processed | `00000002` | `Processed` | The server unwraps the key material — decrypts and/or verifies the Key Block — and stores the extracted inner key as a managed object. |
| Not Processed | `00000003` | `NotProcessed` | The server stores the key material in its wrapped form without processing the Key Block; the outer wrapping is preserved intact. |

## Examples

A client registering a transit key that must be forwarded to an offline HSM sets Unwrap Mode to **Not Processed**, so the server retains the wrapped blob rather than extracting the plaintext key. A client importing a key that was wrapped for delivery to this specific server sets Unwrap Mode to **Processed**, instructing the server to unwrap and store the inner key immediately.

## Related

[Key Wrapping Data](../structures/key-wrapping-data.md) · [Key Block](../structures/key-block.md) · [Get](../operations/get.md)
