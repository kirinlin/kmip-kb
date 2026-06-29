---
title: Link Type Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.28"
status: reviewed
related: ["unique-identifier", "create-key-pair", "certify", "register"]
keywords: ["link type", "linked objects", "certificate link", "public key link", "private key link", "derivation", "replacement", "parent", "child", "42004B", "LinkType"]
tag_hex: "42004B"
xml_text: "LinkType"
tag_type: "Enumeration"
---

# Link Type Enumeration

## Overview

The Link Type enumeration classifies the relationship between a managed object and another managed object referenced via the Link attribute. KMIP managed objects — keys, certificates, split-key shares — do not exist in isolation: a private key is paired with a public key and a certificate; a derived key traces back to its base key; a rotated key has a predecessor and a successor. The Link attribute records these relationships as named directed edges, allowing clients to traverse the object graph by following links rather than searching by attribute. Each Link entry carries one value from this enumeration to declare what relationship the link represents.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Certificate Link | `00000101` | `CertificateLink` | Points from a key object (typically a private or public key) to its associated certificate. |
| Public Key Link | `00000102` | `PublicKeyLink` | Points from a private key or certificate to the corresponding public key object. |
| Private Key Link | `00000103` | `PrivateKeyLink` | Points from a public key or certificate to the corresponding private key object. |
| Derivation Base Object Link | `00000104` | `DerivationBaseObjectLink` | Points from a derived key to the base key or secret from which it was derived. |
| Derived Key Link | `00000105` | `DerivedKeyLink` | Points from a base key to one or more keys derived from it. |
| Replacement Object Link | `00000106` | `ReplacementObjectLink` | Points from a key that has been superseded to the key that replaced it. Used when a key is rotated out of service. |
| Replaced Object Link | `00000107` | `ReplacedObjectLink` | The inverse — points from the new/replacement key back to the old key it superseded. |
| Parent Link | `00000108` | `ParentLink` | Points to the parent in a key hierarchy (e.g., a wrapping key or a higher-level key). |
| Child Link | `00000109` | `ChildLink` | Points to a child in the hierarchy. |
| Previous Link | `0000010A` | `PreviousLink` | Points to the previous object in a sequence (e.g., the key that was active before this one in a time-ordered rotation series). |
| Next Link | `0000010B` | `NextLink` | Points to the next object in the sequence. |
| PKCS#12 Certificate Link | `0000010C` | `PKCS_12CertificateLink` | Points to a certificate stored as part of a PKCS#12 bundle relationship. |
| PKCS#12 Password Link | `0000010D` | `PKCS_12PasswordLink` | Points to the password or secret used to protect a PKCS#12 archive. |
| Wrapping Key Link | `0000010E` | `WrappingKeyLink` |  |

## Examples

After a [Create Key Pair](../operations/create-key-pair.md) operation, KMIP automatically creates reciprocal **Public Key Link** and **Private Key Link** links between the generated key pair objects. When a [Certify](../operations/certify.md) operation produces a certificate for the public key, a **Certificate Link** on the key and a **Public Key Link** on the certificate establish the bidirectional relationship.

## Related

- [Unique Identifier attribute](../attributes/unique-identifier.md) — the value stored in a Link entry points to a Unique Identifier
- [Create Key Pair operation](../operations/create-key-pair.md) — automatically establishes public/private key links
- [Certify operation](../operations/certify.md) — establishes certificate links
