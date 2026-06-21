---
title: Data Length
category: structures
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "7.10"
v1_source_section: "2.1.11"
status: reviewed
related: ["data", "rng-retrieve"]
keywords: ["data length", "requested bytes", "RNG retrieve", "4200C4", "DataLength"]
tag_hex: "4200C4"
xml_text: "DataLength"
tag_type: "Integer"
---

# Data Length

## Overview

A request-side count of how many bytes of output the client wants from a
cryptographic operation. Its main user is
[RNG Retrieve](../operations/rng-retrieve.md), where it specifies how much
random material the server should return.

## Encoding (Tag / Type / Length / Value)

Tag `4200C4`, Integer (so a fixed 4-byte value field plus 4 padding bytes on
the wire).

## Fields & Structure

A bare count; the response delivers the corresponding bytes in a
[Data](data.md) field. Note this is application-level sizing — unrelated to
the TTLV Item Length framing, and also distinct from
[Maximum Response Size](../messages/maximum-response-size.md), which caps the whole
response message.

## Examples

RNG Retrieve with Data Length = 32 returns Data containing 32 random bytes
for use as a locally-assembled key seed.

## Related

[Data](data.md) · [RNG Retrieve](../operations/rng-retrieve.md)
