---
title: Init Indicator
category: structures
spec_version: "2.1"
spec_versions: ["1.3", "1.4", "2.0", "2.1"]
source_section: "7.17"
v1_source_section: "2.1.16"
status: reviewed
related: ["final-indicator", "correlation-value", "data"]
keywords: ["init indicator", "streaming", "multi-part", "first part", "4200D7", "InitIndicator"]
tag_hex: "4200D7"
xml_text: "InitIndicator"
tag_type: "Boolean"
---

# Init Indicator

## Overview

The opening flag of a streamed cryptographic operation (1.3+): True in the
first request of a multi-part sequence, telling the server to set up
streaming state and return a [Correlation Value](correlation-value.md)
instead of finishing in one shot.

## Encoding (Tag / Type / Length / Value)

Tag `4200D7`, Boolean (8-byte value field, `...00` or `...01`).

## Fields & Structure

Appears only in requests, only for operations the server supports in
streaming mode. A single-part operation simply omits both this and
[Final Indicator](final-indicator.md); a two-part operation uses Init = True
on part one and Final = True on part two.

## Examples

First chunk of a streamed Encrypt: key identifier, Cryptographic Parameters,
Init Indicator = True, Data = chunk 1. The response carries ciphertext for
chunk 1 plus the Correlation Value for the rest.

## Related

[Final Indicator](final-indicator.md) ·
[Correlation Value](correlation-value.md) · [Data](data.md)
