---
title: Link Type Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.28"
status: reviewed
related: ["unique-identifier", "create-key-pair", "certify", "register"]
keywords: ["link type", "linked objects", "certificate link", "public key link", "private key link", "derivation", "replacement", "parent", "child"]
---

# Link Type Enumeration

## Overview

The Link Type enumeration classifies the relationship between a managed object and another managed object referenced via the Link attribute. KMIP managed objects — keys, certificates, split-key shares — do not exist in isolation: a private key is paired with a public key and a certificate; a derived key traces back to its base key; a rotated key has a predecessor and a successor. The Link attribute records these relationships as named directed edges, allowing clients to traverse the object graph by following links rather than searching by attribute. Each Link entry carries one value from this enumeration to declare what relationship the link represents.

## Encoding (Tag / Type / Length / Value)

Encoded as a 4-byte integer (TTLV type `05`, Enumeration). Appears in the Link attribute structure alongside the Linked Object Identifier that identifies the related object.

## Fields & Structure

**PKI relationships:**
- **Certificate Link**: Points from a key object (typically a private or public key) to its associated certificate.
- **Public Key Link**: Points from a private key or certificate to the corresponding public key object.
- **Private Key Link**: Points from a public key or certificate to the corresponding private key object.
- **PKCS#12 Certificate Link**: Points to a certificate stored as part of a PKCS#12 bundle relationship.
- **PKCS#12 Password Link**: Points to the password or secret used to protect a PKCS#12 archive.

**Derivation and key hierarchy:**
- **Derivation Base Object Link**: Points from a derived key to the base key or secret from which it was derived.
- **Derived Key Link**: Points from a base key to one or more keys derived from it.
- **Replacement Object Link**: Points from a key that has been superseded to the key that replaced it. Used when a key is rotated out of service.
- **Replaced Object Link**: The inverse — points from the new/replacement key back to the old key it superseded.

**Ordering and hierarchy:**
- **Parent Link**: Points to the parent in a key hierarchy (e.g., a wrapping key or a higher-level key).
- **Child Link**: Points to a child in the hierarchy.
- **Previous Link**: Points to the previous object in a sequence (e.g., the key that was active before this one in a time-ordered rotation series).
- **Next Link**: Points to the next object in the sequence.

## Examples

After a [Create Key Pair](../../operations/create-key-pair.md) operation, KMIP automatically creates reciprocal **Public Key Link** and **Private Key Link** links between the generated key pair objects. When a [Certify](../../operations/certify.md) operation produces a certificate for the public key, a **Certificate Link** on the key and a **Public Key Link** on the certificate establish the bidirectional relationship.

## Related

- [Unique Identifier attribute](../../attributes/unique-identifier.md) — the value stored in a Link entry points to a Unique Identifier
- [Create Key Pair operation](../../operations/create-key-pair.md) — automatically establishes public/private key links
- [Certify operation](../../operations/certify.md) — establishes certificate links
