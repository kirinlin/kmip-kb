---
title: Opaque Data Type Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.35"
status: reviewed
related: ["opaque-data-type", "opaque-object", "object-type-enumeration"]
keywords: ["opaque data type", "opaque object", "vendor-defined", "blob classification", "420059", "OpaqueDataType"]
tag_hex: "420059"
xml_text: "OpaqueDataType"
tag_type: "Enumeration"
---

# Opaque Data Type Enumeration

## Overview

The Opaque Data Type enumeration sub-classifies an Opaque Object — the KMIP managed object type for arbitrary byte blobs whose content the server does not interpret. Because the server cannot inspect opaque content, this enumeration provides the only structured hook for policy engines and clients to distinguish different categories of opaque material. The core KMIP specification defines only one baseline value; implementations use extension ranges for vendor-specific subtypes.

## Fields & Structure

- **Opaque Data**: The single baseline value defined by KMIP itself, indicating the content is opaque data of unspecified kind. Vendor-defined extension values (in ranges above `0x8000 0000`) allow implementations to record more specific categories such as firmware images, PKCS#12 bundles, or proprietary metadata blobs without extending the core specification.

## Examples

A secrets management server that stores JWT signing configurations as opaque blobs can register a vendor extension value "JWT Config" so that policy rules and audit reports can distinguish these from firmware update packages stored under a different extension value.

## Related

[Opaque Data Type attribute](../attributes/opaque-data-type.md) · [Opaque Object](../objects/opaque-object.md) · [Object Type Enumeration](object-type-enumeration.md)
