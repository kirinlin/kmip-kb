---
title: Locate
category: operation
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "6.1.28"
v1_source_section: "4.9"
status: draft
related: ["get", "get-attributes", "recover", "object-group", "cryptographic-usage-mask", "state"]
keywords: ["locate", "search", "find object", "query objects", "attribute match"]
---

# Locate

## Purpose

`Locate` searches the server for managed objects that match a set of attribute
criteria and returns their identifiers. It is the primary discovery operation:
clients use it to find objects they did not just create, then follow up with
[Get](get.md) to retrieve them.

## Request Fields

| Field | Required | Description |
|---|---|---|
| Maximum Items | No | An upper bound on how many identifiers the server should return. |
| Offset Items | No | How many otherwise-matching objects to skip before collecting results (0 is the same as omitting it). |
| Storage Status Mask | No | Selects whether to search online objects, archived objects, or both; online-only is assumed when absent. |
| Object Group Member | No | Selects how a named [object group](../attributes/object-group.md) is sampled (a fresh member versus the group default). |
| Attribute | No (may repeat) | An attribute and value that a candidate object must match. |

## Response Fields

| Field | Required | Description |
|---|---|---|
| Located Items | No | The total count of objects meeting the criteria; a server may omit it if it cannot or will not compute the total. |
| Unique Identifier | No (may repeat) | The identifiers of the matching objects. |

## Behavior & Server Requirements

A candidate must satisfy every supplied attribute; with no attributes given,
every object qualifies. When nothing matches, the response payload is empty.
Several attribute types are matched specially:

- **Dates** — a single date value matches objects with that exact value, while
  two values of the same date attribute define a range and match objects whose
  value falls within it. A date set to its maximum possible value behaves like
  an unset attribute.
- **[Cryptographic Usage Mask](../attributes/cryptographic-usage-mask.md)** —
  matching is by bitwise containment: a candidate matches if it has at least the
  requested bits set, and may have more.
- **[Usage Limits](../attributes/usage-limits.md)** — a candidate matches if its
  count and total are at least the requested values.
- **Structured attributes** (such as [Link](../attributes/link.md)) — only the
  supplied sub-fields need match; unspecified sub-fields are ignored.

Servers may, but need not, support wildcards or regular expressions when
matching text and byte-string fields. Result paging is controlled by the
Maximum Items and Offset Items fields. The ID Placeholder interacts with the
result count: if exactly one object is found, its identifier is copied into the
ID Placeholder; if the match is ambiguous (more than one object could be
returned), the server clears the ID Placeholder so that batched follow-on
operations without an explicit identifier fail rather than act on the wrong
object.

## Errors

Uses the centralized [error handling](../concepts/error-handling.md). Typical
causes: an invalid attribute or value in the criteria, or insufficient
permission.

## Examples

To find all active AES keys usable for encryption, a client sends Locate with
attributes State = Active, Cryptographic Algorithm = AES, and a Cryptographic
Usage Mask selecting Encrypt. The server returns the matching identifiers, which
the client retrieves with [Get](get.md).

## Related Operations

[Get](get.md) · [Get Attributes](get-attributes.md) · [Recover](recover.md)
