---
title: State Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.55"
status: reviewed
related: ["state", "activate", "revoke", "destroy", "archive", "recover"]
keywords: ["state", "object lifecycle", "pre-active", "active", "deactivated", "compromised", "destroyed", "lifecycle state", "42008D"]
tag_hex: "42008D"
xml_text: "State"
tag_type: "Enumeration"
---

# State Enumeration

## Overview

The State enumeration is the lifecycle state of a managed KMIP object. It is the type of the [State attribute](../attributes/state.md) and appears in Locate filters, response structures, and the [State attribute](../attributes/state.md). Every managed object has exactly one State at any moment; state transitions are triggered by lifecycle operations (Activate, Revoke, Destroy, Archive, Recover) or by attribute changes (setting an Activation Date to the past).

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Pre-Active | `00000001` | `PreActive` |  |
| Active | `00000002` | `Active` |  |
| Deactivated | `00000003` | `Deactivated` |  |
| Compromised | `00000004` | `Compromised` |  |
| Destroyed | `00000005` | `Destroyed` |  |
| Destroyed Compromised | `00000006` | `DestroyedCompromised` |  |

The six states form a directed lifecycle graph:

- **Pre-Active** (1): The object exists on the server but cannot yet be used for cryptographic operations. Attributes may be freely modified while in this state. Transition to Active occurs when the Activation Date is reached or via an explicit Activate operation.
- **Active** (2): The object is live and available for its intended cryptographic purposes. Most operations on the object (encrypt, decrypt, sign, verify, MAC) require it to be in this state. Attributes are generally locked against modification.
- **Deactivated** (3): The object's cryptographic lifespan has ended. It cannot be used for new cryptographic operations but its metadata and key material remain accessible for archival or key recovery purposes. The state is entered via Revoke (with a non-compromise reason) or when the Deactivation Date is reached.
- **Compromised** (4): The object's security has been breached or is suspected to have been breached. Key material may still be accessible to authorised parties for forensic or recovery purposes, but the object must not be used for any new cryptographic operations.
- **Destroyed** (5): The object's key material has been deleted or shredded. Only metadata (attributes, audit trail) may remain. The Unique Identifier is no longer usable for cryptographic operations.
- **Destroyed Compromised** (6): The object was in a compromised state when it was destroyed. The metadata records that the material was both destroyed and previously compromised.

## Examples

A Locate request filtered on State = **Active** returns only objects that are currently usable for cryptographic operations. An Activate operation transitions a key from **Pre-Active** to **Active**. Revoke with Key Compromise reason transitions from Active to **Compromised** (if the compromise has occurred), bypassing the Deactivated state.

## Related

[State attribute](../attributes/state.md) · [State attribute](../attributes/state.md) · [Activate](../operations/activate.md) · [Revoke](../operations/revoke.md) · [Destroy](../operations/destroy.md)
