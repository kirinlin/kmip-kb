---
title: Multi-instance Hash
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.23"
status: draft
related: ["attributes"]
keywords: ["Digest", "multi-instance", "SHA-256", "SHA-1", "MD5", "fingerprint", "hash"]
---

# Multi-instance Hash

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

The Digest attribute records a cryptographic hash of a managed object. A single managed object may carry several Digest attribute entries simultaneously, each computed with a distinct hash algorithm. The server always generates a SHA-256 hash at object creation; additional digest instances may be added with other algorithms.

## Guidance

Multiple digest instances are useful when an object must be compared or verified in environments that use different hash functions. A common example is publicly trusted CA certificates, which are often published with both SHA-1 and MD5 fingerprints alongside SHA-256. Each instance is an independent attribute value containing the Hashing Algorithm used and the resulting hash bytes.

## Implementation Notes

Servers always generate the SHA-256 digest automatically. Clients or servers may add additional digest instances for other algorithms (e.g., SHA-1 for legacy compatibility). The multi-instance digest can be used to identify objects across systems that use different hash algorithms for object identification, improving interoperability with non-KMIP certificate stores and HSMs.

## Related Concepts

See [Attributes](attributes.md) for the general multi-instance attribute model.
