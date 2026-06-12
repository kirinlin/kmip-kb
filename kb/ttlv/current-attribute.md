---
title: Current Attribute
category: ttlv
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "5.6"
status: reviewed
related: ["attribute", "new-attribute", "attribute-reference", "set-attribute", "adjust-attribute"]
keywords: ["current attribute", "existing attribute", "attribute value before", "optimistic concurrency", "attribute update"]
---

# Current Attribute

## Overview

Current Attribute is a structure that carries the existing value of an attribute immediately before a modification takes place. It appears in [Set Attribute](../operations/set-attribute.md) and [Adjust Attribute](../operations/adjust-attribute.md) requests as a form of optimistic concurrency check: by including the value the client believes is currently stored, the client allows the server to verify that no concurrent modification has changed the attribute between the client's last read and this update request.

If the value carried in Current Attribute no longer matches what is stored on the object, the server may reject the operation, preventing unintended overwrites in multi-client environments.

## Encoding (Tag / Type / Length / Value)

Current Attribute encodes as a Structure containing a single Attribute.

| Field | Tag | Type | Required |
|---|---|---|---|
| Attribute | `420008` | Structure | Yes |

The inner Attribute carries the name and the client's understanding of the current value. There is exactly one Attribute child — Current Attribute is not a list.

## Fields & Structure

The single child [Attribute](attribute.md) follows the standard Attribute encoding with Attribute Name and Attribute Value sub-fields. The name identifies which attribute is being checked, and the value is what the client last read from the server (or initially set).

Servers that support optimistic locking on attribute updates inspect the value in Current Attribute against their stored record. The exact conflict resolution behavior — reject-on-mismatch versus last-write-wins — is server-policy and may be configurable.

When Current Attribute is absent from an operation that supports it, the operation is treated as an unconditional update: the server applies the change regardless of any concurrent modifications.

## Examples

A client reads an object and finds Cryptographic Usage Mask = `0x00000004` (Encrypt). It wants to add the Decrypt bit. The client sends an Adjust Attribute request with Current Attribute containing Cryptographic Usage Mask = `0x00000004` and New Attribute containing the updated value `0x0000000C`. If another client has already modified the mask to `0x0000000C` in the meantime, the server can detect the mismatch and return an appropriate error rather than silently overwriting a value the client did not anticipate.

## Related

[Attribute](attribute.md) · [New Attribute](new-attribute.md) · [Attribute Reference](attribute-reference.md) · [Set Attribute](../operations/set-attribute.md) · [Adjust Attribute](../operations/adjust-attribute.md)
