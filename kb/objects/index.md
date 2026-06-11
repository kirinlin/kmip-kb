---
title: Objects
category: index
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "2"
v1_source_section: "2.2"
status: draft
related: ["symmetric-key", "certificate", "public-key", "private-key", "split-key", "secret-data", "opaque-object", "pgp-key", "template"]
keywords: ["managed objects", "managed cryptographic objects", "key", "certificate"]
---

# Objects

Managed Objects are the things KMIP key management operations act on. The subset
that carries cryptographic material — keys, certificates, secret data — are
called Managed Cryptographic Objects. Most are built on a shared
[Key Block](../ttlv/key-block.md) and described by common
[attributes](../attributes/) such as
[Unique Identifier](../attributes/unique-identifier.md) and
[State](../attributes/state.md).

## Managed object types

- [Symmetric Key](symmetric-key.md) — a single secret key for symmetric algorithms (e.g. AES).
- [Public Key](public-key.md) — the public half of an asymmetric key pair.
- [Private Key](private-key.md) — the private half of an asymmetric key pair.
- [Certificate](certificate.md) — an X.509 certificate (DER-encoded) binding a public key to an identity.
- [Split Key](split-key.md) — one share of a secret split for distribution among holders.
- [Secret Data](secret-data.md) — a shared secret such as a password or seed, distinct from keys and certificates.
- [Opaque Object](opaque-object.md) — data the server stores without interpreting.
- [PGP Key](pgp-key.md) — an ASCII-armored OpenPGP key (added in 1.2).
- [Template](template.md) — a named bundle of attributes (deprecated in 1.3).
