---
title: Versions
category: index
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4"]
source_section: ""
status: draft
related: []
keywords: ["versions", "TOC", "1.0", "1.1", "1.2", "1.3", "1.4", "deltas"]
---

# Versions

Machine-readable per-version section maps, plus delta notes between the 1.x
releases.

- [1.4-toc.yaml](1.4-toc.yaml) — 157 sections. Regenerate with
  `python scripts/build_kb_scaffold.py --toc-only`.
- [1.3-toc.yaml](1.3-toc.yaml) — 143 sections. Regenerate with
  `python scripts/build_kb_scaffold.py --version 1.3 --toc-only`.
- [1.2-toc.yaml](1.2-toc.yaml) — 134 sections. Regenerate with
  `python scripts/build_kb_scaffold.py --version 1.2 --toc-only`.
- [1.1-toc.yaml](1.1-toc.yaml) — 112 sections. Regenerate with
  `python scripts/build_kb_scaffold.py --version 1.1 --toc-only`.
- [1.0-toc.yaml](1.0-toc.yaml) — 104 sections. Regenerate with
  `python scripts/build_kb_scaffold.py --version 1.0 --toc-only`.

## Changes per release

Each page carries a `spec_versions` front-matter list that records exactly
which 1.x releases include the feature.

### 1.1

Primarily expanded certificate management and added two new operations.

- *New X.509 certificate attributes* (§3.9–12, §3.16, §3.34): the generic
  [Certificate Identifier](../attributes/certificate-identifier.md),
  [Certificate Subject](../attributes/certificate-subject.md), and
  [Certificate Issuer](../attributes/certificate-issuer.md) attributes
  (§3.13–15) are deprecated; replacements are the X.509-specific
  [X.509 Certificate Identifier](../attributes/x-509-certificate-identifier.md),
  [X.509 Certificate Subject](../attributes/x-509-certificate-subject.md),
  and [X.509 Certificate Issuer](../attributes/x-509-certificate-issuer.md).
  [Certificate Length](../attributes/certificate-length.md),
  [Digital Signature Algorithm](../attributes/digital-signature-algorithm.md),
  and [Fresh](../attributes/fresh.md) are also new.
- *New operations*: [Discover Versions](../operations/discover-versions.md)
  (§4.26) lets a client negotiate the highest mutually-supported protocol
  version; [Re-key Key Pair](../operations/re-key-key-pair.md) (§4.5) adds
  asymmetric-key rotation alongside the existing Re-key for symmetric keys.
- *Extension Information* (§2.1.9): new base-object structure carrying
  vendor-extension metadata, returned by Query.
- *Encoding Option*: new field in
  [Key Wrapping Data](../ttlv/key-wrapping-data.md) and
  [Key Wrapping Specification](../ttlv/key-wrapping-specification.md) that
  specifies how the wrapped key-value bytes are encoded.

### 1.2

The largest single release, adding cryptographic service operations, split-key
management, PGP key objects, and attestation.

- *Cryptographic service operations* (§4.29–37): eleven new client-to-server
  operations — [Encrypt](../operations/encrypt.md) and
  [Decrypt](../operations/decrypt.md), [Sign](../operations/sign.md) and
  [Signature Verify](../operations/signature-verify.md),
  [MAC](../operations/mac.md) and [MAC Verify](../operations/mac-verify.md),
  [RNG Retrieve](../operations/rng-retrieve.md) and
  [RNG Seed](../operations/rng-seed.md), [Hash](../operations/hash.md).
- *Split-key operations* (§4.38–39): [Create Split Key](../operations/create-split-key.md)
  and [Join Split Key](../operations/join-split-key.md) support
  threshold-based secret sharing.
- *PGP Key object* (§2.2.9): [PGP Key](../objects/pgp-key.md) is a new
  managed object type alongside symmetric keys, asymmetric key pairs, and
  certificates.
- *Crypto-operation structures* (§2.1.10–14): five new base objects supporting
  the new crypto operations — [Data](../ttlv/data.md),
  [Data Length](../ttlv/data-length.md),
  [Signature Data](../ttlv/signature-data.md),
  [MAC Data](../ttlv/mac-data.md), and
  [Nonce](../ttlv/nonce.md) (used as an attestation challenge).
- *New attributes* (§3.40–43):
  [Alternative Name](../attributes/alternative-name.md),
  [Key Value Present](../attributes/key-value-present.md),
  [Key Value Location](../attributes/key-value-location.md), and
  [Original Creation Date](../attributes/original-creation-date.md).
- *Attestation* (§6.17): an Attestation credential type allows a client to
  present a hardware/software measurement or third-party assertion instead of
  a password. The server issues a [Nonce](../ttlv/nonce.md) challenge; the
  client responds with an Attestation Credential containing either an
  Attestation Measurement or Attestation Assertion. The new
  [Attestation Capable Indicator](../ttlv/attestation-capable-indicator.md)
  message-header flag advertises whether the client supports attestation.
  Query gains a "Query Attestation Types" function to discover which
  attestation methods a server accepts.

### 1.3

Streaming multi-part operations, server-to-client Query, richer server
capability reporting, and several deprecations clearing the path toward 1.4.

- *Streaming crypto* (§2.1.15–17): [Correlation Value](../ttlv/correlation-value.md),
  [Init Indicator](../ttlv/init-indicator.md), and
  [Final Indicator](../ttlv/final-indicator.md) link the batch items of a
  multi-part Encrypt/Decrypt/Sign/MAC sequence into a single logical session.
- *Capability reporting* (§2.1.18–21): four new structures returned by the
  §4.25 Query response —
  [RNG Parameters](../ttlv/rng-parameters.md) describes a random-number
  generator; [Profile Information](../ttlv/profile-information.md),
  [Validation Information](../ttlv/validation-information.md), and
  [Capability Information](../ttlv/capability-information.md) let servers
  advertise their conformance and operational limits in machine-readable form.
- *Random Number Generator attribute* (§3.44): records which RNG was used
  when a managed object was created (see
  [Random Number Generator](../attributes/random-number-generator.md)).
- *Server-to-client Query* (§5.3): the server can now ask a client which
  profiles and capabilities it supports, symmetric to the existing
  client-to-server §4.25 Query (see
  [server-to-client/query](../operations/server-to-client/query.md)).
- *Deprecations*: the [Template](../objects/template.md) managed object and
  the Operation Policy Name attribute (§3.18) are both deprecated — callers
  should use individual Template-Attribute elements instead. The legacy
  Transparent ECDSA/ECDH/ECMQV Private/Public Key structures are deprecated
  in favor of the unified Transparent EC Private/Public Key forms.

### 1.4

Import/Export, AEAD fields, client/server correlation values, PKCS#12,
Sensitive/Always Sensitive, Extractable/Never Extractable, Description and
Comment, Key Wrap Type, Mask Generator parameters.
