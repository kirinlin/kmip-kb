---
title: Suite B minLOS\_128 Authentication Suite
category: profile
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4"]
source_section: "prof-3.3"
status: draft
related: ["suite-b-profiles", "suite-b-minlos-192-authentication-suite", "tls-1-2-authentication-suite", "basic-authentication-suite"]
keywords: ["Suite B", "minLOS_128", "TLS", "ECDSA-256", "AES-128-GCM", "P-256", "cipher suite", "NSA"]
---

# Suite B minLOS\_128 Authentication Suite

## Overview

The Suite B minLOS_128 Authentication Suite specifies the TLS configuration required when two KMIP peers communicate at a minimum level of security of 128 bits — the level adequate for SECRET-classified material under U.S. NSA policy [CNSSP-15]. It is more constrained than the standard [TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md) in its cipher suite and certificate requirements, but offers some flexibility between P-256 and P-384 ECDSA for client authentication.

## Protocol and Cipher Suite

Both peers must use TLS v1.2. The mandatory cipher suite is:

```
TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
```

This provides forward secrecy (ECDHE), ECDSA mutual authentication, AES-128-GCM confidentiality, and SHA-256 integrity.

## Certificate Requirements

Both client and server must present X.509 certificates compliant with the RFC 5759 Suite B Certificate and CRL Profile. Each certificate must contain an elliptic curve public key with the digital signature key usage bit set. RSA certificates — even from an otherwise trusted CA — are not acceptable in Suite B connections.

## Client Authentication Flexibility

At minLOS_128, ECDSA-256 (P-256 + SHA-256) and ECDSA-384 (P-384 + SHA-384) are both valid for mutual authentication. Crucially, the client and server may use different sizes — a client authenticating with ECDSA-256 may connect to a server using ECDSA-384 and vice versa. This asymmetry is intentional: it accommodates mixed-age deployments where some endpoints have been upgraded to 384-bit keys while others have not.

All minLOS_128 implementations must be able to verify ECDSA-256 signatures; verifying ECDSA-384 is recommended but not required.

## Client Authenticity and Port

Client authenticity handling and port assignment follow the same rules as the standard TLS 1.2 Authentication Suite (KMIP-Prof §3.2.3 and §3.2.4 respectively), which require mutual certificate-based authentication and use port 5696.

## Implications for Implementers

- The cipher suite mandates ECDHE key exchange — static ECDH is not sufficient. Implementations that cache or reuse key agreement material must ensure proper ECDHE ephemerality.
- Permitting mixed ECDSA sizes (256 vs. 384) simplifies rollover when renewing long-lived certificates, but both peers must be configured to accept both sizes; a server that rejects ECDSA-256 client certificates would be non-conformant for minLOS_128.
- This authentication suite applies to both the minLOS_128 key management profile and any minLOS_128-configured KMIP session; it does not apply to minLOS_192 sessions, which must use the stronger [Suite B minLOS_192 Authentication Suite](suite-b-minlos-192-authentication-suite.md).

## Related Concepts

[Suite B Profiles](suite-b-profiles.md) ·
[Suite B minLOS_192 Authentication Suite](suite-b-minlos-192-authentication-suite.md) ·
[TLS 1.2 Authentication Suite](tls-1-2-authentication-suite.md)
