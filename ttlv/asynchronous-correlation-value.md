---
title: Asynchronous Correlation Value
category: ttlv
spec_version: "1.4"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4"]
source_section: "6.8"
status: draft
related: ["asynchronous-indicator", "result-status", "correlation-value"]
keywords: ["asynchronous correlation value", "pending operation", "poll", "cancel"]
---

# Asynchronous Correlation Value

## Overview

The claim ticket for a pending operation: when a server answers a batch item
with [Result Status](result-status.md) `Operation Pending`, it includes this
value, and the client quotes it in subsequent
[Poll](../operations/poll.md) or [Cancel](../operations/cancel.md) requests
to retrieve or abort the deferred result.

## Encoding (Tag / Type / Length / Value)

Tag `420006`, Byte String, server-generated, in the response batch item.

## Fields & Structure

Required precisely when the status is Pending. One value identifies one
pending operation; a batch can spawn several. Do not confuse with the
streaming [Correlation Value](correlation-value.md) (multi-part crypto,
1.3+) or the logging-oriented
[client](client-correlation-value.md)/[server](server-correlation-value.md)
correlation values (1.4).

## Examples

A Re-key against an HSM-backed server returns Operation Pending with
correlation value `0x0042`. The client Polls with that value every few
seconds; the third Poll returns Success plus the replacement key's Unique
Identifier.

## Related

[Asynchronous Indicator](asynchronous-indicator.md) ·
[Poll](../operations/poll.md) · [Cancel](../operations/cancel.md) ·
[Result Status](result-status.md)
