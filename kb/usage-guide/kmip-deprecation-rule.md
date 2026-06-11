---
title: KMIP Deprecation Rule
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-5.1"
status: draft
related: ["deprecated-functions"]
keywords: ["deprecation", "major version", "minor version", "removal", "normative", "non-normative"]
---

# KMIP Deprecation Rule

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

KMIP uses a two-phase deprecation model: features are first deprecated in any version but are removed only at a major version boundary. This rule applies to normative content in KMIP-SPEC and KMIP-Prof (profiles), while non-normative content in the Usage Guide and Test Cases may be removed in any version.

## Guidance

A feature deprecated in a minor version (e.g., deprecated in v1.3) will not be removed until the next major version (e.g., v2.0). This gives implementers a full major-version cycle to migrate away from deprecated functionality. The deprecation rule is designed to provide predictability: implementations that stay within a major version family are protected from sudden removal of features they depend on.

Non-normative documents (Usage Guide, Test Cases) follow a looser rule: content may be removed in any version update. Implementers should not build hard dependencies on specific sections of the UG or test cases that could be removed.

## Implementation Notes

When integrating KMIP, prefer the use of non-deprecated features from the start to avoid migration work at the next major version boundary. Review the list of deprecated functions in each spec release and prioritise migration away from them during regular maintenance cycles rather than waiting for forced removal.

## Related Concepts

See [Deprecated Functions](deprecated-functions.md) for the current deprecation list.
