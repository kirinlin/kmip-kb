---
title: Query Function Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.44"
status: reviewed
related: ["query", "server-information", "profile-version", "protection-storage-masks"]
keywords: ["query function", "query", "server capabilities", "query operations", "server information", "profiles", "420074", "QueryFunction"]
tag_hex: "420074"
xml_text: "QueryFunction"
tag_type: "Enumeration"
---

# Query Function Enumeration

## Overview

The Query Function enumeration selects which sections of server information a [Query](../operations/query.md) request returns. Rather than always returning all available data, a client specifies one or more Query Function values to retrieve only the relevant subset. This keeps responses small and allows incremental capability discovery.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Query Operations | `00000001` | `QueryOperations` | Returns the list of KMIP operations the server supports. |
| Query Objects | `00000002` | `QueryObjects` | Returns the list of managed object types the server stores. |
| Query Server Information | `00000003` | `QueryServerInformation` | Returns the [Server Information](../structures/server-information.md) structure — server name, vendor, version, conformance clauses. |
| Query Application Namespaces | `00000004` | `QueryApplicationNamespaces` | Returns vendor-defined application namespaces. |
| Query Extension List | `00000005` | `QueryExtensionList` | Returns names of vendor extensions supported. |
| Query Extension Map | `00000006` | `QueryExtensionMap` | Returns the full extension map (name to numeric code). |
| Query Attestation Types | `00000007` | `QueryAttestationTypes` | Returns the attestation credential types the server accepts. |
| Query RNGs | `00000008` | `QueryRNGs` | Returns random number generation capabilities. |
| Query Validations | `00000009` | `QueryValidations` | Returns cryptographic validation records the server holds. |
| Query Profiles | `0000000A` | `QueryProfiles` | Returns the [Profile Version](../structures/profile-version.md) structures listing supported conformance profiles. *(v1.1+)* |
| Query Capabilities | `0000000B` | `QueryCapabilities` | Returns algorithm-and-mode capability declarations. *(v1.1+)* |
| Query Client Registration Methods | `0000000C` | `QueryClientRegistrationMethods` | Returns how clients may register with the server. *(v1.2+)* |
| Query Defaults Information | `0000000D` | `QueryDefaultsInformation` | Returns the [Defaults Information](../structures/defaults-information.md) structure — server default attributes by object type. *(v2.1)* |
| Query Storage Protection Masks | `0000000E` | `QueryStorageProtectionMasks` | Returns the [Protection Storage Masks](../structures/protection-storage-masks.md) the server supports. *(v2.1)* |

## Examples

A client discovering a new server typically sends a single Query with all relevant Query Function values to learn capabilities in one round-trip. A constrained client may send only **Query Operations** to confirm that the operations it needs are supported before proceeding.

## Related

[Query](../operations/query.md) · [Server Information](../structures/server-information.md) · [Profile Version](../structures/profile-version.md) · [Defaults Information](../structures/defaults-information.md)
