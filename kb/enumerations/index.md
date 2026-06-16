---
title: Enumerations
category: index
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "11"
v1_source_section: "11"
status: reviewed
related: ["object-type-enumeration", "operation-enumeration", "cryptographic-algorithm-enumeration", "state-enumeration", "result-status-enumeration", "result-reason-enumeration", "key-format-type-enumeration"]
keywords: ["enumerations", "named values", "TTLV", "integer encoding", "type codes"]
---

# Enumerations

Named value sets used throughout KMIP (§11). Each enumeration defines the
legal integer values for a specific TTLV-encoded field; on the wire these
are 4-byte big-endian integers with TTLV type `05` (`Enumeration`), except
for [Item Type](item-type-enumeration.md) which appears as the 1-byte TTLV
type field itself. In JSON and XML encodings each value is represented by
its text name.

## Encoding and protocol structure

- [Item Type](item-type-enumeration.md) — the 1-byte TTLV type field values:
  Structure, Integer, Long Integer, Big Integer, Enumeration, Boolean, Text
  String, Byte String, Date-Time, Interval, Date-Time Extended
- [Tag](tag-enumeration.md) — all 420xxx hex tag values assigned in the spec;
  a complete registry of every named TTLV field
- [Encoding Option](encoding-option-enumeration.md) — whether key material is
  stored with a TTLV wrapper or as raw bytes
- [Asynchronous Indicator](asynchronous-indicator-enumeration.md) — whether a
  request is synchronous, polling-based, or streaming

## Managed object types

- [Object Type](object-type-enumeration.md) — Symmetric Key, Public Key,
  Private Key, Split Key, Secret Data, Opaque Object, PGP Key, Certificate
  Request; appears in virtually every request and response
- [Certificate Type](certificate-type-enumeration.md) — X.509, PGP,
  XMSSCertificate
- [Certificate Request Type](certificate-request-type-enumeration.md) — CRMF,
  PKCS#10, PEM
- [Secret Data Type](secret-data-type-enumeration.md) — Password, Seed
- [Opaque Data Type](opaque-data-type-enumeration.md) — extension point for
  non-KMIP data stored on the server
- [Data](data-enumeration.md) — generic data type indicator

## Cryptographic algorithms

- [Cryptographic Algorithm](cryptographic-algorithm-enumeration.md) — AES, RSA,
  ECDSA, ECDH, ChaCha20, Ed25519, ML-KEM, ML-DSA, and many more; the primary
  algorithm selector
- [Hashing Algorithm](hashing-algorithm-enumeration.md) — SHA-1, SHA-256,
  SHA-384, SHA-512, SHA-3 family, RIPEMD-160
- [Digital Signature Algorithm](digital-signature-algorithm-enumeration.md) —
  DSA with SHA-1, RSA with SHA-256, ECDSA with SHA-384, etc.
- [Block Cipher Mode](block-cipher-mode-enumeration.md) — CBC, CFB, CTR, ECB,
  GCM, CCM, XTS, and others
- [Padding Method](padding-method-enumeration.md) — PKCS5, PKCS1v1.5, OAEP,
  PSS, SSL3, ANSI X9.23
- [Mask Generator](mask-generator-enumeration.md) — MGF1; the mask generation
  function used with OAEP and PSS
- [Recommended Curve](recommended-curve-enumeration.md) — P-192, P-224, P-256,
  P-384, P-521, brainpool curves, Curve25519, Curve448
- [Key Compression Type](key-compression-type-enumeration.md) — EC point format:
  uncompressed, compressed, hybrid
- [FIPS 186 Variation](fips186-variation-enumeration.md) — DSA key generation
  variants per FIPS 186
- [DRBG Algorithm](drbg-algorithm-enumeration.md) — Hash DRBG, HMAC DRBG,
  CTR DRBG, Dual EC DRBG
- [RNG Algorithm](rng-algorithm-enumeration.md) — FIPS 186-2, FIPS 186-3,
  X9.31, X9.62, ANSI X9.17
- [RNG Mode](rng-mode-enumeration.md) — Unspecified, Shared, Non-Shared,
  Non-Deterministic

## Key format and wrapping

- [Key Format Type](key-format-type-enumeration.md) — Raw, Opaque, PKCS#1,
  PKCS#8, X.509, ECPrivateKey, TransparentSymmetricKey, and more; controls
  the byte layout of extracted key material
- [Wrapping Method](wrapping-method-enumeration.md) — Encrypt, MAC/sign only,
  Encrypt then MAC/sign, MAC/sign then Encrypt, TR-31
- [Key Wrap Type](key-wrap-type-enumeration.md) — Not Wrapped, Wrapped;
  indicates whether the key value returned by Get is wrapped
- [Unwrap Mode](unwrap-mode-enumeration.md) — Unset, Processed, Not Processed;
  controls what the server does with a wrapped key on ingress

## Key purpose and derivation

- [Key Role Type](key-role-type-enumeration.md) — KEK, DEK, MAC, Master Key,
  IV, Nonce, etc.; classifies how the key is intended to be used
- [NIST Key Type](nist-key-type-enumeration.md) — key classification per
  NIST SP 800-57
- [Derivation Method](derivation-method-enumeration.md) — PBKDF2, HKDF, HKDF
  Expand, Hybrid, KDF/DES3, NIST 800-108-C KDF, AWS Signature V4, Hash, KMAC
- [Split Key Method](split-key-method-enumeration.md) — XOR, Polynomial Sharing
  GF(2^8), Polynomial Sharing Prime, Polynomial Sharing GF(2^16), Portable
  Secret Sharing

## Key lifecycle

- [State](state-enumeration.md) — Pre-Active, Active, Deactivated, Compromised,
  Destroyed, Destroyed Compromised; the lifecycle FSM every managed object
  traverses
- [Revocation Reason Code](revocation-reason-code-enumeration.md) — Unspecified,
  Key Compromise, CA Compromise, Affiliation Changed, Superseded, Cessation
  of Operation, Privilege Withdrawn
- [Destroy Action](destroy-action-enumeration.md) — Shred, Erase, Delete,
  Unrecoverable Shred; what to do with key material on Destroy
- [Shredding Algorithm](shredding-algorithm-enumeration.md) — DoD 5220.22-M,
  ITAR, NISP, USGov, NSA, IETF overwrite patterns

## Attributes and naming

- [Name Type](name-type-enumeration.md) — Uninterpreted Text String, URI
- [Alternative Name Type](alternative-name-type-enumeration.md) — Uninterpreted
  Text String, URI, Object Serial Number, Email Address, DNS Name, X.500 DN,
  IP Address
- [Rotate Name Type](rotate-name-type-enumeration.md) — Prefix, Suffix, Replace
  (2.1+)
- [Link Type](link-type-enumeration.md) — Certificate, Public Key, Private Key,
  Derivation Base Object, Parent, Child, Previous, Next, PKCS#12 Interchange,
  Wrapping Key, Wrapped
- [Object Group Member](object-group-member-enumeration.md) — Group Member Fresh,
  Group Member Default
- [Usage Limits Unit](usage-limits-unit-enumeration.md) — Byte, Object; units
  for the Usage Limits attribute
- [Key Value Location Type](key-value-location-type-enumeration.md) —
  Uninterpreted Text String, URI; points to externally stored key material
- [Unique Identifier](unique-identifier-enumeration.md) — ID generation method:
  UUID, Short UUID, Hash, SHA-256 Hash, Attribute Name, Server-generated (2.0+)

## Operations and protocol

- [Operation](operation-enumeration.md) — numeric codes for every KMIP
  operation; used in Rights, Constraints, Cancel, and Query responses
- [Query Function](query-function-enumeration.md) — Operations, Objects,
  Application Namespaces, Extension Information, Authentication Requirements,
  Profile Names, etc.
- [Result Status](result-status-enumeration.md) — Success, Operation Failed,
  Operation Pending, Operation Undone
- [Result Reason](result-reason-enumeration.md) — over 60 fine-grained failure
  codes covering authentication, access, validation, and server errors
- [Batch Error Continuation Option](batch-error-continuation-option-enumeration.md) —
  Undo, Stop, Continue; how the server proceeds when a batch item fails
- [Cancellation Result](cancellation-result-enumeration.md) — Cancelled, Unable
  to Cancel, Completed, Failed, Unavailable
- [Put Function](put-function-enumeration.md) — New, Replace; controls
  server-to-client Put operation behavior
- [Ticket Type](ticket-type-enumeration.md) — Login (2.0+)

## Authentication and identity

- [Credential Type](credential-type-enumeration.md) — Username and Password,
  Device, Attestation, One Time Password, Hashed Password, Ticket
- [Attestation Type](attestation-type-enumeration.md) — TPM Quote, TCG
  Integrity Report, SAML Assertion
- [Client Registration Method](client-registration-method-enumeration.md) —
  Unspecified, Server Pre-generated, Client Generated, Client Requested,
  Operator Generated
- [Protection Level](protection-level-enumeration.md) — Software, Hardware,
  FIPS 140-2 L1–L4, Other (2.1+)

## Validation

- [Validation Authority Type](validation-authority-type-enumeration.md) —
  Unknown, NIST, Common Criteria, FIPS 140, NSA
- [Validation Type](validation-type-enumeration.md) — Unspecified, Hardware,
  Software, Firmware, Hybrid
- [Validity Indicator](validity-indicator-enumeration.md) — Valid, Invalid,
  Unknown; result of the Validate operation

## Profiling and interoperability

- [Profile Name](profile-name-enumeration.md) — over 40 named conformance
  profiles: Complete Server, Baseline, HTTPS, XML, JSON, symmetric lifecycle,
  tape library, quantum-safe, and others
- [Interop Function](interop-function-enumeration.md) — Begin/End Transaction,
  Begin/End Validate, Begin/End Validate Credentials (2.1+)
- [Endpoint Role](endpoint-role-enumeration.md) — Client, Server (2.1+)
- [Processing Stage](processing-stage-enumeration.md) — Create, Pre-Send,
  Post-Receive, Select Decryption Keys (2.1+)
- [Adjustment Type](adjustment-type-enumeration.md) — Add, Reduce; for
  Protect Stop Date adjustment operations (2.1+)

## PKCS#11 integration

- [PKCS#11 Function](pkcs-11-function-enumeration.md) — function codes used
  in the PKCS#11 Interface structure
- [PKCS#11 Return Code](pkcs-11-return-code-enumeration.md) — standard CKR\_\*
  return codes from PKCS#11 (2.1+)
