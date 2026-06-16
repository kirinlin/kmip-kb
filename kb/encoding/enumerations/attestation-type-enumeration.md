---
title: Attestation Type Enumeration
category: encoding
spec_version: "2.1"
spec_versions: ["1.2","1.3","1.4","2.0","2.1"]
source_section: "11.4"
status: reviewed
related: ["credential-type-enumeration", "login"]
keywords: ["attestation", "TPM", "TCG", "SAML", "credential", "authentication", "hardware trust", "4200C7", "AttestationType"]
tag_hex: "4200C7"
xml_text: "AttestationType"
---

# Attestation Type Enumeration

## Overview

The Attestation Type enumeration identifies the format and origin of an attestation credential, which is a proof provided by a client that its hardware or software environment is in a known-good state. Attestation-based authentication is used in environments where the server needs assurance not just that the client knows a secret, but that the client is running on trustworthy hardware or a verified software stack. The type tells the server which verification method and trust chain to apply when evaluating the credential.

## Fields & Structure

| Value | Hex | XML Text | Description |
|---|---|---|---|
| TPM Quote | `0x00000001` | `TPMQuote` |  |
| TCG Integrity Report | `0x00000002` | `TCGIntegrityReport` |  |
| SAML Assertion | `0x00000003` | `SAMLAssertion` |  |

- **TPM Quote**: An attestation produced by a Trusted Platform Module, in which the TPM signs a selection of Platform Configuration Register (PCR) values that describe the platform's measured boot state. Relying parties can verify the quote using the TPM's endorsement key certificate.
- **TCG Integrity Report**: A broader report format defined by the Trusted Computing Group that can aggregate measurements from multiple components of a platform's boot and runtime environment, often expressed as an XML or binary report.
- **SAML Assertion**: A Security Assertion Markup Language assertion issued by a trusted Identity Provider or attestation service. The SAML token carries attributes and conditions that the KMIP server can verify against a trusted IdP certificate.

## Examples

A storage array client that needs to prove it is running trusted firmware before receiving encryption keys might include a **TPM Quote** in its Authentication header. The KMIP server verifies the TPM signature and PCR values against an expected baseline before processing the request.

## Related

- [Credential Type Enumeration](credential-type-enumeration.md) — the enumeration that selects the credential format, of which Attestation is one option
- [Login operation](../../operations/login.md) — session establishment that may leverage attestation credentials
