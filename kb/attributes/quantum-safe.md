---
title: Quantum Safe
category: attribute
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "4.45"
status: reviewed
related: ["cryptographic-algorithm", "cryptographic-length", "nist-key-type", "protection-level"]
keywords: ["quantum safe", "post-quantum", "quantum resistant", "pqc", "quantum computer", "boolean attribute", "420147", "QuantumSafe"]
tag_hex: "420147"
xml_text: "QuantumSafe"
---

# Quantum Safe

## Purpose

Quantum Safe is a Boolean attribute that signals whether the cryptographic algorithm and parameter choices associated with an object are considered resistant to attacks from a cryptographically-relevant quantum computer. It provides a simple machine-readable flag for policy engines and audit tools that need to identify and segregate post-quantum-capable objects from those that are not, without requiring those systems to independently evaluate algorithm and key-length combinations.

## Data Type & Structure

A Boolean. When `true`, the object's associated algorithm — whether the key's own algorithm or the algorithm used to protect it — is considered quantum-safe by the server or the registering client. When `false` or absent, no such assurance is made.

## Constraints

Single-instance. Optional. The attribute is informational: KMIP does not define the specific algorithm or parameter criteria for quantum safety, leaving that determination to the registering party or server policy. Implementers should document their criteria for setting this attribute to avoid ambiguity between clients and servers.

## Applies To (Object Types)

[Symmetric Key](../objects/symmetric-key.md), [Public Key](../objects/public-key.md), [Private Key](../objects/private-key.md), [Secret Data](../objects/secret-data.md), and [Certificate](../objects/certificate.md).

## Set / Modified By

Client at creation or registration. May be set or updated via [Set Attribute](../operations/set-attribute.md). Servers may override based on their own algorithm policy.

## Related Attributes

[Cryptographic Algorithm](cryptographic-algorithm.md) · [Cryptographic Length](cryptographic-length.md) · [NIST Key Type](nist-key-type.md) · [Protection Level](protection-level.md)
