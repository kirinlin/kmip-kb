---
title: Item Type Enumeration
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.23"
status: reviewed
related: ["tag-enumeration"]
keywords: ["item type", "TTLV", "type byte", "structure", "integer", "boolean", "byte string", "date-time", "enumeration", "big integer"]
---

# Item Type Enumeration

## Overview

The Item Type enumeration is a meta-level enumeration that classifies the TTLV wire-encoding type of a data item. Every TTLV-encoded value carries a 1-byte Type field immediately after its Tag, and the values of that Type field are defined by this enumeration. Understanding item types is fundamental to parsing any KMIP message: a generic TTLV parser uses the type byte to determine how many bytes to read and how to interpret the Value bytes that follow. This enumeration is also used in generic TTLV introspection APIs and any tooling that processes raw KMIP messages.

## Encoding (Tag / Type / Length / Value)

Unlike other KMIP enumerations (which are encoded as 4-byte integers with type `05`), the Item Type enumeration values appear as the Type byte in the TTLV encoding itself. The values are 1-byte constants that precede the Length and Value fields of every TTLV item.

## Fields & Structure

| Value | Hex | XML Text | Description |
|---|---|---|---|
| Structure | `0x00000001` | `Structure` |  |
| Integer | `0x00000002` | `Integer` |  |
| Long Integer | `0x00000003` | `LongInteger` |  |
| Big Integer | `0x00000004` | `BigInteger` |  |
| Enumeration | `0x00000005` | `Enumeration` |  |
| Boolean | `0x00000006` | `Boolean` |  |
| Text String | `0x00000007` | `TextString` |  |
| Byte String | `0x00000008` | `ByteString` |  |
| Date Time | `0x00000009` | `DateTime` |  |
| Interval | `0x0000000A` | `Interval` |  |
| Date Time Extended | `0x0000000B` | `DateTimeExtended` |  |

- **Structure** (`0x01`): A container item that holds a sequence of nested TTLV items. Structures do not have a value of their own — the Length field indicates how many bytes of sub-items follow. Almost every complex KMIP object (request, response, key block) is a Structure.
- **Integer** (`0x02`): A signed 32-bit integer, stored in 4 bytes of value. Used for small numeric fields such as cryptographic key lengths, batch counts, and offset values.
- **Long Integer** (`0x03`): A signed 64-bit integer, stored in 8 bytes of value. Used for timestamps, large counters, and date-time values that require 64-bit precision.
- **Big Integer** (`0x04`): An arbitrary-precision signed integer, stored as a variable-length byte string padded to a multiple of 8 bytes. Used for large public key moduli, elliptic curve parameters, and other big-number fields in transparent key structures.
- **Enumeration** (`0x05`): A 32-bit integer whose value comes from a named enumeration (such as any of the other enumerations documented in this directory). Stored in 4 bytes.
- **Boolean** (`0x06`): A true/false value stored in 8 bytes (padded for alignment). Used for binary flag fields.
- **Text String** (`0x07`): A UTF-8 encoded text string, padded to a multiple of 8 bytes. Used for human-readable names, URIs, and textual attribute values.
- **Byte String** (`0x08`): An arbitrary byte sequence, padded to a multiple of 8 bytes. Used for key material, ciphertext, digests, and other opaque binary data.
- **Date-Time** (`0x09`): A 64-bit Unix epoch timestamp (seconds since 1970-01-01T00:00:00Z), stored in 8 bytes. Used for activation dates, expiry dates, and event timestamps.
- **Interval** (`0x0A`): A 32-bit unsigned duration in seconds. Used for lease time, validity periods, and similar bounded time values.

## Examples

A TTLV parser encountering the byte sequence `42 00 09 07 00 00 00 0C` would interpret tag `420009` (Unique Identifier), type `07` (Text String), length `0x0C` (12 bytes), followed by the 12-byte string value (padded to 16 bytes on the wire). The Item Type byte `07` is the key to interpreting the rest of the item correctly.

## Related

- [Tag Enumeration](tag-enumeration.md) — defines the tag values paired with these type codes in TTLV messages
