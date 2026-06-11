---
title: HTTPS Profiles
category: profile
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "prof-5.3"
v1_source_section: "enc-2"
status: reviewed
related: ["base-profiles", "https-authentication-suite", "xml-profiles", "json-profiles"]
keywords: ["HTTPS", "HTTP over TLS", "message encoding", "transport", "REST-like", "KMIP client", "KMIP server"]
---

# HTTPS Profiles

## Overview

The HTTPS Profiles add an HTTP/1.x framing layer over TLS to the Baseline Client and Baseline Server. They enable KMIP to ride on top of existing HTTPS infrastructure — firewalls, load balancers, and proxies that understand HTTP but not raw TLS connections.

## HTTPS Client

An HTTPS Client extends the [Baseline Client](base-profiles.md) by sending KMIP request messages as HTTP POST bodies to a configurable URI (default `/kmip`). It sets `Content-Type` based on the message encoding (`application/octet-stream` for TTLV, `text/xml` for XML, `application/json` for JSON), adds `Content-Length`, and disables caching with `Cache-Control: no-cache`. If the client also supports server-to-client operations, it must be capable of acting as an HTTPS server to receive them.

## HTTPS Server

An HTTPS Server extends the [Baseline Server](base-profiles.md) to accept KMIP messages over HTTP POST and respond with HTTP 200 and the same content-type conventions. The server should support `/kmip` as the target URI but must allow operators to configure a different path. Servers that initiate server-to-client operations must act as HTTPS clients.

## Mandatory Test Cases

`MSGENC-HTTPS-M-1-21` verifies that the server correctly handles a `Query` request where the initial `Maximum Response Size` is too small, returns the appropriate error, and succeeds on a retry with a larger size. This exercises HTTP framing alongside the KMIP error-response path.

## Implications for Implementers

- HTTPS framing does not change KMIP message semantics. The same TTLV (or XML/JSON) body is transmitted; only the transport layer differs.
- `Maximum Response Size` is still interpreted in terms of TTLV-encoded length, not HTTP body length. A client that configures this based on HTTP expectations will get surprising results.
- Interoperability with HTTP proxies that enforce `Content-Length` is a common issue; always compute the correct value before sending.
- Prefer explicit URI configuration over relying on `/kmip` — some server products use different paths.

## Version History

For v1.0–v1.2 the HTTPS binding was defined in the separate `[KMIP-ENCODE]`
document (*KMIP Additional Message Encodings v1.0*, §2), not in KMIP-PROF.
Starting with v1.3 the HTTPS Client and Server profile IDs appeared in the
core spec enumerations, and by v2.0 the rules were fully absorbed into
KMIP-Prof §5.3 (where they remain in v2.1). The `enc-2` traceability in
`v1_source_section` points to §2 of that earlier document.

## Related Concepts

[Base Profiles](base-profiles.md) ·
[HTTPS Authentication Suite](https-authentication-suite.md) ·
[XML Profiles](xml-profiles.md) ·
[JSON Profiles](json-profiles.md)
