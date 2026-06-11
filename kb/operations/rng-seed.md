---
title: RNG Seed
category: operation
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.50"
v1_source_section: "4.36"
status: reviewed
related: ["rng-retrieve", "rng-parameters"]
keywords: ["rng seed", "seed random", "entropy", "rng"]
---

# RNG Seed

## Purpose

`RNG Seed` offers seeding material to the server's random number generator. It
lets a client contribute entropy to the server's RNG. Added in KMIP 1.2.

## Request Fields

| Field | Required | Description |
|---|---|---|
| Data | Yes | The bytes offered as seed material to the generator. |

## Response Fields

| Field | Required | Description |
|---|---|---|
| Data Length | Yes | How many bytes of the offered seed the server actually used. |

## Behavior & Server Requirements

The server is free to decline the offered material — it may use none of it and
signal that by returning a used length of zero. A client must not treat such a
response as an error; it simply means the server did not incorporate the seed.
The result status in the header reports success or failure of the request
itself.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Note that a
server choosing not to use the seed is not an error (the used length is zero);
genuine errors include insufficient permission.

## Related Operations

[RNG Retrieve](rng-retrieve.md)
