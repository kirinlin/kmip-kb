---
title: Key Format Type
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.25"
status: draft
related: ["key-block", "key-encoding"]
keywords: ["Key Format Type", "Digest", "encoding format", "interoperability", "format negotiation"]
---

# Key Format Type

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

The Key Format Type attribute specifies how the key material is encoded within the Key Block. Clients that need to compute or compare key digests must ensure that the server uses a predictable format; setting Key Format Type in a Create request tells the server exactly which format to use, or to fail rather than pick an incompatible format.

## Guidance

Omitting Key Format Type at object creation allows the server to select any format it considers appropriate. The chosen format affects the raw bytes that comprise the key material, which in turn affects the Digest. A client that later tries to verify the digest using a different format representation will fail to match. Specifying the Key Format Type at creation ensures consistency between the stored object and any external verification.

The server may additionally compute and store digests for other formats, but the primary digest corresponds to the format specified at creation.

## Implementation Notes

In environments where keys are stored in KMIP and must also be verifiable using external tools (certificate management systems, HSMs, PKI directories), it is important to agree in advance on the key format and to specify it explicitly in all Create and Register requests. This avoids silent format mismatches that only manifest as digest comparison failures.

## Related Concepts

See [Key Block](key-block.md) and [Key Encoding](key-encoding.md) for the relationship between format and byte representation.
