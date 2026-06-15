---
title: Versions
category: index
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: ""
status: reviewed
related: []
keywords: ["versions", "TOC", "1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1", "deltas"]
---

# Versions

Machine-readable per-version section maps, plus delta notes between releases.

- [2.1-toc.yaml](2.1-toc.yaml) — 234 sections. Regenerate with
  `python scripts/build_kb_scaffold.py --version 2.1 --toc-only`.
- [2.0-toc.yaml](2.0-toc.yaml) — 215 sections. Regenerate with
  `python scripts/build_kb_scaffold.py --version 2.0 --toc-only`.
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
which releases include the feature.

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
  [Key Wrapping Data](../structures/key-wrapping-data.md) and
  [Key Wrapping Specification](../structures/key-wrapping-specification.md) that
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
  the new crypto operations — [Data](../structures/data.md),
  [Data Length](../structures/data-length.md),
  [Signature Data](../structures/signature-data.md),
  [MAC Data](../structures/mac-data.md), and
  [Nonce](../messages/nonce.md) (used as an attestation challenge).
- *New attributes* (§3.40–43):
  [Alternative Name](../attributes/alternative-name.md),
  [Key Value Present](../attributes/key-value-present.md),
  [Key Value Location](../attributes/key-value-location.md), and
  [Original Creation Date](../attributes/original-creation-date.md).
- *Attestation* (§6.17): an Attestation credential type allows a client to
  present a hardware/software measurement or third-party assertion instead of
  a password. The server issues a [Nonce](../messages/nonce.md) challenge; the
  client responds with an Attestation Credential containing either an
  Attestation Measurement or Attestation Assertion. The new
  [Attestation Capable Indicator](../messages/attestation-capable-indicator.md)
  message-header flag advertises whether the client supports attestation.
  Query gains a "Query Attestation Types" function to discover which
  attestation methods a server accepts.

### 1.3

Streaming multi-part operations, server-to-client Query, richer server
capability reporting, and several deprecations clearing the path toward 1.4.

- *Streaming crypto* (§2.1.15–17): [Correlation Value](../structures/correlation-value.md),
  [Init Indicator](../structures/init-indicator.md), and
  [Final Indicator](../structures/final-indicator.md) link the batch items of a
  multi-part Encrypt/Decrypt/Sign/MAC sequence into a single logical session.
- *Capability reporting* (§2.1.18–21): four new structures returned by the
  §4.25 Query response —
  [RNG Parameters](../structures/rng-parameters.md) describes a random-number
  generator; [Profile Information](../structures/profile-information.md),
  [Validation Information](../structures/validation-information.md), and
  [Capability Information](../structures/capability-information.md) let servers
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

### 2.0

A major revision that reorganized the specification's section numbering, added
ten-plus new operations, and removed features that had been deprecated in
v1.1–v1.3. The section-number mapping to the KB differs from v1.x (see
[2.0-toc.yaml](2.0-toc.yaml)); the `spec_versions` front matter on each KB
page reflects whether the feature is present in v2.0.

**Structural reorganization:** the spec was renumbered from top to bottom.
Managed objects moved to §2, object data structures (Key Block, transparent
key forms) to §3, object attributes to §4, attribute data structures to §5,
operations to §6 (client §6.1, server-to-client §6.2), operations data
structures to §7, message structures to §8–§9, and message protocols
(TTLV, authentication, transport) to §10. Enumerations and bit masks received
their own chapters (§11–§12). The KB's `source_section` fields are baselined
to **v2.1** numbering; the five docs removed in v2.0 (Template object,
Certificate Identifier/Subject/Issuer, Operation Policy Name) keep their
last-present v1.x numbering.

**New operations (§6.1, not in v1.x):**
- *Adjust Attribute* (§6.1.3): atomically increments or decrements a numeric
  attribute — useful for usage counters without a read-modify-write race.
- *Delegated Login* (§6.1.12): allows a client to authenticate on behalf of
  another entity, enabling proxy or delegation patterns.
- *Interop* (§6.1.25): a generic interoperability operation for
  implementation-defined interactions between clients and servers.
- *Log* (§6.1.28): appends a log entry to the server's audit trail, allowing
  clients to annotate key-management events.
- *Login* / *Logout* (§6.1.29–30): explicit session establishment and
  termination, complementing the existing implicit authentication model.
- *PKCS#11* (§6.1.35): tunnels PKCS#11 cryptographic function calls through
  the KMIP transport, letting applications use a KMIP server as a PKCS#11
  token without a local driver.
- *Re-Provision* (§6.1.44): replaces an existing key's cryptographic material
  while preserving its Unique Identifier and associated attributes — an
  in-place rotation that avoids updating every reference to the old key.
- *Set Attribute* (§6.1.47): replaces the v1.x Add Attribute for writing
  single-valued attributes; the existing Add Attribute / Modify Attribute /
  Delete Attribute operations remain for multi-valued attributes and deletion.
- *Set Endpoint Role* (§6.1.48): configures whether the local endpoint acts
  as a client, server, or both — supports the symmetric server-to-client model.

**New server-to-client operations (§6.2, not in v1.x):**
- *Discover Versions* (§6.2.1): the server can now query which KMIP versions
  a client supports, symmetric to the existing client-to-server §6.1.16.
- *Set Endpoint Role* (§6.2.5): server-initiated endpoint role configuration.

**New object (§2):**
- *Certificate Request* (§2.2): a new managed object type holding a
  PKCS#10 or PEM certificate signing request, allowing the server to manage
  CSRs alongside the resulting certificates.

**New attributes (§4, not in v1.x):**
- *Certificate Attributes* (§4.6): a consolidated structure grouping
  X.509-specific attribute fields from the certificate's subject and issuer
  Distinguished Names, replacing the deprecated individual Certificate
  Identifier/Subject/Issuer attributes at the data-model level.
- *NIST Key Type* (§4.34): classifies a key according to the NIST SP 800-57
  key-type taxonomy, independent of its cryptographic algorithm.
- *Protection Level*, *Protection Period*, *Protection Storage Mask* (§4.42–44):
  three new attributes that specify how aggressively a key's storage medium
  must protect the key at rest, for how long, and which storage classes are
  acceptable.
- *Quantum Safe* (§4.45): a Boolean flag asserting that the key's algorithm
  and parameters are considered resistant to quantum-computing attacks.
- *Short Unique Identifier* (§4.49): a shorter, server-assigned handle
  alongside the full Unique Identifier — useful in constrained environments
  where identifiers are transmitted frequently.

**New attribute data structures (§5):** the monolithic Template-Attribute
structure from v1.x was replaced by a structured set — Attributes (§5.1),
Common Attributes (§5.2), Private Key Attributes (§5.3), Public Key Attributes
(§5.4), Attribute Reference (§5.5), Current Attribute (§5.6), and New
Attribute (§5.7) — giving batch attribute operations a type-safe, versioned
envelope.

**Additional encoding formats (§10.2):** alongside TTLV (§10.1), v2.0
explicitly specifies HTTPS/REST (§10.2.1), JSON (§10.2.2), and XML (§10.2.3)
wire formats, making multi-protocol servers an official first-class concern.

**Removals:**
- *Template object* (deprecated v1.3): callers should use per-operation
  [Template-Attribute](../structures/template-attribute-structures.md) structures
  or the new §5 Attribute Data Structures instead.
- *Certificate Identifier*, *Certificate Subject*, *Certificate Issuer*
  attributes (deprecated v1.1): use
  [X.509 Certificate Identifier](../attributes/x-509-certificate-identifier.md),
  [X.509 Certificate Subject](../attributes/x-509-certificate-subject.md), and
  [X.509 Certificate Issuer](../attributes/x-509-certificate-issuer.md).
- *Operation Policy Name* attribute (deprecated v1.3): access-control policy
  is now managed entirely through server-side configuration.
- *Error Handling* as a top-level section (v1.x §11): error codes and
  per-operation error tables are embedded within each operation's definition
  as §6.1.N.N sub-sections.

### 2.1

A focused release that adds automated key-rotation policy attributes, a
constraints management sub-system, asynchronous-request query, and several
utility operations. No features were removed from v2.0.

**Key rotation attributes (§4.48–54, not in v2.0):** seven new attributes
provide a machine-readable key-rotation policy that servers can act on
automatically, without a client having to poll and re-key manually:
- *Rotate Automatic* (§4.48): Boolean flag enabling server-side automatic
  rotation when the policy conditions are met.
- *Rotate Date* (§4.49): a fixed calendar date after which the key should be
  rotated.
- *Rotate Generation* (§4.50): maximum number of Re-key or Re-Provision
  generations before the key must be rotated.
- *Rotate Interval* (§4.51): rotation cadence expressed as a duration
  (e.g., every 90 days).
- *Rotate Latest* (§4.52): Boolean; when true, rotation replaces the key
  in-place using Re-Provision rather than creating a successor via Re-key.
- *Rotate Name* (§4.53): controls whether the rotated key inherits the
  original key's Name attribute.
- *Rotate Offset* (§4.54): shifts the rotation schedule by a fixed duration —
  useful for staggering rotations across a fleet of keys.

**Constraints management (§6.1, §7):** a new sub-system lets servers
declare and enforce per-object or per-class attribute constraints:
- *Get Constraints* (§6.1.22): retrieves the constraint set applied to a
  managed object or to a class of objects.
- *Set Constraints* (§6.1.52): writes or replaces the constraint set.
- *Constraint* (§7.6) and *Constraints* (§7.7): the data structures holding
  individual constraint rules and the full constraint collection respectively.

**Asynchronous request management (§6.1, §7):** builds on the existing
Asynchronous Correlation Value to let clients inspect long-running operations:
- *Query Asynchronous Requests* (§6.1.41): returns status and partial results
  for one or more outstanding asynchronous operations.
- *Asynchronous Correlation Values* (§7.1): plural structure grouping multiple
  correlation handles in a single batch-item field.
- *Asynchronous Request* (§7.2): the per-request status record returned by
  Query Asynchronous Requests.

**Additional utility operations (§6.1):**
- *Ping* (§6.1.36): a lightweight round-trip health-check — the server echoes
  back a client-supplied correlation value, confirming the connection and
  measuring latency without any key-management side effects.
- *Process* (§6.1.39): a generic post-processing operation that triggers
  server-defined transformations on a managed object — for example, wrapping
  a key for a specific target device after it has been created.
- *Set Defaults* (§6.1.53): writes the default attribute values the server
  applies when creating or registering objects that omit those attributes,
  making per-server defaults inspectable and configurable via the protocol.

**Object group and type query structures (§7.23–24):**
- *Object Groups* (§7.23) and *Object Types* (§7.24): companion structures to
  the Query operation's response, grouping available object-group names and
  supported object types the server reports.
