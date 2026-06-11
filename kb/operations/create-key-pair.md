---
title: Create Key Pair
category: operation
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.9"
v1_source_section: "4.2"
status: reviewed
related: ["create", "register", "re-key-key-pair", "certify", "public-key", "private-key", "cryptographic-algorithm"]
keywords: ["create key pair", "asymmetric key", "public key", "private key", "RSA", "key generation"]
---

# Create Key Pair

## Purpose

`Create Key Pair` asks the server to generate a matched public/private key pair
and register both halves as separate managed cryptographic objects. It is the
asymmetric counterpart to [Create](create.md), used for RSA, DSA, EC, and
similar algorithms.

## Request Fields

| Field | Required | Description |
|---|---|---|
| Common Template-Attribute | No | Attributes (individually or via templates) that apply to both the public and private key. |
| Private Key Template-Attribute | No | Attributes that apply only to the [Private Key](../objects/private-key.md); these override the common set. |
| Public Key Template-Attribute | No | Attributes that apply only to the [Public Key](../objects/public-key.md); these override the common set. |

When the same single-valued attribute is supplied in more than one place, the
key-specific template-attribute wins over the common one, and an explicitly
listed attribute wins over one pulled in via a named template; for
multi-valued attributes the values from all three sources are combined. Template
objects have been deprecated since version 1.3, so attributes are better
supplied individually. In KMIP 2.0+ these wrappers are replaced by the
corresponding flat Common Attributes / Private Key Attributes / Public Key
Attributes structures
([Template-Attribute Structures](../ttlv/template-attribute-structures.md));
the routing semantics are unchanged.

## Response Fields

| Field | Required | Description |
|---|---|---|
| Private Key Unique Identifier | Yes | Identifier of the newly created private key. |
| Public Key Unique Identifier | Yes | Identifier of the newly created public key. |
| Private Key Template-Attribute | No | Attributes the server set implicitly on the private key. |
| Public Key Template-Attribute | No | Attributes the server set implicitly on the public key. |

## Behavior & Server Requirements

The server generates both keys, assigns each a [Unique Identifier](../attributes/unique-identifier.md),
and cross-links them: the private key gets a [Link](../attributes/link.md) of
type Public Key pointing at its partner, and the public key gets a Link of type
Private Key in return. The ID Placeholder is set to the private key's
identifier. Certain attributes must agree across the pair — Cryptographic
Algorithm, Cryptographic Length, Cryptographic Domain Parameters, and
Cryptographic Parameters all take the same value for both keys, while the
[Cryptographic Usage Mask](../attributes/cryptographic-usage-mask.md) is set
independently (a signing private key versus a verifying public key, for
instance). Note that an equal Cryptographic Length on both keys does not mean
the two keys are literally the same size; the meaning of that length depends on
the algorithm (RSA modulus bits, the bit length of P for DSA/DH, the bit length
of Q for elliptic-curve algorithms).

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: a missing required attribute (algorithm or usage mask), an
invalid/unsupported algorithm or length, conflicting per-key attributes, or
insufficient permission.

## Related Operations

[Create](create.md) · [Re-key Key Pair](re-key-key-pair.md) ·
[Certify](certify.md) · [Register](register.md) · [Get](get.md)
