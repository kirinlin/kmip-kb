---
title: Re-key
category: operation
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.46"
v1_source_section: "4.4"
status: reviewed
related: ["re-key-key-pair", "create", "revoke", "symmetric-key", "state", "link"]
keywords: ["re-key", "rekey", "replacement key", "key rotation", "symmetric key"]
xml_text: "ReKey"
---

# Re-key

## Purpose

`Re-key` produces a replacement for an existing symmetric key. It behaves much
like [Create](create.md), but the replacement inherits the existing key's
attributes instead of taking them all from the request, making it the standard
way to rotate a symmetric key while preserving its identity and metadata. The
asymmetric equivalent is [Re-key Key Pair](re-key-key-pair.md).

> Note: Re-key is v2.1 §6.1.46 (v1.x §4.4). In the locally mirrored v1.4
> source the section heading was lost during conversion, so the no-verbatim
> guard can't auto-anchor it there; the operation's content is present and
> this document is authored from it.

## Request Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | No | The existing symmetric key to replace. If omitted, the server uses the ID Placeholder. |
| Offset | `420058` | `Offset` | No | An interval giving the gap between the replacement key's initial date and its activation date. |
| Template-Attribute | `420091` | `TemplateAttribute` | No | Additional attributes for the replacement key. In KMIP 2.0+ this wrapper is replaced by the flat [Attributes](../structures/template-attribute-structures.md) structure. |

## Response Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes | Identifier of the newly created replacement key. |
| Template-Attribute | `420091` | `TemplateAttribute` | No | Attributes the server set implicitly on the replacement. |

## Behavior & Server Requirements

The server generates new key material, copies most attributes from the original
key, and links the two together — the original gets a [Link](../attributes/link.md)
of type Replacement Object to the new key, and the new key gets a Link of type
Replaced Key back to the original. The replacement's identifier is written to
the ID Placeholder. The name(s) of the original move to the replacement, which
is why a given key should only be re-keyed once. Several attributes get special
treatment: the [Initial Date](../attributes/initial-date.md) and
[Last Change Date](../attributes/last-change-date.md) are set to the current
time; destroy, compromise, and revocation dates are not carried over; a new
[Unique Identifier](../attributes/unique-identifier.md) is generated; the
[Digest](../attributes/digest.md) is recomputed; and the
[Random Number Generator](../attributes/random-number-generator.md) reflects the
generator used for the new key rather than the old one. When an Offset is given,
the activation, process-start, protect-stop, and deactivation dates of the
replacement are derived from the original key's dates shifted by the offset.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: an unknown or non-symmetric target object, or insufficient permission.

## Related Operations

[Re-key Key Pair](re-key-key-pair.md) · [Create](create.md) ·
[Revoke](revoke.md) · [Destroy](destroy.md)
