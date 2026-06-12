---
title: Opaque Data Type
category: attribute
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "4.37"
status: reviewed
related: ["opaque-object", "object-type", "custom-attribute"]
keywords: ["opaque data type", "opaque object", "vendor-defined", "blob type", "opaque data subtype"]
---

# Opaque Data Type

## Purpose

Opaque Data Type is an attribute that labels the vendor-defined or implementation-specific nature of an [Opaque Object](../objects/opaque-object.md). Because an opaque object's contents are entirely opaque to the KMIP server — the server stores the bytes but does not interpret them — this attribute gives clients and policy engines a way to classify and retrieve opaque blobs by their intended purpose or format.

## Data Type & Structure

An Enumeration. The KMIP specification defines a small set of baseline values (including one for vendor-extension ranges), and implementations may add their own values within permitted extension ranges. The attribute records what category of data the opaque blob represents, not its content.

## Constraints

Single-instance. Optional but strongly recommended for interoperability — without it, a server or a different client has no mechanism to distinguish one kind of opaque blob from another. Can be set at registration and updated via [Set Attribute](../operations/set-attribute.md) while the object is in an appropriate state.

## Applies To (Object Types)

[Opaque Object](../objects/opaque-object.md) only.

## Set / Modified By

Client at [Register](../operations/register.md) time. May be updated by the client via [Set Attribute](../operations/set-attribute.md).

## Related Attributes

[Object Type](object-type.md) · [Custom Attribute](custom-attribute.md)
