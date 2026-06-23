---
title: RNG Retrieve
category: operation
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.49"
v1_source_section: "4.35"
status: reviewed
related: ["rng-seed", "rng-parameters"]
keywords: ["rng retrieve", "random number", "random bytes", "rng output"]
xml_text: "RNGRetrieve"
---

# RNG Retrieve

## Purpose

`RNG Retrieve` asks the server to return random bytes from its random number
generator. It lets a client draw on the server's RNG (often a hardware or
validated generator) rather than its own. Added in KMIP 1.2.

## Request Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Data Length | `4200C4` | `DataLength` | Yes | How many bytes of random output to return. |

## Response Fields

| Field | Tag | XML Text | Required | Description |
|---|---|---|---|---|
| Data | `4200C2` | `Data` | Yes | The random bytes produced by the generator. |

## Behavior & Server Requirements

The server returns the requested number of random bytes. The result status in
the response header reports success or failure.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: a request larger than the server will satisfy, or insufficient
permission.

## Related Operations

[RNG Seed](rng-seed.md)
