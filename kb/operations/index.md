---
title: Operations
category: index
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1"
v1_source_section: "4"
status: draft
related: ["create", "register", "get", "locate", "query"]
keywords: ["operations", "client-to-server", "server-to-client", "lifecycle", "cryptographic operations"]
---

# Operations

Everything a KMIP client can ask a server to do (v2.1 §6.1; v1.x §4), plus the
[server-to-client](server-to-client/index.md) operations (v2.1 §6.2; v1.x §5).
Requests and
responses are carried as [batch items](../ttlv/batch-item.md) inside the
standard [message structure](../ttlv/message-structure.md).

## Object creation and import

- [Create](create.md) · [Create Key Pair](create-key-pair.md) ·
  [Register](register.md) · [Derive Key](derive-key.md) ·
  [Create Split Key](create-split-key.md) · [Join Split Key](join-split-key.md)
- [Import](import.md) / [Export](export.md) — whole-object transfer with
  attributes (added in 1.4).

## Certificates

- [Certify](certify.md) · [Re-certify](re-certify.md) ·
  [Validate](validate.md)

## Retrieval and search

- [Locate](locate.md) · [Get](get.md) · [Get Attributes](get-attributes.md) ·
  [Get Attribute List](get-attribute-list.md) · [Check](check.md)

## Attribute management

- [Add Attribute](add-attribute.md) · [Modify Attribute](modify-attribute.md) ·
  [Delete Attribute](delete-attribute.md)

## Lifecycle

- [Activate](activate.md) · [Revoke](revoke.md) · [Destroy](destroy.md) ·
  [Archive](archive.md) · [Recover](recover.md) · [Re-key](re-key.md) ·
  [Re-key Key Pair](re-key-key-pair.md)
- [Obtain Lease](obtain-lease.md) ·
  [Get Usage Allocation](get-usage-allocation.md)

## Cryptographic services (1.2+)

- [Encrypt](encrypt.md) · [Decrypt](decrypt.md) · [Sign](sign.md) ·
  [Signature Verify](signature-verify.md) · [MAC](mac.md) ·
  [MAC Verify](mac-verify.md) · [Hash](hash.md) ·
  [RNG Retrieve](rng-retrieve.md) · [RNG Seed](rng-seed.md)

## Protocol housekeeping

- [Query](query.md) · [Discover Versions](discover-versions.md) (1.1+) ·
  [Poll](poll.md) · [Cancel](cancel.md)

## Server-to-client

- [Notify](server-to-client/notify.md) · [Put](server-to-client/put.md) ·
  [Query](server-to-client/query.md) (1.3+)
