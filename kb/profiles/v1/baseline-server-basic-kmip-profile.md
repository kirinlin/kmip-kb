---
title: Baseline Server Basic KMIP Profile
category: profile
spec_version: "1.2"
spec_versions: ["1.2"]
source_section: "prof-4.1"
status: reviewed
related: ["basic-authentication-suite", "baseline-server-tls-v1-2-kmip-profile", "baseline-client-basic-kmip-profile", "basic-baseline-server-kmip-profile", "base-profiles"]
keywords: ["baseline server", "Basic Authentication Suite", "conformance", "v1.2", "server profile"]
---

# Baseline Server Basic KMIP Profile

## Overview

The Baseline Server Basic KMIP Profile is the KMIP v1.2 name for the standard baseline server conformance point using the [Basic Authentication Suite](../authentication/basic-authentication-suite.md). It is the renaming — with minor update — of the [Basic Baseline Server KMIP Profile](basic-baseline-server-kmip-profile.md) from v1.1. The word order changed (from "Basic Baseline Server" to "Baseline Server Basic") to make the naming scheme more consistent: the profile name now leads with the capability tier ("Baseline") and ends with the authentication variant ("Basic"). The capability requirements are substantively the same.

The companion client profile is the [Baseline Client Basic KMIP Profile](baseline-client-basic-kmip-profile.md). For the TLS 1.2 variant, see [Baseline Server TLS v1.2 KMIP Profile](baseline-server-tls-v1-2-kmip-profile.md). The v2.x successor is the Baseline Server tier within [Base Profiles](../base-encoding/base-profiles.md).

## Required Operations and Objects

The server must support Create, Register, Get, Get Attributes, Get Attribute List, Locate, Destroy, Query, and Discover Versions, with the full set of baseline attributes and message-envelope elements. This mirrors the [Basic Baseline Server](basic-baseline-server-kmip-profile.md) requirement set.

## Implications for Implementers

- KMIP v1.2 reorganized profile names but did not substantially change baseline server requirements. Implementations that passed the v1.1 Basic Baseline Server test suite will typically satisfy this profile with only minor updates.
- If TLS 1.2 mutual authentication is required, use [Baseline Server TLS v1.2 KMIP Profile](baseline-server-tls-v1-2-kmip-profile.md) instead.
- For the v2.x continuation of this profile, see [Base Profiles](../base-encoding/base-profiles.md).

## Related Concepts

[Basic Authentication Suite](../authentication/basic-authentication-suite.md) ·
[Basic Baseline Server KMIP Profile](basic-baseline-server-kmip-profile.md) ·
[Baseline Client Basic KMIP Profile](baseline-client-basic-kmip-profile.md) ·
[Baseline Server TLS v1.2 KMIP Profile](baseline-server-tls-v1-2-kmip-profile.md) ·
[Base Profiles](../base-encoding/base-profiles.md)
