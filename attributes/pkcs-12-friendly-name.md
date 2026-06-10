---
title: PKCS#12 Friendly Name
category: attribute
spec_version: "1.4"
spec_versions: ["1.4", "2.0", "2.1"]
source_section: "3.45"
status: draft
related: ["link", "name", "secret-data"]
keywords: ["PKCS#12", "friendly name", "alias", "keystore", "private key"]
---

# PKCS#12 Friendly Name

## Purpose

Bridges KMIP and PKCS#12 keystores (added in 1.4 along with the PKCS#12 key
format). PKCS#12 files identify entries by an *alias* (friendlyName); this
attribute carries that alias across the protocol in both directions: telling
the server which entry to pick out of a registered PKCS#12 blob, and telling
it what alias to write when serving a private key back as PKCS#12.

## Data Type & Structure

A Text String. PKCS#12 matches aliases case-insensitively, so the convention
is to store lowercase.

## Constraints

- Optional; single instance; client-modifiable and deletable; the server
  does not rewrite it.
- On [Register](../operations/register.md) of a PKCS#12-format private key:
  if supplied, it selects the entry; if absent, the server records the alias
  of the first private key it finds in the blob.
- On [Get](../operations/get.md) with Key Format Type PKCS#12: the server
  encodes under this alias, defaulting to the literal string `alias` when
  the attribute is missing.
- The certificate chain and encryption password involved in PKCS#12 serving
  hang off the object via [Link](link.md) types added in 1.4 (PKCS#12
  Certificate Link, PKCS#12 Password Link).

## Applies To (Object Types)

Cryptographic objects — in practice, private keys.

## Set / Modified By

Client or server, at registration or later via
[Add Attribute](../operations/add-attribute.md).

## Related Attributes

[Link](link.md) · [Name](name.md)
