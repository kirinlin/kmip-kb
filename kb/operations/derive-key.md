---
title: Derive Key
category: operation
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.14"
v1_source_section: "4.6"
status: reviewed
related: ["create", "register", "secret-data", "symmetric-key", "cryptographic-parameters", "cryptographic-usage-mask"]
keywords: ["derive key", "key derivation", "PBKDF2", "HKDF", "HMAC", "KDF", "SP800-108"]
---

# Derive Key

## Purpose

`Derive Key` creates a new symmetric key or [Secret Data](../objects/secret-data.md)
object from existing keys or secret data already held by the server, using a
key-derivation function. It is used for password-based key derivation, KDF-based
expansion, and similar schemes where new key material is computed from existing
material rather than randomly generated.

## Request Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Object Type | `420057` | `ObjectType` | Yes | The type of object to derive (symmetric key or secret data). |
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes (may repeat) | The base object(s) whose material feeds the derivation. The ID Placeholder may not be substituted here. |
| Derivation Method | `420031` | `DerivationMethod` | Yes | An enumeration naming the derivation function to apply. |
| Derivation Parameters | `420032` | `DerivationParameters` | Yes | A structure carrying the inputs the chosen method needs. |
| Template-Attribute | `420091` | `TemplateAttribute` | Yes | Attributes for the derived object; the length, and for a key the algorithm, must always be given. In KMIP 2.0+ this wrapper is replaced by the flat [Attributes](../ttlv/template-attribute-structures.md) structure. |

## Response Fields

| Field | Tag | XML Element | Required | Description |
|---|---|---|---|---|
| Unique Identifier | `420094` | `UniqueIdentifier` | Yes | Identifier of the newly derived object. |
| Template-Attribute | `420091` | `TemplateAttribute` | No | Attributes the server set implicitly. |

## Behavior & Server Requirements

Each base object must permit derivation — its [Cryptographic Usage Mask](../attributes/cryptographic-usage-mask.md)
must include the Derive Key bit — or the server rejects the request. The client
states the desired output size through [Cryptographic Length](../attributes/cryptographic-length.md);
asking for more output than the method can produce is an error. A client can
derive several keys and IVs at once by deriving a secret-data object sized to
their combined length. After computing the result, the server registers it as a
new managed object, returns its identifier, sets the ID Placeholder to it, and
links the result and its base object(s) with [Link](../attributes/link.md)
attributes of type Derived Key and Derivation Base Object.

Supported derivation methods include PBKDF2 (password-based), HASH, HMAC,
ENCRYPT, and the NIST SP 800-108 KDF modes (Counter, Feedback, and
Double-Pipeline Iteration), plus room for extensions. The Derivation Parameters
structure typically carries [Cryptographic Parameters](../attributes/cryptographic-parameters.md)
(identifying the PRF or mode), an optional initialization vector, and the
derivation data — except that HMAC derivation takes the PRF from the key's own
attributes, and PBKDF2 adds a salt and an iteration count. Derivation data may be
supplied directly or implicitly by naming a secret-data object, but not both.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Common
causes: a base object lacking the Derive Key usage bit, a requested length
exceeding the method's output, both explicit and implicit derivation data
supplied, or a missing required parameter for the chosen method.

## Related Operations

[Create](create.md) · [Register](register.md) · [Get](get.md)
