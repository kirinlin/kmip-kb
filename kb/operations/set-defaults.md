---
title: Set Defaults
category: operation
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "6.1.53"
status: reviewed
related: ["set-constraints", "get-constraints", "create", "create-key-pair", "register", "query", "defaults-information"]
keywords: ["set defaults", "defaults", "default attributes", "object defaults", "server defaults", "attribute defaults", "provisioning policy"]
---

# Set Defaults

## Purpose

`Set Defaults` configures the server-wide or object-type-scoped default attributes that the server applies when a client creates a managed object without specifying those attributes. For example, a deployment might require all new symmetric keys to default to a specific `Cryptographic Usage Mask` or a particular `Deactivation Date` offset. By setting those defaults once with `Set Defaults`, administrators avoid requiring every client to repeat the same attribute values on every [`Create`](create.md) call.

`Set Defaults` was introduced in v2.1 and uses the [Defaults Information](../structures/defaults-information.md) structure as its payload. It is administratively scoped — not all clients should be permitted to change server defaults.

## Request Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Defaults Information | `420152` | `DefaultsInformation` | Yes | The [Defaults Information](../structures/defaults-information.md) structure containing one or more Object Defaults entries. Each entry pairs an Object Type with a list of default attribute values to apply when creating objects of that type. Submitting a new Defaults Information structure replaces whatever defaults were previously configured. |

## Response Fields

The response contains only the standard result status — no payload fields are returned on success.

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Result Status | `42007F` | `ResultStatus` | Yes | Confirms whether the defaults were successfully stored. |

## Behavior & Server Requirements

The server stores the supplied defaults and uses them to fill in missing attributes during subsequent creation operations ([`Create`](create.md), [`Create Key Pair`](create-key-pair.md), [`Register`](register.md), and similar). When a creation request provides an explicit value for an attribute that also has a server default, the client-supplied value takes precedence.

Because the Defaults Information structure is submitted as a complete replacement, callers that want to update a single default must read the current defaults (via [`Query`](query.md) or equivalent), modify the relevant entry, and resubmit the full structure.

Defaults are scoped per Object Type. A default `Cryptographic Usage Mask` for Symmetric Keys does not affect the default usage mask for Private Keys. Each Object Defaults entry in the structure applies independently to its declared type.

Not all attributes can have server-side defaults — for example, `Unique Identifier` is always server-generated and cannot be defaulted. The server should return an error for any attempt to set a default for an attribute that does not support defaulting.

Servers must require administrative credentials for `Set Defaults`. The capability should be advertised in the [`Query`](query.md) response.

## Errors

Uses centralized error handling per the [error handling](../concepts/error-handling.md) conventions. Common failure causes include:

- The Defaults Information structure contains an attribute that cannot be defaulted.
- An attribute value within the structure is invalid for its type.
- The calling client lacks administrative permission to set server defaults.
- The server does not support the Defaults system — returns Operation Not Supported.

## Examples

An administrator configures the server so that all newly created symmetric keys automatically receive a one-year active window and a restricted usage mask:

```
Operation: Set Defaults
  Defaults Information:
    Object Defaults:
      Object Type: Symmetric Key
      Attributes:
        Activation Date: <today's date>
        Deactivation Date: <today + 365 days>
        Cryptographic Usage Mask: Encrypt, Decrypt
```

After this call, every `Create` request for a Symmetric Key that omits `Activation Date`, `Deactivation Date`, or `Cryptographic Usage Mask` will have those attributes filled in by the server automatically.

## Related Operations

[Set Constraints](set-constraints.md) · [Get Constraints](get-constraints.md) · [Create](create.md) · [Create Key Pair](create-key-pair.md) · [Query](query.md)
