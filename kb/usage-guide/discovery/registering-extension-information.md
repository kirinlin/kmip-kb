---
title: Registering Extension Information
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-4.4"
status: reviewed
related: ["vendor-extensions", "message-extensions"]
keywords: ["extension registration", "KMIP TC", "Tag value", "Extension Name", "ballot", "OASIS"]
---

# Registering Extension Information

## Overview

Vendors who define KMIP extensions should register those extensions with the KMIP Technical Committee to avoid tag-space collisions with other vendors and to provide a path toward future standardisation.

## Guidance

The registration procedure:

1. Document the extension: include Extension Tag values, Extension Names, Extension Types, a brief description of the purpose, example use case messages (requests and responses), and usage guidance.
2. Submit the package to the KMIP TC for community review.
3. Request a KMIP TC ballot to formally reserve the extension tag values.

The goal is to create a public registry of extension identifiers so that independent implementations do not accidentally use the same tag value for different purposes.

## Implementation Notes

Unregistered extensions are a significant interoperability risk: two vendors using the same tag value for different purposes will produce silently incorrect behaviour when parsing each other's messages. Registering extensions before deployment, even for purely internal extensions, is good practice. The TC registration process also creates an opportunity for a community review that may improve the extension design.

## Related Concepts

See [Vendor Extensions](vendor-extensions.md) for the full extension model.
