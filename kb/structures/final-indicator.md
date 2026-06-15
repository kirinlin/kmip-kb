---
title: Final Indicator
category: structures
spec_version: "2.1"
spec_versions: ["1.3", "1.4", "2.0", "2.1"]
source_section: "7.14"
v1_source_section: "2.1.17"
status: reviewed
related: ["init-indicator", "correlation-value", "data"]
keywords: ["final indicator", "streaming", "multi-part", "last part", "4200D8", "FinalIndicator"]
tag_hex: "4200D8"
xml_text: "FinalIndicator"
---

# Final Indicator

## Overview

The closing flag of a streamed cryptographic operation (1.3+): True in the
last request of the sequence opened by [Init
Indicator](init-indicator.md), telling the server to finalize — flush any
remaining output, emit the digest/MAC/signature, and discard the streaming
state behind the [Correlation Value](correlation-value.md).

## Encoding (Tag / Type / Length / Value)

Tag `4200D8`, Boolean.

## Fields & Structure

Requests between Init and Final carry neither flag, just the Correlation
Value and the next [Data](data.md) chunk. The Final request may itself carry
a last chunk of data (possibly empty for pure finalization).

## Examples

Closing a streamed MAC over a backup image: Final Indicator = True,
Correlation Value from the first response, Data = the trailing bytes; the
response returns the complete [MAC Data](mac-data.md).

## Related

[Init Indicator](init-indicator.md) ·
[Correlation Value](correlation-value.md) · [Data](data.md)
