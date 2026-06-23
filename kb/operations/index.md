---
title: Operations
category: index
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1"
v1_source_section: "4"
status: reviewed
related: ["create", "register", "get", "locate", "query"]
keywords: ["operations", "client-to-server", "server-to-client", "lifecycle", "cryptographic operations", "42014F"]
tag_hex: "42014F"
xml_text: "Operations"
tag_type: "Structure"
---

# Operations

Everything a KMIP client can ask a server to do (v2.1 §6.1; v1.x §4), plus the
[server-to-client](server-to-client/index.md) operations (v2.1 §6.2; v1.x §5).
Requests and
responses are carried as [batch items](../messages/batch-item.md) inside the
standard [message structure](../messages/message-structure.md).

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
- [Set Attribute](set-attribute.md) · [Adjust Attribute](adjust-attribute.md)
  (2.1)

## Lifecycle

- [Activate](activate.md) · [Revoke](revoke.md) · [Destroy](destroy.md) ·
  [Archive](archive.md) · [Recover](recover.md) · [Re-key](re-key.md) ·
  [Re-key Key Pair](re-key-key-pair.md)
- [Obtain Lease](obtain-lease.md) ·
  [Get Usage Allocation](get-usage-allocation.md)
- [Re-Provision](re-provision.md) (2.1)

## Cryptographic services (1.2+)

- [Encrypt](encrypt.md) · [Decrypt](decrypt.md) · [Sign](sign.md) ·
  [Signature Verify](signature-verify.md) · [MAC](mac.md) ·
  [MAC Verify](mac-verify.md) · [Hash](hash.md) ·
  [RNG Retrieve](rng-retrieve.md) · [RNG Seed](rng-seed.md)
- [Process](process.md) (2.1) — apply a cryptographic operation in a streamed,
  multi-part exchange.

## Sessions (2.1)

- [Login](login.md) · [Logout](logout.md) ·
  [Delegated Login](delegated-login.md)

## Server configuration (2.1)

- [Set Defaults](set-defaults.md) · [Set Constraints](set-constraints.md) ·
  [Get Constraints](get-constraints.md) ·
  [Set Endpoint Role](set-endpoint-role.md)

## Protocol housekeeping

- [Query](query.md) · [Discover Versions](discover-versions.md) (1.1+) ·
  [Poll](poll.md) · [Cancel](cancel.md)
- [Query Asynchronous Requests](query-asynchronous-requests.md) ·
  [Ping](ping.md) · [Log](log.md) · [Interop](interop.md) ·
  [PKCS#11](pkcs-11.md) (2.1)

## Server-to-client

- [Notify](server-to-client/notify.md) · [Put](server-to-client/put.md) ·
  [Query](server-to-client/query.md) (1.3+)
