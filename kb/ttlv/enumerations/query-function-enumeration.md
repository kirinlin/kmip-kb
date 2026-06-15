---
title: Query Function Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.44"
status: reviewed
related: ["query", "server-information", "profile-version", "protection-storage-masks"]
keywords: ["query function", "query", "server capabilities", "query operations", "server information", "profiles"]
---

# Query Function Enumeration

## Overview

The Query Function enumeration selects which sections of server information a [Query](../../operations/query.md) request returns. Rather than always returning all available data, a client specifies one or more Query Function values to retrieve only the relevant subset. This keeps responses small and allows incremental capability discovery.

## Encoding (Tag / Type / Length / Value)

Encoded as a 4-byte integer (TTLV type `05`, Enumeration).

## Fields & Structure

- **Query Operations**: Returns the list of KMIP operations the server supports.
- **Query Objects**: Returns the list of managed object types the server stores.
- **Query Server Information**: Returns the [Server Information](../../structures/server-information.md) structure — server name, vendor, version, conformance clauses.
- **Query Application Namespaces**: Returns vendor-defined application namespaces.
- **Query Extension List**: Returns names of vendor extensions supported.
- **Query Extension Map**: Returns the full extension map (name to numeric code).
- **Query Attestation Types**: Returns the attestation credential types the server accepts.
- **Query RNG Parameters**: Returns random number generation capabilities.
- **Query Validations**: Returns cryptographic validation records the server holds.
- **Query Profiles** *(v1.1+)*: Returns the [Profile Version](../../structures/profile-version.md) structures listing supported conformance profiles.
- **Query Capabilities** *(v1.1+)*: Returns algorithm-and-mode capability declarations.
- **Query Client Registration Methods** *(v1.2+)*: Returns how clients may register with the server.
- **Query Defaults Information** *(v2.1)*: Returns the [Defaults Information](../../structures/defaults-information.md) structure — server default attributes by object type.
- **Query Storage Protection Masks** *(v2.1)*: Returns the [Protection Storage Masks](../../structures/protection-storage-masks.md) the server supports.
- **Query Interop Functions** *(v2.1)*: Returns named interoperability test functions available via the Interop operation.
- **Query PKCS#11 Interfaces** *(v2.1)*: Returns PKCS#11 interface descriptors for the PKCS#11 tunnel.

## Examples

A client discovering a new server typically sends a single Query with all relevant Query Function values to learn capabilities in one round-trip. A constrained client may send only **Query Operations** to confirm that the operations it needs are supported before proceeding.

## Related

[Query](../../operations/query.md) · [Server Information](../../structures/server-information.md) · [Profile Version](../../structures/profile-version.md) · [Defaults Information](../../structures/defaults-information.md)
