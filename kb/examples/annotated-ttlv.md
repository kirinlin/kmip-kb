---
title: Annotated TTLV
category: example
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: ""
status: reviewed
related: ["ttlv-encoding", "message-structure", "locate"]
keywords: ["annotated TTLV", "TTLV", "hex dump", "wire format", "binary encoding", "tag type length value", "examples", "locate", "request", "response"]
---

# Annotated TTLV

## Overview

"Annotated TTLV" is the informal name for a human-readable hex presentation of a KMIP binary message. Each 8-byte item header and its value bytes are printed as spaced hex with a `#` comment giving the field name, type name, and byte count. Indentation tracks nesting depth so the structure tree is visible at a glance.

This format appears in debug logs, KMIP client libraries, and protocol analyzers. It is not defined by the specification — it is a display convention that implementers converged on because it makes the raw [TTLV encoding](../encoding/ttlv-encoding.md) inspectable without a dedicated parser.

## Reading the Format

### Item header

The first 8 bytes of every TTLV item are the header, always on one line:

```
TT TT TT  TP  LL LL LL LL   # FieldName, TypeName, Length=DDD
```

| Segment | Bytes | Meaning |
|---|---|---|
| `TT TT TT` | 3 | Tag — identifies the field. Spec-defined tags start with `42`; vendor extensions start with `54`. |
| `TP` | 1 | Type byte — see the table below. |
| `LL LL LL LL` | 4 | Length — byte count of the value, *not* including padding. Big-endian. |

### Value line

Following the header, the value bytes padded to a multiple of 8:

```
VV VV VV VV PP PP PP PP   # Value=decoded + padding
```

Padding bytes are always zero and are included in the value line but not in the declared length. Structure items have no value line — their length counts the total padded bytes of all sub-items, which follow immediately as indented child items.

### Type codes

| Byte | Name | Wire value size | Notes |
|---|---|---|---|
| `01` | Structure | covers sub-items | no padding of its own |
| `02` | Integer | 4 bytes | + 4 padding bytes |
| `03` | Long Integer | 8 bytes | no padding |
| `04` | Big Integer | variable | length is a multiple of 8; padding counted in length |
| `05` | Enumeration | 4 bytes | + 4 padding bytes; extension values have `8` in the top nibble |
| `06` | Boolean | 8 bytes | final byte is `00` (false) or `01` (true) |
| `07` | Text String | variable | UTF-8; padded to the next 8-byte boundary |
| `08` | Byte String | variable | padded to the next 8-byte boundary |
| `09` | Date-Time | 8 bytes | signed POSIX seconds, big-endian |
| `0A` | Interval | 4 bytes | + 4 padding bytes |
| `0B` | Date-Time Extended | 8 bytes | nanosecond resolution (v2.0+) |

## Example: Locate Request (KMIP 1.4)

A minimal request that authenticates with a username and password, then searches for objects, returning at most one result. The header carries the credential; the payload specifies the limit.

XML encoding:

```xml
<RequestMessage>
    <RequestHeader>
        <ProtocolVersion>
            <ProtocolVersionMajor type="Integer" value="1"/>
            <ProtocolVersionMinor type="Integer" value="4"/>
        </ProtocolVersion>
        <Authentication>
            <Credential>
                <CredentialType type="Enumeration" value="UsernameAndPassword"/>
                <CredentialValue>
                    <Username type="TextString" value="[REDACTED]"/>
                    <Password type="TextString" value="[REDACTED]"/>
                </CredentialValue>
            </Credential>
        </Authentication>
        <TimeStamp type="DateTime" value="2026-06-17T13:21:41+08:00"/>
        <BatchCount type="Integer" value="1"/>
    </RequestHeader>
    <BatchItem>
        <Operation type="Enumeration" value="Locate"/>
        <RequestPayload>
            <MaximumItems type="Integer" value="1"/>
        </RequestPayload>
    </BatchItem>
</RequestMessage>
```

Annotated TTLV:

```
42 00 78 01 00 00 00 C8   # RequestMessage, Structure, Length=200
   42 00 77 01 00 00 00 90   # RequestHeader, Structure, Length=144
      42 00 69 01 00 00 00 20   # ProtocolVersion, Structure, Length=32
         42 00 6A 02 00 00 00 04   # ProtocolVersionMajor, Integer, Length=4
            00 00 00 01 00 00 00 00   # Value=1 + padding
         42 00 6B 02 00 00 00 04   # ProtocolVersionMinor, Integer, Length=4
            00 00 00 04 00 00 00 00   # Value=4 + padding
      42 00 0C 01 00 00 00 40   # Authentication, Structure, Length=64
         42 00 23 01 00 00 00 38   # Credential, Structure, Length=56
            42 00 24 05 00 00 00 04   # CredentialType, Enumeration, Length=4
               00 00 00 01 00 00 00 00   # Value=UsernameAndPassword(0x01) + padding
            42 00 25 01 00 00 00 20   # CredentialValue, Structure, Length=32
               42 00 99 07 00 00 00 04   # Username, TextString, Length=4
                  [REDACTED]
               42 00 A1 07 00 00 00 08   # Password, TextString, Length=8
                  [REDACTED]
      42 00 92 09 00 00 00 08   # TimeStamp, DateTime, Length=8
         00 00 00 00 6A 33 80 65   # Value=2026-06-17T05:21:41Z
      42 00 0D 02 00 00 00 04   # BatchCount, Integer, Length=4
         00 00 00 01 00 00 00 00   # Value=1 + padding
   42 00 0F 01 00 00 00 28   # BatchItem, Structure, Length=40
      42 00 5C 05 00 00 00 04   # Operation, Enumeration, Length=4
         00 00 00 08 00 00 00 00   # Value=Locate(0x08) + padding
      42 00 79 01 00 00 00 10   # RequestPayload, Structure, Length=16
         42 00 4F 02 00 00 00 04   # MaximumItems, Integer, Length=4
            00 00 00 01 00 00 00 00   # Value=1 + padding
```

### Walk-through

The outermost header `42 00 78 01 00 00 00 C8` decodes as tag `420078` = `RequestMessage`, type `01` = Structure, length `0xC8` = 200 bytes. Those 200 bytes are the total of every nested item's padded size: the `RequestHeader` block (8-byte header + 144 bytes of contents = 152) plus the `BatchItem` block (8 + 40 = 48), totalling 200.

`RequestHeader` itself reports a length of `0x90` = 144 bytes, which is the sum of its four children:

| Child field | Header | Value + padding | Sub-total |
|---|---|---|---|
| ProtocolVersion (Structure) | 8 | 32 | 40 |
| Authentication (Structure) | 8 | 64 | 72 |
| TimeStamp (Date-Time) | 8 | 8 | 16 |
| BatchCount (Integer) | 8 | 4 + 4 | 16 |
| **Sum** | | | **144** |

Integers and Enumerations always declare a length of 4 but occupy 8 wire bytes because of mandatory zero-padding. The decoded value sits in the first 4 bytes; the trailing `00 00 00 00` is padding, not data.

The `CredentialType` enumeration value `00 00 00 01` = 1 = `UsernameAndPassword`. The `Operation` enumeration value `00 00 00 08` = 8 = `Locate`.

The `TimeStamp` bytes `00 00 00 00 6A 33 80 65` are the 64-bit big-endian POSIX timestamp 1,781,760,101 = 2026-06-17T05:21:41Z. TTLV always stores timestamps in UTC regardless of the local timezone offset expressed in an XML encoding.

## Example: Locate Response (KMIP 1.4)

The server found one matching object and returns its identifier.

XML encoding:

```xml
<ResponseMessage>
    <ResponseHeader>
        <ProtocolVersion>
            <ProtocolVersionMajor type="Integer" value="1"/>
            <ProtocolVersionMinor type="Integer" value="4"/>
        </ProtocolVersion>
        <TimeStamp type="DateTime" value="2026-06-17T13:21:41+08:00"/>
        <BatchCount type="Integer" value="1"/>
    </ResponseHeader>
    <BatchItem>
        <Operation type="Enumeration" value="Locate"/>
        <ResultStatus type="Enumeration" value="Success"/>
        <ResponsePayload>
            <UniqueIdentifier type="TextString" value="00000001"/>
        </ResponsePayload>
    </BatchItem>
</ResponseMessage>
```

Annotated TTLV:

```
42 00 7B 01 00 00 00 90   # ResponseMessage, Structure, Length=144
   42 00 7A 01 00 00 00 48   # ResponseHeader, Structure, Length=72
      42 00 69 01 00 00 00 20   # ProtocolVersion, Structure, Length=32
         42 00 6A 02 00 00 00 04   # ProtocolVersionMajor, Integer, Length=4
            00 00 00 01 00 00 00 00   # Value=1 + padding
         42 00 6B 02 00 00 00 04   # ProtocolVersionMinor, Integer, Length=4
            00 00 00 04 00 00 00 00   # Value=4 + padding
      42 00 92 09 00 00 00 08   # TimeStamp, DateTime, Length=8
         00 00 00 00 6A 33 80 65   # Value=2026-06-17T05:21:41Z
      42 00 0D 02 00 00 00 04   # BatchCount, Integer, Length=4
         00 00 00 01 00 00 00 00   # Value=1 + padding
   42 00 0F 01 00 00 00 38   # BatchItem, Structure, Length=56
      42 00 5C 05 00 00 00 04   # Operation, Enumeration, Length=4
         00 00 00 08 00 00 00 00   # Value=Locate(0x08) + padding
      42 00 7F 05 00 00 00 04   # ResultStatus, Enumeration, Length=4
         00 00 00 00 00 00 00 00   # Value=Success(0x00) + padding
      42 00 7C 01 00 00 00 10   # ResponsePayload, Structure, Length=16
         42 00 94 07 00 00 00 08   # UniqueIdentifier, TextString, Length=8
            30 30 30 30 30 30 30 31   # Value="00000001"
```

The response header omits the `Authentication` field present in the request — the response header carries only `ProtocolVersion`, `TimeStamp`, and `BatchCount`, totalling 72 bytes (compared to the request header's 144).

The batch item adds `ResultStatus` (`42007F`, Enumeration, `0x00` = `Success`) between `Operation` and `ResponsePayload`. The `UniqueIdentifier` text string `"00000001"` is shown as its raw ASCII bytes: `30 30 30 30 30 30 30 31` (eight ASCII digits, no padding needed because 8 is already a multiple of 8).

## Related

[TTLV Encoding](../encoding/ttlv-encoding.md) · [Message Structure](../messages/message-structure.md) · [Locate](../operations/locate.md)
