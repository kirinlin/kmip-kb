---
title: NIST Key Type Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "11.32"
status: reviewed
related: ["nist-key-type", "cryptographic-usage-mask", "cryptographic-algorithm-enumeration"]
keywords: ["NIST key type", "SP 800-57", "key classification", "signature key", "encryption key", "key agreement", "authorization key", "42013A", "NISTKeyType"]
tag_hex: "42013A"
xml_text: "NISTKeyType"
tag_type: "Enumeration"
---

# NIST Key Type Enumeration

## Overview

The NIST Key Type enumeration classifies a cryptographic key according to the functional categories defined in NIST Special Publication 800-57 Part 1, which provides recommendations for cryptographic key management. SP 800-57 classifies keys by their purpose — signature, authentication, encryption, key wrapping, key agreement, random number generation, master key, or authorisation — and distinguishes private from public from symmetric variants of each. This classification informs key management policy decisions: different key types have different recommended lifetimes, storage requirements, and access controls. The enumeration appears in the [NIST Key Type attribute](../attributes/nist-key-type.md).

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Private signature key | `00000001` | `PrivateSignatureKey` |  |
| Public signature verification key | `00000002` | `PublicSignatureVerificationKey` |  |
| Symmetric authentication key | `00000003` | `SymmetricAuthenticationKey` |  |
| Private authentication key | `00000004` | `PrivateAuthenticationKey` |  |
| Public authentication key | `00000005` | `PublicAuthenticationKey` |  |
| Symmetric data encryption key | `00000006` | `SymmetricDataEncryptionKey` |  |
| Symmetric key wrapping key | `00000007` | `SymmetricKeyWrappingKey` |  |
| Symmetric random number generation key | `00000008` | `SymmetricRandomNumberGenerationKey` |  |
| Symmetric master key | `00000009` | `SymmetricMasterKey` |  |
| Private key transport key | `0000000A` | `PrivateKeyTransportKey` |  |
| Public key transport key | `0000000B` | `PublicKeyTransportKey` |  |
| Symmetric key agreement key | `0000000C` | `SymmetricKeyAgreementKey` |  |
| Private static key agreement key | `0000000D` | `PrivateStaticKeyAgreementKey` |  |
| Public static key agreement key | `0000000E` | `PublicStaticKeyAgreementKey` |  |
| Private ephemeral key agreement key | `0000000F` | `PrivateEphemeralKeyAgreementKey` |  |
| Public ephemeral key agreement key | `00000010` | `PublicEphemeralKeyAgreementKey` |  |
| Symmetric authorization key | `00000011` | `SymmetricAuthorizationKey` |  |
| Private authorization key | `00000012` | `PrivateAuthorizationKey` |  |
| Public authorization key | `00000013` | `PublicAuthorizationKey` |  |

**Signature keys:**
- **Private Signature Key**: An asymmetric private key used to generate digital signatures (RSA, DSA, ECDSA, EdDSA). Must be strongly protected; exposure compromises all previously signed material.
- **Public Signature Verification Key**: The corresponding asymmetric public key used to verify signatures. May be widely distributed.

**Authentication keys:**
- **Symmetric Authentication Key**: A symmetric key (e.g., HMAC key) used to generate and verify message authentication codes.
- **Private Authentication Key**: An asymmetric private key used in authentication protocols.
- **Public Authentication Key**: The corresponding public key for asymmetric authentication.

**Data encryption keys:**
- **Symmetric Encryption Key**: A symmetric key (e.g., AES) used directly to encrypt and decrypt data. These keys require strong access controls and short active lifetimes in high-volume environments.

**Key management keys:**
- **Symmetric Key Wrapping Key**: A symmetric key used to encrypt other keys for storage or transport (a Key Encryption Key). Typically has longer lifetimes and higher access restrictions than data encryption keys.
- **Symmetric Master Key**: A root key from which other keys are derived or protected. Examples include HSM Master Keys and Key Encryption Keys at the top of a hierarchy.

**Random number and derivation keys:**
- **Symmetric Random Number Generation Key**: A key used as seed material for a DRBG or PRNG, ensuring reproducibility of the random stream.

**Key agreement keys:**
- **Private Key Agreement Key**: An asymmetric private key used in a key agreement protocol (e.g., ECDH private key).
- **Public Key Agreement Key**: The corresponding public key shared with the peer during key agreement.

**Authorisation keys:**
- **Symmetric Authorization Key**: A symmetric key used to protect authorisation data or access tokens.
- **Private Authorization Key**: An asymmetric private key used in authorisation schemes.
- **Public Authorization Key**: The corresponding public key.

## Examples

An AES-256 key used by a database to encrypt columns is classified as **Symmetric Encryption Key** with an SP 800-57 recommended active lifetime of 2 years. The AES-256 key that wraps it in the HSM is a **Symmetric Key Wrapping Key** with a longer recommended lifetime and higher protection requirements.

## Related

- [NIST Key Type attribute](../attributes/nist-key-type.md) — the attribute that stores this enumeration on a key object
- [Cryptographic Usage Mask attribute](../attributes/cryptographic-usage-mask.md) — records permitted operations, which should be consistent with the key type
- [Cryptographic Algorithm Enumeration](cryptographic-algorithm-enumeration.md) — the algorithm that implements the key type's purpose
