---
title: Asymmetric Key Lifecycle Profiles
category: profile
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "prof-5.8"
status: reviewed
related: ["base-profiles", "symmetric-key-lifecycle-profiles", "cryptographic-profiles"]
keywords: ["asymmetric key", "RSA", "public key", "private key", "key pair", "PKI", "key lifecycle"]
---

# Asymmetric Key Lifecycle Profiles

## Overview

The Asymmetric Key Lifecycle Profiles define what a KMIP server must support to manage RSA public/private key pairs across their full lifecycle. This is the profile of choice for applications that need certificate-bound keys, code-signing keys, or TLS key pairs stored under centralized key management.

## Client

An Asymmetric Key Lifecycle Client extends the [Baseline Client](../base-encoding/base-profiles.md). No additional mandatory operations are imposed on the client side; it may invoke any server operation that fits its use case.

## Server

An Asymmetric Key Lifecycle Server extends the [Baseline Server](../base-encoding/base-profiles.md) and adds:
- **Objects**: Public Key, Private Key
- **Attributes**: `Cryptographic Algorithm`, `Object Type`, `Process Start Date`, `Process Stop Date`
- **Algorithm**: RSA
- **Key formats**: PKCS#1, PKCS#8, Transparent RSA Public Key, Transparent RSA Private Key
- **Object Types**: Public Key, Private Key

## Mandatory Test Cases

Test case identifiers encode the protocol version in their numeric suffix: `-10` = KMIP 1.0, `-11` = 1.1, `-12` = 1.2, `-21` = 2.1, and so on. For KMIP v2.1, `AKLC-M-1-21`, `AKLC-M-2-21`, and `AKLC-M-3-21` exercise RSA key-pair operations. `AKLC-O-1-21` (optional) covers additional scenarios such as key wrapping. The same test sequences appear under `-10`/`-11`/`-12` labels in the v1.x-era standalone companion document.

## Permitted Test Case Variations

When validating against these test cases, the following values may legitimately differ between implementations without being deemed non-conformant: `UniqueIdentifier`, `PrivateKeyUniqueIdentifier`, `PublicKeyUniqueIdentifier`, `UniqueBatchItemIdentifier`, `TimeStamp`, and key material for server-generated objects. Datetime attributes (`ActivationDate`, `InitialDate`, `DeactivationDate`, etc.) may vary when not fixed in the request. `DigestValue` and the `HashingAlgorithm` selected by the server for dynamically generated objects may also vary, as may `KeyFormatType` when the server selects it. Extensions reported in `Query` (`ExtensionList`, `ExtensionMap`, `ApplicationNamespaces`) are similarly unconstrained.

## Implications for Implementers

- The profile requires PKCS#1 and PKCS#8 key format support, which are the standard DER-encoded formats used by most TLS stacks and certificate authorities.
- `Process Start Date` and `Process Stop Date` govern the operational window for asymmetric key usage (signing, decryption). Set these in conjunction with certificate validity periods.
- RSA is the only mandated algorithm; EC key pairs are not required by this profile. Servers wishing to support ECDSA or other asymmetric algorithms should consider the Cryptographic Profiles or Quantum Safe Profiles.
- For KMIP 1.0–1.2, the normative profile source was the standalone OASIS companion document (`kmip-asym-key-profile/v1.0`) rather than KMIP-Prof. From v1.3 onward the profile was consolidated into KMIP-Prof §5.x, and in v2.x it appears at `prof-5.8`.

## Related Concepts

[Base Profiles](../base-encoding/base-profiles.md) ·
[Symmetric Key Lifecycle Profiles](symmetric-key-lifecycle-profiles.md) ·
[Cryptographic Profiles](cryptographic-profiles.md)
