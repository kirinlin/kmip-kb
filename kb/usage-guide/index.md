---
title: Usage Guide
category: index
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: ""
status: reviewed
related: ["id-placeholder", "key-life-cycle-and-key-state", "using-wrapped-keys-with-kmip"]
keywords: ["usage guide", "KMIP-UG", "implementation guidance", "best practices", "deprecations"]
---

# Usage Guide

Implementation guidance distilled from the non-normative OASIS KMIP Usage
Guide ([KMIP-UG]): how the protocol is meant to be used in practice — advice,
rationale, and worked patterns the normative spec deliberately leaves out.
Articles trace to UG §2–§5 via the `ug-` prefix in `source_section`.

## Messaging, batching & asynchronous flow

- [Batched Requests and Responses](batched-requests-and-responses.md) ·
  [Reducing Multiple Requests Through the Use of Batch](reducing-multiple-requests-through-the-use-of-batch.md)
- [Synchronous and Asynchronous Operations](synchronous-and-asynchronous-operations.md) ·
  [Full Async](full-async.md) · [Process](process.md) ·
  [Canceling Asynchronous Operations](canceling-asynchronous-operations.md) ·
  [Querying Outstanding Asynchronous Requests](querying-outstanding-asynchronous-requests.md)
- [Flow Control](flow-control.md) · [Large Responses](large-responses.md) ·
  [Maximum Message Size](maximum-message-size.md) ·
  [Reliable Message Delivery](reliable-message-delivery.md)
- [Message Security](message-security.md) ·
  [Client and Server Correlation Values](client-and-server-correlation-values.md)
- [Result Reasons](result-reasons.md) ·
  [Result Message Text](result-message-text.md) ·
  [Constraints](constraints.md) ·
  [Using Notify and Put Operations](using-notify-and-put-operations.md)

## Discovery, versioning & extensibility

- [Query](query.md) · [Discover Versions](discover-versions.md) ·
  [Interop](interop.md)
- [Extensible Protocol](extensible-protocol.md) ·
  [Message Extensions](message-extensions.md) ·
  [Vendor Extensions](vendor-extensions.md) ·
  [Registering Extension Information](registering-extension-information.md)
- [KMIP Deprecation Rule](kmip-deprecation-rule.md) ·
  [Deprecated Functions](deprecated-functions.md)

## Identity, trust & policy

- [Authentication](authentication.md) · [Login and Logout](login-and-logout.md) ·
  [Delegated Login](delegated-login.md) ·
  [Passing Attestation Data](passing-attestation-data.md)
- [KMIP Client Registration Models](kmip-client-registration-models.md) ·
  [Island of Trust](island-of-trust.md) · [Server Policy](server-policy.md) ·
  [State-less Server](state-less-server.md)
- [Support for Intelligent Clients and Key-Using Devices](support-for-intelligent-clients-and-key-using-devices.md) ·
  [Authorization for Revoke, Recover, Destroy and Archive Operations](authorization-for-revoke-recover-destroy-and-archive-operations.md)

## Object lifecycle & state

- [Key Life Cycle and Key State](key-life-cycle-and-key-state.md) ·
  [Key State and Times](key-state-and-times.md) ·
  [Mutating Attributes](mutating-attributes.md)
- [Key Rotation](key-rotation.md) ·
  [Using Offset in Re-key and Re-certify Operations](using-offset-in-re-key-and-re-certify-operations.md) ·
  [Usage Allocation](usage-allocation.md)
- [Compromised Objects](compromised-objects.md) ·
  [Revocation Reason Codes](revocation-reason-codes.md) ·
  [Archive Operations](archive-operations.md)
- [Key Shredding](key-shredding.md) ·
  [Cryptographic Shredding (Erasure)](cryptographic-shredding-erasure.md)

## Identification & lookup

- [Unique Identifiers](unique-identifiers.md) · [ID Placeholder](id-placeholder.md)
- [Locating Keys in Specific States](locating-keys-in-specific-states.md) ·
  [Handling Large Locate Result Sets](handling-large-locate-result-sets.md) ·
  [Returning Related Objects](returning-related-objects.md) ·
  [Object Group](object-group.md)
- [Application Specific Information](application-specific-information.md) ·
  [Interoperable Key Naming for Tape](interoperable-key-naming-for-tape.md)

## Attributes & metadata

- [Attributes](attributes.md) ·
  [Description and Comment Attributes](description-and-comment-attributes.md) ·
  [Multi-instance Hash](multi-instance-hash.md)
- [Extractable and Sensitive Attributes](extractable-and-sensitive-attributes.md) ·
  [Protection Storage Mask](protection-storage-mask.md)
- [Non-Cryptographic Objects](non-cryptographic-objects.md) ·
  [Use of Meta-Data Only (MDO) Keys](use-of-meta-data-only-mdo-keys.md)

## Key material & formats

- [Key Block](key-block.md) · [Key Encoding](key-encoding.md) ·
  [Key Format Type](key-format-type.md) ·
  [Using the Raw Key Format Type](using-the-raw-key-format-type.md) ·
  [PKCS#12 Key Format](pkcs-12-key-format.md)
- [Using Wrapped Keys with KMIP](using-wrapped-keys-with-kmip.md) ·
  [Split Key](split-key.md) ·
  [Key Replication Between Servers](key-replication-between-servers.md)

## Asymmetric keys & certificates

- [Registering a Key Pair](registering-a-key-pair.md) ·
  [Cryptographic Length of Asymmetric Keys](cryptographic-length-of-asymmetric-keys.md) ·
  [Asymmetric Concepts with Symmetric Keys](asymmetric-concepts-with-symmetric-keys.md) ·
  [Using the Same Asymmetric Key Pair in Multiple Algorithms](using-the-same-asymmetric-key-pair-in-multiple-algorithms.md)
- [Elliptic Curve Cryptography (ECC) Recommended Curve Mapping](elliptic-curve-cryptography-ecc-recommended-curve-mapping.md)
- [Certify and Re-certify](certify-and-re-certify.md) ·
  [Certificate Renewal, Update and Re-key](certificate-renewal-update-and-re-key.md) ·
  [Certificate Revocation Lists](certificate-revocation-lists.md) ·
  [Using KMIP for PGP Keys](using-kmip-for-pgp-keys.md)

## Cryptographic services

- [Cryptographic Services](cryptographic-services.md) ·
  [Default Crypto Parameters](default-crypto-parameters.md) ·
  [Re-encrypt](reencrypt.md) ·
  [Using One-Time Pad Algorithms](using-one-time-pad-algorithms.md)
