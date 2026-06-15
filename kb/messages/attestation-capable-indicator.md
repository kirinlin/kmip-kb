---
title: Attestation Capable Indicator
category: messages
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "9.3"
v1_source_section: "6.17"
status: reviewed
related: ["credential", "nonce", "result-reason"]
keywords: ["attestation capable indicator", "TPM", "attestation required", "request header", "4200D3", "AttestationCapableIndicator"]
tag_hex: "4200D3"
xml_text: "AttestationCapableIndicator"
---

# Attestation Capable Indicator

## Overview

A request-header flag (1.2+) declaring whether the client can produce an
Attestation [Credential](credential.md). It shapes how the server reacts when
policy demands attestation it did not receive: a capable client gets a
retryable `Attestation Required` (with a [Nonce](nonce.md) to attest over);
an incapable one gets a terminal `Permission Denied`.

## Encoding (Tag / Type / Length / Value)

Tag `4200D3`, Boolean, request header; absent means False.

## Fields & Structure

The header may also carry Attestation Type values (`4200C7`) listing the
evidence formats the client supports (TPM Quote, TCG Integrity Report, SAML
Assertion), letting the server pick one it can verify. Capability is also
discoverable out-of-band via
[Capability Information](../structures/capability-information.md).

## Examples

A client sets the indicator True and requests Get on an attestation-gated
key: the failure response carries Attestation Required plus a Nonce; the
client repeats the Get with an Attestation Credential and succeeds.

## Related

[Credential](credential.md) · [Nonce](nonce.md) ·
[Result Reason](result-reason.md)
