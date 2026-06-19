---
title: Re-key Key Pair
category: operation
spec_version: "2.1"
spec_versions: ["1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.47"
v1_source_section: "4.5"
status: reviewed
related: ["re-key", "create-key-pair", "certify", "public-key", "private-key", "link"]
keywords: ["re-key key pair", "rekey", "replacement key pair", "asymmetric rotation"]
---

# Re-key Key Pair

## Purpose

`Re-key Key Pair` produces a replacement public/private key pair for an existing
pair. It is to [Create Key Pair](create-key-pair.md) what [Re-key](re-key.md) is
to [Create](create.md): the new pair inherits most of the original pair's
attributes, making it the standard way to rotate an asymmetric key pair. It was
introduced in KMIP 1.1.

## Request Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Private Key Unique Identifier | `420066` | `PrivateKeyUniqueIdentifier` | No | The existing pair to replace, named by its private key. If omitted, the ID Placeholder is used. |
| Offset | `420058` | `Offset` | No | An interval giving the gap between the replacement pair's initial date and its activation date. |
| Common Template-Attribute | `42001F` | `CommonTemplateAttribute` | No | Attributes that apply to both replacement keys. |
| Private Key Template-Attribute | `420065` | `PrivateKeyTemplateAttribute` | No | Attributes for the replacement private key (override the common set). |
| Public Key Template-Attribute | `42006E` | `PublicKeyTemplateAttribute` | No | Attributes for the replacement public key (override the common set). |

The same precedence rules as [Create Key Pair](create-key-pair.md) apply when an
attribute is supplied in more than one place. In KMIP 2.0+ these wrappers are
replaced by the corresponding flat Common Attributes / Private Key Attributes /
Public Key Attributes structures
([Template-Attribute Structures](../structures/template-attribute-structures.md));
the routing semantics are unchanged.

## Response Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Private Key Unique Identifier | `420066` | `PrivateKeyUniqueIdentifier` | Yes | Identifier of the replacement private key. |
| Public Key Unique Identifier | `42006F` | `PublicKeyUniqueIdentifier` | Yes | Identifier of the replacement public key. |
| Private Key Template-Attribute | `420065` | `PrivateKeyTemplateAttribute` | No | Attributes the server set implicitly on the replacement private key. |
| Public Key Template-Attribute | `42006E` | `PublicKeyTemplateAttribute` | No | Attributes the server set implicitly on the replacement public key. |

## Behavior & Server Requirements

The server generates a new pair and links each new key to its predecessor with
[Link](../attributes/link.md) attributes of type Replacement Key (new → old) and
Replaced Key (old → new). The ID Placeholder is set to the replacement private
key's identifier. As with [Re-key](re-key.md), the original names move to the
replacement pair, so a pair should only be re-keyed once; initial and
last-change dates are set to now; destroy, compromise, and revocation dates are
not carried over; fresh identifiers are generated; and digests are recomputed.
When an Offset is supplied, the replacement pair's activation and deactivation
dates are derived from the original pair's dates shifted by the offset.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: an unknown target pair, or insufficient permission.

## Related Operations

[Re-key](re-key.md) · [Create Key Pair](create-key-pair.md) ·
[Certify](certify.md) · [Revoke](revoke.md)
