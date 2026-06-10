---
title: Signature Data
category: ttlv
spec_version: "1.4"
spec_versions: ["1.2", "1.3", "1.4"]
source_section: "2.1.12"
status: draft
related: ["data", "mac-data", "digital-signature-algorithm"]
keywords: ["signature data", "sign", "signature verify", "digital signature bytes"]
---

# Signature Data

## Overview

The signature bytes exchanged by [Sign](../operations/sign.md) (output) and
[Signature Verify](../operations/signature-verify.md) (input). Kept distinct
from [Data](data.md) so a verify request can carry both the original message
and the signature unambiguously.

## Encoding (Tag / Type / Length / Value)

Tag `4200C3`, Byte String. The signature format follows the algorithm in
play (e.g. PKCS#1 v1.5 block, ECDSA r‖s per the negotiated convention) —
KMIP does not re-encode it.

## Fields & Structure

Opaque bytes. The signing scheme comes from
[Cryptographic Parameters](../attributes/cryptographic-parameters.md) — a
[Digital Signature Algorithm](../attributes/digital-signature-algorithm.md)
value, or an algorithm + hashing-algorithm pair. In streaming mode the
signature appears only on the final part.

## Examples

Signature Verify request: key identifier, Cryptographic Parameters
(ECDSA with SHA-256), Data = the message, Signature Data = the 64-byte ECDSA
signature. Response: Validity Indicator = Valid.

## Related

[Data](data.md) · [Sign](../operations/sign.md) ·
[Signature Verify](../operations/signature-verify.md)
