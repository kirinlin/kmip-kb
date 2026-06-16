---
title: Data Structures
category: index
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: ""
status: reviewed
related: ["key-block", "attribute", "key-wrapping-specification", "rng-parameters"]
keywords: ["data structures", "object data structures", "attribute data structures", "operations data structures", "key block"]
---

# Data Structures

Composite TTLV structures that serve as reusable building blocks across managed
objects, attributes, and operation payloads. These are the things the
[TTLV encoding](../encoding/index.md) serializes; the request/response envelope that
carries them lives under [Messages](../messages/index.md). Covers v2.1 §3
(Object Data Structures), §5 (Attribute Data Structures), and §7 (Operations
Data Structures); the v1.x base objects (§2.1) map here too.

## Object data structures (§3)

- [Key Block](key-block.md) → [Key Value](key-value.md) →
  [Transparent Key Structures](transparent-key-structures.md)
- [Key Wrapping Data](key-wrapping-data.md) — wrapped key metadata on a Key Block.

## Attribute data structures (§5)

- [Attribute](attribute.md) · [Attribute Reference](attribute-reference.md) ·
  [Current Attribute](current-attribute.md) · [New Attribute](new-attribute.md)
- [Common Attributes](common-attributes.md) ·
  [Private Key Attributes](private-key-attributes.md) ·
  [Public Key Attributes](public-key-attributes.md)
- [Template-Attribute Structures](template-attribute-structures.md)

## Operations data structures (§7)

### Key wrapping & derivation

- [Key Wrapping Specification](key-wrapping-specification.md) ·
  [Derivation Parameters](derivation-parameters.md)

### Cryptographic-service payload fields (1.2+)

- [Data](data.md) · [Data Length](data-length.md) ·
  [Signature Data](signature-data.md) · [MAC Data](mac-data.md)
- Streaming (1.3+): [Correlation Value](correlation-value.md) ·
  [Init Indicator](init-indicator.md) · [Final Indicator](final-indicator.md)
- AEAD (1.4): [Authenticated Encryption Additional Data](authenticated-encryption-additional-data.md) ·
  [Authenticated Encryption Tag](authenticated-encryption-tag.md)

### Discovery & defaults (1.3+)

- [RNG Parameters](rng-parameters.md) · [Profile Information](profile-information.md) ·
  [Profile Version](profile-version.md) · [Validation Information](validation-information.md) ·
  [Capability Information](capability-information.md) ·
  [Server Information](server-information.md)
- [Defaults Information](defaults-information.md) · [Object Defaults](object-defaults.md) ·
  [Extension Information](extension-information.md) (1.1+)

### Objects, groups & operations

- [Objects](objects.md) · [Object Groups](object-groups.md) ·
  [Object Types](object-types.md) · [Operations](operations.md)

### Constraints & limits

- [Constraint](constraint.md) · [Constraints](constraints.md) ·
  [Usage Limits](usage-limits.md) · [Protection Storage Masks](protection-storage-masks.md)

### Access control

- [Right](right.md) · [Rights](rights.md) · [Ticket](ticket.md)

### PKCS#11 interface (2.0+)

- [PKCS#11 Interface](pkcs-11-interface.md) · [PKCS#11 Function](pkcs-11-function.md) ·
  [PKCS#11 Input Parameters](pkcs-11-input-parameters.md) ·
  [PKCS#11 Output Parameters](pkcs-11-output-parameters.md) ·
  [PKCS#11 Return Code](pkcs-11-return-code.md)

### Interop & async

- [Interop Function](interop-function.md) · [Interop Identifier](interop-identifier.md)
- [Asynchronous Correlation Values](asynchronous-correlation-values.md) ·
  [Asynchronous Request](asynchronous-request.md)
- [Log Message](log-message.md)
