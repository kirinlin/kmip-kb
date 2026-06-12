---
title: Secret Data Type Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.52"
status: reviewed
related: ["secret-data", "object-type-enumeration"]
keywords: ["secret data type", "password", "seed", "secret data", "non-key secret"]
---

# Secret Data Type Enumeration

## Overview

The Secret Data Type enumeration sub-classifies a [Secret Data](../../objects/secret-data.md) managed object — the KMIP type for non-key secrets that need lifecycle management but are not cryptographic keys. It distinguishes the two primary semantic categories of secret data: opaque password-like values and random seeds used for key derivation or other purposes.

## Encoding (Tag / Type / Length / Value)

Encoded as a 4-byte integer (TTLV type `05`, Enumeration), tag `420086`.

## Fields & Structure

- **Password**: The secret is a password, passphrase, PIN, or other authentication credential. The server stores and manages it under the full KMIP lifecycle without interpreting its contents beyond the byte string.
- **Seed**: The secret is a random seed value — typically entropy used to initialise a deterministic key-generation process, a DRBG, or a key derivation function. Seeds have the same lifecycle and access control needs as keys but are not themselves keys.

## Examples

A database connection password managed by a secrets vault is registered as Secret Data with type **Password**. The master seed of an HD (hierarchical deterministic) wallet system is stored as Secret Data with type **Seed** and restricted to HSM-level protection.

## Related

[Secret Data](../../objects/secret-data.md) · [Object Type Enumeration](object-type-enumeration.md)
