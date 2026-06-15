---
title: Re-Provision
category: operation
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "6.1.48"
status: reviewed
related: ["register", "get", "destroy", "create", "activate", "re-key", "unique-identifier"]
keywords: ["re-provision", "reprovisioning", "re-issue", "endpoint", "device", "binding refresh", "attribute update", "lifecycle", "refresh"]
---

# Re-Provision

## Purpose

`Re-Provision` refreshes the binding between a managed object and the device or endpoint that originally received it. It re-issues the object to the same endpoint with updated lifecycle attributes — such as a new activation date, new expiration date, or refreshed credentials — without requiring a full [`Destroy`](destroy.md) + [`Create`](create.md) cycle. The key material itself is typically unchanged; what changes is the policy envelope surrounding it.

This operation is most useful in device-provisioning and certificate-enrollment workflows where the same physical device needs its key or certificate renewed periodically, and where continuity of the object's identifier matters (for example, because the device has cached it, or because audit records reference it).

`Re-Provision` was introduced in v2.1.

## Request Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes | Identifies the managed object to be re-provisioned. The object must already exist on the server. |
| Attribute | `420008` | `Attribute` | No (repeatable) | One or more attributes to update on the object as part of the re-provisioning. Typical examples include `Activation Date`, `Deactivation Date`, and `Name`. Attributes not listed here retain their current values. |
| Authentication | `42000C` | `Authentication` | No | A credential or token representing the endpoint receiving the re-provisioned object. The server uses this to bind the refreshed object to the correct endpoint identity. |

## Response Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes | Confirms the identifier of the re-provisioned object. Remains the same as in the request — the object retains its identity. |

## Behavior & Server Requirements

The server locates the identified object and verifies that the calling client has permission to re-provision it. It then applies the supplied attribute updates atomically, simultaneously updating any endpoint-binding metadata (such as the endpoint credential or the device identifier associated with the object).

The object's state is reset or adjusted according to server policy. In most implementations the object transitions to a provisioned-but-not-yet-active state, similar to where it was immediately after initial creation, so that the endpoint must re-activate it. This prevents an automatically renewed object from becoming active before the endpoint has acknowledged receipt.

The server must record a re-provisioning event in the object's audit history, noting the previous and updated attribute values. This record is important for certificate or key lifecycle accountability.

`Re-Provision` does not change the key material of cryptographic objects. If new key material is also needed, callers should use [`Re-Key`](re-key.md) in addition to or instead of `Re-Provision`.

## Errors

Uses centralized error handling per the [error handling](../concepts/error-handling.md) conventions. Common failure causes include:

- The Unique Identifier refers to an object that does not exist or has been destroyed.
- The calling client lacks permission to re-provision the identified object.
- The supplied attribute updates are invalid for the object type or conflict with the current object state.
- The object is in a state that does not permit re-provisioning (e.g., it has been revoked and the server's policy forbids re-activating revoked objects).

## Examples

An IoT gateway holds a managed AES key with a one-year expiry. When the key nears expiration, the provisioning service extends the deactivation date without issuing a new key:

```
Operation: Re-Provision
  Unique Identifier: "iot-gw-enc-key-0042"
  Attribute:
    Attribute Name: Deactivation Date
    Attribute Value: 2027-06-12T00:00:00Z
  Attribute:
    Attribute Name: Activation Date
    Attribute Value: 2026-06-12T00:00:00Z
```

The server updates the dates and the key retains its identifier `"iot-gw-enc-key-0042"`. The gateway can continue using the same key handle it cached locally without any re-enrollment handshake.

## Related Operations

[Register](register.md) · [Re-Key](re-key.md) · [Activate](activate.md) · [Destroy](destroy.md) · [Get Attributes](get-attributes.md)
