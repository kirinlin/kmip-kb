---
title: Cryptographic Usage Mask
category: attribute
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4.17"
v1_source_section: "3.19"
status: draft
related: ["cryptographic-algorithm", "state", "usage-limits", "operation-policy-name"]
keywords: ["usage mask", "bitmask", "encrypt", "sign", "wrap key", "key usage"]
---

# Cryptographic Usage Mask

## Purpose

Declares what the key is *allowed to do*: a bit per permitted function.
Servers enforce it on their own cryptographic operations (an
[Encrypt](../operations/encrypt.md) with a key lacking the Encrypt bit
fails), and clients are expected to honor it for operations they perform
locally.

## Data Type & Structure

An Integer bitmask. Bits defined in 1.4, with their hex values:

Sign (1), Verify (2), Encrypt (4), Decrypt (8), Wrap Key (10), Unwrap Key
(20), Export (40), MAC Generate (80), MAC Verify (100), Derive Key (200),
Content Commitment / non-repudiation (400), Key Agreement (800), Certificate
Sign (1000), CRL Sign (2000), Generate Cryptogram (4000), Validate Cryptogram
(8000), Translate Encrypt/Decrypt/Wrap/Unwrap (10000–80000).

The list deliberately covers X.509 Key Usage: digitalSignature maps to
Sign/Verify, keyEncipherment to Wrap/Unwrap Key, dataEncipherment to
Encrypt/Decrypt, keyAgreement, keyCertSign, and cRLSign map to their
namesakes, encipherOnly/decipherOnly to Encrypt/Decrypt. Extended Key Usage
has no mapping.

## Constraints

- Always present on cryptographic objects; single instance.
- Modifiable by the server only; clients cannot change or delete it after
  creation. Different clients may even be shown different values, per server
  policy.
- Pair bits sensibly: a key for AES-GCM data encryption typically gets
  Encrypt|Decrypt; a KEK gets Wrap Key|Unwrap Key; mixing signing and
  encryption bits on one key is poor practice the protocol does not forbid.

## Applies To (Object Types)

All cryptographic objects (and formerly templates).

## Set / Modified By

Initially set by client (in the create/register request) or server;
implicitly by every object-creating operation. Server-modifiable thereafter.

## Related Attributes

[State](state.md) · [Usage Limits](usage-limits.md) ·
[Cryptographic Algorithm](cryptographic-algorithm.md)
