---
title: TTLV Encoding
category: ttlv
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "10.1"
v1_source_section: "9.1"
status: reviewed
related: ["message-structure", "extension-information", "transport"]
keywords: ["TTLV", "tag type length value", "binary encoding", "padding", "big endian"]
---

# TTLV Encoding

## Overview

KMIP's native wire format: every protocol element is a Tag-Type-Length-Value
record. The scheme trades bandwidth for simplicity and alignment — it is
designed so small clients can encode/decode with minimal CPU and memory, and
every item value starts on an 8-byte boundary for friendly 32/64-bit
processing.

## Encoding (Tag / Type / Length / Value)

Each item is:

1. **Tag** — 3 bytes, big-endian. First byte `42` for tags defined by the
   spec, `54` for vendor extensions; the deliberate constants make corrupt
   messages obvious in hex dumps.
2. **Type** — 1 byte: `01` Structure, `02` Integer, `03` Long Integer, `04`
   Big Integer, `05` Enumeration, `06` Boolean, `07` Text String, `08` Byte
   String, `09` Date-Time, `0A` Interval.
3. **Length** — 4 bytes, big-endian: the byte count of the value
   *excluding* padding (for structures: the full padded length of all
   sub-items). Fixed: Integer/Enumeration/Interval 4; Long Integer /
   Boolean / Date-Time 8; the rest variable.
4. **Value** — the data, padded out to a multiple of 8 bytes: 4-byte types
   get 4 padding bytes; strings get however many zero bytes reach the next
   8-byte boundary.

Value semantics: integers are two's-complement big-endian; Big Integers are
sign-extended to a multiple of 8 bytes (padding counted in the length);
enumerations are unsigned 32-bit (extension values flagged by `8` in the
top nibble); Booleans are 8 bytes ending in `00`/`01`; Text Strings are
UTF-8 without null termination; Date-Times are POSIX seconds as a signed
64-bit value; Intervals are unsigned 32-bit seconds; structure values are
the concatenation of their sub-items in the order their definitions list.

## Fields & Structure

The defined tag registry (`420001`–`420124` in 1.4, extended in later
releases) is the master list in the spec's tag enumeration (v1.x §9.1.3.1);
`540000`–`54FFFF` is the [extensions](../structures/extension-information.md) space. TTLV is
one of several possible encodings — the encoding chapter (v2.1 §10.1; v1.x §9)
is structured to admit alternatives, and v2.0 promoted HTTPS/REST, JSON, and
XML to first-class wire formats in the core spec (§10.2) — but TTLV is the
baseline every implementation speaks.

## Examples

A Cryptographic Length of 256 — an Integer under tag `42002A`:
`42 00 2A | 02 | 00 00 00 04 | 00 00 01 00 00 00 00 00` — tag, type 02,
length 4, then the 4-byte value plus 4 padding bytes. A Text String
`"Hello World"` has length `0B` and 5 padding bytes after the UTF-8 text.

## Related

[Message Structure](../messages/message-structure.md) ·
[Extension Information](../structures/extension-information.md) ·
[Transport](../concepts/transport.md)
