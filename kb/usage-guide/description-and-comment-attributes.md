---
title: Description and Comment Attributes
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.19"
status: draft
related: ["attributes"]
keywords: ["Description", "Comment", "human-readable", "metadata", "informational attributes"]
---

# Description and Comment Attributes

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

The Description and Comment attributes provide human-readable text fields for annotating managed objects. Description is intended for a concise imperative statement about the object's purpose; Comment provides space for more verbose contextual information.

## Guidance

An example pairing: a Description of "Root Key for internal servers" paired with a Comment of "Ensure new internal servers are provisioned with this key before going live." Description is meant to be action-oriented and concise; Comment is the place for extended notes, reminders, or operational context.

Both attributes are optional and informational only — they carry no semantic weight in protocol operations and must not be used for policy enforcement. Servers may surface these attributes in management UIs and audit logs, but KMIP itself does not act on their contents.

## Implementation Notes

Because these attributes are not enforced by the protocol, their value depends entirely on the discipline of the parties managing objects. Organisations should establish naming conventions for Description to ensure objects are uniformly identifiable across implementations. Comment can document rotation schedules, responsible owners, or incident history.

## Related Concepts

See [Attributes](attributes.md) for the general attribute management model.
