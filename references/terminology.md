---
title: Terminology
category: reference
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "1.1"
status: draft
related: ["normative-references", "non-normative-references"]
keywords: ["terminology", "definitions", "glossary", "RFC 2119", "SP 800-57"]
---

# Terminology

## Summary

Spec §1.1 does two jobs: it imports the RFC 2119 keyword conventions (SHALL,
SHOULD, MAY, ...) that give the document its normative force, and it defines
a glossary of cryptographic terms, most of them aligned with NIST SP 800-57
Part 1. Definitions not found in the spec are deferred to SP 800-57.

## Entries

The glossary terms, grouped by theme (paraphrased — consult §1.1 for the
normative wording):

- **Key material and algorithms** — *symmetric key* (one secret key used for
  an operation and its inverse), *asymmetric key pair* (public + private
  key), *cryptographic key/algorithm*, *public key cryptographic algorithm*,
  *digital signature (algorithm)*, *hashing algorithm/digest*, *MAC*
  (symmetric-key checksum detecting modification), *key derivation*, *key
  wrapping* (encrypting and/or MACing/signing a key), *split key* (n
  components, k of which reconstruct the secret while k−1 reveal nothing).
- **PKI** — *public key certificate*, *X.509 certificate* (the public-key
  flavor, DER-encoded), *certification authority*, *Public Key
  Infrastructure*, *certificate length*, *PGP key* (RFC 4880 container).
- **Security properties** — *authentication*, *authorization*,
  *confidentiality*, *integrity*, *compromise* (unauthorized disclosure or
  use of sensitive data), *ciphertext/encryption/decryption*.
- **Lifecycle and management** — *key management* (handling keying material
  across its whole life), *archive* (move to long-term storage), *recover*
  (bring back from archive), *profile* (a named bundle of objects,
  attributes, operations, and authentication requirements for a usage
  context).

This knowledge base uses the same vocabulary throughout; per-concept pages
(e.g. [State](../attributes/state.md),
[Key Block](../ttlv/key-block.md)) carry the operational detail.

## External References

- RFC 2119 — requirement keywords.
- NIST SP 800-57 Part 1 — the source for most definitions.
- Appendix E of the 1.4 spec — acronym list.
