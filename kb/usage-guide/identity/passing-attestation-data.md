---
title: Passing Attestation Data
category: usage-guide
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "ug-3.58"
status: reviewed
related: ["authentication"]
keywords: ["attestation", "TPM", "nonce", "Attestation Credential", "integrity measurement", "freshness", "Attestation Capable Indicator"]
---

# Passing Attestation Data

## Overview

In some deployments, a KMIP server requires attestation — a verifiable integrity measurement of the client's environment — before honouring requests. KMIP supports a four-step attestation protocol that provides freshness (via a server-generated nonce) and integrity (via a measured assertion from the client or a trusted third party).

## Guidance

The attestation flow:

1. The client sets the **Attestation Capable Indicator** flag in the request header.
2. When attestation is required, the server replies with an "Attestation Required" error and provides a **Nonce** in the response header.
3. Client creates an **Attestation Credential Object** containing an integrity measurement (or a third-party assertion) that includes the server's nonce.
4. Client resubmits the request with the Attestation Credential in the request header. The server validates the measurement and the nonce, then completes the request.

If attestation fails (invalid measurement or nonce mismatch), the server returns "Attestation Failed." If the Attestation Capable Indicator was not set, the server returns "Permission Denied" without a nonce.

## Implementation Notes

Attestation frequency (every request, every N requests) is server-policy-defined, as is the nonce lifetime. Clients must handle the "Attestation Required" response as a non-fatal error that triggers the attestation sub-flow rather than as a permanent failure. Multiple Attestation Credentials may be required in a single request header when the server needs both attestation and another credential type.

## Related Concepts

See [Authentication](authentication.md) for the broader credential model.
