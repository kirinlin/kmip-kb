---
title: Attributes
category: index
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "4"
v1_source_section: "3"
status: reviewed
related: ["unique-identifier", "state", "cryptographic-algorithm", "cryptographic-usage-mask"]
keywords: ["attributes", "metadata", "attribute rules", "multi-instance", "lifecycle dates", "420125"]
tag_hex: "420125"
xml_text: "Attributes"
tag_type: "Structure"
---

# Attributes

The metadata KMIP keeps about every managed object (v2.1 §4; v1.x §3). Attributes are
read with [Get Attributes](../operations/get-attributes.md) /
[Get Attribute List](../operations/get-attribute-list.md) and written with
[Add](../operations/add-attribute.md) /
[Modify](../operations/modify-attribute.md) /
[Delete Attribute](../operations/delete-attribute.md), within per-attribute
rules: who may set it, whether it can change, whether multiple instances may
exist, and which operations set it implicitly. On the wire each one travels
in an [Attribute structure](../structures/attribute.md) (name + optional index +
value).

## Identity

[Unique Identifier](unique-identifier.md) ·
[Short Unique Identifier](short-unique-identifier.md) (2.1) · [Name](name.md) ·
[Alternative Name](alternative-name.md) · [Object Type](object-type.md)

## Cryptographic description

[Cryptographic Algorithm](cryptographic-algorithm.md) ·
[Cryptographic Length](cryptographic-length.md) ·
[Cryptographic Parameters](cryptographic-parameters.md) ·
[Cryptographic Domain Parameters](cryptographic-domain-parameters.md) ·
[Digest](digest.md) ·
[Random Number Generator](random-number-generator.md) (1.3+) ·
[Key Format Type](key-format-type.md) (2.1) ·
[NIST Key Type](nist-key-type.md) (2.1) ·
[Quantum Safe](quantum-safe.md) (2.1)

## Certificates

[Certificate Type](certificate-type.md) ·
[Certificate Length](certificate-length.md) (1.1+) ·
[X.509 Certificate Identifier](x-509-certificate-identifier.md) /
[Subject](x-509-certificate-subject.md) /
[Issuer](x-509-certificate-issuer.md) (1.1+) ·
[Digital Signature Algorithm](digital-signature-algorithm.md) (1.1+) ·
[Certificate Attributes](certificate-attributes.md) (2.1) ·
deprecated 1.0 forms: [Certificate Identifier](certificate-identifier.md) ·
[Certificate Subject](certificate-subject.md) ·
[Certificate Issuer](certificate-issuer.md)

## Usage policy

[Cryptographic Usage Mask](cryptographic-usage-mask.md) ·
[Usage Limits](usage-limits.md) · [Lease Time](lease-time.md) ·
[Operation Policy Name](operation-policy-name.md) (deprecated 1.3) ·
1.4 protection flags: [Sensitive](sensitive.md) /
[Always Sensitive](always-sensitive.md) ·
[Extractable](extractable.md) / [Never Extractable](never-extractable.md)

## Lifecycle

[State](state.md) · [Initial Date](initial-date.md) ·
[Activation Date](activation-date.md) ·
[Process Start Date](process-start-date.md) ·
[Protect Stop Date](protect-stop-date.md) ·
[Deactivation Date](deactivation-date.md) ·
[Destroy Date](destroy-date.md) ·
[Compromise Occurrence Date](compromise-occurrence-date.md) ·
[Compromise Date](compromise-date.md) ·
[Revocation Reason](revocation-reason.md) ·
[Archive Date](archive-date.md) ·
[Original Creation Date](original-creation-date.md) (1.2+) ·
[Last Change Date](last-change-date.md) · [Fresh](fresh.md) (1.1+)

## Organization & application data

[Object Group](object-group.md) · [Link](link.md) ·
[Application Specific Information](application-specific-information.md) ·
[Contact Information](contact-information.md) ·
[Description](description.md) / [Comment](comment.md) (1.4) ·
[Custom Attribute](custom-attribute.md) ·
[Key Value Present](key-value-present.md) /
[Key Value Location](key-value-location.md) (1.2+) ·
[PKCS#12 Friendly Name](pkcs-12-friendly-name.md) (1.4) ·
[Opaque Data Type](opaque-data-type.md) (2.1)

## Protection storage (2.1)

[Protection Level](protection-level.md) ·
[Protection Period](protection-period.md) ·
[Protection Storage Mask](protection-storage-mask.md)

## Key rotation (2.1)

[Rotate Automatic](rotate-automatic.md) · [Rotate Date](rotate-date.md) ·
[Rotate Generation](rotate-generation.md) ·
[Rotate Interval](rotate-interval.md) · [Rotate Latest](rotate-latest.md) ·
[Rotate Name](rotate-name.md) · [Rotate Offset](rotate-offset.md)
