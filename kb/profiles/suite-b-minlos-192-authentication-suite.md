---
title: Suite B minLOS\_192 Authentication Suite
category: profile
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4"]
source_section: "prof-3.4"
status: draft
related: ["suite-b-profiles", "suite-b-minlos-128-authentication-suite", "tls-1-2-authentication-suite", "basic-authentication-suite"]
keywords: ["Suite B", "minLOS_192", "TLS", "ECDSA-384", "AES-256-GCM", "P-384", "cipher suite", "NSA", "TOP SECRET"]
---

# Suite B minLOS\_192 Authentication Suite

## Overview

The Suite B minLOS_192 Authentication Suite specifies the TLS configuration required when two KMIP peers communicate at a minimum level of security of 192 bits — the level required for TOP SECRET-classified material under U.S. NSA policy [CNSSP-15]. It is the stricter counterpart to the [Suite B minLOS_128 Authentication Suite](suite-b-minlos-128-authentication-suite.md): where minLOS_128 allows flexibility between P-256 and P-384, minLOS_192 mandates P-384 exclusively with no fallback.

## Protocol and Cipher Suite

Both peers must use TLS v1.2. The mandatory cipher suite is:

```
TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
```

This provides forward secrecy (ECDHE), ECDSA mutual authentication, AES-256-GCM confidentiality, and SHA-384 integrity — Column 2 primitives throughout.

## Certificate Requirements

Both client and server must present X.509 certificates compliant with the RFC 5759 Suite B Certificate and CRL Profile, containing an elliptic curve public key with the digital signature key usage bit set. As with minLOS_128, RSA certificates are not accepted.

## Authentication — No Size Flexibility

Unlike minLOS_128, minLOS_192 requires ECDSA-384 (P-384 + SHA-384) from **both** the client and the server. There is no allowance for one party to use ECDSA-256 while the other uses ECDSA-384. Both parties must be able to verify ECDSA-384 signatures; ECDSA-256 verification is not required.

## Client Authenticity and Port

Client authenticity handling and port assignment follow the same rules as the standard TLS 1.2 Authentication Suite (KMIP-Prof §3.2.3 and §3.2.4 respectively), requiring mutual certificate-based authentication on port 5696.

## Implications for Implementers

- The total absence of P-256 options means deployments cannot gradually migrate from 256-bit to 384-bit keys while maintaining minLOS_192 compliance. All certificates and TLS material must already be at the P-384 level before a session can be established.
- AES-256-GCM is the only acceptable symmetric cipher for the TLS record layer. Implementations that negotiate AES-128 as a fallback must disable that behaviour in minLOS_192 contexts.
- Because both authentication tiers share the same base TLS 1.2 infrastructure and port, a server supporting both minLOS_128 and minLOS_192 sessions must select the appropriate cipher suite and certificate based on the classification level of the connecting client — typically driven by client certificate inspection.

## Related Concepts

[Suite B Profiles](suite-b-profiles.md) ·
[Suite B minLOS_128 Authentication Suite](suite-b-minlos-128-authentication-suite.md) ·
[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md)
