---
title: Non-Normative References
category: reference
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "1.4"
v1_source_section: "1.3"
status: draft
related: ["normative-references", "terminology"]
keywords: ["non-normative references", "usage guide", "test cases", "Shamir"]
---

# Non-Normative References

## Summary

Background material the spec cites for context rather than as binding
requirements. The two most useful entries for implementers are the other
members of the KMIP 1.4 document family: the Usage Guide and the Test Cases.

## Entries

- **[KMIP-UG]** — KMIP Usage Guide 1.4: rationale, deployment guidance, and
  worked explanations that the terse spec omits. The best companion when a
  spec section is ambiguous.
- **[KMIP-TC]** — KMIP Test Cases 1.4: complete request/response message
  transcripts used for interoperability testing; invaluable as encoding
  ground truth for [TTLV](../ttlv/ttlv-encoding.md) implementations.
- **[w1979]** — Shamir, "How to share a secret" (1979): the polynomial
  secret-sharing scheme behind [Split Key](../objects/split-key.md) methods.
- **[RFC6151]** — security considerations for MD5/HMAC-MD5; context for why
  those algorithms, though present in the enumerations, are discouraged.
- **[RFC7292]** — PKCS#12, backing the PKCS#12 key format type and
  [friendly-name attribute](../attributes/pkcs-12-friendly-name.md) added in
  1.4.
- **[ISO/IEC 9945-2]** — regular expressions (Single UNIX Specification),
  cited for pattern-matching semantics.

## External References

URLs for each entry are in v2.1 §1.4 of the mirrored spec. The normative
counterparts live in [Normative References](normative-references.md).
