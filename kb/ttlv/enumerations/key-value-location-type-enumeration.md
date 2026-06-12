---
title: Key Value Location Type Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["1.3","1.4","2.0","2.1"]
source_section: "11.27"
status: reviewed
related: ["key-block", "get"]
keywords: ["key value location", "URI", "text string", "key reference", "external key", "key location"]
---

# Key Value Location Type Enumeration

## Overview

The Key Value Location Type enumeration classifies how the Key Value Location attribute describes where the actual key material resides when the key is not stored directly in the KMIP server's object store. In architectures where large volumes of key material reside in external vaults, hardware security modules, or cloud key stores, the KMIP server may hold only metadata and a pointer to the actual key rather than the key bytes themselves. This enumeration tells consumers whether the location is a plain text descriptor or a dereferenceable URI.

## Encoding (Tag / Type / Length / Value)

Encoded as a 4-byte integer (TTLV type `05`, Enumeration). Appears alongside the Key Value Location string in the Key Value Location attribute structure.

## Fields & Structure

- **Uninterpreted Text String**: The location is a free-form string whose interpretation is application-specific. It could be a hardware slot identifier, an HSM label, a partition name, or any other opaque reference that the consuming system understands without a standard URI scheme.
- **URI**: The location is a Uniform Resource Identifier that can be used to retrieve or reference the key material through a standard protocol (e.g., an HTTPS URL to a REST key vault API or a PKCS#11 URI as defined in RFC 7512).

## Examples

An enterprise that stores its HSM partition assignments in a configuration management database might use **Uninterpreted Text String** with a value like `HSM-Cluster-A:Partition-7` to record where a key physically resides. A cloud-native deployment might use **URI** with a value like `https://keyvault.example.com/keys/mykey/versions/abc123` to point at an Azure Key Vault or HashiCorp Vault endpoint.

## Related

- [Key Block structure](../key-block.md) — the structure within which key location metadata may appear
- [Get operation](../../operations/get.md) — the operation that retrieves key material, potentially by following a location reference
