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

- [Batched Requests and Responses](messaging/batched-requests-and-responses.md) ·
  [Reducing Multiple Requests Through the Use of Batch](messaging/reducing-multiple-requests-through-the-use-of-batch.md)
- [Synchronous and Asynchronous Operations](messaging/synchronous-and-asynchronous-operations.md) ·
  [Full Async](messaging/full-async.md) · [Process](messaging/process.md) ·
  [Canceling Asynchronous Operations](messaging/canceling-asynchronous-operations.md) ·
  [Querying Outstanding Asynchronous Requests](messaging/querying-outstanding-asynchronous-requests.md)
- [Flow Control](messaging/flow-control.md) · [Large Responses](messaging/large-responses.md) ·
  [Maximum Message Size](messaging/maximum-message-size.md) ·
  [Reliable Message Delivery](messaging/reliable-message-delivery.md)
- [Message Security](messaging/message-security.md) ·
  [Client and Server Correlation Values](messaging/client-and-server-correlation-values.md)
- [Result Reasons](messaging/result-reasons.md) ·
  [Result Message Text](messaging/result-message-text.md) ·
  [Constraints](messaging/constraints.md) ·
  [Using Notify and Put Operations](messaging/using-notify-and-put-operations.md)

## Discovery, versioning & extensibility

- [Query](discovery/query.md) · [Discover Versions](discovery/discover-versions.md) ·
  [Interop](discovery/interop.md)
- [Extensible Protocol](discovery/extensible-protocol.md) ·
  [Message Extensions](discovery/message-extensions.md) ·
  [Vendor Extensions](discovery/vendor-extensions.md) ·
  [Registering Extension Information](discovery/registering-extension-information.md)
- [KMIP Deprecation Rule](discovery/kmip-deprecation-rule.md) ·
  [Deprecated Functions](discovery/deprecated-functions.md)

## Identity, trust & policy

- [Authentication](identity/authentication.md) · [Login and Logout](identity/login-and-logout.md) ·
  [Delegated Login](identity/delegated-login.md) ·
  [Passing Attestation Data](identity/passing-attestation-data.md)
- [KMIP Client Registration Models](identity/kmip-client-registration-models.md) ·
  [Island of Trust](identity/island-of-trust.md) · [Server Policy](identity/server-policy.md) ·
  [State-less Server](identity/state-less-server.md)
- [Support for Intelligent Clients and Key-Using Devices](identity/support-for-intelligent-clients-and-key-using-devices.md) ·
  [Authorization for Revoke, Recover, Destroy and Archive Operations](identity/authorization-for-revoke-recover-destroy-and-archive-operations.md)

## Object lifecycle & state

- [Key Life Cycle and Key State](lifecycle/key-life-cycle-and-key-state.md) ·
  [Key State and Times](lifecycle/key-state-and-times.md) ·
  [Mutating Attributes](lifecycle/mutating-attributes.md)
- [Key Rotation](lifecycle/key-rotation.md) ·
  [Using Offset in Re-key and Re-certify Operations](lifecycle/using-offset-in-re-key-and-re-certify-operations.md) ·
  [Usage Allocation](lifecycle/usage-allocation.md)
- [Compromised Objects](lifecycle/compromised-objects.md) ·
  [Revocation Reason Codes](lifecycle/revocation-reason-codes.md) ·
  [Archive Operations](lifecycle/archive-operations.md)
- [Key Shredding](lifecycle/key-shredding.md) ·
  [Cryptographic Shredding (Erasure)](lifecycle/cryptographic-shredding-erasure.md)

## Identification & lookup

- [Unique Identifiers](identification/unique-identifiers.md) · [ID Placeholder](identification/id-placeholder.md)
- [Locating Keys in Specific States](identification/locating-keys-in-specific-states.md) ·
  [Handling Large Locate Result Sets](identification/handling-large-locate-result-sets.md) ·
  [Returning Related Objects](identification/returning-related-objects.md) ·
  [Object Group](identification/object-group.md)
- [Application Specific Information](identification/application-specific-information.md) ·
  [Interoperable Key Naming for Tape](identification/interoperable-key-naming-for-tape.md)

## Attributes & metadata

- [Attributes](attributes/attributes.md) ·
  [Description and Comment Attributes](attributes/description-and-comment-attributes.md) ·
  [Multi-instance Hash](attributes/multi-instance-hash.md)
- [Extractable and Sensitive Attributes](attributes/extractable-and-sensitive-attributes.md) ·
  [Protection Storage Mask](attributes/protection-storage-mask.md)
- [Non-Cryptographic Objects](attributes/non-cryptographic-objects.md) ·
  [Use of Meta-Data Only (MDO) Keys](attributes/use-of-meta-data-only-mdo-keys.md)

## Key material & formats

- [Key Block](key-material/key-block.md) · [Key Encoding](key-material/key-encoding.md) ·
  [Key Format Type](key-material/key-format-type.md) ·
  [Using the Raw Key Format Type](key-material/using-the-raw-key-format-type.md) ·
  [PKCS#12 Key Format](key-material/pkcs-12-key-format.md)
- [Using Wrapped Keys with KMIP](key-material/using-wrapped-keys-with-kmip.md) ·
  [Split Key](key-material/split-key.md) ·
  [Key Replication Between Servers](key-material/key-replication-between-servers.md)

## Asymmetric keys & certificates

- [Registering a Key Pair](asymmetric/registering-a-key-pair.md) ·
  [Cryptographic Length of Asymmetric Keys](asymmetric/cryptographic-length-of-asymmetric-keys.md) ·
  [Asymmetric Concepts with Symmetric Keys](asymmetric/asymmetric-concepts-with-symmetric-keys.md) ·
  [Using the Same Asymmetric Key Pair in Multiple Algorithms](asymmetric/using-the-same-asymmetric-key-pair-in-multiple-algorithms.md)
- [Elliptic Curve Cryptography (ECC) Recommended Curve Mapping](asymmetric/elliptic-curve-cryptography-ecc-recommended-curve-mapping.md)
- [Certify and Re-certify](asymmetric/certify-and-re-certify.md) ·
  [Certificate Renewal, Update and Re-key](asymmetric/certificate-renewal-update-and-re-key.md) ·
  [Certificate Revocation Lists](asymmetric/certificate-revocation-lists.md) ·
  [Using KMIP for PGP Keys](asymmetric/using-kmip-for-pgp-keys.md)

## Cryptographic services

- [Cryptographic Services](crypto-services/cryptographic-services.md) ·
  [Default Crypto Parameters](crypto-services/default-crypto-parameters.md) ·
  [Re-encrypt](crypto-services/reencrypt.md) ·
  [Using One-Time Pad Algorithms](crypto-services/using-one-time-pad-algorithms.md)
