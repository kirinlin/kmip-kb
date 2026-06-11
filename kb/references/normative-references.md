---
title: Normative References
category: reference
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "1.3"
v1_source_section: "1.2"
status: draft
related: ["non-normative-references", "terminology"]
keywords: ["normative references", "RFC", "NIST", "FIPS", "PKCS", "ANSI X9"]
---

# Normative References

## Summary

Documents the 1.4 spec depends on normatively — conforming implementations
inherit requirements from them. They cluster into NIST/FIPS standards, IETF
RFCs, RSA PKCS documents, ANSI X9 financial-industry standards, and the
companion KMIP profiles document.

## Entries

By cluster (citation keys as used in the spec):

- **Companion document**: [KMIP-Prof] — KMIP Profiles 1.4, which carries the
  conformance and transport-security requirements
  (see [profiles](../profiles/index.md)).
- **NIST FIPS**: [FIPS180-4] SHS, [FIPS186-4] DSS, [FIPS197] AES,
  [FIPS198-1] HMAC, [FIPS202] SHA-3.
- **NIST Special Publications**: [SP800-38A/B/C/D/E] block-cipher modes
  (CBC/CTR, CMAC, CCM, GCM, XTS), [SP800-56A] key establishment,
  [SP800-57-1] key-management recommendations (lifecycle model behind
  [State](../attributes/state.md)), [SP800-108] KDFs.
- **IETF RFCs**: 1319/1320/1321 (MD2/MD4/MD5), 1421/1424 (PEM), 2104 (HMAC),
  2119 (keywords), 2898 (PBKDF2), 2986 (PKCS#10), 3447 (RSA), 3629 (UTF-8,
  the Text String encoding), 3686 (AES-CTR), 4210/4211 (CMP/CRMF), 4880
  (OpenPGP), 4949 (security glossary), 5272 (CMC), 5280/6818 (X.509 PKI),
  5639 (Brainpool curves), 5958 (asymmetric key packages), 6402 (CMC
  updates).
- **RSA PKCS**: #1 (RSA), #5 (password-based crypto), #8 (private-key
  syntax), #10 (certification requests) — these define several
  [Key Format Types](../ttlv/key-block.md).
- **ANSI X9 / ISO**: X9.24-1 (retail key management), X9.31, X9.42 (DH),
  X9.62 (ECDSA), X9.63 (EC key agreement), X9.102 (key wrapping), X9 TR-31
  (interoperable key blocks; source of the Key Role Types in
  [Cryptographic Parameters](../attributes/cryptographic-parameters.md)),
  ISO 16609 and ISO/IEC 9797-1 (banking MACs).
- **Curves and ciphers**: [SEC2] curve parameters, [ECC-Brainpool],
  [CHACHA] and [POLY1305] (algorithms added to the 1.4 enumeration),
  [X.509] ITU-T, [IEEE1003-1] POSIX time (the Date-Time encoding).

## External References

All entries resolve to public documents; URLs are listed in v2.1 §1.3 of the
mirrored spec. For the references that only inform rather than bind, see
[Non-Normative References](non-normative-references.md).
