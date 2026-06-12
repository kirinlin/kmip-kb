---
title: Item Data Types
category: reference
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "1.5"
status: reviewed
related: ["ttlv-encoding", "message-structure", "protocol-version"]
keywords: ["data types", "ttlv", "item type", "structure", "integer", "long integer", "big integer", "enumeration", "boolean", "text string", "byte string", "date-time", "interval", "encoding"]
---

# Item Data Types

## Summary

KMIP defines a fixed set of primitive data types used throughout the protocol. Every field in a TTLV-encoded message is assigned one of these types, identified by a one-byte Type octet in the TTLV header. The set is small and stable across all KMIP versions, giving the encoding a self-describing character: a parser that knows only the type byte can determine the length and structure of any value without a schema.

## Entries

**Structure** — a container type whose value is a sequence of nested TTLV items. Structures have no intrinsic value themselves; their content is a concatenation of child items. All KMIP request and response messages are ultimately a hierarchy of structures.

**Integer** — a 32-bit signed two's-complement integer, stored in 4 bytes of value field and padded to 8 bytes total (with 4 bytes of padding). Used for counts, enumeration wire values, and small numeric fields.

**Long Integer** — a 64-bit signed two's-complement integer in 8 bytes of value field with no padding. Used for fields whose range exceeds 32 bits, such as usage counts or large counters.

**Big Integer** — a variable-length signed integer encoded in a multiple of 8 bytes with leading-zero or sign-extension padding as needed. Used for public-key exponents, DSA parameters, and other arbitrary-precision values.

**Enumeration** — a 32-bit value occupying the same wire layout as Integer but semantically interpreted as a named constant from one of KMIP's enumeration types. Encoders select the Enumeration type byte rather than Integer when the field is a named constant.

**Boolean** — an 8-byte field whose value is `0x0000000000000001` for true or `0x0000000000000000` for false, with 7 bytes of padding following the 1-byte value.

**Text String** — a variable-length UTF-8 string. The length field records the byte count of the string (not the code-point count); the value is padded to the nearest 8-byte boundary with zero bytes.

**Byte String** — a variable-length opaque octet sequence. Like Text String in encoding but carries no text-encoding guarantee. Used for key material, digests, signatures, and other binary blobs.

**Date-Time** — a 64-bit unsigned integer containing seconds since the UNIX epoch (1970-01-01T00:00:00 UTC), stored in 8 bytes. All point-in-time attributes (Activation Date, Deactivation Date, and so on) use this type.

**Interval** — a 32-bit unsigned integer representing a duration in seconds, stored in 4 bytes of value with 4 bytes of padding for an 8-byte total. Used for lease times, rotation intervals, and protection periods.

## External References

The data-type encodings are specified in the [TTLV Encoding](../ttlv/ttlv-encoding.md) section, which defines the full Type-Tag-Length-Value wire format. All protocol messages are built from these types, as described in [Message Structure](../ttlv/message-structure.md).
