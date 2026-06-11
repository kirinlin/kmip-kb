---
title: Link
category: attribute
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.31"
v1_source_section: "3.35"
status: draft
related: ["unique-identifier", "object-type", "pkcs-12-friendly-name"]
keywords: ["link", "link type", "object relationships", "replacement object", "certificate chain", "derived key"]
---

# Link

## Purpose

Connects related managed objects into a graph: a public key to its private
half, a certificate to its issuing CA's certificate, a derived key to its
base key, a re-keyed key to its successor. Clients walk these links to fetch
a whole key pair, follow a certificate chain, or find the replacement after
a rotation.

## Data Type & Structure

A structure:

| Field | Type | Required |
|---|---|---|
| Link Type | Enumeration | Yes — the relationship kind |
| Linked Object Identifier | Text String | Yes — the target's [Unique Identifier](unique-identifier.md) |

Link types and their direction:

- *Private Key Link* (on a public key) / *Public Key Link* (on a private key
  or certificate) — the other half of the pair, or the certified key.
- *Certificate Link* — on a certificate: the parent in the chain; on a public
  key: the certificate(s) containing it.
- *Derivation Base Object Link* / *Derived Key Link* — what this was derived
  from / what was derived from this.
- *Replacement Object Link* / *Replaced Object Link* — successor (at most
  one) and predecessor after re-key or re-certify.
- *Parent / Child / Previous / Next Link* — generic hierarchy and ordering.
- *PKCS#12 Certificate Link* / *PKCS#12 Password Link* (1.4) — the
  certificate and the password secret used when serving a private key as
  PKCS#12.

## Constraints

- Optional; multi-instance (a private key typically links to both its public
  key and a certificate).
- At most one Replacement Object Link per object.
- Links may legitimately be missing when the related material lives outside
  the server (e.g. a registered CA certificate whose private key is
  elsewhere).

## Applies To (Object Types)

All cryptographic objects; which link types are sensible depends on the
[Object Type](object-type.md).

## Set / Modified By

Client or server; client-modifiable and deletable. Set implicitly by the
operations that create related objects:
[Create Key Pair](../operations/create-key-pair.md) (pairs),
[Derive Key](../operations/derive-key.md) (derivation links),
[Certify](../operations/certify.md) /
[Re-certify](../operations/re-certify.md),
[Re-key](../operations/re-key.md) /
[Re-key Key Pair](../operations/re-key-key-pair.md)
(replacement/replaced links).

## Related Attributes

[Unique Identifier](unique-identifier.md) · [Object Type](object-type.md) ·
[PKCS#12 Friendly Name](pkcs-12-friendly-name.md)
