---
title: Credential
category: messages
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "9.11"
v1_source_section: "2.1.2"
status: reviewed
related: ["authentication", "nonce", "message-structure"]
keywords: ["credential", "username password", "device credential", "attestation", "client identity", "420023"]
tag_hex: "420023"
xml_text: "Credential"
tag_type: "Structure"
---

# Credential

## Overview

A client identity claim carried inside the request header's
[Authentication](authentication.md) structure. Not a managed object — just a
message component. Three credential types exist; what a server accepts is
profile/policy territory (see the
[authentication concept](../concepts/authentication.md)).

## Encoding (Tag / Type / Length / Value)

Structure, tag `420023`:

| Field | Tag | XML Text | Type | Required |
|---|---|---|---|---|
| Credential Type | `420024` | `CredentialType` | Enumeration | Yes |
| Credential Value | `420025` | `CredentialValue` | varies by type | Yes |

## Fields & Structure

- **Username and Password** (type 1): Credential Value is a structure of
  Username (`420099`, required) and Password (`4200A1`, optional) text
  strings.
- **Device** (type 2): identifies a machine rather than a user. Value
  structure offers Device Serial Number (`4200B0`), Password, Device
  Identifier (`4200A2`), Network Identifier (`4200AB`), Machine Identifier
  (`4200A9`), and Media Identifier (`4200AA`) — all optional text strings,
  but at least one identifying field must be present and the combination
  must be unique on the server.
- **Attestation** (type 3, 1.2+): evidence of platform state. Value
  structure: a [Nonce](nonce.md) previously issued by the server (required),
  Attestation Type (`4200C7`: TPM Quote, TCG Integrity Report, SAML
  Assertion), and either an Attestation Measurement (`4200CB`) or an
  Attestation Assertion (`4200CC`) byte string — one of the two must be
  supplied.

## Examples

A storage appliance authenticates per-request with a Device credential
holding its serial number plus a shared-secret Password, layered on top of
its TLS client certificate.

## Related

[Authentication](authentication.md) · [Nonce](nonce.md) ·
[Authentication concept](../concepts/authentication.md)
