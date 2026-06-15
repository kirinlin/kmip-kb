---
title: Operation Policy Name
category: attribute
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4"]
source_section: "del_v2"
v1_source_section: "3.18"
status: reviewed
related: ["cryptographic-usage-mask", "sensitive", "extractable"]
keywords: ["operation policy", "access control", "default policy", "deprecated", "owner", "42005D", "OperationPolicyName"]
tag_hex: "42005D"
xml_text: "OperationPolicyName"
---

# Operation Policy Name

## Purpose

KMIP 1.x's hook for access control: the attribute names a server-side policy
object that decides which clients may run which operations on this object.
The policies themselves are opaque to the protocol — created and administered
by mechanisms KMIP does not define. **Deprecated since 1.3** (and dropped in
KMIP 2.0); real deployments do authorization through server-native mechanisms
instead.

## Data Type & Structure

A single Text String naming a policy known to the server.

## Constraints

- Optional; single instance; clients cannot modify or delete it once set
  (the server can).
- The spec defines a reserved policy named `default` plus the access matrix
  it implies: for secret objects (symmetric/private/split keys, secret data,
  opaque objects) essentially everything is owner-only; for certificates and
  public keys, read-style operations (Locate, Get, Get Attributes,
  Obtain Lease, Check) are open to all while mutations remain owner-only.
- A short list of operations sits outside policy control entirely — object
  creation (Register, Create, Create Key Pair, plus Certify and Re-certify)
  and protocol utilities (Query, Validate, Poll, Cancel).

## Applies To (Object Types)

All managed objects.

## Set / Modified By

Set by client or server when the object is created or registered (implicitly
by every object-creating operation); thereafter only the server may change
it.

## Related Attributes

[Cryptographic Usage Mask](cryptographic-usage-mask.md) ·
[Sensitive](sensitive.md) · [Extractable](extractable.md)
