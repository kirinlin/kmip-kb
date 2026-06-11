---
title: Deprecated Functions
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-5.2"
status: draft
related: ["kmip-deprecation-rule"]
keywords: ["deprecated", "deprecated functions", "KMIP 2.x", "v2.0", "v2.1", "removed features"]
---

# Deprecated Functions

<!-- Author original prose only. Do NOT paste spec text. See CONTRIBUTING.md. -->

## Overview

This article tracks KMIP functions that have been marked deprecated in the v2.x family. As of KMIP 2.1, there are no deprecated functions in the 2.x family — all functionality introduced in v2.0 and v2.1 remains fully active. Features deprecated in the v1.x family were removed at the v2.0 boundary.

## Guidance

The KMIP v2.0 release removed a number of features that were deprecated during the v1.x release cycle. These included the Template managed object type, the Operational Policy feature, and certain v1.x-specific object types and attributes. Any v1.x implementation that used these features must be updated before migrating to v2.0 or later.

Since KMIP 2.1 introduces no new deprecations, v2.1-targeting implementations can use the full v2.1 feature set without concern about near-term removals.

## Implementation Notes

Monitor each new KMIP release for newly deprecated features. The KMIP-UG deprecation section is updated with each release. When a feature is deprecated, plan the migration within the current major version cycle to avoid a forced migration at the next major boundary.

## Related Concepts

See [KMIP Deprecation Rule](kmip-deprecation-rule.md) for the deprecation policy.
