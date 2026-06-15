---
title: Unique Identifier Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["2.0","2.1"]
source_section: "11.58"
status: reviewed
related: ["unique-identifier", "locate", "message-structure"]
keywords: ["unique identifier", "ID placeholder", "filtered", "sentinel", "batch operations", "ID reference"]
---

# Unique Identifier Enumeration

## Overview

The Unique Identifier field in KMIP is normally a free-form Text String assigned by the server. However, in certain batch and deferred-reference contexts, a client needs to refer to an object by a symbolic handle rather than a literal identifier — for example, to target "the object I just created in the previous batch item" or "all objects matching the current Locate filter". The Unique Identifier Enumeration defines these sentinel values, encoded as Enumeration type rather than Text String.

## Encoding (Tag / Type / Length / Value)

When the Unique Identifier field carries a sentinel value from this enumeration, it is encoded with TTLV type `05` (Enumeration) rather than type `07` (Text String). Parsers must check the type byte to determine which form is present.

## Fields & Structure

- **ID Placeholder**: Refers to the object identified by the server's current ID Placeholder — a per-session register that holds the Unique Identifier of the most recently created or located object. A batch item can use this sentinel in a Get immediately after a Create to retrieve the key that was just made, without needing to capture the Create response's Unique Identifier first.
- **Filtered**: Applies the operation to every object currently matched by the active Locate filter in the batch. Allows a single operation to target a set of objects identified by a preceding Locate step, without enumerating individual IDs.

## Examples

A two-item batch — item 1: Create (Symmetric Key), item 2: Get (Unique Identifier = **ID Placeholder**) — retrieves the just-created key in the same round-trip without the client knowing the assigned Unique Identifier in advance.

A three-item batch — item 1: Locate (attributes = State: Active, Object Type: Symmetric Key), item 2: Activate (Unique Identifier = **Filtered**) — activates all matched symmetric keys in one batch.

## Related

[Unique Identifier attribute](../../attributes/unique-identifier.md) · [Locate](../../operations/locate.md) · [Message Structure](../../messages/message-structure.md)
