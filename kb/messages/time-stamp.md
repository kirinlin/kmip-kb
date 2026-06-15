---
title: Time Stamp
category: messages
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "9.20"
v1_source_section: "6.5"
status: reviewed
related: ["message-structure", "initial-date", "last-change-date"]
keywords: ["time stamp", "message header", "clock skew", "POSIX time", "420092", "TimeStamp"]
tag_hex: "420092"
xml_text: "TimeStamp"
---

# Time Stamp

## Overview

The header field carrying the sender's clock. Servers always stamp their
responses (and their server-initiated requests); clients may stamp requests,
which lets a server enforce sane time usage — e.g. rejecting requests whose
clock is implausibly far from its own as possible replays.

## Encoding (Tag / Type / Length / Value)

Tag `420092`, Date-Time — POSIX seconds since 1970-01-01 UTC in an 8-byte
value, like every KMIP timestamp.

## Fields & Structure

Optional in client request headers; required in response headers and in
[server-to-client](../operations/server-to-client/index.md) request headers.
A clever side use: a clockless client with only a countdown timer can
subtract the response Time Stamp from date attributes (e.g.
[Deactivation Date](../attributes/deactivation-date.md)) to get usable
"seconds from now" durations.

## Examples

A client sees Time Stamp drift of +400 s in server responses, flags its own
clock, and resynchronizes NTP before the server starts rejecting its
requests.

## Related

[Message Structure](message-structure.md) ·
[Initial Date](../attributes/initial-date.md) ·
[Last Change Date](../attributes/last-change-date.md)
