---
title: Key State and Times
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.16"
status: reviewed
related: ["key-life-cycle-and-key-state", "mutating-attributes"]
keywords: ["key state", "Activation Date", "Deactivation Date", "Process Start Date", "Protect Stop Date", "Initial Date", "cryptoperiod"]
---

# Key State and Times

## Overview

KMIP provides a rich set of time-related attributes that govern when a managed cryptographic object is active, when it may be used for applying cryptographic protection, and when it may be used for processing already-protected data. These attributes together define the object's cryptoperiod and control lifecycle state transitions.

## Guidance

The key time attributes are:

- **Initial Date**: Set by the server when the object is first created or registered; not client-modifiable.
- **Activation Date**: When the key becomes eligible for use in applying cryptographic protection; may be set in the past or future.
- **Process Start Date**: When a symmetric key becomes eligible for processing (e.g., decryption) previously protected data; must be ≥ Activation Date.
- **Protect Stop Date**: When a symmetric key should stop being used for applying new protection; must be ≤ Deactivation Date.
- **Deactivation Date**: When the key should no longer be used for applying protection; may be set even when Activation Date is absent.

Guidelines: an Active object cannot be destroyed directly; it must be Revoked or Deactivated first. Setting Process Start Date and Protect Stop Date independently from Activation Date and Deactivation Date is recommended for symmetric keys, allowing a key to continue decrypting data after it is no longer used for encryption.

## Implementation Notes

Clock skew between client and server is an important practical concern. If a client sets a time attribute to "now" and the server's clock is slightly ahead, the server may reject the attribute as a backdated value. Servers that do not accept backdated attributes will return an error; clients should issue the corresponding state-change operation (e.g., Activate) rather than setting the Activation Date directly when they want the server to use its own current time.

## Related Concepts

See [Key Life-cycle and Key State](key-life-cycle-and-key-state.md) and [Mutating Attributes](mutating-attributes.md).
