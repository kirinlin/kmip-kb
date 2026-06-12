---
title: Key Wrap Type Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["2.0","2.1"]
source_section: "11.29"
status: reviewed
related: ["key-block", "key-wrapping-data", "wrapping-method-enumeration", "encoding-option-enumeration", "get"]
keywords: ["key wrap type", "wrapped", "not wrapped", "key wrapping", "key block", "transport"]
---

# Key Wrap Type Enumeration

## Overview

The Key Wrap Type enumeration indicates whether and how the key material in a [Key Block](../key-block.md) is currently wrapped. Key wrapping is the process of encrypting or integrity-protecting key material under another key for storage or transport; the wrap type lets consumers determine immediately whether they are receiving plaintext key bytes or an encrypted blob that must first be unwrapped before use. A transitional state is also defined for use during in-place re-wrapping operations.

## Encoding (Tag / Type / Length / Value)

Encoded as a 4-byte integer (TTLV type `05`, Enumeration). Appears in the Key Block structure to describe the wrapping state of the enclosed key material.

## Fields & Structure

- **Not Wrapped**: The key material is present in plaintext form (subject only to transport-layer protection). The client receives raw key bytes and can use them directly.
- **As Registered That Is**: The key is delivered exactly as it was stored — wrapped or unwrapped — without any additional wrapping applied by the server at retrieval time. Used when a client wants to retrieve the key in its stored form rather than requesting a specific wrap.
- **Processing**: A transient state indicating that the key is being re-wrapped or otherwise processed. Consumers should not attempt to use a key in this state; they should retry after the operation completes.

## Examples

A client that registered a key wrapped under a Key Encryption Key receives it back with type **As Registered That Is** when it supplies no wrapping specification in the Get request, allowing it to retrieve the original wrapped blob. A client that wants the key in cleartext for local use requests it with an unwrapping specification and receives the key with type **Not Wrapped** in the response.

## Related

- [Key Block structure](../key-block.md) — the container that carries this field
- [Key Wrapping Data structure](../key-wrapping-data.md) — describes the wrapping parameters used when the key is wrapped
- [Wrapping Method Enumeration](wrapping-method-enumeration.md) — specifies how the wrapping was applied
- [Encoding Option Enumeration](encoding-option-enumeration.md) — controls whether the Key Value was TTLV-encoded before wrapping
- [Get operation](../../operations/get.md) — retrieves key material; clients can specify wrapping behaviour
