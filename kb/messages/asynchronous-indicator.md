---
title: Asynchronous Indicator
category: messages
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "9.2"
v1_source_section: "6.7"
status: reviewed
related: ["asynchronous-correlation-value", "result-status", "capability-information"]
keywords: ["asynchronous indicator", "async", "polling", "request header", "420007", "AsynchronousIndicator"]
tag_hex: "420007"
xml_text: "AsynchronousIndicator"
---

# Asynchronous Indicator

## Overview

The request-header flag by which a client states whether it can cope with
asynchronous answers. If True, the server may respond to any batch item with
`Operation Pending` and let the client [Poll](../operations/poll.md) for the
outcome; if False (or absent — False is the default), the server must finish
every operation synchronously.

## Encoding (Tag / Type / Length / Value)

Tag `420007`, Boolean, request header only.

## Fields & Structure

Even when permitted, going asynchronous is the server's choice per
operation; a batched request may come back with a mix of completed and
pending items. Pending items carry an
[Asynchronous Correlation Value](asynchronous-correlation-value.md) for the
follow-up [Poll](../operations/poll.md) / [Cancel](../operations/cancel.md).
Servers advertise async support in
[Capability Information](../structures/capability-information.md).

## Examples

A client that cannot poll (stateless CLI) leaves the flag absent; a
long-running [Certify](../operations/certify.md) then either completes in
the request or fails, but never parks as pending.

## Related

[Asynchronous Correlation Value](asynchronous-correlation-value.md) ·
[Poll](../operations/poll.md) · [Result Status](result-status.md)
