---
title: Attributes
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.15"
status: draft
related: ["mutating-attributes"]
keywords: ["attributes", "Add Attribute", "Set Attribute", "Modify Attribute", "Delete Attribute", "Adjust Attribute", "multi-instance"]
tag_hex: "420125"
xml_element: "Attributes"
---

# Attributes

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

Every managed object in KMIP has a set of associated attributes that describe its properties and govern its use. Attributes may be mandatory or optional, single-instance or multi-instance, and may be settable by the client, the server, or both. Attribute management operations allow clients to create, read, modify, and delete attribute values.

## Guidance

The primary operations for attribute management are:

- **Add Attribute / Set Attribute**: Both create an attribute value; Set Attribute is preferred for single-instance attributes because it does not require knowing whether the attribute already exists.
- **Modify Attribute**: Updates an existing attribute value, identified by its current value for multi-instance attributes.
- **Delete Attribute**: Removes an attribute; for multi-instance attributes, the specific instance to remove is identified by its current value.
- **Adjust Attribute**: Provides a transaction-safe, convenient way to modify an attribute where applicable.

Multi-instance attributes require Add Attribute or Modify Attribute; applying Set Attribute to them is not permitted.

## Implementation Notes

The choice between Add Attribute and Set Attribute is significant: Add Attribute will fail if the attribute already exists for a single-instance attribute, while Set Attribute will overwrite it. Clients should use Set Attribute as the default for single-instance attributes to avoid idempotency issues. The Adjust Attribute operation is both more convenient and transactionally safer than separate read-modify-write sequences for supported attribute types.

## Related Concepts

See [Mutating Attributes](mutating-attributes.md) for guidance on attribute update constraints and clock-skew considerations.
