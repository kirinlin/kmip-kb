---
title: Correlation Value
category: structures
spec_version: "2.1"
spec_versions: ["1.3", "1.4", "2.0", "2.1"]
source_section: "7.8"
v1_source_section: "2.1.15"
status: reviewed
related: ["init-indicator", "final-indicator", "data", "asynchronous-correlation-value"]
keywords: ["correlation value", "streaming", "multi-part operation", "session handle", "4200D6", "CorrelationValue"]
tag_hex: "4200D6"
xml_text: "CorrelationValue"
---

# Correlation Value

## Overview

The session handle for multi-part (streaming) cryptographic operations,
added in 1.3. When a client starts a streamed
[Encrypt](../operations/encrypt.md) / [Decrypt](../operations/decrypt.md) /
[Sign](../operations/sign.md) / [MAC](../operations/mac.md) / Hash, the
server mints this value in the first response; every follow-up part of the
same logical operation must quote it.

## Encoding (Tag / Type / Length / Value)

Tag `4200D6`, Byte String, server-chosen content.

## Fields & Structure

Lifecycle: request 1 sets [Init Indicator](init-indicator.md) = True →
response 1 returns the Correlation Value → middle parts carry the value with
chunks of [Data](data.md) → the last part adds
[Final Indicator](final-indicator.md) = True, and the server completes the
computation (returning, say, the final MAC). Which operations support
streaming is the server's choice — advertised via
[Capability Information](capability-information.md) (Streaming Capability).
Distinct from the
[Asynchronous Correlation Value](../messages/asynchronous-correlation-value.md) (pending
operations) and the 1.4 client/server correlation values (logging).

## Examples

Hashing a 4 GiB file in 8 MiB chunks: first Hash request has Init Indicator
= True and chunk 1; the response supplies Correlation Value `0xA1B2...`;
each later request repeats it; the request with Final Indicator = True gets
back the digest.

## Related

[Init Indicator](init-indicator.md) · [Final Indicator](final-indicator.md) ·
[Data](data.md) ·
[Asynchronous Correlation Value](../messages/asynchronous-correlation-value.md)
