---
title: Using Notify and Put Operations
category: usage-guide
spec_version: "2.1"
spec_versions: ["2.0", "2.1"]
source_section: "ug-3.50"
status: draft
related: ["flow-control", "synchronous-and-asynchronous-operations"]
keywords: ["Notify", "Put", "server-to-client", "server-initiated", "acknowledgement", "key push", "proxy"]
---

# Using Notify and Put Operations

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

Notify and Put are server-initiated operations: the server sends them to the client rather than the client sending a request to the server. They are optional in KMIP and are intended to provide an efficient push mechanism that avoids the need for clients to poll for new or updated objects.

## Guidance

Before using Notify or Put, the client must enrol with the server out-of-band (outside KMIP) to specify: how the server can locate the client, which events trigger a Notify, and whether Put is supported and which attributes may be included.

Client-to-server communication must be authenticated using at least the mandatory authentication mechanisms from KMIP-Prof. Clients are expected to acknowledge Notify and Put messages, either at the KMIP layer or via transport-level acknowledgement (e.g., TCP acknowledgement).

For non-responsive clients (those that cannot accept incoming connections), a proxy entity communicates with the server on the client's behalf using KMIP, while the proxy communicates with the client using a potentially proprietary protocol.

## Implementation Notes

Because enrolment is out-of-band, Notify/Put deployments require a configuration step that is not standardised by KMIP. This is the main friction point for interoperability: clients and servers from different vendors may use incompatible enrolment mechanisms. Implementations should document the enrolment procedure clearly.

## Related Concepts

See [Flow Control](flow-control.md) for handling intermittently available clients.
