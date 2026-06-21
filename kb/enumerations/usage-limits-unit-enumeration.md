---
title: Usage Limits Unit Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.60"
status: reviewed
related: ["usage-limits", "get-usage-allocation", "obtain-lease"]
keywords: ["usage limits", "usage unit", "byte count", "object count", "key usage counting", "420098", "UsageLimitsUnit"]
tag_hex: "420098"
xml_text: "UsageLimitsUnit"
tag_type: "Enumeration"
---

# Usage Limits Unit Enumeration

## Overview

The Usage Limits Unit enumeration specifies how the usage counter in the [Usage Limits](../structures/usage-limits.md) structure is measured. It is the unit of the Usage Limits Count and Usage Limits Total fields, determining whether the server counts individual operation invocations or the total data volume processed with the key.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Byte | `00000001` | `Byte` |  |
| Object | `00000002` | `Object` |  |

- **Byte**: Usage is counted in bytes of plaintext or ciphertext processed. A key with a 1 GB Usage Limits Total set to Byte may encrypt up to 1,073,741,824 bytes before its limit is exhausted. Appropriate for bulk encryption where volume matters more than invocation count.
- **Object** (or Count): Usage is counted in operation invocations. A key with Usage Limits Total = 1000 and unit = Object may be used for 1000 cryptographic operations (e.g., 1000 MAC computations) before exhaustion. Appropriate for signing keys or other operations where each invocation is independently significant regardless of data size.

## Examples

An AES-GCM key for database column encryption might have Usage Limits Unit = **Byte** with a 10 GB total, enforcing a nonce-safety limit. An HMAC signing key for API authentication might have Unit = **Object** with a total of 100,000 invocations.

## Related

[Usage Limits structure](../structures/usage-limits.md) · [Get Usage Allocation](../operations/get-usage-allocation.md) · [Obtain Lease](../operations/obtain-lease.md)
