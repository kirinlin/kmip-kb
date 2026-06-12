---
title: Rotate Name
category: attribute
spec_version: "2.1"
spec_versions: ["2.1"]
source_section: "4.53"
status: reviewed
related: ["rotate-automatic", "rotate-date", "rotate-generation", "rotate-interval", "rotate-latest", "rotate-offset", "name"]
keywords: ["rotate name", "rotation group", "rotation policy name", "key family", "rotation identifier"]
---

# Rotate Name

## Purpose

Rotate Name is a label that groups all versions of a key family under a shared, stable identifier. While [Unique Identifier](unique-identifier.md) changes with each rotation (each rotated key is a distinct object), Rotate Name stays constant across the entire lineage. Clients that need to reference "the payment-encryption key" as a durable concept — regardless of which generation is current — can use Rotate Name as a persistent handle.

## Data Type & Structure

A Text String. The value is assigned by the client or server at key-creation time and copied to each successor during rotation. No specific format is mandated; implementers commonly use human-readable names, URNs, or path-style identifiers.

## Constraints

Single-instance. Optional but important for automated rotation workflows. Should be immutable once set — changing it would break the linkage between generations. Servers may allow clients to search or locate by Rotate Name via [Locate](../operations/locate.md), making it a practical query handle for key-family management.

## Applies To (Object Types)

[Symmetric Key](../objects/symmetric-key.md), [Private Key](../objects/private-key.md), [Secret Data](../objects/secret-data.md).

## Set / Modified By

Client at creation or registration. Propagated automatically by the server to successor keys during rotation.

## Related Attributes

[Rotate Latest](rotate-latest.md) · [Rotate Generation](rotate-generation.md) · [Name](name.md)
